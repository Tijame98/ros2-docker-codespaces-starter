import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StatusSubscriber(Node):
    def __init__(self):
        super().__init__("status_subscriber")
        self.subscription = self.create_subscription(
            String,
            "robot/status",
            self.status_callback,
            10
        )

    def status_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = StatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    #mkdir -p ros2_ws/src/robot_status_demo/launch