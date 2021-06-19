import os, sys, subprocess, json
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus

class Zabbix_DB_Rollback():
    """This class handles the Zabbix DB Rollback
    """    

    def remove_mysql(self):
        send_status = sendstatus()
        hostname = subprocess.getoutput("hostname -s")
        # server_type = sys.argv[1]
        component = "DB"
        global_json = open(os.environ['Admin_Root'] + '/zabbix/Input/global.json', 'r')
        load_variable = json.load(global_json)
        environment = load_variable["Environment"]
        api_payload = {"ToolName": "Zabbix", "Component": component, "ServerFQDN": hostname,
                            "ServerType": "-", "Environment": environment, "Stage": "2",
                            "Status": "1", "StatusReason": "DB roll back triggered"
                            }
        send_status.send_logs([api_payload])
        try:
            os.system("service mysqld stop")
            os.system("service zabbix-agent stop")
            os.system("yum -y  remove mysql-community-server")
            os.system("yum -y  remove mysql-community-common-8.0.20-1.el7.x86_64")
            os.system("yum -y  remove mysql80-community-release-el7-1.noarch")
            os.system("rm -rf /var/lib/mysql")
            os.system('rm -rf /var/run/mysqld')
            os.system("rm -rf /etc/mysql")
            os.system("rm -rf /var/db/mysql")
            os.system("rm -rf /var/log/mysqld.log")
            os.system('rm -rf /etc/zabbix')
            os.system("rm -f mysql80-community-release-el7-1.noarch.rpm")
            os.system("yum -y remove zabbix-agent")
            api_payload["StatusReason"] = "Rollback Completed for DB"
            send_status.send_logs([api_payload])
            os.system('rm -rf /usr/share/mtaas/zabbix')
            os.system('reboot')
            print("true")

        except OSError as error:
            # print(error)
            print("false")
 

if __name__ == "__main__":

    zabbix_db = Zabbix_DB_Rollback()
    zabbix_db.remove_mysql()


