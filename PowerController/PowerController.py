""" 
	Only For Windows

	comming soon
"""

import os
# import platform
		

class PowerController:
	"""docstring for PowerController"""
	def __init__(self, time):
		self.time = time
	

class Shutdown(PowerController):
	def shutdown(self):
		os.system(f'shutdown -s -t {str(self.time)}')


class Reboot(PowerController):
	def reboot(self):
		os.system(f'shutdown -r -t {str(self.time)}')


# if __name__ == '__main__':
# 	Shutdown(10).shutdown()
