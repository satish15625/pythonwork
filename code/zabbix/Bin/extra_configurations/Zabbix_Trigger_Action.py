
# File Name:- Zabbix_Heartbeat.py
# Service Name:- N/A
# Purpose: To coonfigure Zabbix Hearbeat
# Author Name: satish
# Create Date: 24/Dec/20
# Modifed By:-24/Dec/2020
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A

import sys
import os
import json
import time
import subprocess

import sys
from pyzabbix import ZabbixAPI
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import logging, time, subprocess, os, sys, json
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Zabbix_TriggerAction():


    def __init__(self):
        self.flag = 0
        self.root = os.environ['Admin_Root']
        self.server_type = sys.argv[1]
        self.zabbix_host = sys.argv[2]
        #self.zabbix_host = "ptest0135"
        self.zabbix_ip = subprocess.getoutput('hostname -i').split()[0]

        self.zapi = ZabbixAPI("https://{}/zabbix".format(self.zabbix_host))
        self.zapi.session.verify = False
        self.zapi.login("Admin", "testing123")
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.hostname = subprocess.getoutput("hostname -s")
        self.environment = self.load_variable["Environment"]

        self.template = self.load_variable['host_creds']['tmp_name']
        self.hostgroup = self.load_variable['host_creds']['hostgroup']

        self.component = "Core"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Configuring Zabbix Hearbeat"
                            }
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/zabbix_trigger_action_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Zabbix Trigger Action configuration Started.. " + dt)
        self.rules = None

    def create_action(self):
        """[summary]
        
        [description]
        """
        post_data = {
        "name": "Proxy-Down-Switch_Over",
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
                
                    "command": "/usr/lib/zabbix/externalscripts/proxy-round-robin.py svcas0047 svcas0197 "
                }
            }
        ]
    }
        

        method = 'action.create'
        response = self.zapi.do_request(method, post_data)
        print(response)
    
    def create_action1(self):
        """[summary]
        
        [description]
        """
        post_data = {
        "name": "Proxy-Down-Switch_Over1",
        "eventsource": 0,
        "status": 0,
        "esc_period": "2m",
        "filter": {
            "evaltype": 0,
            "conditions": [
                {
                    "conditiontype": 2,
                    "operator": 0,
                    "value": "17255"
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
                
                    "command": "/usr/lib/zabbix/externalscripts/proxy-round-robin.py svcas0197 svcas0047"
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


    def final_check(self):
        if self.flag == 0:
            self.logger.info("Zabbix Triger & Action Configuration Success")
            self.api_payload["StatusReason"] = "Trigger Action Configuration Success"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("Zabbix Proxy Trigger Configuration Fail")
            self.api_payload["StatusReason"] = "Trigger Action Configuration Fail"
            self.api_payload["Status"] = 3
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")




if __name__ == '__main__':

 zabbix = Zabbix_TriggerAction()
 zabbix.create_action()
 zabbix.create_action1()
 zabbix.get_trigger_id()
 zabbix.get_host_id()
 zabbix.final_check()



