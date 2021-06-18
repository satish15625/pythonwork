
# Using the following link for reference
#https://www.zabbix.com/documentation/3.4/manual/api/reference/mediatype/create
try:
    from pyzabbix import ZabbixAPI, ZabbixAPIException
except:
    status,out=commands.getstatusoutput('pip3.7 install pyzabbix')
import os
import sys

from pyzabbix import ZabbixAPI
import sys,logging, time, subprocess, os, sys, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class ZabbixSMTPConfigure():


    def __init__(self):
        self.flag = 0
        self.root = os.environ['Admin_Root']
        self.server_type = sys.argv[1]
        self.zabbix_host = sys.argv[2]
        self.zapi = ZabbixAPI("https://{}/zabbix".format(self.zabbix_host))
        self.zapi.session.verify = False
        self.zapi.login("Admin", "zabbix")
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.hostname = subprocess.getoutput("hostname -s")
        self.environment = self.load_variable["Environment"]
        self.component = "Core"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                            "Status": "1", "StatusReason": "Zabbix SMTP Initiated"
                            }
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/zabbix_smtp_status_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("SMTP Configuration Started.. " + dt)




    def create_smtp(self ):
        try:
            method1 = 'mediatype.update'
            send_data = {
                "mediatypeid" : "1",
                "status": 0,
                "type": 0,
                "smtp_server": self.load_variable['smtp_details'] ['smtp_server'],
                "smtp_helo": self.load_variable['smtp_details'] ['smtp_helo'],
                "smtp_email": self.load_variable['smtp_details'] ['smtp_email'],
                "smtp_port": self.load_variable['smtp_details'] ['smtp_port'],
                "username": self.load_variable['smtp_details'] ['username'],
                "passwd": self.load_variable['smtp_details'] ['passwd'],
                "smtp_authentication": self.load_variable['smtp_details'] ['smtp_authentication'],
                "smtp_security": self.load_variable['smtp_details'] ['smtp_security']

            }

            response = self.zapi.do_request(method1, send_data)
            if response:
                data = response['result']['mediatypeids']
                self.logger.info("smtp success:"+  ''.join(data))
            else:
                self.flag = 1


        except Exception as e:
            self.logger.info("Zabbix API Exception caught:" + str(e))
            self.api_payload["Stage"] = 3
            self.api_payload["StatusReason"] = "Zabbix API Error: " + str(e)
            self.send_status.send_logs([self.api_payload])
            self.flag = 1
    def activate(self):
        try:

            method = 'action.update'
            send_data = {"actionid": "3", "status": "0"}
            response = self.zapi.do_request(method, send_data)
            if response:
                data = response['result']['actionids']
                self.logger.info("Activated  notification action :" + ''.join(data))
            else:
                self.logger.info("Notfication action activation failed")


        except Exception as e:
            self.logger.info("Zabbix API Exception caught:" + str(e))
    def final_check(self):
        if self.flag == 0:
            self.logger.info("SMTP Configuration Success")
            self.api_payload["StatusReason"] = "SMTP Configuration Success"
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("SMTP Configuration Failed")
            self.api_payload["StatusReason"] = "SMTP Configuration Failed"
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")


if __name__ == '__main__':

 zabbix = ZabbixSMTPConfigure()
 zabbix.create_smtp()
 zabbix.activate()
 zabbix.final_check()