import sys
import psutil
import os
import logging
import socket
import subprocess
import multiprocessing
from math import ceil
sys.path.insert(0, os.environ["Admin_Root"]+"/zabbix/Lib/uistatus")
from uistatus import sendstatus


class prechecks():
	
	def __init__(self):
		self.sendstatus = sendstatus()

	def api_call(self,ToolName,Component,ServerFQDN,ServerType,Environment):
		self.msg = {"ToolName": ToolName, "Component": Component, "ServerFQDN": ServerFQDN, "ServerType": ServerType,
		"Environment": Environment, "Stage": "1", "Status": "1", "StatusReason": "Initiated Alerts"}

	def memory_check(self,input_val):
		try :
			self.msg["StatusReason"] = "Memory check Initiated on {ServerType} {Component}".format(ServerType=self.msg["ServerType"],Component=self.msg["Component"])
			self.msg["Status"] = 1
			self.sendstatus.send_logs([self.msg])
			
			mem = psutil.virtual_memory().total >> 30
			if mem >= int(input_val):
				self.msg["StatusReason"] = "Memory check passed"
				self.msg["Status"] = 2
				self.sendstatus.send_logs([self.msg])
				
				return True
			else:
				self.msg["StatusReason"] = "Memory check failed required Memory is {in_val} and found {mem} instead".format(in_val=input_val, mem=mem)
				self.msg["Status"] = 3
				self.sendstatus.send_logs([self.msg])
				
				return False
		except Exception as e:
			self.msg["StatusReason"] = "Something failed during memory check"
			self.msg["Status"] = 3
			self.sendstatus.send_logs([self.msg])
			
			return False


	def port_check(self,port):
		try:
			self.msg["StatusReason"] = "Port check Initiated on {ServerType} {Component}".format(ServerType=self.msg["ServerType"],Component=self.msg["Component"])
			self.msg["Status"] = 1
			self.sendstatus.send_logs([self.msg])
			
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex(('127.0.0.1',int(port)))
			if result == 0:
				self.msg["StatusReason"] = "Port check passed"
				self.msg["Status"] = 2
				self.sendstatus.send_logs([self.msg])
				
				return True
			else :
				self.msg["StatusReason"] = "Port check failed"
				self.msg["Status"] = 3
				self.sendstatus.send_logs([self.msg])
				
				return False
		except Exception as e:
			self.msg["StatusReason"] = "Something failed during port check"
			self.msg["Status"] = 3
			self.sendstatus.send_logs([self.msg])
			
			return False


	def disk_check(self,dirname,disk_size):
		try:
			self.msg["StatusReason"] = "Disk check Initiated on {ServerType} {Component}".format(ServerType=self.msg["ServerType"],Component=self.msg["Component"])
			self.msg["Status"] = 1
			self.sendstatus.send_logs([self.msg])
			dir_first = dirname.split('/')
			mount = subprocess.getoutput('ls /')
			# print(mount)
			if dir_first[0] in mount:
				fs = "/" + dirname
				st = os.statvfs(fs)
				ldisk = int(round((st.f_bavail * st.f_frsize / 1024 / 1024) / 1024))
				if int(ldisk) >= int(disk_size):
					self.msg["StatusReason"] = "Disk check passed"
					self.msg["Status"] = 2
					self.sendstatus.send_logs([self.msg])
					
					return True
				else : 
					self.msg["StatusReason"] = "Disk check failed, required disk is {disk_size} and found {ldisk} instead".format(disk_size=disk_size, ldisk=int(ldisk))
					self.msg["Status"] = 3
					self.sendstatus.send_logs([self.msg])
					
					return False
			else:
				self.msg["Status"] = 3
				self.msg["StatusReason"] = "Something failed during disk check"
				self.sendstatus.send_logs([self.msg])
				
				return False

		except Exception as e:
			self.msg["StatusReason"] = "Something failed during disk check"
			self.msg["Status"] = 3
			self.sendstatus.send_logs([self.msg])
			
			return False

	def sql_check(self):
		try:
			self.msg["StatusReason"] = "SQL check Initiated on {ServerType} {Component}".format(ServerType=self.msg["ServerType"],Component=self.msg["Component"])
			self.msg["Status"] = 1
			self.sendstatus.send_logs([self.msg])
			
			service=subprocess.getoutput("service mysqld status")
			if "running" in service or os.path.exists("/etc/mysql") or os.path.exists("/var/lib/mysql") or os.path.exists("/var/db/mysql"):
				self.msg["StatusReason"] = "SQL check failed, uninstall sql and clean"
				self.msg["Status"] = 3
				self.sendstatus.send_logs([self.msg])
				
				return False
			else : 
				self.msg["StatusReason"] = "SQL check passed"
				self.msg["Status"] = 2
				self.sendstatus.send_logs([self.msg])
				
				return True

		except Exception as e:
			self.msg["StatusReason"] = "Something failed during SQL check"
			self.msg["Status"] = 3
			self.sendstatus.send_logs([self.msg])
			
			return False

	def cpu_check(self,input_val):
		try:
			self.msg["StatusReason"] = "CPU check Initiated on {ServerType} {Component}".format(ServerType=self.msg["ServerType"],Component=self.msg["Component"])
			self.msg["Status"] = 1
			self.sendstatus.send_logs([self.msg])
			
			cpu_count = multiprocessing.cpu_count()
			if int(cpu_count)>=int(input_val):
				self.msg["StatusReason"] = "CPU check passed"
				self.msg["Status"] = 2
				self.sendstatus.send_logs([self.msg])
				
				return True
			else : 
				self.msg["StatusReason"] = "CPU check failed, required {input_val} found {cpu_count}".format(input_val=input_val,cpu_count=cpu_count)
				self.msg["Status"] = 3
				self.sendstatus.send_logs([self.msg])
				
				return False

		except Exception as e:
			self.msg["StatusReason"] = "Something failed during CPU check"
			self.msg["Status"] = 3
			self.sendstatus.send_logs([self.msg])
			
			return False

	def os_check(self,os_list):
			
		try:
			self.msg["StatusReason"] = "OS check Initiated on {ServerType} {Component}".format(ServerType=self.msg["ServerType"],Component=self.msg["Component"])
			self.msg["Status"] = 1
			self.sendstatus.send_logs([self.msg])
			platforms = {'linux1' : 'Linux', 'linux2' : 'Linux', 'win32' : 'Windows','linux':'Linux'}
			else_check = 1
			
			if sys.platform  in platforms.keys():
				if platforms[sys.platform] == "Linux":
					version = subprocess.getoutput('cat /etc/os-release | grep "VERSION_ID" | cut -d "=" -f2')
					version = float(version.strip('\'"'))
					if str(version) in os_list:
						self.msg["StatusReason"] = "OS check passed, "
						self.msg["Status"] = 2
						self.sendstatus.send_logs([self.msg])
						else_check = 0
						return True

			if else_check == 1:
				self.msg["StatusReason"] = "Unsupported OS"
				self.msg["Status"] = 3
				self.sendstatus.send_logs([self.msg])
				return False
		except Exception as e:
			# print(str(e))
			self.msg["StatusReason"] = "Unsupported OS"
			self.msg["Status"] = 3
			self.sendstatus.send_logs([self.msg])			
			return False


# if __name__ == "__main__":

# 	check = prechecks()
# 	check.api_call("Moogsoft","DB","ptest0134","primary","nonProd")
# 	# check.memory_check(10)
# 	# check.port_check(33)
# 	# check.disk_check("root",100)
# 	# check.sql_check()
# 	# check.cpu_check(4)
# 	check.os_check(["7.3","7.2"])


