# -----------------------------------------------------------------------------
# Module: Classes
#
# What: Main class for reading binary data.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules
import sys
import os
import struct

# Local functions 

# Local classes

# Local resources 


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class Header:
    '''Header class for v. 28 p-files.

    Provides framework for writing header information and contains information about
    byte location of various attributes. Locations are hard-coder for v.28.

    Args:
        None

    Attributes:
        header (dict): Contains dictionary keys associated to header. 
            Actual values are read during __init__
        location (dict): Contains location, data type, size and n byte
            location information related to reading data from the
            binary file.
    '''

    # ---- Constructor ---- #
    def __init__(self) -> None:
        self.header = dict.fromkeys(["hdr_rev", "off_data", "nechoes", "nframes", \
        "frame_size", "rcv", "rhuser19", "spec_width", "csi_dims", "xcsi", "ycsi", \
        "zcsi", "ps_mps_freq", "te"])

        self.header_location = self.header.copy()
        self.header_location["hdr_rev"] = {"loc": 0, "type": "f", "size": 4, "n": 1}
        self.header_location["off_data"] = {"loc": 4, "type": "i", "size": 4, "n": 1}
        self.header_location["nechoes"] = {"loc": 146, "type": "h", "size": 2, "n": 1}
        self.header_location["nframes"] = {"loc": 150, "type": "h", "size": 2, "n": 1}
        self.header_location["frame_size"] = {"loc": 156, "type": "h", "size": 2, "n": 1}
        self.header_location["rcv"] = {"loc": 264, "type": "h", "size": 2, "n": 8}
        self.header_location["rhuser19"] = {"loc": 356, "type": "f", "size": 4, "n": 1}
        self.header_location["spec_width"] = {"loc": 432, "type": "f", "size": 4, "n": 1}
        self.header_location["csi_dims"] = {"loc": 436, "type": "h", "size": 2, "n": 1}
        self.header_location["xcsi"] = {"loc": 438, "type": "h", "size": 2, "n": 1}
        self.header_location["ycsi"] = {"loc": 440, "type": "h", "size": 2, "n": 1}
        self.header_location["zcsi"] = {"loc": 442, "type": "h", "size": 2, "n": 1}
        self.header_location["ps_mps_freq"] = {"loc": 488, "type": "I", "size": 4, "n": 1}
        self.header_location["te"] = {"loc": 1148, "type": "h", "size": 2, "n": 1}


class pFile(Header):
    '''Reads and fixes v. 28 p-files
    
    Class that contains functions and data related to reading and
    converting v. 28 GE p-files.  

    Args:
        path (str): File path to folder or single p-file.
        folder (bool): True if an entire folder with p-files #TODO: Maybe do handling of this inside user_interface.

    Attributes:
        TODO
    '''

    # ---- Constructor ---- #
    def __init__(self, path: str, folder: bool) -> None:
        super().__init__()

        # General variables
        self.file = open(path, "rb")
        self.file_size = os.path.getsize(path)

        # Read header
        self.header = self.read_header(file=self.file, header_locations=self.header_location, header=self.header)
        self.header_raw = self.file.read(self.header["off_data"])

        # Calculate header variables
        self.coils = self.calc_coils(self.header)
        self.data_points = int((self.file_size - self.header["off_data"]) / 4)
        self.expected_data_points = self.coils * (self.header["nframes"] * self.header["nechoes"] + self.header["nechoes"]) * self.header["frame_size"] * 2
        self.surplus_data_points = self.data_points - self.expected_data_points
        self.excess_data_points = self.surplus_data_points / self.coils

        # Print
        print(f"Header = {self.header}")
        print(f"Coils = {self.coils}")
        print(f"Items = {self.data_points}")
        print(f"Expected items = {self.expected_data_points}")
        print(f"Surplus items = {self.surplus_data_points}")
        print(f"Excess items = {self.excess_data_points}")
        # TODO - Check function. Throw exception if expected match items. No need to run anything then.


    # ---- Functions ---- #
    def repair_p_file(self, output_path: str) -> None:
        ''' Main function that repairs and writes new p-file. Also responsible for error handling. '''

        # Check if there is actually more data points than expected
        if self.expected_data_points == self.data_points:
            print("File is not corrupted (expected data points match data points)")
            return 0

        # Read raw data and removes corrupted data
        self.raw_data = self.read_raw_data(file=self.file, header=self.header, data_points=self.data_points)
        self.extracted_data = self.remove_corrupted_data(self.coils, self.raw_data, self.excess_data_points)
        
        # Writes extracted data to binary
        self.extract_data_binary = struct.pack("i"*self.expected_data_points, *self.extracted_data)

        # Write data
        with open(output_path, "wb") as file:
            file.write(self.header_raw)
            file.write(self.extract_data_binary)
            print("P-file was converted sucessfully!")

    def read_header(self, file: __file__, header_locations: Header, header: Header) -> Header:
        ''' Reads header data based on location data '''
        
        # Go trough all binary location in header location and write to header proper.
        for location in header_locations:
            file.seek(header_locations[location]["loc"])
            read_data = file.read(header_locations[location]["size"])

            # Check if multiple parameters to read
            if header_locations[location]["n"] == 1:
                unpacked_data = struct.unpack(header_locations[location]["type"], read_data)[0]
                header[location] = unpacked_data
            else:
                header[location] = list()
                for i in range(header_locations[location]["n"]):
                    unpacked_data = struct.unpack(header_locations[location]["type"], read_data)[0]
                    header[location].append(unpacked_data)
                    read_data = file.read(header_locations[location]["size"])
        
        # Return
        return header

    def read_raw_data(self, file: __file__, header: Header, data_points: int) -> list:
        ''' Read raw data. Will only read actual data starting from the "off_data" location. '''

        # Creaate empty list and seek to correct location
        raw_data = list()
        file.seek(header["off_data"])

        # Read binary data 4 bytes at a time and stores this in data variable
        for i in range(data_points):
            read_data = file.read(4)
            unpacked_data = struct.unpack("i", read_data)[0]
            raw_data.append(unpacked_data)

        # Return
        return raw_data

    # Extract data
    def remove_corrupted_data(self, coils: int, raw_data: list, excess_items: int) -> list:
        ''' Removes corrupted data fro raw data. '''
        
        good_data = list()
        index_start = 0
        index_end = 0

        # Extract good data from corrupted data
        for i in range(coils):
            index_end = index_start + 40960
            dat = raw_data[int(index_start):int(index_end)]
            index_start = index_end + 1 + excess_items
            good_data.extend(dat)

        # Return
        return good_data

    def calc_coils(self, header: Header) -> int:
        ''' Calculates amount of coils in use on the basis of rcv. '''

        # Calculate coils
        coils = 0
        for n in range(0, 8, 2):
            if header["rcv"][n] != 0 or header["rcv"][n + 1] != 0:
                coils = coils + 1 + header["rcv"][n+1] - header["rcv"][n]
        
        # Return
        if coils == 0:
            return 1
        else:
            return coils

