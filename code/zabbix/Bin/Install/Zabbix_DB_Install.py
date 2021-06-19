# File Name:- zabbix_mysql_install.py
# Service Name:- N/A
# Purpose: Installing mysql for zabbix
# Author Name: Satish
# Create Date: 25/Sep/20
# Modifed By:-
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A


import os,sys
import subprocess
import logging, time, subprocess, os, sys, json

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class ZabbixMysqlInstall():

    def __init__(self):
        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_DB_Install_" + dt + ".txt", "w+")
        self.environment = self.load_variable["Environment"]
        self.db_user = self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "2",
                            "Status": "1", "StatusReason": "DB Installation started"
                            }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])

        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_Install_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)
        # self.flag = 0
        # self.server_type = sys.argv[1]
        # self.root = os.environ['Admin_Root']
        # global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        # self.load_variable = json.load(global_json)
        # dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        # logging.basicConfig(filename=self.log_file,
        #                     format='%(asctime)s %(message)s',
        #                     filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        # self.logger = logging.getLogger()
        # self.logger.setLevel(logging.INFO)
        # self.environment = self.load_variable["Environment"]
        # self.hostname = subprocess.getoutput("hostname -s")
        # self.component = "DB"
        # self.send_status = sendstatus()
        # self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
        #                     "ServerType": self.server_type, "Environment": self.environment, "Stage": "2",
        #                     "Status": "1", "StatusReason": "DB installation started"
        #                     }
        #
        # self.send_status.send_status([self.api_payload])
        # self.send_status.send_logs([self.api_payload])
        process = subprocess.Popen(['yum', 'install', '-y',
                'wget'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

    def get_rpm(self):
        self.api_payload["StatusReason"] = "Enable RPMs"
        self.send_status.send_logs([self.api_payload])
        process = subprocess.Popen(['wget',
                'https://repo.mysql.com/mysql80-community-release-el7-1.noarch.rpm'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()


    def local_install(self):
        self.api_payload["StatusReason"] = "Running localinstall"
        self.send_status.send_logs([self.api_payload])
        
        process = subprocess.Popen(['yum', 'localinstall', '-y',
                'mysql80-community-release-el7-1.noarch.rpm'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()


    def install_mysql_community(self):
        self.api_payload["StatusReason"] = "Installing community server"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])

        process = subprocess.Popen(['yum', 'install', '-y',
                'mysql-community-server'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()


    def start_service(self):

        process = subprocess.Popen(['service', 'mysqld', 'start'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()


    def secure_install(self):
        self.api_payload["StatusReason"] = "Secure install started"
        self.send_status.send_logs([self.api_payload])
        self.logger.info("secure install going on")

        output = os.popen("grep 'temporary password' /var/log/mysqld.log").read()
        split_output = output.split()
        temp_passwod = split_output[-1].strip()

        self.logger.info("temporary Password is:"+str(temp_passwod))
        self.api_payload["StatusReason"] = "Secure install started"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])

        # process = subprocess.Popen(['sh', 'mysql_secure.sh', temp_passwod, self.db_pwd],
        #                         stdin=subprocess.PIPE,
        #                         stderr=subprocess.PIPE
        #                     )
        # stdout, stderr = process.communicate()
        # print(stdout)
        #creating mysql_secure.sh
        f = open('mysql_secure_new.sh', "w+")

        self.logger.info("creating mysql_secure_new.sh")
        self.api_payload["StatusReason"] = "Updating Secure Password"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])

        f.writelines("#!/bin/bash\n")
        f.writelines("yum -y install expect\n")
        f.writelines('SECURE_MYSQL=$(expect -c "\n')
        f.writelines("set timeout 10\n")
        f.writelines("spawn mysql_secure_installation\n")
        f.writelines('expect \\"Enter password for user root:\\"\n')
        f.writelines('send \\"'+str(temp_passwod)+'\\r\\"\n')
        f.writelines('expect \\"The existing password for the user account root has expired. Please set a new password.\n')
        f.writelines('		New password:\\"\n')
        f.writelines('send \\"'+self.db_pwd+'\\r\\"\n')
        f.writelines('expect \\"Re-enter new password:\\"\n')
        f.writelines('send \\"'+self.db_pwd+'\\r\\"\n')
        f.writelines('expect \\"Change the password for root ? (Press y|Y for Yes, any other key for No) :\\"\n')
        f.writelines('send \\"n\\r\\"\n')
        f.writelines('expect \\"Remove anonymous users? (Press y|Y for Yes, any other key for No) :\\"\n')
        f.writelines('send \\"y\\r\\"\n')
        f.writelines('expect \\"Disallow root login remotely? (Press y|Y for Yes, any other key for No) :\\"\n')
        f.writelines('send \\"n\\r\\"\n')
        f.writelines('expect \\"Remove test database and access to it? (Press y|Y for Yes, any other key for No) :\\"\n')
        f.writelines('send \\"y\\r\\"\n')
        f.writelines('expect \\"Reload privilege tables now? (Press y|Y for Yes, any other key for No) :\\"\n')
        f.writelines('send \\"y\\r\\"\n')
        f.writelines('expect eof\n')
        f.writelines('")\n')
        f.writelines('\n')
        f.writelines('echo "$SECURE_MYSQL"\n')
        f.close()
        #setting permission to sh to execute
        subprocess.getoutput('chmod 777 mysql_secure_new.sh')
        status,out = subprocess.getstatusoutput('./mysql_secure_new.sh  >>'+self.root+'/zabbix/Logs/mysql_secure_install.log')
        if status == 0:
            self.api_payload["StatusReason"] = "Secure install completed"
            self.send_status.send_logs([self.api_payload])
            self.logger.info("secure install completed")
            self.api_payload["StatusReason"] = "Secure install completed"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
        else:
            self.api_payload["StatusReason"] = "Secure install failed"
            self.send_status.send_logs([self.api_payload])
            self.logger.info("secure install failed")
            self.flag = 1

    def check_status(self):
        status = subprocess.getoutput('service mysqld status')
        if "active (running)" in status and self.flag == 0:
            self.logger.info("DB Proxy Installation Success")
            self.output.writelines("Pass")
            self.api_payload["StatusReason"] = "DB Installation Success"
            self.api_payload["Status"] = 2
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("DB Proxy Installation Failed")
            self.output.writelines("Fail")
            self.api_payload["StatusReason"] = "DB Installation Failed"
            self.api_payload["Status"] = 3
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")



if __name__ == '__main__':
    mysql = ZabbixMysqlInstall()
    mysql.get_rpm()
    mysql.local_install()
    mysql.install_mysql_community()
    mysql.start_service()
    mysql.secure_install()
    mysql.check_status()