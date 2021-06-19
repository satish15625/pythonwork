
# Referenced From https://www.zabbix.com/documentation/4.2/manual/api/reference/action/object
# https://www.zabbix.com/documentation/4.2/manual/api/reference/action/create
# In order to make any changes please refer to the documentation above


import sys
from pyzabbix import ZabbixAPI
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ZabbixOnboarding():
	"""docstring for ZabbixOnboarding"""
	def __init__(self, hostname):

		self.zapi = ZabbixAPI("https://{}/zabbix".format(hostname))
		self.zapi.session.verify = False
		self.zapi.login("Admin", "zabbix")


	def create_action_linux(self):
		
		params = {
			"name" : "Auto registration - Linux",
			"value" : "Linux",
			"templateid" : "10001"
		}
		self.create_action(params)


	def create_action_windows(self):
		
		params = {
			"name" : "Auto registration - windows",
			"value" : "Windows",
			"templateid" : "10081"
		}
		self.create_action(params)
		

	def create_action(self, params):
		"""Creates autoregistration action on zabbix server
		
		Arguments:
			params {[dict]} -- configuration parameters for windows and 
		"""

		post_data = {
		        "name": params['name'],
		        "eventsource": 2,
		        "status": 0,
		        "esc_period": 120,
		        "def_shortdata": "Auto registration: {HOST.HOST}",
        		"def_longdata": "Host name: {HOST.HOST}\r\nAgent port: {HOST.PORT}\r\nHost IP: {HOST.IP}",
		        "filter": {
	            "evaltype": 0,
	            #Meta data condition
	            "conditions": [
		                {
		                    "conditiontype": 24, #Host Metadata
		                    "operator": 2,
		                    "value": params['value']
		                },
		                {
		                    "conditiontype": 20, # Proxy
		                    "operator": 0,
		                    "value": self.proxy_id
		                },
		            ]
		        },

		        "operations": [
		        	#Template Option 
		              {
		                  "operationtype": 6,
		                  "optemplate": [
		                       {
		                         "templateid": params['templateid']
		                       }
		                 ]
		              },
		              #Add Host
		              {
		                  "operationtype": 2,
		              },
		              #Add to host group
		              {
		                  "operationtype": 4,
		                  "opgroup" : {
		                  	# Host Group Linux Servers
	              		  	"groupid" : "2"  
		                  }
		              },
		              #Enable Host
		              {
		                  "operationtype": 8,
		              },

		              #Set Host Inventory Mode
		              {
		                  "operationtype": 10,
		                  "opinventory" : {
	              		  	"inventory_mode" : "1"  
		                  }
		              },

		              #Remove from host groups discovered hosts
		              {
		                  "operationtype": 5,
		                  "opgroup" : {
	              		  	"groupid" : "5"  
		                  }
		              },

		        ]
		     }
		

		method = 'action.create'
		response = self.zapi.do_request(method, post_data)
		print(response)

	def get_proxy(self, proxy_name):
		"""This function finds proxy installed on zabbix, and stores the 
		proxy id in a class variable self.proxy_id
		
		Arguments:
			proxy_name {[string]} -- Name of the proxy
		"""


		proxy_data = {
			    "params": {
			        "host": proxy_name,
			        "status" : 5
			        # "selectInterface": "extend"
			    },
			}
		method = 'proxy.get'
		response = self.zapi.do_request(method, proxy_data)
		response = response['result']
		self.proxy_id = response[0]['proxyid']
		

if __name__ == '__main__':

	command_inputs = sys.argv
	if len(command_inputs) < 2:
		raise NameError("Please Provide Zabbix ui Hostname or IP Address for accessing the API")

	zabbix_host = sys.argv[1]
	proxy_name = sys.argv[2]
	zabbix = ZabbixOnboarding(zabbix_host)
	zabbix.get_proxy(proxy_name)
	zabbix.create_action_linux()
	zabbix.create_action_windows()


		