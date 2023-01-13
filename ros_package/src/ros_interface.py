#!/usr/bin/env python3

# Python
import signal

# ROS
import rospy
from std_msgs.msg import Header, Bool, String

# Local
from ros_package.srv import BlahBlah, BlahBlahResponse
from core_functionality import MyClass


class ROSInterface:
    """
    ROSInterface is a class that provides a ROS wrapper for core_functionality.py
    
    Attributes:
        arg1 (type): Description of arg1
        arg2 (type): Description of arg2
    """
    def __init__(self, arg1, arg2):
        rospy.init_node('ros_interface', anonymous=False, log_level=rospy.INFO)

        self.arg1 = arg1
        self.arg2 = arg2

        # Wait for parameter
        while not rospy.has_param('example_param'):
            rospy.loginfo_throttle(30, "Waiting for example_param")

        self.arg3 = rospy.get_param('example_param')

        # Termination callbacks
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

        self.kill_now = False

        # Register Publisher
        self.output_pub = rospy.Publisher('/output', String, queue_size=1, latch=True)

        # Register Subscriber
        self.subscription = rospy.Subscriber("/should_i_die", Bool, self.subsciption_callback)

        # Register a Service
        self.service = rospy.Service('blah_service', BlahBlah, self.service_callback)
        self.servicable_value = False

        self.rate = rospy.Rate(1)


    def exit_gracefully(self, *args):
        self.kill_now = True


    def subsciption_callback(self, msg):
        self.kill_now = msg.data


    def service_callback(self, request):
        self.servicable_value = request.enable
        return BlahBlahResponse(True)


    def run(self):
        with MyClass(self.arg1, self.arg2, self.arg3) as instance:
            while not rospy.is_shutdown() and not self.kill_now:
                for item in instance:
                    string = f"{item} | Servicable Value: {self.servicable_value}"
                    rospy.loginfo(string)
                    self.output_pub.publish(string)

                    self.rate.sleep()



if __name__ == '__main__':
    try:
        ros_interface = ROSInterface("arg1", "arg2")
        ros_interface.run()
    except rospy.ROSInterruptException:
        pass
