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

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus
from database_connection import Fun_Database_Connection,Fun_Fetch_Data,Fun_Update_Data,Fun_Execute,Fun_Close

class ZabbixAdminPassword():
    def __init__(self):
        self.default_user = "Admin"
        self.default_pass = "zabbix"
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        self.db_user =  self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.environment = self.load_variable["Environment"]
        self.component = "DB"
        self.new_pass = self.load_variable['new_admin_password']
        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_Config_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def update_password(self):
        connection = Fun_Database_Connection(self.db_user, self.db_pwd,
        											 "mysql", 'localhost', self.log_file)
        create_db = Fun_Execute(connection,
                                    "update zabbix.users set passwd=md5('{}') where alias='Admin';".format(self.new_pass))

       	if connection != "false" and create_db != "false":
       		print("3rr0rC0d3[200]")
       	else:
       		print("3rr0rC0d3[500]")





if __name__ == '__main__':
	password = ZabbixAdminPassword()
	password.update_password()	
		