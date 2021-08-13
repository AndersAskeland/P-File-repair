# %%
# Imports
import sys, os, struct
import ctypes as ct


# Functions
def read_pfile_header(file):
    # Create dict with only keys
    header = dict.fromkeys(["hdr_rev", "off_data", "nechoes", "nframes", \
        "frame_size", "rcv", "rhuser19", "spec_width", "csi_dims", "xcsi", "ycsi", \
        "zcsi", "ps_mps_freq", "te"])
    
    # Set byte location of different parameters
    location = header.copy()
    location["hdr_rev"] = {"loc": 0, "type": "f", "size": 4, "n": 1}
    location["off_data"] = {"loc": 4, "type": "i", "size": 4, "n": 1}
    location["nechoes"] = {"loc": 146, "type": "h", "size": 2, "n": 1}
    location["nframes"] = {"loc": 150, "type": "h", "size": 2, "n": 1}
    location["frame_size"] = {"loc": 156, "type": "h", "size": 2, "n": 1}
    location["rcv"] = {"loc": 264, "type": "h", "size": 2, "n": 8}
    location["rhuser19"] = {"loc": 356, "type": "f", "size": 4, "n": 1}
    location["spec_width"] = {"loc": 432, "type": "f", "size": 4, "n": 1}
    location["csi_dims"] = {"loc": 436, "type": "h", "size": 2, "n": 1}
    location["xcsi"] = {"loc": 438, "type": "h", "size": 2, "n": 1}
    location["ycsi"] = {"loc": 440, "type": "h", "size": 2, "n": 1}
    location["zcsi"] = {"loc": 442, "type": "h", "size": 2, "n": 1}
    location["ps_mps_freq"] = {"loc": 488, "type": "I", "size": 4, "n": 1}
    location["te"] = {"loc": 1148, "type": "h", "size": 2, "n": 1}

    # Open and read
    with open(file, "rb") as file:
        for location_key, header_key in zip(location, header):
            print(location[location_key]["loc"])
            file.seek(location[location_key]["loc"])

            # Check list objects
            if location[location_key]["n"] > 1:
                header[location_key] = list()
                for i in range(location[location_key]["n"]):
                    value = struct.unpack(location[location_key]["type"], file.read(location[location_key]["size"]))[0]
                    header[header_key].append(value)
            else:
                value = struct.unpack(location[location_key]["type"], file.read(location[location_key]["size"]))[0]
                header[header_key] = value

    # Correct te
    header["te"] = float(header["te"]) / 1e6

    # Return
    return(header)

# Read raw data
def read_raw_data(file, header, n):
    with open(file, "rb") as file: 
        file.seek(header["off_data"])
        print(struct.unpack("i", file.read(4))[0])
        file.seek(header["off_data"])

        data = list()
        print(data)
        for i in range(int(n)):
            value = struct.unpack("i", file.read(4))[0]
            data.append(value)

    return data

# Get coils
def get_coils(header):
    coils = 0
    
    for n in range(0, 8, 2):
        print(n)
        if header["rcv"][n] != 0 or header["rcv"][n + 1] != 0:
            coils = coils + 1 + header["rcv"][n+1] - header["rcv"][n]
    
    if coils == 0:
        coils = 1
    
    return coils

# extract data
def extract_data(coils, raw_data, empty_values):
    extracted_data = list()
    index_start = 0
    index_end = 0
    print(len(raw_data))
    for i in range(coils):
        index_end = index_start + 40960
        print(f"Index start is: {index_start}")
        print(f"Index end is: {index_end}")

        dat = raw_data[int(index_start):int(index_end)]

        index_start = index_end + 1 + empty_values

        extracted_data.extend(dat)

    return extracted_data

# Read raw header
def read_raw_header(file, header):
    with open(file, "rb") as file:
        raw = file.read(header["off_data"])

    return raw

# Write data
def write_data(file, header_data, data):
    with open(file, "wb") as file:
        file.write(header_data)
        file.write(data)


##############
#### Main ####
##############
# Variablers
file_dir = "/Users/andersaskeland/Documents/Statistics (Local)/GE_MRI/210177-1752/P34304.7"
file_out =  "/Users/andersaskeland/Documents/Statistics (Local)/GE_MRI/210177-1752/P34304_python_fix.7" 
file_bytes = os.path.getsize(file_dir)

# Get header
header = read_pfile_header(file_dir)
print(header)

# Calculate data points
data_points = (file_bytes - header["off_data"]) / 4
print(data_points)

# Read raw data
raw_data = read_raw_data(file_dir, header, data_points)
print(raw_data[:1000])

# Get raw header
raw_header = read_raw_header(file_dir, header)

# Get coils
coils = get_coils(header)
print(coils)

# Expected data points
expected_data_points = coils * (header["nframes"] * header["nechoes"] + header["nechoes"]) * header["frame_size"] * 2
print(expected_data_points)

# Surplus
surplus_data_points = data_points - expected_data_points
empty_values = surplus_data_points / coils

# Extract data
extracted_data = extract_data(coils, raw_data, empty_values)
# print(extracted_data)
print(f"lenght of list is: {len(extracted_data)}")

# write_data(output_file, data)
# data_byte = bytes(extracted_data)
data_byte = struct.pack("i"*expected_data_points, *extracted_data)
write_data(file_out, raw_header, data_byte)

print(raw_header.count())
print(sys.getsizeof(data_byte))
print(sys.getsizeof(raw_header))

# %%
