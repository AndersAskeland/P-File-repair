# Read data
file_example <- system.file("extdata", "philips_spar_sdat_WS.SDAT", package = "spant")
mrs_example <- read_mrs(file_example, format="spar_sdat")

file_name <- "~/Documents/GE_MRI/210177-1752/P34304.7"
mrs_data <- read_mrs(file_name, format = "pfile") # Becomes list of two classes


# View data
plot(mrs_data[["metab"]])
plot(mrs_data[["ref"]], xlim=c(-4,8))

plot(mrs_example)


########################
##   Open it myself   ##
########################
fname <- "~/Documents/GE_MRI/170180-1462/P56320.7"

# Get size
fbytes <- file.size(fname)

# -------- 1 - Read header  -------- #
header <- read_pfile_header(fname)


# Open file connection

# Read binary
# Get file revision
endian <- "little"
header$hdr_rev <- readBin(connection, "numeric", size = 4, endian = endian)

read_pfile_header <- function(file_name) {
  # Settings
  endian <- "little"
  connection <- file(file_name, "rb")

  # Set variables
  header <- vector(mode = "list", length = 14)
  names(header) <- c("hdr_rev", "off_data", "nechoes", "nframes", "frame_size",
                   "rcv", "rhuser19", "spec_width", "csi_dims", "xcsi", "ycsi",
                   "zcsi", "ps_mps_freq", "te")

  # Set byte location of various stuff
  location <- header
  location$hdr_rev <- 0
  location$off_data <- 4
  location$nechoes <- 146
  location$nframes <- 150
  location$frame_size <- 156
  location$rcv <- 264
  location$rhuser19 <- 356
  location$spec_width <- 432
  location$csi_dims <- 436
  location$xcsi <- 438
  location$ycsi <- 440
  location$zcsi <- 442
  location$ps_mps_freq <- 488
  location$te <- 1148

  # Set variables by reading bytes (based on byte start location) - Using seek()
  seek(connection, location$hdr_rev)
  header$hdr_rev <- readBin(connection, "numeric", size = 4, endian = endian)

  seek(connection, location$off_data)
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

  return(header)
}


# ---- 2. Back to data ----- #
# Read amount of data points
data_points <- (fbytes - header$off_data) / 4

# Go to start of data
seek(connection, hdr$off_data)

# Read
raw_pts <- readBin(connection, "int", n = data_points, size = 4, endian = endian)




#################################################################################################
#####  ERROR: This does not match when using GE p-file v. 28. This is where the problem is. #####
#####  I Need to clean data before moving to next step.                                     #####
#################################################################################################
# Read data
data <- raw_data[c(TRUE, FALSE)] + 1i * raw_data[c(FALSE, TRUE)]
dyns <- header$nechoes * header$nframes + header$nechoes

# Create array with dimensions
data <- array(data, dim = c(header$frame_size, dyns, coils, 1, 1, 1, 1))
test_array <- array(NA, dim = c(4096, 5, 32, 1, 1, 1, 1)) # Makes the same thingy.

# Transposit dimensions
data <- aperm(data, c(7,6,5,4,2,3,1))

# Remove something? - Removes one from the dyns - Dont know why
rem <- seq(from = 1, to = dyns, by = dyns / header$nechoes)

data2 <- data[,,,,-rem,,,drop = FALSE]

res <- c(NA, NA, NA, NA, 1, NA, 1 / header$spec_width)
freq_domain <- rep(FALSE, 7)

ref <- def_ref() # Default value for ppm scale
nuc <- def_nuc() # Default nucleus

# Some meta data?
meta <- list(EchoTime = header$te)



# Read data into class
mrs_data <- mrs_data_function(data = data, ft = header$ps_mps_freq / 10, resolution = res,
                              ref = ref, nuc = nuc, freq_domain = freq_domain,
                              affine = NULL, meta = meta, extra = NULL)



# ------------ Testing ------------- #

# Test extract raw data
for (i in 1:20){
  # Add data
  extracted_data <- data[c(1:40960),]

  # Remove data
  data <- data[-c(1:122880),]

  # Bind data
  new_data <- rbind(new_data, extracted_data)
}


# Try finding a pattern
# Find last zero
last_zero <- length(raw_data) - min(which(rev(raw_data) > 0 | rev(raw_data) <0)) + 1

# Subset
new_data <- raw_data[1:last_zero]

first_zero <- length(new_data) - min(which(rev(new_data) == 0)) + 1

#
n <- last_zero - first_zero


# ------------------ Functions ---------------- #

