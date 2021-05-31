# Load the libraries
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)

# Global variables
PATH_RAW_DATA <-  ""
PATH_LISTP <-  ""

# Initialize a list to store the charts
listP <- list()

# Read the data
raw_data <- read_csv(PATH_RAW_DATA)

# Process the data
data_claned <- raw_data

# Create charts

# Export the charts
saveRDS(listP, PATH_LISTP)
