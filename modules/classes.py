# -----------------------------------------------------------------------------
# Module: Classes
#
# What: Main class for reading binary data.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1- Imports
# ------------------------------------------------------------------------------
# External modules
import sys, os, struct

# Local functions 

# Local classes

# Local resources 


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class PFile:
    '''Reads and fixes v. 28 p-files
    
    Class that contains functions and data related to reading and
    converting v. 28 GE p-files.  

    TODO:
        * Make a parent class that contains information about location, size, version
            etc. Perhaps a p-file (parent) + header (child) + data (child).

    Args:
        None
    
    Attributes:
        header (dict): Contains dictionary keys associated to header. 
            Actual values are read during __init__
        location (dict): Contains location, data type, size and n byte
            location information related to reading data from the
            binary file.
    '''
    
    # ---- Class attributes ---- #
    # Define header
    header = dict.fromkeys(["hdr_rev", "off_data", "nechoes", "nframes", \
    "frame_size", "rcv", "rhuser19", "spec_width", "csi_dims", "xcsi", "ycsi", \
    "zcsi", "ps_mps_freq", "te"])

    # Define location (HARDCODED)
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


    # ---- Instance/object attributes ---- #
    def __init__(self, file_path):
        # General variables
        self.file = open(file_path, "rb")
        self.file_size = os.path.getsize(file_path)

        # Read header
        self.header = self.read_header(self.file, self.location, self.header)
        self.header_raw = self.file.read(self.header["off_data"])

        # Variables
        self.coils = self.calc_coils(self.header)
        self.items = self.file_size - self.header["off_data"] / 4
        self.expected_items = self.coils * (self.header["nframes"] * self.header["nechoes"] + self.header["nechoes"]) * self.header["frame_size"] * 2
        self.surplus_items = self.items - self.expected_items
        self.excess_items = self.surplus_items / self.coils

        # Read data
        self.raw_data = self.read_raw_data(self.file, self.header, self.items)
        self.extracted_data = self.extract_data(self.coils, self.raw_data, self.excess_items)
        self.extract_data_raw = struct.pack("i"*self.expected_items, *self.extracted_data)

    ''' Functions '''
    # Read header
    def read_header(file, location, header):
        for location_key in location:
            # Seek to first location ("hdr_rev")
            file.seek(location[location_key]["loc"])
            dat = file.read(location[location_key]["size"])

            # Read binary data into header dict
            if location[location_key]["n"] > 1: # If more than 1 value
                header[location_key] = list()
                for i in range(location[location_key]["n"]):
                    value = struct.unpack(location[location_key]["type"], dat)[0]
                    header[location_key].append(value)
            else: # If only 1 value
                value = struct.unpack(location[location_key]["type"], dat)[0]
                header[location_key] = value

    # Read data
    def read_raw_data(file, header, n):
        # Creaate empty list and go to correct location
        data = list()
        file.seek(header["off_data"])

        # Read trough file
        for i in range(int(n)):
            value = struct.unpack("i", file.read(4))[0]
            data.append(value)

        # Return
        return data

    # Extract data
    def extract_data(coils, raw_data, excess_items):
        # Creaate empty list
        extracted_data = list()

        # Set indexs
        index_start = 0
        index_end = 0

        # Read data
        for i in range(coils):
            index_end = index_start + 40960
            dat = raw_data[int(index_start):int(index_end)]
            index_start = index_end + 1 + excess_items
            extracted_data.extend(dat)

        # Return
        return extracted_data

    # Calculate coils
    def calc_coils(header):
        coils = 0
    
        for n in range(0, 8, 2):
            if header["rcv"][n] != 0 or header["rcv"][n + 1] != 0:
                coils = coils + 1 + header["rcv"][n+1] - header["rcv"][n]
        
        if coils == 0:
            return 1
        else:
            return coils

    # Write data
    def write_data(path, header, data):
        with open(path, "wb") as file:
            file.write(header)
            file.write(data)