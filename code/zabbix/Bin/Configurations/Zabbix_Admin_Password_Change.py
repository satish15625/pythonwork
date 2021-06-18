# File Name:- change_admin_password.py
# Service Name:- N/A
# Purpose: To install  zabbix proxy db
# Author Name: 
# Create Date: 25/Sep/20
# Modifed By:-28/09/2020
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A

import os
import sys
import logging
import time
import subprocess
import json
try:
    from pyzabbix import ZabbixAPI
except:
    os.system('pip3.7 install pyzabbix')

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class ZabbixAdminPassword():
    """docstring for ZabbixAdminPassword"""
    def __init__(self):
        self.server_type = sys.argv[1]
        self.default_user = "Admin"
        self.default_pass = "zabbix"
        zabbix_server = sys.argv[2] # Zabbix server hostname

        self.zapi = ZabbixAPI("https://{}/zabbix".format(zabbix_server))
        self.zapi.session.verify = False
        self.zapi.login(self.default_user, self.default_pass)
        
        self.root = os.environ['Admin_Root']
        
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        self.environment = self.load_variable["Environment"]
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                    "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                    "Status": "1", "StatusReason": "Zabbix Admin Password Change Initiated"
                    }
        self.send_status.send_logs([self.api_payload])
        self.new_pass = self.load_variable['new_admin_password']
        self.log_file = self.root + "/zabbix/Logs/Zabbix_Password_Change_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def update_password(self):
        try:
            method = 'user.update'
            post_data = {
                "userid" : 1,
                "passwd" : self.new_pass,
                "alias" : "Admin"
            }

            response = self.zapi.do_request(method, post_data)
            
            if  response['id'] == 1:
                self.logger.info("Admin password Password Changed")
                self.api_payload["StatusReason"] = "Admin Password Changed Success"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Admin Chnaged Password Failed")
                self.api_payload["StatusReason"] = "Admin Password Changed Failed"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Fail")
                print("3rr0rC0d3[500]")
        except :
            self.logger.info("Admin Chnaged Password Failed")
            self.api_payload["StatusReason"] = "Admin Password Changed Failed"
            self.api_payload["Status"] = 3
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            # self.output.writelines("Fail")
            print("3rr0rC0d3[500]")


if __name__ == '__main__':
    password = ZabbixAdminPassword()
    password.update_password()
