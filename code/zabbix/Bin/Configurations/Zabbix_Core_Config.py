# File Name:- Zabbix_Core_Config.py
# Service Name:- N/A
# Purpose: Installing mysql for zabbix
# Author Name: Satish
# Create Date: 28/Sep/20
# Modifed By:-
# Last Modify Date:
# Current Version: 1.0
# Summary of Last Change: N/A



from shutil import copyfile
import logging, time, subprocess, os, sys, json
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
# sys.path.insert(0, os.environ["Admin_Root"] +'zabbix/Variables/')
sys.path.insert(0, os.environ["Admin_Root"] +'/zabbix/Input/')

from uistatus import sendstatus
# from sendstatus import authenticate,SendLog,SendStatus
# from variables import *

class Zabbix_Config_Core():

    def __init__(self):
        self.flag = 0
        self.server_type = sys.argv[1]
        self.db_ip = sys.argv[2]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.Conf_File=self.root+'/zabbix/Input/conf.php'
        self.Conf_File1=self.root+'/zabbix/Input/conf1.php'

        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        # self.status, self.output = subprocess.getstatusoutput("sudo -v")
        self.environment = self.load_variable["Environment"]
        self.db_usr = self.load_variable['db_creds']['username']
        self.db_pwd = self.load_variable['db_creds']['password']
        self.timezone = self.load_variable['Timezone']

        self.hostname = subprocess.getoutput("hostname -s")
        self.component = "Core"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                                "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                                "Status": "1", "StatusReason": "Core Configuration Initiated"
                                }
        self.send_status.send_status([self.api_payload])
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/Zabbix_Core_Config" + dt + ".log"
        self.output = open(self.root + "/zabbix/Output/Zabbix_Core_Config_" + dt + ".txt", "a+")
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Configuring Zabbix Core " + dt)

    def Config(self):


        try:
            # Agent conf part
            FileName_agent = '/etc/zabbix/zabbix_agentd.conf'

            with open(FileName_agent) as f:
                newText = f.read().replace('Server=127.0.0.1', 'Server=' + self.hostname)
            with open(FileName_agent, "w") as f:
                f.write(newText)
            with open(FileName_agent) as f:
                newText = f.read().replace('ServerActive=127.0.0.1', 'ServerActive=' + self.hostname)
            with open(FileName_agent, "w") as f:
                f.write(newText)
            with open(FileName_agent) as f:
                newText = f.read().replace('Hostname=Zabbix server', 'Hostname=' + self.hostname)
            with open(FileName_agent, "w") as f:
                f.write(newText)

            with open(FileName_agent) as f:
                newText = f.read().replace('LogFileSize=0', 'LogFileSize=1')
            with open(FileName_agent, "w") as f:
                f.write(newText)

            with open(FileName_agent) as f:
                newText = f.read().replace('# LogRemoteCommands=0', 'LogRemoteCommands=1')
            with open(FileName_agent, "w") as f:
                f.write(newText)

            with open(FileName_agent) as f:
                newText = f.read().replace('# HostMetadataItem=', 'HostMetadataItem=system.uname')
            with open(FileName_agent, "w") as f:
                f.write(newText)

            subprocess.getstatusoutput("service zabbix-agent restart")
            # agent part over

            #DB Server Host name updating 
             
            FileName='/etc/zabbix/zabbix_server.conf'
            
            with open(FileName) as f:
                newText=f.read().replace('# SourceIP=', 'SourceIP=10.1.150.234')

            with open(FileName) as f:
                newText=f.read().replace('# DBPassword=', 'DBPassword='+self.db_pwd)
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText=f.read().replace('# DBHost=localhost', 'DBHost='+self.db_ip)
            with open(FileName, "w") as f:
                f.write(newText)
            with open(FileName) as f:
                newText=f.read().replace('LogFileSize=0', 'LogFileSize=1')
            with open(FileName, "w") as f:
                f.write(newText)


            zabbix_configuration_file = '/etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf'

            with open(zabbix_configuration_file) as file:

                newText=file.read().replace('; php_value[date.timezone] = Europe/Riga', 'php_value[date.timezone] = '+self.timezone)

            with open(zabbix_configuration_file, "w") as file:
                file.write(newText)

            status,output = subprocess.getstatusoutput("firewall-cmd --reload")

            self.logger.info('restarting zabbix-server')
            self.api_payload["StatusReason"] = "DB Server Host name should be added in etc/zabbix/zabbix_server.conf  & restarting zabbix-server"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])

            cmd3="systemctl restart zabbix-server  httpd rh-php72-php-fpm"
            os.system(cmd3)

            cmd4="systemctl enable zabbix-server  httpd rh-php72-php-fpm"
            os.system(cmd4)
            self.logger.info('disabling firewall')
            self.api_payload["StatusReason"] = "restarting zabbix-server"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])

            copyfile(self.Conf_File,self.Conf_File1)

            with open(self.Conf_File1) as f:
                db = f.read().replace('<dbserver>', self.db_ip)
            with open(self.Conf_File1, "w") as f:
                f.write(db)
            with open(self.Conf_File1) as f:
                db_pwd = f.read().replace('<ZABBIX_DB_PWD>', self.db_pwd)
            with open(self.Conf_File1, "w") as f:
                f.write(db_pwd)
            # os.rename(self.root+"/Input/conf1.php","/etc/zabbix/web/zabbix.conf.php")
            subprocess.getoutput('mv '+self.Conf_File1+' /etc/zabbix/web/zabbix.conf.php')
            os.system(cmd3)
            os.system(cmd4)

            if os.path.isfile('/etc/zabbix/web/zabbix.conf.php'):
                self.api_payload["StatusReason"] = "Core Configuration Completed"
                self.api_payload["Status"] = 2
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Pass")
                print("3rr0rC0d3[200]")
            else:
                self.api_payload["StatusReason"] = "Core Configuration Failed"
                self.api_payload["Status"] = 3
                self.send_status.send_status([self.api_payload])
                self.send_status.send_logs([self.api_payload])
                self.output.writelines("Fail")
                print("3rr0rC0d3[500]")




        except Exception as e:
            self.logger.info("Exception caught:" + str(e))

if __name__ == "__main__":
    conf = Zabbix_Config_Core()
    conf.Config()


