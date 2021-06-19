#!/usr/bin/env python3

import os
import csv
import ssl
import json
import socket
import psutil
import smtplib
import logging
import subprocess
from sys import platform
from string import Template
from email import encoders
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if platform == "win32":
	import win32serviceutil

class ServiceStatusCheck():
	"""This class checks the services status on the os
	
	Variables:
		uninstalled_service_list {list} -- contains services which arev not 
										   present on OS. 
		stopped_service_list {list} -- contains services which are present but 
									   currently not running or stopped on OS.
		running_service_list {list} -- contains services which are present and 
									   running on OS.
	"""
	uninstalled_service_list = []
	stopped_service_list = []
	running_service_list = []
	running_process_list = []
	No_SuchProcess_List = []

	# MYADDRESS = 'mtaasdev@gmail.com'
	# PASSWORD = 'Password@123'
	

	def __init__(self):
		self.hostname = socket.gethostname()
		
		logging.basicConfig(filename='runtime.log',
			format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
			level=logging.DEBUG)
		
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Bot execution started")
	
	def read_file(self, filename):
		"""This method reads services from input file and return List of those 
		   services.
		
		Arguments:
			filename {[csv]} -- csv file containing services.
		
		Returns:
			[list] -- contains all services from csv file.
		"""
		service_list = []
		process_list = []
		with open(filename,'rt')as f:
			data = csv.reader(f)
		
			if platform == "win32":
				for row in data:
					service_list.append(row[0])
				service_list.pop(0)
				print(service_list)
				return service_list

			if platform == "linux" or platform == "linux2":
				for row in data:
					service_list.append(row[0])
					process_list.append(row[1])

				service_list.pop(0)
				process_list.pop(0)
				print(service_list)
				print(process_list)
				return service_list, process_list


	def list_to_mail(self):
		"""
		Write the stopped service list to csv file.
		"""

		if not os.path.exists('..//Output'):
			os.makedirs('..//Output')

		
		if platform == "win32":

			filename = '..//Output//message.txt'
			with open(filename, "w") as outfile:
				outfile.write("Hi ${PERSON_NAME},\n")
				outfile.write("\nFollowing services are not working on Windows host " + self.hostname)
				outfile.write("\n\nSTOPPED_SERVICES\n")
				for entries in self.stopped_service_list:
					outfile.write(entries)
					outfile.write("\n")
				outfile.write("\n\nUNAVAILABLE_SERVICES\n")
				for entries in self.uninstalled_service_list:
					outfile.write(entries)
					outfile.write("\n")
				outfile.write("\nThanks.\n")
		

		if platform == "linux" or platform == "linux2":
			filename = '..//Output//message.txt'
			with open(filename, "w") as outfile:
				outfile.write("Hi ${PERSON_NAME},\n")
				outfile.write("\nFollowing services and processes are not working on Linux host " +self.hostname)
				outfile.write("\n\nSTOPPED_SERVICES\n")
				for entries in self.stopped_service_list:
					outfile.write(entries)
					outfile.write("\n")
				outfile.write("\n\nUNAVAILABLE_PROCESSES\n")
				for entries in self.No_SuchProcess_List:
					outfile.write(entries)
					outfile.write("\n")
				outfile.write("\nThanks.\n")

	

	def check_linux_status(self, service_name):
		"""This method checks the status of services present in linux OS.
		
		Arguments:
			service_name {[string]} -- contains name of service for which we 
									   have to check it's status.
		
		Returns:
			[int] -- contains status of service.
		"""
		service_stats = None
		service_cmd = "systemctl show -p SubState "+service_name+ " | sed 's/SubState=//g'"
		try:
			proc = subprocess.Popen(args=service_cmd, stdout=subprocess.PIPE, shell=True)
			(service_stats, err) = proc.communicate()

			service_stats = str(service_stats, 'utf-8')
			service_stats = service_stats.strip()
			print(service_stats)
			print("check---->", service_stats)
			return service_stats	
		except Exception as e:
			print(str(e))
			self.uninstalled_service_list.append(service_name)
			print(service_name, "NOT installed")

	def checkIfProcessRunning(self, processName):
		'''
		Check if there is any running process that contains the given name 
		processName.
		'''
		for proc in psutil.process_iter():
			try:
			# Check if process name contains the given name string.
				if processName.lower() in proc.name().lower():
					self.running_process_list.append(processName)
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass

	def check_windows_status(self, service_name):
		"""This method checks the status of services present in window OS.
		
		Arguments:
			service_name {[string]} -- contains name of service for which we 
									   have to check it's status.
		
		Returns:
			[int] -- contains status of service.
		"""
		service_stats = None
		try:
			service_stats = win32serviceutil.QueryServiceStatus(service_name)
			print("check--->", service_stats[1])
			return service_stats[1]	
		except:
			self.uninstalled_service_list.append(service_name)
			print(service_name, "NOT installed")

	def get_contacts(self, filename):
		"""
		Return two lists names, emails containing names and email addresses
		read from a file specified by filename.
		"""
		
		names = []
		emails = []
		with open(filename, mode='r') as contacts_file:
			for a_contact in contacts_file:
				names.append(a_contact.split()[0])
				emails.append(a_contact.split()[1])
		return names, emails

	def read_template(self, filename):
		"""
		Returns a Template object comprising the contents of the 
		file specified by filename.
		"""
		
		with open(filename, 'r') as template_file:
			template_file_content = template_file.read()
		return Template(template_file_content)

	def read_counter_file(self):
		"""Reads polling_counter.json to find out polling counter
		
		[description]
		
		Returns:
			bool -- [description]
		"""
		with open("../Input/polling_counter.json") as f:
			self.polling_data = json.load(f)

		self.error_polling_count = self.polling_data['counter'] 


	def update_counter_file(self, reset=False):
		"""updating counter json file for checking polling 
		
		[description]
		
		Keyword Arguments:
			reset {bool} -- [if reset is false the counter will increase by 1
							if reset is true the counter will reset to 0
							] (default: {False})
		
		Returns:
			bool -- [If the counter file was updated]
		"""
		tmp = self.polling_data['counter']
		
		if not reset:
			self.polling_data['counter'] = self.error_polling_count + 1
			self.error_polling_count = self.error_polling_count + 1

		if reset:
			self.polling_data['counter'] = 0
			self.error_polling_count = 0

		with open("../Input/polling_counter.json", "w") as jsonFile:
			json.dump(self.polling_data, jsonFile)


	# def attatch_file(self, filename):
	# 	"""
	# 	Return file content in encode format which will be sent as an 
	# 	attatchment to mail.
		
	# 	Arguments:
	# 		filename {text} -- attatchment file that contain stopped services.
		
	# 	"""
		
	# 	# Open PDF file in binary mode

	# 	with open(filename, 'r') as attatchment:
	# 		# Add file as application/octet-stream
	# 		part = MIMEBase("application", "octet-stream")
	# 		part.set_payload(attatchment.read())

	#         # Encode file in ASCII characters to send by email
	# 		encoders.encode_base64(part)

	# 		# Add header as key/value pair to attachment part
	# 		part.add_header("Content-Disposition","attachment; filename= stopped_services.csv")
	# 	return part

	def send_mail(self):
		"""
		This function uses smtp library to sent mail about stopped services.
		"""

		if not self.is_email_eligible_time():
			self.logger.debug("Not sending email because duration \
				 is not breached. Last email sent at: " + 
				str(self.last_email_sent_at))
			return False
		with open("../Input/mail_details.json") as f:
			self.mail_details = json.load(f)
		message = """From: {} <{}>
To: MTaaS <{}>
CC: {}
Subject: Services stopped on {}

Hi,
Following services are stopped on the {} host:
{}
		""".format(	self.mail_details['from_name'],
					self.mail_details['from'],
					self.mail_details['to'],
					",".join(self.mail_details['cc']),
					self.hostname,
					self.hostname,
					str(self.stopped_service_list))
		
		try:
			# s = smtplib.SMTP(self.mail_details['smtpHost'])
			context = ssl.create_default_context()
			s = smtplib.SMTP_SSL(host = self.mail_details["smtpHost"],
							 port = self.mail_details["smtp_port"],
							 context = context)
			s.login(self.mail_details['from'], self.mail_details['passwd'])
			s.sendmail(self.mail_details['from'], self.mail_details['to'], message)         
			print ("Successfully sent email")
			self.update_last_email_sent()
			#Updating last email send timing
		except Exception as e:
			print(str(e))
			self.update_last_email_sent()
			print ("Error: unable to send email using gmail smtp host")
			self.logger.debug(str(e))
		# message_template = self.read_template('..//Output//message.txt')
		return True


	def check_last_email_sent(self):
		"""Reads the last_email_sent_at.json file and reads the last email time
		
		[description]
		"""
		with open("../Input/last_email_sent_at.json") as f:
			self.email_timing = json.load(f)

		self.last_email_sent_at = self.email_timing['last_email_time']
		return self.last_email_sent_at


	def update_last_email_sent(self):
		"""Updates the last email sent time to current time in last_email_sent_at
		.json file 
		
		"""
		# tmp = self.email_timing['last_email_time']
		now = datetime.now()
		current_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
		
		self.email_timing['last_email_time'] = current_datetime
		

		with open("../Input/last_email_sent_at.json", "w") as jsonFile:
			json.dump(self.email_timing, jsonFile)


	def is_email_eligible_time(self):
		"""Checks if the email sending time is eligible
		"""
		with open("../Input/mail_details.json") as f:
			mail_details = json.load(f)

		#Read duplication time from json file
		email_duplication_time = int(mail_details['email_duplication_time'])

		#Get last email sent time
		last_email_sent_time = self.check_last_email_sent()
		# convert to datetime object
		last_email_sent_time = datetime.strptime(last_email_sent_time,"%d/%m/%Y %H:%M:%S" )

		current_datetime = datetime.now()

		#Get the duration between current time and last sent time
		duration = current_datetime - last_email_sent_time
		
		duration_in_s = duration.total_seconds()
		self.duration_in_minutes = int(divmod(duration_in_s, 60)[0])

		#iF duration in minutes is less than the required time before resending the email
		# return false

		if self.duration_in_minutes < email_duplication_time:
			return False

		#return true in case the duplication time is breached
		return True
		


	def send_mail_local_smtp(self):
		"""This function is used to send out mail using simple smtp 
		
		[description]
		
		Returns:
			bool -- [description]
		"""
		# self.check_last_email_sent()
		if not self.is_email_eligible_time():
			self.logger.debug("Not sending email because duration \
				 is not breached. Last email sent at: " + 
				str(self.last_email_sent_at))
			return False

		with open("../Input/mail_details.json") as f:
			self.mail_details = json.load(f)
		message = """From: {} <{}>
To: MTaaS <{}>
CC: {}
Subject: Services stopped on {}

Hi,
Following services are stopped on the {} host:
{}
		""".format(	self.mail_details['from_name'],
					self.mail_details['from'],
					self.mail_details['to'],
					",".join(self.mail_details['cc']),
					self.hostname,
					self.hostname,
					str(self.stopped_service_list))
		
		try:
			s = smtplib.SMTP(self.mail_details['smtpHost'])
			s.sendmail(self.mail_details['from'], self.mail_details['to'], message)         
			print ("Successfully sent email")
			#Updating last email send timing
			self.update_last_email_sent()
		except Exception as e:
			print(str(e))
			self.update_last_email_sent()
			print ("Error: unable to send email")
			self.logger.debug(str(e))
		# message_template = self.read_template('..//Output//message.txt')
		return True


if __name__ == '__main__':
	"""This is main function which will execute first.
	
	"""
	status = ServiceStatusCheck()
	# status.send_mail_local_smtp()
	# import sys 
	# sys.exit()

	#Follwing code will be executed only in linux environment
	if platform == "linux" or platform == "linux2":
		

		status.logger.debug("Reading services file")
		service_list, process_list = status.read_file('..//Input//service_list.csv')
		service_list = list(filter(None, service_list))
		process_list = list(filter(None, process_list))
		for linux_service_name in service_list:
		
			status.logger.debug("checking linux services")
			service_status = status.check_linux_status(linux_service_name)

			if service_status == "running":
				status.running_service_list.append(linux_service_name)
			else:
				status.stopped_service_list.append(linux_service_name)
		
		for linux_process_name in process_list:
			status.checkIfProcessRunning(linux_process_name)
		

		process_list_set = set(process_list)
		running_Process_set = set(status.running_process_list)

		status.No_SuchProcess_List = list(sorted(process_list_set - running_Process_set))
		status.running_process_list = list(running_Process_set)

		print("Running process ---->", status.running_process_list)
		print("No_SuchProcess ----->", status.No_SuchProcess_List)

		status.list_to_mail()

		status.read_counter_file()
		
		if len(status.stopped_service_list) or len(status.uninstalled_service_list):
			status.logger.debug("updating COunter +1")
			status.update_counter_file()
		else:
			status.logger.debug("Resetting Counter")
			status.update_counter_file(reset=True)

		if status.error_polling_count > 1:
			status.logger.debug("More than one sample is postitive. Initiating email process")
			print("Going to check mail sending eligibiliity criteria")
			with open("../Input/mail_details.json") as f:
				mail_details = json.load(f)
			if mail_details['passwd'] == "":
				status.send_mail_local_smtp()
			else:
				status.send_mail()

		# if len(status.stopped_service_list) or len(status.No_SuchProcess_List):
		# 	status.send_mail()

	if platform == "win32":
		status.logger.debug("Reading services file")
		service_list = status.read_file('..//Input//service_list.csv')
		service_list = list(filter(None, service_list))
		for window_service_name in service_list:

			status.logger.debug("Checking service status")
			service_status = status.check_windows_status(window_service_name)
		
			if service_status == 4:
				status.running_service_list.append(window_service_name)
			if service_status == 1:
				status.stopped_service_list.append(window_service_name)

		status.list_to_mail()
		
		status.logger.debug("Reading counter file")
		status.read_counter_file()
		
		if len(status.stopped_service_list) or len(status.uninstalled_service_list):
			status.logger.debug("Updating counter file to +1")
			status.update_counter_file()
		else:
			status.logger.debug("Resetting Counter file")
			status.update_counter_file(reset=True)

		if status.error_polling_count > 1:
			status.logger.debug("More than one sample is postitive. Initiating email process")
			print("Going to check mail sending eligibiliity criteria")
			with open("../Input/mail_details.json") as f:
				mail_details = json.load(f)
			if mail_details['passwd'] == "":
				status.send_mail_local_smtp()
			else:
				status.send_mail()

		# if len(status.stopped_service_list) or len(status.uninstalled_service_list):
	
	print("stopped services -->", status.stopped_service_list)
	print("running services -->", status.running_service_list)
	print("uninstalled services -->", status.uninstalled_service_list)