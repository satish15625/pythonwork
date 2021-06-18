# File Name:- Zabbix_Proxy_Install.py
# Service Name:- N/A
# Purpose: To install zabbix proxy
# Author Name: Sankar
# Create Date: 25/Sep/20
# Modifed By:-
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A

import os
import sys
import logging
import time
import subprocess
import json
from shutil import copyfile
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# status, out = subprocess.getstatusoutput('pip3 install pyzabbix')
from pyzabbix import ZabbixAPI
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Proxy():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        self.db_ip = sys.argv[2]
        self.zabbix_server = sys.argv[3]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_Proxy_Config_" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.db_user = self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Proxy"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Proxy Configuration Initiated"
                            }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_Proxy_Config_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)


    def config(self):
        try:
            conf_flag = 0
            self.logger.info("Configuring Zabbix Proxy")
            self.api_payload["StatusReason"] = "Configuring Zabbix Proxy"
            self.api_payload["Status"] = 1
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            FileName = '/etc/zabbix/zabbix_proxy.conf'
            with open(FileName) as f:
                newText = f.read().replace('# DBHost=localhost', 'DBHost=' + self.db_ip)
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText = f.read().replace('# DBPassword=', 'DBPassword='+self.db_pwd)
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText = f.read().replace('Hostname=Zabbix proxy', 'Hostname=' + self.hostname)
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText = f.read().replace('Server=127.0.0.1', 'Server=' + self.zabbix_server)
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText = f.read().replace('LogFileSize=0', 'LogFileSize=1')
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText = f.read().replace('# LogRemoteCommands=0', 'LogRemoteCommands=1')
            with open(FileName, "w") as f:
                f.write(newText)
            status1, out = subprocess.getstatusoutput("iptables -A INPUT -p tcp -s " + self.zabbix_server + " --dport 10050 -m state --state NEW,ESTABLISHED -j ACCEPT")
            status2, t = subprocess.getstatusoutput('systemctl start zabbix-proxy')
            try:
                ZABBIX_USER = "Admin"
                ZABBIX_PASS = "zabbix"
                ZABBIX_SERVER = 'http://' + self.zabbix_server + '/zabbix/api_jsonrpc.php'
                zapi = ZabbixAPI(ZABBIX_SERVER)
                zapi.session.verify = False
                # Login to the Zabbix API
                zapi.login(ZABBIX_USER, ZABBIX_PASS)
                # print PROXY_TYPE
                PROXY_TYPE = 'active'
                proxy_val = ''
                if PROXY_TYPE.lower() == 'active':
                    proxy_val = 5
                elif PROXY_TYPE.lower() == 'passive':
                    proxy_val = 6
                # print Hostgroup
                # print templates
                # exit()
                # print proxy_val
                if proxy_val != '':
                    zapi.proxy.create({"host": self.hostname, "status": proxy_val})
            except Exception as e:
                self.logger.info("Zabbix API Exception caught:"+str(e))
                self.api_payload["Stage"] = 3
                self.api_payload["StatusReason"] = "Zabbix API Error: "+str(e)
                self.send_status.send_logs([self.api_payload])
                conf_flag = 1
            status3, output = subprocess.getstatusoutput("systemctl restart zabbix-proxy")
            status4, output = subprocess.getstatusoutput("systemctl restart zabbix-sender")
            status5, output = subprocess.getstatusoutput("systemctl restart zabbix-get")
            self.logger.info("Restart status of zabbix-proxy,zabbix-sender,zabbix-get: "+str(status3)+str(status4)+str(status5))

            if conf_flag == 0:
                self.logger.info("Proxy Configuration Success")
                self.api_payload["Stage"] = 3
                self.api_payload["StatusReason"] = "Proxy Configuration Success"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Proxy Configuration Failed")
                self.api_payload["Stage"] = 3
                self.api_payload["StatusReason"] = "Proxy Configuration Failed"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Fail")
                print("3rr0rC0d3[500]")

        except Exception as e:
            self.logger.info("Zabbix Proxy Config Exception caught" + str(e))




if __name__ == "__main__":

    call = Proxy()
    call.config()
