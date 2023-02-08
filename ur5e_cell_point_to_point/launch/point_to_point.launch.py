from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder(robot_name="ur5e_workcell_fake", package_name="ur5e_cell_moveit_config").to_moveit_configs()

    # MoveGroupInterface demo executable
    point_to_point_demo = Node(
        name="p2p_node",
        package="ur5e_cell_point_to_point",
        executable="point_to_point_node",
        output="screen",
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
        ],
    )

    return LaunchDescription([point_to_point_demo])