#!/bin/bash

# exit when any command fails
set -e

# setup directory constants
VRC_P1_DIR=~/Documents/VRC-2021-Phase-I
VENV_P1_DIR=~/Documents/VRC-2021-Phase-I/.venv

# create a little command to print out a bar
bar() {
    echo "============================================"
}

# colors
RED='\033[0;31m'
LIGHTRED='\033[1;31m'
GREEN='\033[0;32m'
LIGHTGREEN='\033[1;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# check to make sure code has already been cloned
if [[ ! -d $VRC_P1_DIR ]]; then
    echo "VRC Phase 1 repository has not been cloned to $VRC_P1_DIR"
    echo "Do this with 'sudo apt update && sudo apt install -y git && git clone https://github.com/bellflight/VRC-2021-Phase-I $VRC_P1_DIR --recurse-submodules'"
    exit 1
fi

echo -e "${RED}"                                                                          
echo "██████████████████████████████████████████████████████████████████████████"
echo -e "█████████████████████████████████████████████████████████████████████${NC}TM${RED}███"
echo "█████▌              ▀████            ████     ██████████     █████████████"
echo "███████▄▄▄  ▄▄▄▄     ▐███    ▄▄▄▄▄▄▄▄████     ██████████     █████████████"
echo "████████▀   █████    ████    ▀▀▀▀▀▀▀▀████     ██████████     █████████████"
echo "████████            ▀████            ████     ██████████     █████████████"
echo "████████    ▄▄▄▄▄     ███    ████████████     ██████████     █████████████"
echo "████████    ████▀     ███    ▀▀▀▀▀▀▀▀████     ▀▀▀▀▀▀▀███     ▀▀▀▀▀▀▀▀█████"
echo "████████             ▄███            ████            ███             █████"
echo "████████▄▄▄▄▄▄▄▄▄▄▄██████▄▄▄▄▄▄▄▄▄▄▄▄████▄▄▄▄▄▄▄▄▄▄▄▄███▄▄▄▄▄▄▄▄▄▄▄▄▄█████"
echo "██████████████████████████████████████████████████████████████████████████"
echo "                                                                          "
echo "██████████████████████████████▄▄          ▄▄██████████████████████████████"
echo "██████████████████████████████████▄    ▄██████████████████████████████████"
echo "████████████████████████████████████  ████████████████████████████████████"
echo "███▀▀▀▀▀██████████████████████████▀    ▀██████████████████████████▀▀▀▀▀███"
echo "████▄▄          ▀▀▀▀█████████████        █████████████▀▀▀▀          ▄▄████"
echo "████████▄▄▄                ▀▀▀▀▀██████████▀▀▀▀▀                ▄▄▄████████"
echo "█████████████▄▄                   ▀████▀                   ▄▄█████████████"
echo "█████████████████▄                  ██                  ▄█████████████████"
echo "██████████████████████████████▀     ██     ▀██████████████████████████████"
echo "███████████████████████▀▀           ██           ▀▀███████████████████████"
echo "████████████████▀▀▀                 ██                 ▀▀▀████████████████"
echo "█████████▀▀                       ▄████▄                       ▀▀█████████"
echo "████▀▀                         ▄███▀  ▀███▄                         ▀▀████"
echo " ████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█████▀      ▀█████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████ "
echo " ▀███████████████████████████████▄      ▄███████████████████████████████▀ "
echo "  ▀████████████████████████████████    ████████████████████████████████▀  "
echo "    ██████████████████████████████▀    ▀██████████████████████████████    "
echo "     ▀████████████████████████████▄    ▄████████████████████████████▀     "
echo "       ▀███████████████████████████    ███████████████████████████▀       "
echo "         ▀█████████████████████████    █████████████████████████▀         "
echo "           ▀███████████████████████    ███████████████████████▀           "
echo "             ▀█████████████████████    █████████████████████▀             "
echo "               ▀███████████████████    ███████████████████▀               "
echo "                 ▀█████████████████    █████████████████▀                 "
echo "                    ▀██████████████    ██████████████▀                    "
echo "                      ▀████████████    ████████████▀                      "
echo "                        ▀██████████    ██████████▀                        "
echo "                           ▀███████    ███████▀                           "
echo "                             ▀▀████    ████▀▀                             "
echo "                                ▀███  ███▀                                "
echo "                                  ▀█▄▄█▀                                  "
echo -e "${NC}"


bar


echo -e "${CYAN}Updating system package index${NC}"
bar
sudo apt update
bar


echo -e "${CYAN}Upgrading system packages${NC}"
bar
# upgrade existing packages
sudo apt upgrade -y
# autoremove a bunch
sudo apt autoremove -y
bar


echo -e "${CYAN}Installing prerequisites${NC}"
bar
# install some useful prereqs
sudo apt install -y git make apt-utils software-properties-common wget unzip htop nano

cd $VRC_P1_DIR
# cache the git credentials (mainly during development)
git config --global credential.helper cache
# updates submodules
git submodule update --init --recursive
# update repo
git pull --recurse-submodules
bar


echo -e "${CYAN}Installing Python 3.8${NC}"
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


echo -e "${CYAN}Creating Python virtual environment${NC}"
bar
# this doesn't overwrite it if it already exists
python3.8 -m venv $VENV_P1_DIR --prompt "VRC Phase 1"
# update pip
source $VENV_P1_DIR/bin/activate
python -m pip install pip --upgrade
deactivate

echo "Environment created at $VENV_P1_DIR"
echo -e "Activate this environment with '${LIGHTGREEN}source $VENV_P1_DIR/bin/activate${NC}'"
bar


echo -e "${CYAN}Installing mavp2p${NC}"
bar
cd ~/Documents
# download premade release from github
wget https://github.com/aler9/mavp2p/releases/download/v0.6.5/mavp2p_v0.6.5_linux_arm64.tar.gz
tar -xzvf mavp2p_v0.6.5_linux_arm64.tar.gz
rm mavp2p_v0.6.5_linux_arm64.tar.gz

# move binary to usr/local/bin so it's in PATH
sudo mv mavp2p /usr/local/bin/

# remove old service file, skip if doesn't exist
mavp2p_service_file=/etc/systemd/system/mavp2p.service

if [ -f $mavp2p_service_file ] ; then
    sudo rm $mavp2p_service_file
fi

# write new service file
{
    echo '[Unit]'
    echo 'Description=mavp2p service'
    echo ''
    echo '[Service]'
    echo 'Type=simple'
    echo 'Restart=on-failure'
    # this config:
    # - listens on 14550 for QGC with UDP
    # - listens on 5790 for QGC with TCP (I've found more reliable)
    # - connects on serial to pixhawk
    # - connects 14541 to VMC 
    echo 'ExecStart=/usr/local/bin/mavp2p udps:0.0.0.0:14550 tcps:0.0.0.0:5790 serial:/dev/ttyTHS1:500000 udpc:127.0.0.1:14541'
    echo ''
    echo '[Install]'
    echo 'WantedBy=multi-user.target'
} | sudo tee -a $mavp2p_service_file > /dev/null
# https://stackoverflow.com/a/17491223

# reload systemctl
sudo systemctl daemon-reload
# enable the service
sudo systemctl enable mavp2p.service
sudo systemctl start mavp2p.service

bar


echo -e "${CYAN}Installing final utilities${NC}"
bar
# install jtop
sudo -H python3 -m pip install -U jetson-stats
bar


echo -e "${GREEN}VRC Phase 1 finished setting up!${NC}"
bar
