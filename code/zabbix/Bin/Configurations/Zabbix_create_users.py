
# Using the following link for reference
#https://www.zabbix.com/documentation/3.4/manual/api/reference/mediatype/create
try:
    from pyzabbix import ZabbixAPI, ZabbixAPIException
except:
    status,out=commands.getstatusoutput('pip3.7 install pyzabbix')
import os
import sys
from pyzabbix import ZabbixAPI
import sys,logging, time, subprocess, os, sys, json, csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Users():


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
                            "Status": "1", "StatusReason": "Creating Users"
                            }
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/zabbix_create_users_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Group creation Started.. " + dt)


    def create(self ):
        try:
            reader = csv.DictReader(open(self.root+'/zabbix/Input/users.csv'))

            for raw in reader:
                name = raw ['name']
                uname = raw['username']
                pwd  = raw['password']
                typ = raw['type']
                group = raw['groupname']
                email = raw['email']
                grouplookup = self.zapi.usergroup.get(filter=({'name':str(group)}))
                group_id = grouplookup[0]["usrgrpid"]
                if group_id != '':
                    method = 'user.create'
                    send_data = {"name":  name,"alias": uname, "passwd": pwd, "type": str(typ),
                                 "usrgrps": [{"usrgrpid": group_id}] ,
                                 "user_medias":[{"mediatypeid":"1","sendto":[email]}]}
                    response = self.zapi.do_request(method, send_data)
                    if response:
                        data = response['result']['userids']
                        self.logger.info(uname+" user creation success: id-"+  ''.join(data))
                    else:
                        self.logger.info("user creation failed for :"+ uname)


        except Exception as e:
            self.logger.info("Zabbix API Exception caught:" + str(e))
            self.api_payload["Stage"] = 3
            self.api_payload["StatusReason"] = "Zabbix API Error: " + str(e)
            self.send_status.send_logs([self.api_payload])
            self.flag = 1

    def final_check(self):
        if self.flag == 0:
            self.logger.info("Users Created Successfully")
            self.api_payload["StatusReason"] = "Users Created Successfully"
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("Users Creation failed")
            self.api_payload["StatusReason"] = "Users Creation failed"
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")


if __name__ == '__main__':

 zabbix = Users()
 zabbix.create()
 zabbix.final_check()