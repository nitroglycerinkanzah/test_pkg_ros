#write your python code here 
import rclpy
from rclpy.node import Node


def main(args=None):

  rclpy.init(args=args)
  print('*******************************************************************')
  print("Code Time ")
  print('*******************************************************************')


# shutdown the ROS communication
  rclpy.shutdown()

if __name__ == '__main__':
  main() #call the main function
