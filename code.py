#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pyModbusTCP.client import ModbusClient

# Using https://pypi.org/project/pyModbusTCP/ for reference and sample code

if __name__ == '__main__':
	try:
		print("Hello, world!")
		c = ModbusClient()
		c.host("192.168.1.200")
		c.port(502)
		c.open()
		regs = c.read_holding_registers(518, 8)
		if regs:
			print(regs)
		else:
			print("read error")	
		rospy.init_node('monitor_driver', anonymous=True)
		rospy.spin()
		print("\nGoodbye, world!")
	except rospy.ROSInterruptException:
		pass
