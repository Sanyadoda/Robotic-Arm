#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pyModbusTCP.client import ModbusClient
from sensor_msgs.msg import FluidPressure

# Using https://pypi.org/project/pyModbusTCP/ for reference and sample code

def publish_node():
  length= len(msg.fluid_pressure)
  pub = rospy.Publisher('Transducer', FluidPressure)
  rospy.init_node('publish_node', anonymous=True)
  rate = rospy.Rate(1) # 1Hz
  while not rospy.is_shutdown():
    pub.publish(msg.fluid_pressure)
    rate.sleep()
  msg.ack()
 
def callback(msg)
   while not rospy.is_shutdown():
     print(msg.fluid_pressure)

if __name__ == '__main__':
	try:
		print("Hello, world!")
		c = ModbusClient()
		c.host("192.168.1.200")
		c.port(502)
		c.open()
		regs = c.read_holding_registers(518, 2)
		if regs:
			print(regs)
			rospy.init_node('Transducer', anonymous=True)
			sub = rospy.Subscriber('Pressure', FluidPressure, callback)
			publish_node()
		else:
			print("read error")	
		
    			
		
		rospy.spin()
		print("\nGoodbye, world!")
	except rospy.ROSInterruptException:
		pass
