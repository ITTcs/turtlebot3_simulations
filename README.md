# TurtleBot3
<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/turtlebot3/logo_turtlebot3.png" width="300">

To aggregate these simulations copy the folder `turtlebot3_gazebo` to your `turtlebot3_simulations` folder to merge the files.

In the folder `scripts` are Python programs that we use to create the `model.sdf` file of the circuits. You can modify the parameters to create other circuits with diferent sizes but with the same structure.

These resouces are part of a master's thesis where we use the Python [fuzzylab](https://github.com/ITTcs/fuzzylab) library to create fuzzy logic controlers with the implementation of deep reinforcement learning algorithhms.

## Gazebo stages

**turtlebot3_circuit_left_right_turns**: a 5x5 stage based on the gym-gazebo  GazeboCircuit2TurtlebotLidar env.

```
roslaunch turtlebot3_gazebo turtlebot3_circuit_left_right_turns.launch
```

<img src="images/turtlebot3_circuit_left_right_turns.jpg" width="400">

**turtlebot3_circuit_simple**: a 3x3 stage.

```
roslaunch turtlebot3_gazebo turtlebot3_circuit_simple.launch
```

<img src="images/turtlebot3_circuit_simple.jpg" width="400">

**turtlebot3_stage_1_eavelar**: a 1.8x1.8 stage based on the turtlebot3_stage_1.

```
roslaunch turtlebot3_gazebo turtlebot3_stage_1_eavelar.launch
```

<img src="images/turtlebot3_stage_1_eavelar.jpg" width="400">

This is a simple stage for simple real tests.

<img src="images/real_turtlebot3_stage_1_eavelar.jpg" width="400">
