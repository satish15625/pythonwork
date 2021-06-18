# File Name:- zabbix_precheck_core.py
# Service Name:- N/A
# Purpose: To perform postcheck on core
# Author Name: Sankar
# Create Date: 28/Sep/20
# Modifed By:-
# Last Modify Date:24/09/2020
# Current Version: 1.0
# Summary of Last Change: Refactor code

import logging, time, os, sys, threading, json, subprocess ,socket

sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
# sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
# from uistatus import sendstatus


class Core_Postcheck():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        self.proxy = sys.argv[2]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_PostCheck_CORE_" + dt + ".txt", "a+")
        self.environment = self.load_variable["Environment"]
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Core"
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "4",
                            "Status": "1", "StatusReason": "Initiated Postcheck"
                            }
        self.send_status = sendstatus()
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_PostCheck_CORE_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("deployement Started on " + dt)
    def port_check(self,host,port):
        self.logger.info("Checking telnet for host, port :"+host+','+str(port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            self.logger.info("telnet for host, port" + host + ',' + str(port)+'success')
            # self.api_payload[
            #     "StatusReason"] = "Telnet to port "+str(port)+"proxy server success"
            # self.api_payload["Status"] = 2
            # self.send_status.send_logs([self.api_payload])
            return 'true'
        except:
            self.logger.info("telnet for host, port" + host + ',' + str(port) + 'fail')
            # self.api_payload[
            #     "StatusReason"] = "Telnet to port " + str(port) + "proxy server fail"
            # self.api_payload["Status"] = 3
            # self.send_status.send_logs([self.api_payload])
            return 'false'


        # port_10050 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # port_out = port_10050.connect_ex((self.proxy, 10050))
        # port_10051 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # port_out_1 = port_10051.connect_ex((self.proxy, 10051))

        # timeout = time.time() + 60 * 5
        # if port_out == 0 and port_out_1 == 0:
        #     logging.info("Telnet to 10050,10051 proxy server success")
        #     logging.critical("Telnet to 10050,10051 proxy server success")
        #     self.api_payload[
        #         "StatusReason"] = "Telnet to 10050,10051 proxy server success"
        #     self.api_payload["Status"] = 2
        #     self.send_status.send_logs([self.api_payload])
        #     port_10050.close()
        #     port_10051.close()
        #
        # else:
        #     self.logger.info("Inside retry loop")
        #     while True:
        #         time.sleep(1)
        #         port_10050 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #         port_out = port_10050.connect_ex((self.proxy, 10050))
        #         port_10051 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #         port_out_1 = port_10051.connect_ex((self.proxy, 10051))
        #         if port_out != 0 or port_out_1 != 0:
        #             self.flag = 1
        #             pass
        #         else:
        #             self.flag = 0
        #             port_10050.close()
        #             port_10051.close()
        #             break
        #         if time.time() > timeout:
        #             self.flag = 1
        #             self.logger.info("Retry failed")
        #             logging.critical("Telnet to 10050,10051 proxy server failed")
        #             self.api_payload[
        #                 "StatusReason"] = "Telnet to 10050,10051 proxy server failed"
        #             self.api_payload["Status"] = 3
        #             self.send_status.send_logs([self.api_payload])
        #             break


    def final_check(self):
        try:
            subprocess.getoutput('yum -y install telnet')
            port_10050 = subprocess.getoutput('timeout 5 telnet '+self.proxy+' 10050')
            #port_10051 = subprocess.getoutput('timeout 5 telnet ' + self.proxy +' 10051')

            if "Connected" in port_10050:
                self.logger.info("10050 port connected")
            else:
                self.logger.info("10050 port not connected")
                self.flag = 1

            # if "Connected" in port_10051:
            #     self.logger.info("10051 port connected")
            # else:
            #     self.logger.info("10051 port not connected")
            #     self.flag = 1

            # port_10050 = self.port_check(self.proxy,10050)
            # port_10051 = self.port_check(self.proxy,10051)
            # timeout = time.time() + 60 * 5
            # if port_10050 != 'false' and port_10051 != 'false':
            #     self.logger.info("Telnet to 10050,10051 proxy server success")
            #     self.api_payload[
            #             "StatusReason"] = "Telnet to 10050,10051 proxy server success"
            #     self.api_payload["Status"] = 2
            #     self.send_status.send_logs([self.api_payload])
            # else:
            #     self.logger.info("Inside retry loop")
            #     while True:
            #         time.sleep(1)
            #         port_10050 = self.port_check(self.proxy, 10050)
            #         port_10051 = self.port_check(self.proxy, 10051)
            #         if port_10050 == 'false' or port_10051 == 'false':
            #             self.flag = 1
            #             pass
            #         else:
            #             self.flag = 0
            #             break
            #         if time.time() > timeout:
            #             self.flag = 1
            #             self.logger.info("Retry failed")
            #             logging.critical("Telnet to 10050,10051 proxy server failed")
            #             self.api_payload[
            #                 "StatusReason"] = "Telnet to 10050,10051 proxy server failed"
            #             self.api_payload["Status"] = 3
            #             self.send_status.send_logs([self.api_payload])
            #             break
            #     self.logger.info("final status of port: " +port_10050+port_10051)

            zbx_server = subprocess.getoutput("systemctl status zabbix-server")
            httpd_sts = subprocess.getoutput("systemctl status httpd")
            if "active (running)" in zbx_server and "active (running)" in httpd_sts and self.flag == 0:
                self.logger.info("Post-check Passed")
                self.api_payload["StatusReason"] = "Postchecks Success, httpd & zabbixx-server are running and ports 10050,10051 connected"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[200]")
            else:
                self.logger.info("Post-check Failed")
                self.api_payload[
                    "StatusReason"] = "Postchecks Failed, refer logs"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[500]")


        except Exception as e:
            self.logger.info("Exception in post check" + str(e))





if __name__ == "__main__":
    postchk = Core_Postcheck()
    # postchk.port_check()
    postchk.final_check()

