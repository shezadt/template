# Download Chrome, VScode, Anaconda, RStudio

# R

    # Install R on Ubuntu 22.04
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo gpg --dearmor -o /usr/share/keyrings/r-project.gpg
echo "deb [signed-by=/usr/share/keyrings/r-project.gpg] https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/" | sudo tee -a /etc/apt/sources.list.d/r-project.list
sudo apt update
sudo apt install --no-install-recommends r-base

    # Install dependencies required to install R packages such as tidyverse
sudo apt-get install build-essential
sudo apt-get install libssl-dev
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libxml2-dev
sudo apt-get install libfontconfig1-dev
sudo apt-get install libcairo2-dev

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
