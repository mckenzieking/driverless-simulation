#!/bin/sh

# Run this script as sudo with command "sudo ./ros_install.sh"

# Insall ROS
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
apt update
pt install ros-noetic-desktop-full

# Source noetic
source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Deps
apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
apt install python3-rosdep
rosdep init
sudo -u username rosdep update