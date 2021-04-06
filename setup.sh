#!/bin/bash

# exit when any command fails
set -e

# setup directory constants
VRC_P1_DIR=~/Documents/vrc_phase1
VENV_P1_DIR=~/Documents/vrc_phase1/.venv

# create a little command to print out a bar
bar() {
    echo "============================================"
}

# check to make sure code has already been cloned
if [[ ! -d $VRC_P1_DIR ]]; then
    echo "VRC repository has not been cloned to $VRC_P1_DIR"
    echo "Do this with 'sudo apt update && sudo apt install -y git && git clone https://github.com/bellflight/VRC-2021-Phase-I $VRC_P1_DIR --recurse-submodules'"
    exit 1
fi

bar

echo "Updating system package index"
bar
sudo apt update
bar

echo "Upgrading system packages"
bar
# upgrade existing packages
sudo apt upgrade -y
# autoremove a bunch
sudo apt autoremove -y
bar

echo "Installing prerequisites"
bar
# install some useful prereqs
sudo apt install git make apt-utils software-properties-common wget unzip htop nano -y

cd $VRC_P1_DIR
# cache the git credentials (mainly during development)
git config --global credential.helper cache
# updates submodules
git submodule update --init --recursive
# update repo
git pull --recurse-submodules
bar

echo "Installing Python 3.8"
bar
# Add deadsnakes PPA to sources
echo | sudo add-apt-repository ppa:deadsnakes/ppa
# Install Python 3.8
sudo apt install -y python3.8 python3.8-dev python3.8-venv python3-pip python3-dev

# add Python 3.8 as a python3 alternative
# $s update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
# set it as the default
# $s update-alternatives --set python /usr/bin/python3.8

# upgrade pip
python3 -m pip install pip --upgrade
bar

echo "Creating Python virtual environment"
bar
# this doesn't overwrite it if it already exists
python3.8 -m venv $VENV_P1_DIR --prompt "VRC Phase 1"
echo "Environment created at $VENV_P1_DIR"
echo "Activate this environment with 'source $VENV_P1_DIR/bin/activate'"
bar

echo "Final Setup"
bar
# install jtop and nano text editor
sudo -H python3 -m pip install -U jetson-stats
sudo apt install nano
bar

echo "Installing final utilities"
bar
# install jtop
sudo -H python3 -m pip install -U jetson-stats
bar

echo "VRC Phase 1 finished setting up!"
bar
