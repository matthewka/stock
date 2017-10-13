import os
import time
import datetime
import inspect


class Log:

	file_name = "logfile.log"

	def __init__(self):

		self.DEBUG = True
		self.VERBOSE = False

		# if len(file_name) > 0:
		# 	self.file_name = file_name
		# else:
		# 	start_time = datetime.datetime.today()
		# 	self.file_name = file_name + str(start_time) + ".log"

		# print("log file: " + file_name)
		if os.path.isfile(self.file_name):
			self.f = os.open(self.file_name, os.O_RDWR | os.O_APPEND)
		else:
			self.f = os.open(self.file_name, os.O_RDWR|os.O_CREAT)


	def logd(self, message):
		if self.DEBUG:
			self.log("{D} " + str(message))
		else:
			return

	def logv(self, message):
		if self.VERBOSE:
			self.log("{V} " + str(message))
		else:
			return

	def loge(self, message):
		self.log("{E} " + str(message))

	def log(self, message):
		caller = inspect.stack()[2][1] + ":" + str(inspect.stack()[2][2])
		logtime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		logMessage = caller + " [" + logtime +"]: " + message + "\n"
		print(logMessage)
		os.write(self.f, logMessage.encode("UTF-8"))


