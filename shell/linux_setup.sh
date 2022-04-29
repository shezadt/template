# Download Chrome, VScode, Anaconda, RStudio

# R

    # Install R on Ubuntu 20.04
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt update
sudo apt install r-base

    # Install dependencies required to install R packages such as tidyverse
sudo apt-get install libssl-dev
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libxml2-dev 

# PYTHON

    # Create a virtual environnement called ds_env
conda create -n ds_env python=3.9 numpy pandas scikit-learn jupyter seaborn

# GIT

    # Install
sudo apt install git

    # Config
git config --global user.name "shezadt"
git config --global user.email "shezad.t*@gmail.com"

# VIRTUAL BOX

    # Shared folder access
sudo apt-get install virtualbox-guest-utils
sudo adduser $USER vboxsf

# FONTS
sudo apt install fonts-firacode

# SYSTEM
sudo apt install htop