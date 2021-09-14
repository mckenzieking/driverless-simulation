# Simulation Mock-Up
![Image of sim](https://github.com/mckenzieking/driverless-simulation/blob/main/mock_ups/demo_image.png)
Information on how to use these mock-up model files is available on the main README.md file.
The test_vehicle model is an articulated simplistic model of a car. It has two rotating wheels at the front as well as a caster (represented as a ball joint) at the rear. 
There is a depth camera at the front of the vehicle, much like what we will have in the full version of the project.
Currently the controls code is a gazebo plugin that detects depth from the attached camera and moves it toward whatever object is in front of it within a certain range.
This mock-up was done with the help of a guided gazebo tutorial.
