# File Name:- Zabbix_Mysql_DB Master.py
# Service Name:- N/A
# Purpose: To config  zabbix  db Master
# Author Name: Satish Kumar
# Create Date: 10/Nov/20
# Modifed By:-00/00/20
# Last Modify Date:
# Current Version: 2.0
# Summary of Last Change: To Configure Master on DB Primary Server.


import os
import sys
import logging
import time
import subprocess
import json
import mysql.connector
from mysql.connector import Error
import urllib3
from pyzabbix import ZabbixAPI
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus
import config
class Zabbix_Ha_Proxy():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        #self.sec_db = sys.argv[2]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_HA_Proxy_Config_Master" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.db_user =  self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Core"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Zabbix HA PROXY Confiuration Initiated"
                            }
        # self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_HA_Proxy_Config" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)
        
    def install_python_pip(self):
        try:
        #self.logger("Installing Python Setup Tool ....")
            setuptool = "yum -y install python-setuptools"
            os.system(setuptool)
            getPackge = "wget https://bootstrap.pypa.io/get-pip.py"
            os.system(getPackge)
            time.sleep(5)
            #self.logger("Installing Python Pip Package ....")
            getPip= "python get-pip.py"
            os.system(getPip)
            time.sleep(5)
            self.output.writelines("Python Pip Done.")
            print("Done")

        except Exception as e:
           self.logger.info("Exception caught to install Python pip" + str(e))
           self.flag = 1
           print("Hii")

    # ''' install pyzabbix modeule '''
    def pyzabbix_module(self):
        try:
            
            pyzabbix = "pip install pyzabbix"
            os.system(pyzabbix)
            time.sleep(5)
            
            conf = "pip install config"
            os.system(conf)
            time.sleep(5)
            self.logger.info("pyzabix Module Done.")

        except Exception as e:
            self.logger.info("Exception caught to install pyzabbix_module" + str(e))
            self.flag = 1


    #     ''' pyzabbix module configuration '''
    def pyzabbix_conf(self):

        try:

            #grep passwd
            grp = "grep zabbix /etc/passwd"
            os.system(grp)

            time.sleep(5)
            #create directory if not exist
            if not os.path.exists('/var/lib/zabbix'):
                os.makedirs('/var/lib/zabbix')

            # config file in /var/lib/zabbix/config.py
            path = "/var/lib/zabbix"
            os.system('cp config.py /var/lib/zabbix')
            os.system('chown zabbix. /var/lib/zabbix/config.py')
            print("After copying file:")
            print(os.listdir(path))
        except Exception as e:
                self.logger.info("Exception caught to install pyzabbix_module" + str(e))
                self.flag = 1


    def externalscripts_file(self):

        try:
            #self.logger("Put list-all-proxies.py in externalscripts directory. Move to the directory....")
            
            os.system('cp list-all-proxies.py config.py /usr/lib/zabbix/externalscripts/')
            os.system('chown zabbix. /usr/lib/zabbix/externalscripts/list-all-proxies.py')
            os.system('chmod +x /usr/lib/zabbix/externalscripts/list-all-proxies.py')
            os.system('python /usr/lib/zabbix/externalscripts/list-all-proxies.py')
            time.sleep(5)

            print("Importing Zabbix Template ")
            os.system('python importTemplate.py')

            time.sleep(5)
            print("Template Linking with given Host.")

            os.system("python host_update.py")

            print("Distribute proxy-round-robin-1.py to /usr/lib/zabbix/externalscripts and set it executable:")
            #files1 = ['proxy-round-robin-1.py']
            #for px in files1:
                #   shutil.move(px,'/usr/lib/zabbix/externalscripts')
            os.system('cp proxy-round-robin-1.py /usr/lib/zabbix/externalscripts')
            os.system('chown zabbix. /usr/lib/zabbix/externalscripts/proxy-round-robin-1.py')
            os.system('chmod +x /usr/lib/zabbix/externalscripts/proxy-round-robin-1.py')
            sys.path.insert(0,'/var/lib/zabbix')
            #get Host list
            ZABBIX_SERVER = config.url
            zapi = ZabbixAPI(ZABBIX_SERVER)
            zapi.session.verify=False
            zapi.login(config.username, config.password)
            result = zapi.proxy.get()
            a = []
            for elem in result:
            #  h = elem['host']
                a.append(elem['host'])

            aa = u" ".join(a)
            print(aa)

            # os.system('python /usr/lib/zabbix/externalscripts/proxy-round-robin-1.py {host}'.format(host=aa))
            time.sleep(5)

        except Exception as e:
                self.logger.info("Exception caught to install pyzabbix_module" + str(e))
                self.flag = 1  
   
    def final_check(self):


            if self.flag == 0:
                self.logger.info("Zabbix HA Proxy Configuration Success")
                self.api_payload["StatusReason"] = "Zabbix HA Configuration Success"
                self.api_payload["Status"] = 2
                # self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Zabbix HA Proxy Configuration Failed")
                self.api_payload["StatusReason"] = "Zabbix HA Proxy Configuration Failed"
                self.api_payload["Status"] = 3
                # self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Fail")
                print("3rr0rC0d3[500]")

if __name__ == "__main__":
    call = Zabbix_Ha_Proxy()
    call.install_python_pip()
    call.pyzabbix_module()
    call.pyzabbix_conf()
    call.externalscripts_file()
    call.final_check()