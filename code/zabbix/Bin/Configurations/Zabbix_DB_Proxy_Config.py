# File Name:- Zabbix_DB_Proxy_Config.py
# Service Name:- N/A
# Purpose: To install  zabbix proxy db
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

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus
from database_connection import Fun_Database_Connection,Fun_Fetch_Data,Fun_Update_Data,Fun_Execute,Fun_Close

class DB_Proxy():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_DB_Proxy_Config_" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.db_user =  self.load_variable['db_creds'] ['username']
        self.db_pwd = self.load_variable['db_creds'] ['password']
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB Proxy"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "DB Proxy Configuration Initiated"
                            }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_Proxy_Config_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)

    def config(self):
        try:

            self.logger.info("Configuring database")
            self.api_payload["StatusReason"] = "Configuring database"
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            # Function to connect to database
            connection = Fun_Database_Connection(self.db_user, self.db_pwd, "mysql", 'localhost',
                                                  self.log_file)
            logging.info('Fetching Details From Database for Zabbix')
            logging.info('Creating database zabbix')
            create_db = Fun_Execute(connection,
                                    "create database if not exists zabbix_proxy character set utf8 collate utf8_bin;")
            self.logger.info('Creating User zabbix on the database')
            # Function call to fetch
            create_user = Fun_Execute(connection,
                             "CREATE USER if not exists 'zabbix'@'%' IDENTIFIED WITH mysql_native_password BY '"+self.db_pwd+"';")
            alter_user = Fun_Execute(connection,
                                     "ALTER USER 'zabbix'@'%' IDENTIFIED WITH mysql_native_password BY '"+self.db_pwd+"';")
            self.logger.info('Granting privileges to user zabbix')
            grant_priv = Fun_Execute(connection,
                              "GRANT ALL PRIVILEGES ON *.* TO 'zabbix'@'%' WITH GRANT OPTION;")  # Function call to fetch
            flush_priv = Fun_Execute(connection,"FLUSH PRIVILEGES;")

            self.logger.info('Import initial schema and data.')
            cmd = 'zcat proxy_schema.sql.gz | mysql -uzabbix -p'+self.db_pwd+' zabbix_proxy'
            status,out = subprocess.getstatusoutput(cmd)
            close_sql = Fun_Close(connection)

            if connection != 'false' and flush_priv !='false' and create_db != 'false' and create_user != 'false' and alter_user != 'false' and grant_priv != 'false' and status == 0 and close_sql != 'false':
                self.logger.info("DB Proxy Configuration Success")
                self.api_payload["StatusReason"] = "DB Proxy Configuration Success"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("DB Proxy Configuration Failed")
                self.api_payload["StatusReason"] = "DB Proxy Configuration Failed"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Fail")
                print("3rr0rC0d3[500]")

        except Exception as e:
            self.logger.info("Exception caught" + str(e))




if __name__ == "__main__":
    call = DB_Proxy()
    call.config()
