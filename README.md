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

This will begin the installation of ROS. This may take up to 45 minutes depending on your internet connection.

## Running the Mock-Up Simulation
This start-up routine will not be this involved once ROS is integrated, since this is a stand-alone model, there is a bit more of a process to get it running.
1. Open a terminal window, type `gazebo` and hit enter.
2. Click on the Insert tab on the left side of the window.
3. Select Add Path and navigate to driverless-simulation/mock_ups/model_editer_models and hit Ok.
4. From this path, click on the test_vehicle option then click into the scene. This will add the vehicle to the simulated world.
5. From this same path, select test_box then click into the scene just as before, but try to place the box directly in front of the side of the vehicle with the camera (piece that is cube shaped).
6. Hit the play button at the bottom of the screen

You should see the robot moving toward the box automatically based on the camera sensor. If the robot does not seem to be moving, try repositioning the cube by hitting the move icon at the top, then dragging the cube.
More info will be found in the ReadMe located within the mock-up file path.
