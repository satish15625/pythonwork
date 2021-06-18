# File Name:- Zabbix_Mysql_DB Slave.py
# Service Name:- N/A
# Purpose: To config  zabbix  db Slave
# Author Name: Satish Kumar
# Create Date: 20/Dec/20
# Modifed By:-24/00/20
# Last Modify Date:
# Current Version: 2.0
# Summary of Last Change: To Configure Slave on DB Secondary Server.


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
        self.master_ip = sys.argv[2]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_MySql_DB_Config_Secondary" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.db_user =  self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.hostname = subprocess.getoutput("hostname -s")

        #self.master_ip = '10.1.150.204'
        self.dbname ='zabbix'
        self.dbUser = 'zabbix'
        self.dbPass ='Password@12"'
        self.HOST = "localhost"
        self.PORT = 3306
        self.FILE = "zabbix_bkp.sql"
        self.component = "DB"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Zabbix MYSQL DB Slave Confiuration Initiated"
                            }
        # self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_Mysql_DB_Config_Slave" + dt + ".log"
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
            self.logger.info("Updating the my.cnf file Master")

            conf_data = [
                "server-id = 2\n",
                "log-bin = mysql-bin\n",
                "relay-log = relay-log-server\n",
                "read-only = ON\n",
                "gtid-mode=ON\n",
                "enforce-gtid-consistency\n",
                "log-slave-updates\n"
            ]

            # production config path
            file_object = open('/etc/my.cnf', 'a')
            file_object.writelines(conf_data)
            file_object.close()
        except Exception as e:
            self.logger.info("Exception caught updating  my.cnf file" + str(e))
            self.flag = 1

    # def dbDump(self):
    #     """
    #         Dumping mysql databse Master Database
    #     """
    #     command = "mysqldump --user='zabbix' --password='Password@12' -h 10.1.150.204 zabbix > mysqldump.sql"

    #     os.system(command)

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

    def restart_mysql(self):
        reset = "systemctl restart mysqld"
        os.system(reset)


    def run_mysql_commands(self):

        try:
           
            USERNAME = "zabbix"
            PASSWORD = "Password@12"
            DBNAME = "zabbix"
            HOST = "localhost"
            PORT = 3306
            FILE = "zabbix_bkp.sql"
            conn = None
            
            conn = mysql.connector.connect(host='localhost',
                                        database=DBNAME,
                                        user=USERNAME,
                                        password=PASSWORD)

            if conn.is_connected():
                print('Connected to MySQL database')

                print("Configuring.............")
                mycursor=conn.cursor()

                #Close the file
                

                #execute mysql query
                print('All Database List')
                print('--------------------------')

                mycursor.execute("SHOW DATABASES")

                for x in mycursor:
                    print(x)

                command = """mysql -u %s -p"%s" --host %s --port %s %s < %s""" %(USERNAME, PASSWORD, HOST, PORT, DBNAME, FILE)
                os.system(command)    
                
                mycursor.execute("stop slave;")
                
                mycursor.execute("reset slave;")
                    
                mycursor.execute("stop slave;")

                #tmpsecond = "CHANGE MASTER TO MASTER_HOST = '{ip}', MASTER_PORT = 3306, MASTER_USER = '{dbuser}', MASTER_PASSWORD = '{password}', MASTER_AUTO_POSITION = 1;".format(ip=self.master_ip,dbuser=self.dbUser,password=self.dbPass)
                tmpsecond = "CHANGE MASTER TO MASTER_HOST = '10.1.150.204', MASTER_PORT = 3306, MASTER_USER ='zabbix', MASTER_PASSWORD = 'Password@12', MASTER_AUTO_POSITION = 1;"
                mycursor.execute(tmpsecond)
                
                mycursor.execute("start slave;")
         
                mycursor.execute("show slave status;")
                
                self.logger.info("--------------Slave Configuration done-----------------------")

            else:
                self.logger.info("Connection err")
                self.flag = 1
        except Exception as e:
            self.logger.info("Exception caught during config" + str(e))
            self.flag = 1


    def final_check(self):


            if self.flag == 0:
                self.logger.info("Zabbix Mysql DB Master Configuration Success")
                self.api_payload["StatusReason"] = "Zabbix Mysql DB Slave Configuration Success"
                self.api_payload["Status"] = 2
                # self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Zabbix HA DB Configuration Failed")
                self.api_payload["StatusReason"] = "Zabbix Mysql DB Slave Configuration Failed"
                self.api_payload["Status"] = 3
                # self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                # self.output.writelines("Fail")
                print("3rr0rC0d3[500]")


if __name__ == "__main__":
    call = Zabbix_DB()
    call.update_file()
    #call.dbDump()
    #call.restart_service()
    call.restart_mysql()
    call.run_mysql_commands()
    call.final_check()

