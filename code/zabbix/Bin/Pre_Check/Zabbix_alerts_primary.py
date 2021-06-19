# File Name:- moogsoft_postcheck_core.py
# Service Name:- N/A
# Purpose: To perform MoogSoft Core Post Check
# Author Name: Priyanka Jain
# Create Date: 24/May/2018
# Modifed By:-
# Last Modify Date:
# Current Version: 1.1
# Summary of Last Change: N/A
# Arguments: N/A.
import  commands, sys, os, json
sys.path.insert(0, os.environ['Admin_Root']+'/iDeploy/tools/zabbix_5.0/zabbix/Lib/uistatus')
from uistatus import sendstatus

def connection_check(inventory):
	send_status = sendstatus(os.environ['Admin_Root']+'/iDeploy/tools/zabbix_5.0/zabbix/Input/global.json')
	with open("../../Input/global.json") as f:
		env_variables_file = json.load(f)
	environment = env_variables_file["Environment"]
	for i in inventory:
		host = i['ServerFQDN']
		component = i['component']
		server_types = i['ServerType']
		responses = os.system("ping -c 1 " + host)
		if responses == 0:
			dict_data = [{"ToolName": "Zabbix", "Component": component, "ServerFQDN": host, "ServerType": server_types,
					 "Environment": environment, "Stage": "1", "Status": "1", "StatusReason": " Connection successful"}]
			send_status.send_status(dict_data)
			send_status.send_logs(dict_data)
		else:
			dict_data = [{"ToolName": "Zabbix", "Component": component, "ServerFQDN": host, "ServerType": server_types,
					 "Environment": environment, "Stage": "3", "Status": "1", "StatusReason": " Connection failed"}]
			send_status.send_status(dict_data)
			send_status.send_logs(dict_data)

hostname = commands.getoutput('hostname -s')
server_type=sys.argv[1]
core_primary=sys.argv[2]
db_primary=sys.argv[3]
proxy_primary=sys.argv[4]
proxydb_primary=sys.argv[5]

inventory = [{"component":"Core","ServerFQDN": core_primary,"ServerType": server_type},
			 {"component":"DB","ServerFQDN": db_primary,"ServerType": server_type},
             {"component":"Proxy","ServerFQDN": proxy_primary,"ServerType": server_type},
             {"component":"DB Proxy","ServerFQDN": proxydb_primary,"ServerType": server_type}
			 ]

connection_check(inventory)
