# TurtleBot3
<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/turtlebot3/logo_turtlebot3.png" width="300">

To aggregate these simulations copy the folder `turtlebot3_gazebo` to your `turtlebot3_simulations` folder to merge the files.

In the folder `scripts` are Python programs that we use to create the `model.sdf` file of the circuits. You can modify the parameters to create other circuits with diferent sizes but with the same structure.

These resouces are part of a master's thesis where we use the Python [fuzzylab](https://github.com/ITTcs/fuzzylab) library to create fuzzy logic controlers with the implementation of deep reinforcement learning algorithms.

To use these resources, you first need to setup your PC following these tutorials:

1. [Install Gazebo using Ubuntu packages](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install)

2. [PC Setup](http://emanual.robotis.com/docs/en/platform/turtlebot3/pc_setup/)

3. [Simulation](http://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)

You can apply deep reinforcement learning algorithms in the robot navigation training from [OpenAI Baselines](https://github.com/openai/baselines) and [Stable Baselines](https://github.com/hill-a/stable-baselines) to these environments with the library [gym-turtlebot3](https://github.com/ITTcs/gym-turtlebot3). Check the examples of the library.

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

To cite this repository in publications:

    @misc{turtlebot3environments,
      author = {Avelar, Eduardo},
      title = {Research Gazebo environments for TurtleBot3 robot},
      year = {2019},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/ITTcs/turtlebot3_simulations}},
    }

