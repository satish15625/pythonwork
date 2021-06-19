# File Name:- Zabbix_Mysql_DB_HA_Config_Primary.py
# Service Name:- N/A
# Purpose: To config  zabbix  db replica
# Author Name: sankar
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
import mysql.connector
from mysql.connector import Error


sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Zabbix_DB():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        self.sec_db = sys.argv[2]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_DB_HA_Config_" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.db_user =  self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Zabbix HA DB Configuration Initiated"
                            }
        # self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_HA_Config_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)

    def update_file(self):
        """
        Code for updating the file
        """
        try:
            # put server conf file in /etc/my.cnf
            self.logger.info("Updating the my.cnf file")

            conf_data = [
                "server-id = 1\n",
                "log-bin = mysql-bin\n",
                "binlog_format = row\n",
                "gtid-mode=ON\n",
                "enforce-gtid-consistency\n",
                "log-slave-updates\n",
                "relay-log = relay-log-server\n"
            ]

            # production config path
            file_object = open('/etc/my.cnf', 'a')
            file_object.writelines(conf_data)
            file_object.close()
        except Exception as e:
            self.logger.info("Exception caught updating  my.cnf file" + str(e))
            self.flag = 1

    def restart_service(self):
        """
        	Code for restarting services
        """
        try:
            self.logger("Mysql Restarting.......")
            reset = "systemctl restart mysqld"
            os.system(reset)
            time.sleep(5)
        except Exception as e:
            self.logger.info("Exception caught while restart" + str(e))

    def run_mysql_commands(self):

        # with open('primary_data.json') as data_file:
        #     data = json.load(data_file)
        try:
            dbname = 'zabbix'
            user = 'zabbix'
            pwd = self.db_pwd

            rep_User = self.load_variable['Zabbix HA']['replication_User']
            rep_Pass = self.load_variable['Zabbix HA'] ['replication_Pass']
            master_usr = self.load_variable['Zabbix HA'] ['master_user']
            master_pass = self.load_variable['Zabbix HA'] ['master_password']


            conn = mysql.connector.connect(host='localhost',
                                           database=dbname,
                                           user=user,
                                           password=pwd)


            if conn.is_connected():
                self.logger.info('Connected to MySQL database')
                mycursor = conn.cursor()
                self.logger.info("Creating Replication dbuser")
                tmpsecond = "create user '{replication_dbuser}'@'%' identified by '{replication_Pass}';".format(
                    replication_dbuser=rep_User, replication_Pass=rep_Pass)
                mycursor.execute(tmpsecond)

                self.logger.info("GRANT REPLICATION SLAVE ON")
                gtmp = "GRANT REPLICATION SLAVE ON *.* TO '{replication_dbuser}'@'%';".format(replication_dbuser=rep_User)
                mycursor.execute(gtmp)

                self.logger.info('-------------------Creating User in Secondry Ip  -----------------')
                tmpsec = "CREATE USER '{replication_dbuser}'@'{replication_Ip}' IDENTIFIED WITH mysql_native_password BY '{replication_Pass}';".format(
                    replication_dbuser=rep_User, replication_Ip=self.sec_db, replication_Pass=rep_Pass)
                mycursor.execute(tmpsec)

                self.logger.info("Grant Permisson")
                prsectmp = "GRANT ALL ON *.* TO '{replication_dbuser}'@'{replication_Ip}'".format(
                    replication_dbuser=rep_User, replication_Ip=self.sec_db)
                mycursor.execute(prsectmp)

                mycursor.execute("FLUSH PRIVILEGES;")
                self.logger.info("------Master Status------------")

                mycursor.execute("show master status;")
                for st in mycursor:
                    self.logger.info(str(st))

                # stop slave status
                self.logger.info("Stoping slave..")
                mycursor.execute("stop slave;")
                time.sleep(5)
                # CHANGE MASTER TO MASTER_HOST

                master_host = "CHANGE MASTER TO MASTER_HOST = '{replication_Ip}', MASTER_PORT = 3306, MASTER_USER = '{replication_user}', MASTER_PASSWORD = '{replication_password}', MASTER_AUTO_POSITION = 1;".format(
                    replication_Ip=self.sec_db, replication_user=master_usr, replication_password=master_pass)

                mycursor.execute(master_host)
                self.logger.info("CHANGE MASTER TO MASTER_HOST Done")

                # start slave
                self.logger.info("Restarting the Slave....")
                mycursor.execute("start slave;")
                time.sleep(8)

                self.logger.info("Show slave status ")

                mycursor.execute("show slave status")

                for sst in mycursor:
                    self.logger.info(str(sst))

                self.logger.info("--------------done-----------------------")

            else:
                self.logger.info("Connection err")
                self.flag = 1
        except Exception as e:
            self.logger.info("Exception caught during config" + str(e))
            self.flag = 1


    def final_check(self):


            if self.flag == 0:
                self.logger.info("Zabbix HA DB Configuration Success")
                self.api_payload["StatusReason"] = "Zabbix HA DB Primary Configuration Success"
                self.api_payload["Status"] = 2
                # self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Zabbix HA DB Configuration Failed")
                self.api_payload["StatusReason"] = "Zabbix HA DB Primary Configuration Failed"
                self.api_payload["Status"] = 3
                # self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Fail")
                print("3rr0rC0d3[500]")






if __name__ == "__main__":
    call = Zabbix_DB()
    call.update_file()
    call.restart_service()
    #call.run_mysql_commands()
    call.final_check()

