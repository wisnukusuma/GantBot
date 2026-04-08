#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class JointBridge(Node):
    def __init__(self):
        super().__init__('joint_bridge')
        self.joint_state_subscriber = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )
        self.joint_trajectory_publisher = self.create_publisher(
            JointTrajectory,
            '/joint_trajectory',
            10
        )

    def joint_state_callback(self, msg):
        joint_trajectory_msg = JointTrajectory()
        joint_trajectory_msg.header.stamp = self.get_clock().now().to_msg()
        joint_trajectory_msg.joint_names = msg.name
        point = JointTrajectoryPoint()
        point.positions = msg.position
        point.velocities = [0.0] * len(msg.position)  # Set velocities to zero
        point.time_from_start.sec = 1  # Set a time from start (e.g., 1 second)
        joint_trajectory_msg.points.append(point)
        
        self.joint_trajectory_publisher.publish(joint_trajectory_msg)
    
def main():
    rclpy.init()
    joint_bridge = JointBridge()
    rclpy.spin(joint_bridge)

if __name__ == '__main__':
    main()

