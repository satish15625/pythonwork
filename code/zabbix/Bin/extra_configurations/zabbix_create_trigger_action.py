
# Referenced From https://www.zabbix.com/documentation/4.2/manual/api/reference/action/object
# https://www.zabbix.com/documentation/4.2/manual/api/reference/action/create
# In order to make any changes please refer to the documentation above


import sys
from pyzabbix import ZabbixAPI
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class ZabbixTriggerAction():
	"""docstring for ZabbixTriggerAction"""
	def __init__(self, hostname):
		"""[summary]
		
		[description]
		"""
		self.zapi = ZabbixAPI("https://{}/zabbix".format(hostname))
		self.zapi.session.verify=False
		self.zapi.login("Admin", "testing123")

	def create_action(self):
		"""[summary]
		
		[description]
		"""
		post_data = {
        "name": "Proxy Down 3",
        "eventsource": 0,
        "status": 0,
        "esc_period": "2m",
        "filter": {
            "evaltype": 0,
            "conditions": [
                {
                    "conditiontype": 2,
                    "operator": 0,
                    "value": "17241"
                }
            ]
        },
        "operations": [
            {
                "operationtype": 0,
                "esc_period": "0s",
                "esc_step_from": 1,
                "esc_step_to": 2,
                "evaltype": 0,
                "opmessage_grp": [
                    {
                        "usrgrpid": "7"
                    }
                ],
                "opmessage": {
                    "default_msg": 1,
                    "mediatypeid": "1"
                }
            },
            {
                "operationtype": 1,
                "esc_step_from": 3,
                "esc_step_to": 4,
                "evaltype": 0,
                "opconditions": [
                    {
                        "conditiontype": 14,
                        "operator": 0,
                        "value": "0"
                    }
                ],
                "opcommand_grp": [
                    {
                        "groupid": "2"
                    }
                ],
                "opcommand": {
                    "type": 0,
                    "scriptid": "3",
					"execute_on" : 1,
                   
                    "command": "/usr/lib/zabbix/externalscripts/proxy-round-robin.py svcas0127 svcas0197 "
                }
            }
        ]
    }
		

		method = 'action.create'
		response = self.zapi.do_request(method, post_data)
		print(response)

	def get_trigger_id(self):
		params = {
	        "output": [
	            "triggerid",
	            "description",
	            # "tags"
	            # "description"
	        ],

	        # This needs to be dynamic
	        "groupids": 4
    	}
		method = 'trigger.get'

		response = self.zapi.do_request(method, params)
		print(response)

	def get_host_id(self):
		pass

if __name__ == '__main__':

	command_inputs = sys.argv
	if len(command_inputs) < 2:
		raise NameError("Please Provide Zabbix ui Hostname or IP Address for accessing the API")

	zabbix_host = sys.argv[1]
	zabbix = ZabbixTriggerAction(zabbix_host)
	zabbix.create_action()
	# 17391
	# zabbix.get_trigger_id()
		
