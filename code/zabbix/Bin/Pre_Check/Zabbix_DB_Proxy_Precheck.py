    # File Name:- Zabbix_DB_Proxy_Precheck.py
    # Service Name:- N/A
    # Purpose: To perform prechecks on zabbix proxy db
    # Author Name: Sankar
    # Create Date: 24/Sep/20
    # Modifed By:-
    # Last Modify Date:
    # Current Version: 1.0
    # Summary of Last Change: N/A

    import logging, time, subprocess, os, sys, json,requests

    sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
    sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
    from uistatus import sendstatus
    from precheck import prechecks


    class DB_Precheck():

    def __init__(self):

        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)

        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.output = open(self.root + "/zabbix/Output/Zabbix_DB_Proxy_Precheck_" + dt + ".txt", "w+")
        self.environment = self.load_variable["Environment"]
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "DB Proxy"
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                            "ServerType": self.server_type, "Environment": self.environment, "Stage": "1",
                            "Status": "1", "StatusReason": "Initiated precheck"
                            }
        self.checks = prechecks()
        self.checks.api_call("Zabbix", self.component, self.hostname, self.server_type, self.environment)
        self.send_status = sendstatus()
        self.log_file = self.root + "/zabbix/Logs/Zabbix_DB_Proxy_Precheck_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Deployment Started on " + dt)

    def make_dirs(self):
        try:
            if not os.path.exists(self.root + "/zabbix/Logs") and not os.path.exists(self.root + "/zabbix/Output"):
                subprocess.getoutput("mkdir " + self.root + "/zabbix/Logs")
                subprocess.getoutput("mkdir " + self.root + "/zabbix/Output")
            else:
                self.logger.info("Log,Output dirs exists")
        except Exception as e:
            self.logger.info("Make dirs failed" + str(e))

    def root_check(self):

        try:
            # Check Root Login
            user = subprocess.getoutput("whoami")
            rootcheck = subprocess.getoutput("echo $EUID")
            if int(rootcheck) != 0:
                self.logger.info(
                    "Please execute script with Sudo Privileges,User:: " + user + " may not have sudo privileges on " + self.hostname)
                self.api_payload[
                    "StatusReason"] = "Please execute script with Sudo Privileges,User:: " + user + " may not have sudo privileges on " + self.hostname
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[500]")
                sys.exit()
            else:
                # print("Root Account detected.")
                self.logger.info("Root Account detected.")
                self.api_payload["StatusReason"] = "Prechecks Initiated"
                self.api_payload["Status"] = 1
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

    def internet_check(self):
        try:
            # r = requests.get(url, timeout=timeout)
            self.logger.info('Checking Internet Connectivity')

            self.api_payload["StatusReason"] = "Checking Internet Connectivity"
            self.send_status.send_logs([self.api_payload])
            r = requests.head(url='http://www.google.com/', timeout=3)
            if r.status_code == 200:
                self.api_payload["StatusReason"] = "Internet Connectivity Present"
                self.send_status.send_logs([self.api_payload])
                self.logger.info('Internet Connectivity Present')

            else:
                self.flag = 1
                self.api_payload["StatusReason"] = "Internet Connectivity Not-Present.Please check log for more details"
                self.send_status.send_logs([self.api_payload])
                self.logger.info('Internet Connectivity Not-Present')

        except requests.ConnectionError as ex:
            self.flag = 1
            self.api_payload["StatusReason"] = "Internet Connectivity Not-Present.Please check log for more details"
            self.send_status.send_logs([self.api_payload])
            self.logger.info('Internet Connectivity Not-Present')
            self.logger.info(str(ex))

    def internet_check(self):
        try:
            # r = requests.get(url, timeout=timeout)
            self.logger.info('Checking Internet Connectivity')

            self.api_payload["StatusReason"] = "Checking Internet Connectivity"
            self.send_status.send_logs([self.api_payload])
            r = requests.head(url='http://www.google.com/', timeout=3)
            if r.status_code == 200:
                self.api_payload["StatusReason"] = "Internet Connectivity Present"
                self.send_status.send_logs([self.api_payload])
                self.logger.info('Internet Connectivity Present')

            else:
                self.flag = 1
                self.api_payload["StatusReason"] = "Internet Connectivity Not-Present.Please check log for more details"
                self.send_status.send_logs([self.api_payload])
                self.logger.info('Internet Connectivity Not-Present')

        except requests.ConnectionError as ex:
            self.flag = 1
            self.api_payload["StatusReason"] = "Internet Connectivity Not-Present.Please check log for more details"
            self.send_status.send_logs([self.api_payload])
            self.logger.info('Internet Connectivity Not-Present')
            self.logger.info(str(ex))

    def rhel_sub_check(self):
        try:
            self.logger.info('Checking RHEL Subscription status')
            self.api_payload["StatusReason"] = "Checking RHEL Subscription status"
            self.send_status.send_logs([self.api_payload])
            rhel_sts = subprocess.getoutput("subscription-manager list | egrep -i 'status:'")
            self.logger.info(str(rhel_sts))

            time.sleep(5)
            if 'not' in rhel_sts.lower() or 'unknown' in rhel_sts.lower() or 'unsubscribed' in rhel_sts.lower():
                self.flag = 1
                self.api_payload["StatusReason"] = "RHEL Not-Subscribed"
                self.send_status.send_logs([self.api_payload])
                self.logger.info("RHEL Not-Subscribed")
            else:
                self.api_payload["StatusReason"] = "RHEL Subscribed"
                self.send_status.send_logs([self.api_payload])
                self.logger.info("RHEL Subscribed")


    def disk_check(self):
        try:
            self.logger.info("Root Disk Qualification started")
            self.output.write('TestName,Status,Recommended Value,Actual Value\n')
            disk = self.load_variable["requirement"][self.component]['disk']
            dirname = ['var/lib']
            for i in dirname:
                diskstatus = self.checks.disk_check(i, disk)

                if diskstatus == True:
                    self.logger.info("Disk Check Passed. " + i)
                    self.output.write("Root Disk space Check: PASS, " + i + "\n")
                else:
                    self.logger.info("Root Disk Check: FAIL " + i)
                    self.flag = 1
                    self.output.write("Root Disk Space Check: FAIL," + i + "\n")
        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

    def memory_check(self):
        try:
            self.logger.info("Memory Check Started")
            memory = self.load_variable["requirement"][self.component]['memory']
            mem_status = self.checks.memory_check(memory)
            if mem_status == True:
                # #print("CPU check PASS")
                self.logger.info("Memory Check PASS")
                self.output.write("Memory Check: PASS, " + "\n")
            else:
                # #print("CPU Check FAILED")
                self.logger.info("Memory Check FAILED")
                self.flag = 1
                self.output.write("Memory Check: FAIL, " + "\n")
        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

    def mysql_check(self):
        try:
            self.logger.info("Mysql Trace Check Started")
            sqlstatus = self.checks.sql_check()
            if sqlstatus == True:
                # print("MYSQL traces found in the server. Check FAILED")
                self.logger.info("MYSQL traces not found in the server. CHECK PASS")
                self.output.writelines("MYSQL existence Check: PASS,Not Present\n")

            else:
                # print("MYSQL not found in the server. Check PASS")
                self.flag = 1
                self.logger.info("MYSQL found in the server. Check FAIL")
                self.output.writelines("MYSQL existence Check: FAIL,  Present\n")

        except Exception as e:
            self.logger.info("Exception caught:" + str(e))
    def cpu_check(self):
        try:
            cpu = self.load_variable["requirement"][self.component]['cpu']
            self.logger.info("CPU Check Started")
            cpu_status = self.checks.cpu_check(cpu)
            if cpu_status == True:
                self.logger.info("CPU Check PASS")
                self.output.writelines("CPU Check: PASS, " + "\n")
            else:
                self.logger.info("CPU Check FAILED")
                self.flag = 1
                self.output.writelines("CPU Check: FAIL, " + "\n")
        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

    def os_check(self):
        try:
            os_verion = self.load_variable["requirement"][self.component]['os_version']
            self.logger.info("OS Version Check started")
            os_status = self.checks.os_check(os_verion)
            if os_status == True:
                self.logger.info("Linux OS qualification Check pass")
                self.output.writelines("Linux OS Version " + (','.join(os_verion)) + ": PASS,Above or Equal" + "\n")
            else:
                self.logger.info("Linux OS Version " + (','.join(os_verion)) + " Failed")
                self.output.writelines("OS Version Check " + (','.join(os_verion)) + ": FAIL\n")
                self.flag = 1
        except Exception as e:
            self.logger.info("Exception caught:" + str(e))
    def port_check(self):
        try:
            self.logger.info("Port Check Started")

            ports = self.load_variable["requirement"][self.component]['ports']
            for j in ports:
                port_status = self.checks.port_check(j)
                if port_status == True:
                    self.logger.info("Port " + j + " is opened on the server")
                    self.output.writelines("Port Check: PASS ," + j + "\n")
                else:
                    self.logger.info("Port " + j + " not opened.")
                    self.flag = 1
                    self.output.writelines("Port Check: FAIL ," + j + "\n")

        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

    def firewall_disable(self):
        try:
            subprocess.getstatusoutput('service firewalld stop')
            subprocess.getstatusoutput('systemctl disable firewalld')
            #disabling selinux
            cmd = subprocess.getoutput('sestatus')
            if "disabled" in cmd:
                self.logger.info("SElinux already disabled")
            else:
                subprocess.getstatusoutput('setenforce 0')
            # if status1 == 0 and status2 == 0 and status3 == 0:
            #     self.logger.info("Disabled firewalld and selinux")
            # else:
            #     self.logger.info("firewalld and selinux not disabled")
            #     self.flag = 1
        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

    def final_check(self):
        try:
            if self.flag == 0:
                self.logger.info("All Pre-check Passed")
                self.api_payload["StatusReason"] = "Prechecks completed successfully"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[200]")

            else:
                self.logger.info("Pre-check Failed")
                self.api_payload["StatusReason"] = "Precheck failed kindly refer to log for more details"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                print("3rr0rC0d3[500]")

        except Exception as e:
            self.logger.info("Exception caught:" + str(e))


    if __name__ == "__main__":
    precheck = DB_Precheck()
    precheck.make_dirs()
    precheck.root_check()
    precheck.internet_check()
    precheck.rhel_sub_check()
    precheck.disk_check()
    precheck.memory_check()
    precheck.mysql_check()
    precheck.cpu_check()
    precheck.os_check()
    precheck.firewall_disable()
    precheck.port_check()
    precheck.final_check()

