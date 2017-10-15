pepper_teleop
================

Simple Pepper Teleoperation implementation based on turtlebot one.

raw version. Test only in ubuntu 14.04, ros indigo

##add to your catkin_ws and compile
dependecies to roscpp, geometry_msgs, naoqi_bridge_msgs, joy

##Launch joy for teleop 
roslaunch pepper_teleop pepper_ps3_teleop.launch

configuration can be change in launch file with parameter
by default joy    has to be mount as /dev/input/js0

