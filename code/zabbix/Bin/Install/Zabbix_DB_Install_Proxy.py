# File Name:- Zabbix_DB_Install_Proxy.py
# Service Name:- N/A
# Purpose: To install zabbix proxy db
# Author Name: Sankar
# Create Date: 25/Sep/20
# Modifed By:-
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A
import os
import subprocess
import sys
import json , logging, time

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus
from precheck import prechecks

class ZabbixMysqlInstall():

    def __init__(self):
        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_DB_Install_Proxy_" + dt + ".txt", "w+")
        self.environment = self.load_variable["Environment"]
        self.db_user = self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB Proxy"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "2",
                            "Status": "1", "StatusReason": "DB Proxy Installation started"
                            }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        
        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_Install_Proxy_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)

        process = subprocess.Popen(['sudo', 'yum', 'install', '-y',
                'wget'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

    def get_rpm(self):
        self.api_payload["StatusReason"] = "Fetching RPMs"
        self.send_status.send_logs([self.api_payload])
        self.logger.info("Getting RPM file")

        process = subprocess.Popen(['wget',
                'https://repo.mysql.com/mysql80-community-release-el7-1.noarch.rpm'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # print(stdout)

    def local_install(self):
        self.api_payload["StatusReason"] = "Running local install"
        self.send_status.send_logs([self.api_payload])
        self.logger.info("running localinstall")
        self.api_payload["StatusReason"] = "Running local install"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])
        process = subprocess.Popen(['sudo', 'yum', 'localinstall', '-y',
                'mysql80-community-release-el7-1.noarch.rpm'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # print(stdout)


    def install_mysql_community(self):
        self.api_payload["StatusReason"] = "Installing community server"
        self.send_status.send_logs([self.api_payload])
        self.logger.info("installing community server")
        self.api_payload["StatusReason"] = "Installation MySQL  database server  latest version"
        self.api_payload["Status"] = 2
        self.send_status.send_logs([self.api_payload])
        process = subprocess.Popen(['sudo', 'yum', 'install', '-y',
                'mysql-community-server'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # print(stdout)


    def start_service(self):
        process = subprocess.Popen(['sudo', 'service', 'mysqld', 'start'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # print(stdout)


    # def secure_install(self):
    #     self.api_payload["StatusReason"] = "Secure install started"
    #     self.send_status.send_logs([self.api_payload])
    #     self.logger.info("secure install going on")
    #
    #     output = os.popen("grep 'temporary password' /var/log/mysqld.log").read()
    #     split_output = output.split()
    #     temp_passwod = split_output[-1].strip()
    #
    #     self.logger.info("temporary Password is:"+str(temp_passwod))
    #
    #     # process = subprocess.Popen(['sh', 'mysql_secure.sh', temp_passwod, self.db_pwd],
    #     #                         stdin=subprocess.PIPE,
    #     #                         stderr=subprocess.PIPE
    #     #                     )
    #     # stdout, stderr = process.communicate()
    #     # print(stdout)
    #     #setting permission to sh to execute
    #     subprocess.getoutput('chmod 777 mysql_secure.sh')
    #     status,out = subprocess.getstatusoutput('./mysql_secure.sh '+str(temp_passwod)+' '+self.db_pwd+' >>'+self.root+'/zabbix/Logs/mysql_secure_install.log')
    #     if status == 0:
    #         self.api_payload["StatusReason"] = "Secure install completed"
    #         self.send_status.send_logs([self.api_payload])
    #         self.logger.info("secure install completed")
    #     else:
    #         self.api_payload["StatusReason"] = "Secure install failed"
    #         self.send_status.send_logs([self.api_payload])
    #         self.logger.info("secure install failed")
    #         self.flag = 1

    def secure_install(self):
        self.api_payload["StatusReason"] = "Secure install started"
        self.send_status.send_logs([self.api_payload])
        self.logger.info("secure install going on")

        output = os.popen("grep 'temporary password' /var/log/mysqld.log").read()
        split_output = output.split()
        temp_passwod = split_output[-1].strip()

        self.logger.info("temporary Password is:"+str(temp_passwod))
        self.api_payload["StatusReason"] = "Mysql grep & Change the default password"
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
            self.api_payload["StatusReason"] = "DB Proxy Installation Success"
            self.api_payload["Status"] = 2
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("DB Proxy Installation Failed")
            self.output.writelines("Fail")
            self.api_payload["StatusReason"] = "DB Proxy Installation Failed"
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