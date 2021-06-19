# File Name:- Zabbix_DB_Proxy_Postcheck.py
# Service Name:- N/A
# Purpose: To perform postcheck on core
# Author Name: Sankar
# Create Date: 28/Sep/20
# Modifed By:-
# Last Modify Date:24/09/2020
# Current Version: 1.0
# Summary of Last Change: Refactor code

import logging, time, os, sys, threading, json, subprocess

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus


class DB_Proxy_Postcheck():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_DB_Proxy_Postcheck_" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB Proxy"
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "4",
                            "Status": "1", "StatusReason": "Initiated Postcheck"
                            }

        self.send_status = sendstatus()
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_Proxy_Postcheck_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("deployement Started on " + dt)

    def check(self):
        try:
            status = subprocess.getoutput("systemctl status mysqld")

            if "active (running)" in status:
                self.logger.info("Post-check Passed")
                self.api_payload["StatusReason"] = "Postcheck Success, mysql service is running"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Post-check Failed")
                self.api_payload[
                    "StatusReason"] = "Postcheck Failed, mysql not running"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[500]")


        except Exception as e:
            self.logger.info("Exception in post check" + str(e))





if __name__ == "__main__":
    postchk = DB_Proxy_Postcheck()
    postchk.check()

