# ------------------------------------------------------------------------------
# Open GE p-files manually (Binary mode)
# ------------------------------------------------------------------------------
# There is something wrong with v. 28 GE p-files. It is
# always 10058420 bytes and contains a lot of corrupted 0 values.
# This code removes these values and writes a new file without those
# values.

# Some code is adapted from the "Spant" package.


## ------------ Packages ------------- #
library(tidyverse)
library(spant)
library(hexView)

## ------------ Functions ------------- #
read_pfile_header <- function(file_name) {
  # Settings
  endian <- "little"
  connection <- file(file_name, "rb")

  # Set variables
  header <- vector(mode = "list", length = 15)
  names(header) <- c("hdr_rev", "text", "off_data", "nechoes", "nframes", "frame_size",
                     "rcv", "rhuser19", "spec_width", "csi_dims", "xcsi", "ycsi",
                     "zcsi", "ps_mps_freq", "te")

  # Set byte location of various stuff
  location <- header
  location$hdr_rev <- 0
  location$off_data <- 4 #
  location$nechoes <- 146 # Hvor mange gange den lytter efter signal - 1 gang
  location$nframes <- 150 # ????
  location$frame_size <- 156 # Antal gråtoner
  location$rcv <- 264 # Måske noget med CV procenter
  location$rhuser19 <- 356 #
  location$spec_width <- 432 # X axis?
  location$csi_dims <- 436 #
  location$xcsi <- 438 # Gradienter - Noget med voxel at gøre
  location$ycsi <- 440 # Gradienter
  location$zcsi <- 442 # Gradienter
  location$ps_mps_freq <- 488 #
  location$te <- 1148 #

  # Set variables by reading bytes (based on byte start location) - Using seek()
  seek(connection, location$hdr_rev)
  header$hdr_rev <- readBin(connection, "numeric", size = 4, endian = endian)
  seek(connection, 0)
  header$text <- readBin(connection, "string", n = 2000, size = 8, endian = endian)
  seek(connection, 4)
  header$off_data <- readBin(connection, "int", size = 4, endian = endian)

  seek(connection, location$nechoes)
  header$nechoes <- readBin(connection, "int", size = 2, endian = endian)

  seek(connection, location$nframes)
  header$nframes <- readBin(connection, "int", size = 2, endian = endian)

  seek(connection, location$frame_size)
  header$frame_size <- readBin(connection, "int", size = 2, signed = FALSE,
                               endian = endian)

  seek(connection, location$rcv)
  header$rcv <- readBin(connection, "int", n = 8, size = 2, endian = endian)

  seek(connection, location$rhuser19)
  header$rhuser19 <- readBin(connection, "numeric", size = 4, endian = endian)

  seek(connection, location$spec_width)
  header$spec_width <- readBin(connection, "numeric", size = 4, endian = endian)

  seek(connection, location$csi_dims)
  header$csi_dims <- readBin(connection, "int", size = 2, endian = endian)

  seek(connection, location$xcsi)
  header$xcsi <- readBin(connection, "int", size = 2, endian = endian)

  seek(connection, location$ycsi)
  header$ycsi <- readBin(connection, "int", size = 2, endian = endian)

  seek(connection, location$zcsi)
  header$zcsi <- readBin(connection, "int", size = 2, endian = endian)

  seek(connection, location$ps_mps_freq)
  # read as int
  ps_mps_freq_bits <- intToBits(readBin(connection, "int", size = 4, endian = endian))
  # convert to uint
  header$ps_mps_freq <- sum(2^.subset(0:31, as.logical(ps_mps_freq_bits)))

  seek(connection, location$te)
  header$te <- readBin(connection, "int", size = 4, endian = endian) / 1e6

  # Close conneciton
  close(connection)

  # Return
  return(header)
}
mrs_data_function <- function(data, ft, resolution, ref, nuc, freq_domain, affine, meta, extra) {

  mrs_data <- list(data = data, ft = ft, resolution = resolution, ref = ref,
                   nuc = nuc, freq_domain = freq_domain, affine = affine,
                   meta = meta, extra = extra)

  class(mrs_data) <- "mrs_data"
  return(mrs_data)
}
get_coils <- function(header){
  coils <- 0
  for (n in seq(1, 8, 2)) {
    if ((header$rcv[n] != 0) || (header$rcv[n + 1] != 0)) {
      coils <- coils + 1 + header$rcv[n + 1] - header$rcv[n]
    }
  }
  if (coils == 0) coils <- 1
  return(coils)
}

# ------------ Opening/reading p-file ------------- # Skal skiftes til sine egne filer.
# Set file location
file_name <- "/Users/andersaskeland/Documents/Statistics (Local)/GE_MRI/210177-1752/P34304.7" # v. 28 (20 coils)
file_output <- "~/Documents/GE_MRI/210177-1752/P34304_fixed.7"

file_name <- "~/Documents/GE_MRI/010262-1352 2/P04608.7" # v. 28 (15 coils)
file_output <- "~/Documents/GE_MRI/010262-1352 2/P04608_fixed.7"

file_name <- "~/Documents/GE_MRI/170180-1462/P56320.7" # v. 27 - Working (32 coils)

# Get size of file
file_bytes <- file.size(file_name)

# Read header - Remember to activate function
header <- read_pfile_header(file_name)

# Read raw data points
endian <- "little" # Some binary read setting I don't understand
connection <- file(file_name, "rb")

# Possibly an error in off_data . Off_data should say how much of the data is header. But it seems like this does not work. A solution is just to read the file till its end.
data_points <- (file_bytes - header$off_data) / 4

# Saves it as "int" vector. More compact
seek(connection, header$off_data)
raw_data <- readBin(connection, "int", n = data_points, size = 4, endian = endian) # Read till end of file.

# Read using hexView
seek(connection, 0)
raw_header <- readRaw(file_name, nbytes = header$off_data)

# Create data table/tibble from data
data_tibble <- tibble(raw_data)

# Calculate amount of selected coils
coils <- get_coils(header)

# Calculate expected points -
expected_data_points <- coils * (header$nframes * header$nechoes + header$nechoes) * header$frame_size * 2
surpluess_data_points <- data_points - expected_data_points

# Calculate empty values
empty_values <- surpluess_data_points / coils


# Remove empty values
extracted_data <- NULL
min_line = 1
max_line = 1
for (i in 1:coils){
  max_line <- min_line + 40959
  print(min_line)
  print(max_line)
  # Add data
  dat <- raw_data[min_line:max_line]

  # Remove data
  min_line <- max_line + 1 + empty_values

  # Bind data
  extracted_data <- c(extracted_data, dat)
}

# Write new binary
output_file <- file(file_output, "wb")

# Write header information
writeBin(raw_header[["fileRaw"]], output_file, endian = endian)

# Write data
writeBin(extracted_data, output_file, size = 4, endian = endian)
close(output_file)

size = object.size(raw_header[["fileRaw"]])
print(size, standard="IEC")
object.size(extracted_data)

