# Download Chrome, VScode, Anaconda, RStudio

# R

    # Install dependencies required to install R packages such as tidyverse
sudo apt-get install libssl-dev
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libxml2-dev 

# PYTHON

    # Create a virtual environnement called ds_env
conda create -n ds_env python=3.9 numpy pandas scikit-learn jupyter seaborn

# GIT
sudo apt install git

# VIRTUAL BOX

    # Shared folder access
sudo apt-get install virtualbox-guest-utils
sudo adduser $USER vboxsf

# FONTS
sudo apt install fonts-firacode