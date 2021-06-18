import os, sys, subprocess, json
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Zabbix_Core_Rollback():
    """This class handles the Zabbix Core Rollback
    """

    def remove_zabbix_core(self):
        send_status = sendstatus()
        hostname = subprocess.getoutput("hostname -s")
        # server_type = sys.argv[1]
        component = "Core"
        global_json = open(os.environ['Admin_Root'] + '/zabbix/Input/global.json', 'r')
        load_variable = json.load(global_json)
        environment = load_variable["Environment"]
        api_payload = {"ToolName": "Zabbix", "Component": component, "ServerFQDN": hostname,
                            "ServerType": "-", "Environment": environment, "Stage": "2",
                            "Status": "1", "StatusReason": "Core roll back triggered"
                            }
        send_status.send_logs([api_payload])
        try:
            #os.system('systemctl stop zabbix-server')
            # os.system('systemctl stop zabbix-agent')
            os.system('yum -y remove zabbix*')
            os.system("yum -y remove zabbix-server-mysql zabbix-web-mysql zabbix-web zabbix-agent")
            os.system("yum -y remove zabbix-web-mysql-scl zabbix-apache-conf-scl")
            os.system("yum -y remove zabbix-release-5.0-1.el7.noarch")
            os.system('rm -rf /etc/zabbix')
            os.system('rm -rf /var/run/zabbix')
            os.system('rm -rf /var/log/zabbix')
            os.system('rm -rf /var/lib/zabbix')
            os.system('rm -rf /var/lib/mysql')
            os.system('rm -rf /etc/mysql')
            os.system('rm -rf /var/db/mysql')
            os.system('yum -y remove rh-php72*')
            os.system('pcs cluster destroy')
            os.system('yum -y remove pcs')
            os.system('yum -y remove corosync')
            os.system('yum -y remove openssl')
            os.system('yum -y remove mod_ssl')
            os.system("yum -y remove zabbix-agent")
            api_payload["StatusReason"] = "Rollback Completed for Core"
            send_status.send_logs([api_payload])
            os.system('rm -rf /usr/share/mtaas/zabbix')
            os.system('reboot')
            print("true")


        except OSError as error:
            # print(error)
            print("false")
 

if __name__ == "__main__":

    zabbix_db = Zabbix_Core_Rollback()
    zabbix_db.remove_zabbix_core()




