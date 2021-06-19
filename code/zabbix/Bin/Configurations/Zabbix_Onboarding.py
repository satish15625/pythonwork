
# Referenced From https://www.zabbix.com/documentation/4.2/manual/api/reference/action/object
# https://www.zabbix.com/documentation/4.2/manual/api/reference/action/create
# In order to make any changes please refer to the documentation above



import sys,logging, time, subprocess, os, sys, json
status,out=subprocess.getstatusoutput('pip3.7 install pyzabbix')
from pyzabbix import ZabbixAPI
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus


class ZabbixOnboarding():
    """docstring for ZabbixOnboarding"""
    def __init__(self):
        self.flag = 0
        self.root = os.environ['Admin_Root']
        self.server_type = sys.argv[1]
        self.zabbix_host = sys.argv[2]
        self.proxy_name = sys.argv[3]
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
                            "Status": "1", "StatusReason": "Zabbix Onboarding Initiated"
                            }
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/zabbix_onboarding_status_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("SSL Configuration Started.. " + dt)
        self.windows_id = None

    def create_windows_host_group(self):
        """[summary]

        [description]
        """
        # group = ["Windows servers"]
        try:
            method = 'hostgroup.create'
            data = {
                "name": "Windows servers"
            }

            response = self.zapi.do_request(method, data)
            if  response:
                self.windows_id = response ['result']['groupids']
                self.logger.info("win hostgroup id"+str(self.windows_id))
            else:
                self.logger.info("win hostgroup creation failed")
        except:
            self.logger.info("Zabbix API Exception caught:" + str(e))
            self.api_payload["Stage"] = 3
            self.api_payload["StatusReason"] = "Zabbix API Error: " + str(e)
            self.send_status.send_logs([self.api_payload])
            self.flag = 1



    def create_action_linux(self):
        self.logger.info("creating action linux")
        params = {
            "name" : "Auto registration - Linux",
            "value" : "Linux",
            "templateid" : "10001",
            "hostgroup_id": "2"
        }
        resp = self.create_action(params)
        if resp != '':
            self.api_payload["StatusReason"] = "Created action: Auto registration - Linux"
            self.send_status.send_logs([self.api_payload])
            self.logger.info("created action linux: " + ''.join(str(resp)))
        else:
            self.logger.info("failed to create action linux: " + ''.join((resp)))
            self.flag = 1


    def create_action_windows(self):
        self.logger.info("creating action windows")
        id = self.windows_id[0]
        params = {
            "name" : "Auto registration - windows",
            "value" : "Windows",
            "templateid" : "10081",
            "hostgroup_id" : id
        }
        resp = self.create_action(params)
        if resp != 'false':
            self.api_payload["StatusReason"] = "Created action: Auto registration - windows"
            self.send_status.send_logs([self.api_payload])
            self.logger.info("created action linux: " + ''.join(str(resp)))
        else:
            self.logger.info("failed to create action linux: " + ''.join((resp)))
            self.flag = 1


    def create_action(self, params):
        """Creates autoregistration action on zabbix server

        Arguments:
            params {[dict]} -- configuration parameters for windows and
        """
        try:
            post_data = {
                    "name": params['name'],
                    "eventsource": 2,
                    "status": 0,
                    "esc_period": 120,
                    "def_shortdata": "Auto registration: {HOST.HOST}",
                    "def_longdata": "Host name: {HOST.HOST}\r\nAgent port: {HOST.PORT}\r\nHost IP: {HOST.IP}",
                    "filter": {
                    "evaltype": 0,
                    #Meta data condition
                    "conditions": [
                            {
                                "conditiontype": 24, #Host Metadata
                                "operator": 2,
                                "value": params['value']
                            },
                            {
                                "conditiontype": 20, # Proxy
                                "operator": 0,
                                "value": self.proxy_id
                            },
                        ]
                    },

                    "operations": [
                        #Template Option
                          {
                              "operationtype": 6,
                              "optemplate": [
                                   {
                                     "templateid": params['templateid']
                                   }
                             ]
                          },
                          #Add Host
                          {
                              "operationtype": 2,
                          },
                          #Add to host group
                          {
                              "operationtype": 4,
                              "opgroup" : {
                                # Host Group Linux Servers
                                "groupid" : params['hostgroup_id']
                              }
                          },
                          #Enable Host
                          {
                              "operationtype": 8,
                          },

                          #Set Host Inventory Mode
                          {
                              "operationtype": 10,
                              "opinventory" : {
                                "inventory_mode" : "1"
                              }
                          },

                          #Remove from host groups discovered hosts
                          {
                              "operationtype": 5,
                              "opgroup" : {
                                "groupid" : "5"
                              }
                          },

                    ]
                 }


            method = 'action.create'
            response = self.zapi.do_request(method, post_data)
            # print(response)
            if response:
                data = response['result']['actionids']
                return data
            else:
                return 'false'
        except Exception as e:
            self.logger.info("Zabbix API Exception caught:" + str(e))
            self.api_payload["Stage"] = 3
            self.api_payload["StatusReason"] = "Zabbix API Error: " + str(e)
            self.send_status.send_logs([self.api_payload])
            self.flag = 1


    def get_proxy(self):
        """This function finds proxy installed on zabbix, and stores the
        proxy id in a class variable self.proxy_id

        Arguments:
            proxy_name {[string]} -- Name of the proxy
        """
        self.logger.info("getting proxy data")
        proxy_data = {
                "params": {
                    "host": self.proxy_name,
                    "status" : 5
                    # "selectInterface": "extend"
                },
            }
        method = 'proxy.get'
        response = self.zapi.do_request(method, proxy_data)
        response = response['result']
        self.proxy_id = response[0]['proxyid']



    def final_check(self):
        if self.flag == 0:
            self.logger.info("Zabbix Onboarding Success")
            self.api_payload["StatusReason"] = "Zabbix Onboarding Success"
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("Zabbix  Onboarding Failed")
            self.api_payload["StatusReason"] = "Zabbix  Onboarding Failed"
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")


if __name__ == '__main__':

    # command_inputs = sys.argv
    # if len(command_inputs) < 2:
    # 	raise NameError("Please Provide Zabbix ui Hostname or IP Address for accessing the API")


    zabbix = ZabbixOnboarding()
    zabbix.get_proxy()
    zabbix.create_windows_host_group()
    zabbix.create_action_linux()
    zabbix.create_action_windows()
    zabbix.final_check()


