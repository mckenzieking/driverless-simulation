# driverless-simulation
CSI 4999 Follow The Car Driverless Simulation

## Setup Instructions
### Install Ubuntu Virtual Machine
Follow instructions in .pdf slideshow located at driverless-simulation/documentation_of_sprint_work/ubuntu_vm_creation.pdf
### Install Robot Operating System (ROS)
Note: The version used in this project is ROS Noetic, which is compatible with Ubuntu 20.04 _only_. This script was made to simplify the install procedure. The normal installation instructions can be found [here](http://wiki.ros.org/noetic/Installation/Ubuntu)
1. Open the terminal application in your VM (or computer in general if you are choosing to dual-boot or use Ubuntu as your primary OS), install git and clone this repository onto your machine. 
2. Navigate to the setup_scripts folder of this repository.
3. Type `chmod +x ros_install.sh` into the terminal and hit enter
4. Type `sudo ./ros_install.sh`. It will prompt you to enter your password.

This will begin the installation of ROS
