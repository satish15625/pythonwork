# File Name:- zabbix_install_Core_v5.0.py
# Service Name:- N/A
# Purpose: Installing mysql for zabbix
# Author Name: Satish
# Create Date: 25/Sep/20
# Modifed By:- Sankar
# Last Modify Date: 28/Sep/20
# Current Version: 1.0
# Summary of Last Change: refactoring again



from shutil import copyfile
import logging, time, subprocess, os, sys, json,subprocess
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
from uistatus import sendstatus

class Zabbix_Install_Core():

    def __init__(self):
        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.environment = self.load_variable["Environment"]
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Core"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                                "ServerType": self.server_type, "Environment": self.environment, "Stage": "2",
                                "Status": "1", "StatusReason": "Zabbix Core installation initiated"
                                }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])

        self.log_file = self.root + "/zabbix/Logs/Zabbix_Install_Core" + dt + ".log"
        self.output = open(self.root + "/zabbix/Output/Zabbix_Install_Core_" + dt + ".txt", "w+")
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Installing Zabbix RPM Started " + dt)

    ''' Zabbix Core Instalation '''
    def Install_Zabbix(self):

        try:
            self.logger.info('--------Starting-------')
            # if not os.path.exists(Conf_File):
            #     self.logger.info('Conf.php does not exists in Input folder')
            #     self.logger.info('Exiting Script')
            #     self.output.writelines("Fail")

            # status,prim_fqdn=commands.getstatusoutput('hostname --fqdn')
            # # strip(prim_fqdn)
            # status,p_IP_IP=commands.getstatusoutput('hostname -I')
            # # strip(p_IP)
            # status,hostname=commands.getstatusoutput('hostname')

            self.logger.info("Installing Zabbix Core components")
            # self.api_payload["StatusReason"] = "Installing Zabbix RPM For Core"
            status1,out = subprocess.getstatusoutput("yum -y install httpd")
            status,out = subprocess.getstatusoutput("systemctl restart httpd")



            self.logger.info('Checking if Zabbix rpm zabbix-release-5.0-1.el7.noarch is installed')
            self.api_payload["StatusReason"] = "Checking if Zabbix rpm Installed or Not"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])

            cmd='rpm -qa|grep zabbix-release-5.0-1.el7.noarch'

            if(os.system(cmd)==0):
                # print ("already installed")
                self.logger.info('Zabbix rpm zabbix-release-5.0-1.el7.noarch is already installed')
                self.api_payload["StatusReason"] = "Zabbix rpm already installed"
                self.api_payload["Status"] = 2
                self.send_status.send_logs([self.api_payload])
            else:
                self.logger.info('Going to install Zabbix rpm zabbix-release-5.0-1.el7.noarch')
                self.api_payload["StatusReason"] = "Installing Zabbix RPM For Core"
                self.api_payload["Status"] = 2
                self.send_status.send_logs([self.api_payload])
                command = ['rpm',
                        '-Uvh',
                        'https://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm']
                p = subprocess.Popen(command)
                p.wait()
                if p.returncode == 0:
                    self.logger.info("Zabbix rpm zabbix-release-5.0-1.el7.noarch successfully installed")
                    self.api_payload["StatusReason"] = "Installed Zabbix RPM zabbix-release-5.0-1.el7.noarch"
                    self.api_payload["Status"] = 2
                    self.send_status.send_logs([self.api_payload])
                else:
                    self.logger.info(" Unable to install Zabbix RPM zabbix-release-5.0-1.el7.noarch")
                    self.flag = 1
            self.logger.info("Going to install zabbix server, front-end and agent")
            self.api_payload["StatusReason"] = "Going to install zabbix server front-end and agent"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
            
            os.system("yum clean all")
            subprocess.getoutput('yum-config-manager --enable rhel-server-rhscl-7-rpms')
            self.logger.info("Creating repos")
            self.api_payload["StatusReason"] = "Enable yum-config-manager --enable rhel-server-rhscl-7-rpms"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])

            zabbix_repo = '/etc/yum.repos.d/zabbix.repo'
            with open(zabbix_repo) as repofile:
                edited_txt = repofile.read().replace("enabled=0", 'enabled=1')

            with open(zabbix_repo, "w") as repofile:
                repofile.write(edited_txt)
                self.logger.info("Repos created")
                self.api_payload["StatusReason"] = "yum Repos created Done"
                self.api_payload["Status"] = 2
                self.send_status.send_logs([self.api_payload])

            subprocess.getoutput('yum-config-manager --enable rhel-server-rhscl-7-rpms')
            status2,out = subprocess.getstatusoutput('yum -y install zabbix-server-mysql zabbix-agent >>'+self.log_file)
            status3,out = subprocess.getstatusoutput('yum -y install zabbix-web-mysql-scl zabbix-apache-conf-scl >>'+self.log_file)
            timeout = time.time() + 60 * 5
            self.logger.info("Initial status1,2,3:"+str(status1)+str(status2)+str(status3))
            self.api_payload["StatusReason"] = "install zabbix-server-mysql zabbix-agent & install zabbix-web-mysql-scl"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
            
            if status2 != 0 or status3 != 0:
                self.logger.info("Inside retry loop")
                while True:
                    time.sleep(1)
                    status2, out = subprocess.getstatusoutput(
                        'yum -y install zabbix-server-mysql zabbix-agent >>' + self.log_file)
                    status3, out = subprocess.getstatusoutput(
                        'yum -y install zabbix-web-mysql-scl zabbix-apache-conf-scl >>' + self.log_file)
                    if status2 != 0 or status3 !=0:
                        self.flag = 1
                        pass
                    else:
                        self.flag = 0
                        break
                    if time.time() > timeout:
                        self.flag = 1
                        self.logger.info("Retry failed")
                        break
            else:
                pass
            self.logger.info("Final status1,2,3:"+str(status1)+str(status2)+str(status3))

            if self.flag == 0:
                self.api_payload["StatusReason"] = "Zabbix Core Installation Success"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Pass")
                self.logger.info("Core Installation Success")
                print("3rr0rC0d3[200]")
            else:
                self.api_payload["StatusReason"] = "Zabbix Core Installation Failed"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Fail")
                self.logger.info("Core Installation Failed")
                print("3rr0rC0d3[500]")


        except Exception as e:
            self.logger.info("Exception caught:" + str(e))




if __name__ == "__main__":

    zabbix = Zabbix_Install_Core()
    zabbix.Install_Zabbix()

