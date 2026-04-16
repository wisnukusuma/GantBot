## Gantry Robot for simulation
Presequite :
- Ubuntu 22.04
- ROS 2 Distro (Humble Hawksbill) 
- Gazebo (Classic)

Robot Model:
![Gazebo (Ubuntu-22 04) 2026-04-14 16-17-02](https://github.com/user-attachments/assets/6ade5d47-6a3b-473f-83a5-0377da472f0e)


Test move the robot move to (0.2 , 0 , 0.1) :
```
ros2 topic pub /gantry_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['x_joint', 'y_joint', 'z_joint'],
  points: [
    {
      positions: [0.2, 0.0, 0.1],
      velocities: [0.0, 0.0, 0.0],
      time_from_start: {sec: 2}
    }
  ]
}"
```