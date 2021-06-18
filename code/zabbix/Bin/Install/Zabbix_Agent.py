

import logging, time, subprocess, os, sys, json,subprocess
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Zabbix_Agent():

    def __init__(self):
        self.flag = 0
        self.server_type = sys.argv[1]
        self.zabbix_server = sys.argv[2]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.environment = self.load_variable["Environment"]
        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Agent"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                                "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                                "Status": "1", "StatusReason": "Zabbix Agent installation started"
                                }

        self.send_status.send_logs([self.api_payload])

        self.log_file = self.root + "/zabbix/Logs/Zabbix_Agent" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Installing Zabbix Agent " + dt)

    def Install_RPM(self):

        cmd = 'rpm -qa|grep zabbix-release-5.0-1.el7.noarch'
        if (os.system(cmd) == 0):
            self.logger.info('Zabbix rpm zabbix-release-5.0-1.el7.noarch is already installed')

        else:
            self.logger.info('installing Zabbix rpm zabbix-release-5.0-1.el7.noarch')
            command = ['rpm','-Uvh','https://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm']
            p = subprocess.Popen(command)
            p.wait()
            if p.returncode == 0:
                self.logger.info("Zabbix rpm zabbix-release-5.0-1.el7.noarch successfully installed")
            else:
                self.logger.info(" Unable to install Zabbix RPM zabbix-release-5.0-1.el7.noarch")
                self.flag = 1

    def Install_Agent(self):

        if(self.flag != 1):
            status,out = subprocess.getstatusoutput("yum -y install zabbix-agent")
            status2,out = subprocess.getstatusoutput("service zabbix-agent start")
            if (status != 0 or status2 != 0):
                self.flag = 1
            else :
                
                status3,out = subprocess.getstatusoutput('systemctl status zabbix-agent')
                if(status3 == 1) :
                    self.flag =1

    def Final(self):

        # zabbix_configuration_file = '/etc/zabbix/zabbix_agentd.conf'
        # f = open('/etc/zabbix/zabbix_agentd.conf', 'w+')
        # config_file = f.read()
        # config_file = config_file.replace('Server=127.0.0.1', 'Server='+self.zabbix_server)
        # config_file = config_file.replace('ServerActive=127.0.0.1', 'ServerActive=' + self.zabbix_server)
        # config_file = config_file.replace('Hostname=Zabbix server', 'Hostname='+self.hostname)
        # config_file = config_file.replace('LogFileSize=0', 'LogFileSize=1')
        # config_file = config_file.replace('# LogRemoteCommands=0', 'LogRemoteCommands=1')
        # f.write(config_file)
        # f.close()
        FileName='/etc/zabbix/zabbix_agentd.conf'

        with open(FileName) as f:
            newText=f.read().replace('Server=127.0.0.1', 'Server='+self.zabbix_server)
        with open(FileName, "w") as f:
            f.write(newText)
        with open(FileName) as f:
            newText=f.read().replace('ServerActive=127.0.0.1', 'ServerActive=' + self.zabbix_server)
        with open(FileName, "w") as f:
            f.write(newText)
        with open(FileName) as f:
            newText=f.read().replace('Hostname=Zabbix server', 'Hostname='+self.hostname)
        with open(FileName, "w") as f:
            f.write(newText)

        with open(FileName) as f:
            newText=f.read().replace('LogFileSize=0', 'LogFileSize=1')
        with open(FileName, "w") as f:
            f.write(newText)

        with open(FileName) as f:
            newText=f.read().replace('# LogRemoteCommands=0', 'LogRemoteCommands=1')
        with open(FileName, "w") as f:
            f.write(newText)

        with open(FileName) as f:
            newText=f.read().replace('# HostMetadataItem=', 'HostMetadataItem=system.uname')
        with open(FileName, "w") as f:
            f.write(newText)

        subprocess.getstatusoutput("service zabbix-agent restart")

        if self.flag == 0:
            self.api_payload["StatusReason"] = "Zabbix Agent Installation Success"
            self.api_payload["Status"] = 2
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            self.logger.info("Agent Installation Success")
            print("3rr0rC0d3[200]")
        else:
            self.api_payload["StatusReason"] = "Agent  Installation Failed"
            self.api_payload["Status"] = 3
            self.send_status.send_status([self.api_payload])
            self.send_status.send_logs([self.api_payload])
            self.logger.info("Agent Installation Failed")
            print("3rr0rC0d3[500]")

if __name__ == "__main__":
    zabbix = Zabbix_Agent()
    zabbix.Install_RPM()
    zabbix.Install_Agent()
    zabbix.Final()



