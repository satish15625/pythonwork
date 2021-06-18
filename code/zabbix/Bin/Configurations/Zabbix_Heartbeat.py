
# File Name:- Zabbix_Heartbeat.py
# Service Name:- N/A
# Purpose: To coonfigure Zabbix Hearbeat
# Author Name: satish
# Create Date: 06/oct/20
# Modifed By:-06/oct/2020
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A

import sys
import os
import json
import time
import subprocess

try:
    from pyzabbix import ZabbixAPI, ZabbixAPIException
except:
    status,out=os.system('pip3.7 install pyzabbix')

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import logging, time, subprocess, os, sys, json
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Zabbix_HeartBeat():


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

        self.component = "Proxy"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Configuring Zabbix Hearbeat"
                            }
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/zabbix_heartbeat_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Zabbix HeartBeat configuration Started.. " + dt)
        self.rules = None


    

    def create_host(self):
        """update host
        """
        try:
            request_host = {
                        "host": "ptest0135",
                        "interfaces": [
                            {
                                "type": 1,
                                "main": 1,
                                "useip": 1,
                                "ip": self.zabbix_ip,
                                "dns": "",
                                "port": "10050",

                            }
                        ],
                        "groups": [
                            {
                                "groupid": "4"
                            }
                        ],
                        "templates": [
                            {
                                "templateid": "10001"
                            }
                        ]
                    }
            # print(request_data)
            response = self.zapi.host.create(request_host)
            if response:
                # data = response['result']['actionids']
                # self.logger.info("Activated  notification action :" + ''.join(data))
                self.logger.info("Host Created success")
                subprocess.getoutput('zabbix_server -R config_cache_reload')
                self.api_payload["StatusReason"] = "Host Created Successfully"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Create Host failed")
                self.api_payload["StatusReason"] = "Host Creation Failed"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                
                print("3rr0rC0d3[500]")

        except Exception as e:
            self.logger.info("Zabbix API Exception caught:" + str(e))

    

    def add_rules(self):
        """
        : set rules for template creation
        
        [description]
        """
        self.logger.info("Inside add rules")
        self.rules = {
            'applications': {
                'createMissing': True,
            },
            'discoveryRules': {
                'createMissing': True,
                'updateExisting': True
            },
            'graphs': {
                'createMissing': True,
                'updateExisting': True
            },
            'groups': {
                'createMissing': True
            },
            'hosts': {
                'createMissing': True,
                'updateExisting': True
            },
            'images': {
                'createMissing': True,
                'updateExisting': True
            },
            'items': {
                'createMissing': True,
                'updateExisting': True
            },
            'maps': {
                'createMissing': True,
                'updateExisting': True
            },
            'screens': {
                'createMissing': True,
                'updateExisting': True
            },
            'templateLinkage': {
                'createMissing': True,
            },
            'templates': {
                'createMissing': True,
                'updateExisting': True
            },
            'templateScreens': {
                'createMissing': True,
                'updateExisting': True
            },
            'triggers': {
                'createMissing': True,
                'updateExisting': True
            },
            'valueMaps': {
                'createMissing': True,
                'updateExisting': True
            },
        }
        return self
    
    def read_template(self):
        """: Read template xml file and store in a class variable
        
        [description]
        """
        with open('zbx_heartbeat_templates.xml', 'r') as f:
            self.template = f.read()
    
    def create(self):
        """: Call pyzabbix to create template on the server
        
        [description]
        """
        try:
            self.zapi.confimport('xml', self.template, self.rules)
        except ZabbixAPIException as e:
            self.logger.info(str(e))

    #Hostupdate 

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
        self.hostid = self.zapi.host.get(filter=({'host':self.hostname}))
        # print(self.groupid)

    def update_host(self):
        """update host 
        """
        try:
            request_data = {
                            "hostid":self.hostid[0]['hostid'],
                            "templates": [
                                {
                                "templateid" : self.template_data[0]['templateid'],
                                }
                            ],
                        }
            # print(request_data)
            response = self.zapi.host.update(request_data)
            if response:
                # data = response['result']['actionids']
                # self.logger.info("Activated  notification action :" + ''.join(data))
                self.logger.info("Update success")
            else:
                self.logger.info("Update failed")
        except Exception as e:
            self.logger.info("Zabbix API Exception caught:" + str(e))



    def final_check(self):
        if self.flag == 0:
            self.logger.info("HeartBeat Configuration Success")
            self.api_payload["StatusReason"] = "HeartBeat Configuration Success"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("HeartBeat Configuration Fail")
            self.api_payload["StatusReason"] = "HEARTBEAT Configuration Fail"
            self.api_payload["Status"] = 3
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")




if __name__ == '__main__':

 zabbix = Zabbix_HeartBeat()
 #zabbix.create_host()
 zabbix.add_rules()
 zabbix.read_template()
 zabbix.create()

 #hostupdate function calling 
 zabbix.search_template()
 zabbix.search_hostgroup()
 zabbix.search_hostid()
 zabbix.update_host()
 zabbix.final_check()

