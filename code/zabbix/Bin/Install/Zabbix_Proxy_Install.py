# File Name:- Zabbix_Proxy_Install.py
# Service Name:- N/A
# Purpose: To install zabbix proxy
# Author Name: satish
# Create Date: 25/Sep/20
# Modifed By:-
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A

import os
import sys
import logging
import datetime
import subprocess
import json
import time
from shutil import copyfile
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
subprocess.getoutput('pip3.7 install pyzabbix')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus


class Proxy():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        # self.db_ip = sys.arg[2]
        # self.zabbix_server = sys.arg[3]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_Proxy_Install_" + dt + ".txt", "w+")
        self.environment = self.load_variable["Environment"]
        # self.db_user = self.load_variable['db_creds']['username']
        # self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Proxy"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "2",
                            "Status": "1", "StatusReason": "Proxy Installation Initiated"
                            }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_Proxy_Install_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)

    def install(self):

        self.logger.info('Getting Hostname '+self.hostname)
        self.api_payload["StatusReason"] = "Server Host Name "+self.hostname
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])

        self.logger.info('Checking if Zabbix rpm zabbix-release-5.0-1.el7.noarch is installed')
        self.api_payload["StatusReason"] = "Zabbix rpm  zabbix-release-5.0-1.el7.noarch.rpm successfully installed"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])

        cmd = 'rpm -qa|grep zabbix-release-*'

        if (os.system(cmd) == 0):
            # print("already installed")
            self.logger.info('Zabbix rpm zabbix-release-5.0-1.el7.noarch is already installed')
        else:
            self.logger.info('Going to install Zabbix rpm zabbix-release-5.0-1.el7.noarch')
            command = ['rpm', '-Uvh',
                       'https://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm']
            p = subprocess.Popen(command)
            p.wait()
            # print(p.returncode)
            if p.returncode == 0:
                self.logger.info('Zabbix rpm  zabbix-release-5.0-1.el7.noarch.rpm successfully installed') 
                # print("OK")
                self.api_payload["StatusReason"] = "Zabbix rpm  zabbix-release-5.0-1.el7.noarch.rpm successfully installed"
                self.api_payload["Status"] = 2
                self.send_status.send_logs([self.api_payload])
            else:
                self.flag = 1
                self.logger.info("Unable to install Zabbix RPM  zabbix-release-5.0-1.el7.noarch.rpm")

                
        os.system('yum clean all')
        self.logger.info('Going to install zabbix proxy')
        status1,out = subprocess.getstatusoutput('yum install -y zabbix-proxy-mysql zabbix-sender zabbix-get >>'+self.log_file)
        # os.system(cmd_ms)
        status2, out = subprocess.getstatusoutput('rpm -q zabbix-proxy-mysql')
        timeout = time.time() + 60 * 5
        self.logger.info("Initial status1,2:" + str(status1) + str(status2) )
        self.api_payload["StatusReason"] = "Installing zabbix-proxy-mysql zabbix-sender zabbix-get"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])
        if status1 != 0 or status2 != 0:
            self.logger.info("Inside retry loop")
            while True:
                time.sleep(1)
                status1, out = subprocess.getstatusoutput(
                    'yum install -y zabbix-proxy-mysql zabbix-sender zabbix-get >>' + self.log_file)
                status2, out = subprocess.getstatusoutput('rpm -q zabbix-proxy-mysql')

                if status1 != 0 or status2 != 0:
                    self.flag = 1
                    pass
                else:
                    self.logger.info("retry success")
                    self.flag = 0
                    break
                if time.time() > timeout:
                    self.flag = 1
                    self.logger.info("Retry failed")
                    break
        else:
            pass
        self.logger.info("Final status1,2:" + str(status1) + str(status2))
        
        
        if self.flag == 0:
            self.logger.info("Proxy Installtion Success")
            self.api_payload["StatusReason"] = "Proxy Installation Success"
            self.api_payload["Status"] = 2
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            self.output.writelines("Pass")
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("Proxy Installtion Failed")
            self.api_payload["StatusReason"] = "Proxy Installation Failed"
            self.api_payload["Status"] = 3
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            self.output.writelines("Fail")
            print("3rr0rC0d3[500]")





if __name__ == "__main__":

    call = Proxy()
    call.install()
