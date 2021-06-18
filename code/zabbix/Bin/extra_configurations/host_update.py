
#!/usr/bin/python

"""
This script create update hosts on zabbix sever
to that 

@USAGE: python host_update.py {zabbix_reporting_url}
@AUTHOR: satyam.s / k.satish
@Date: 
@Update Date : 14/08/2020

"""
import os
import sys
import json
import logging
import datetime
# import commands
import subprocess


try:
	from pyzabbix import ZabbixAPI, ZabbixAPIException
except:
	# status,out=os.getstatusoutput('pip install pyzabbix')
	pass

#lib for https 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ZabbixHost():
	"""This class handles the registration  of zabbix host on the console """
	def __init__(self, zabbix, template, hostgroup,host):
		"""Constructor function for zabbixhost class
		
		Arguments:
			zabbix {string} -- zabbix ui ip
			template {string} -- naem of the template
			hostgroup {[type]} -- name of the hostgroup
		"""
		self.username = "Admin"
		self.password = "testing123"
		self.host = host
		self.zabbix_ui_ip = zabbix
		self.template = template # This should exist in zabbix
		self.hostgroup = hostgroup #This should exist in zabbix
		
	def login(self):
		"""logs in to the zabbix server API
		"""
		
		self.zapi = ZabbixAPI("https://{}/zabbix".format(self.zabbix_ui_ip))
		self.zapi.session.verify = False
		self.zabbix = self.zapi.login(self.username, self.password) 
	
	def search_template(self):
		"""Search for template id by template name
		"""
		# print(self.template)
		self.template_data = self.zapi.template.get(filter=({'host':self.template}))

		
	def search_hostgroup(self):
		"""search for hostgroup ip by name
		"""
		self.grouplookup = self.zapi.hostgroup.get(filter=({'name':self.hostgroup}))

	def search_hostid(self):
		"""search for hostgroup ip by name
		"""
		# print(self.host)
		self.hostid = self.zapi.host.get(filter=({'host':self.host}))
		# print(self.groupid)

	def update_host(self):
		"""update host 
		"""
		request_data = {
						"hostid":self.hostid[0]['hostid'],
						"templates": [
							{
							"templateid" : self.template_data[0]['templateid'],
							}
						],	
					}
		print(request_data)

		response = self.zapi.host.update(request_data)

#main function 

if __name__ == '__main__':
	"""[summary]
	
	[description]
	"""
	#TODO : Add functionality to take input from command line

	# command_arg = sys.argv
	# # zabbx_ui = 'ptest0100'
	# zabbix_ui = command_arg[1]
	# # template_name = 'MoogsoftDBTemplate'
	# template_name = command_arg[2]
	# host = command_arg[3]
	# hostgroup = 'moogsoft-self-health'

	#hostgroup = 'Zabbix servers'

	#getting data template link data from json file.
	with open('linktemplate.json') as data_file:
		data = json.load(data_file)

	zabbix_ui = data['ip']
	template_name = data['templatename']
	hostgroup =  data['hostgroup']
	host = data['host']

	#host = ZabbixHost('10.1.150.234','Auto fuzzytime trigger for Zabbix Proxy','Zabbix servers','ptest0016')
	
	host = ZabbixHost(zabbix_ui, template_name, hostgroup,host)

	host.login()
	host.search_template()
	# host.search_hostgroup()
	host.search_hostid()
	host.update_host()
