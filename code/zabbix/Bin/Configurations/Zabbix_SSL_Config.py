

# Reference https://ma.ttias.be/how-to-create-a-self-signed-ssl-certificate-with-openssl/
# https://www.zabbix.com/documentation/4.2/manual/installation/requirements/best_practices

import subprocess
import fileinput
import logging

import logging, time, subprocess, os, sys, json
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Lib/uistatus')
from uistatus import sendstatus



class ZabbixSSLConfiguration():
    """docstring for ZabbixSSLConfiguration"""
    def __init__(self):
        """[summary]

        [description]
        """

        self.flag = 0
        self.server_type = sys.argv[1]
        self.root = os.environ['Admin_Root']
        global_json = open(self.root + '/zabbix/Input/global.json', 'r')
        self.load_variable = json.load(global_json)
        dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.hostname = subprocess.getoutput("hostname -s")
        self.environment = self.load_variable["Environment"]
        self.component = "Core"
        self.send_status = sendstatus()
        self.api_payload = {"ToolName": "Zabbix", "Component": self.component, "ServerFQDN": self.hostname,
                        "ServerType": self.server_type, "Environment": self.environment, "Stage": "3",
                        "Status": "1", "StatusReason": "SSL Configuration Initiated"
                        }
        self.send_status.send_logs([self.api_payload])
        self.log_file = self.root + "/zabbix/Logs/zabbix_ssl_config_" + dt + ".log"
        logging.basicConfig(filename=self.log_file,
                            format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("SSL Configuration Started.. " + dt)

        self.apache_ssl_conf = '/etc/httpd/conf.d/ssl.conf'
        self.cert_dir1 = '/etc/httpd/ssl/'
        self.cert_dir = '/etc/httpd/ssl/private'
        self.certificate_path = '/etc/httpd/ssl/apache-selfsigned.crt'
        self.certificate_key_path = '/etc/httpd/ssl/private/apache-selfsigned.key'



    def install_yum(self):
        """[summary]

        [description]
        """
        self.logger.info('Installing mod_ssl openssl packages')
        cmd = 'yum -y install mod_ssl openssl >>'+self.log_file
        status, out = subprocess.getstatusoutput(cmd)
        if status == 0:
            self.logger.info('Installed mod_ssl openssl packages')
        else:
            self.logger.info('Installing mod_ssl openssl failed')
            self.flag = 1


    def create_directory(self):
        """[summary]

        [description]
        """
        if not os.path.exists(self.cert_dir):
            self.logger.info('Creating httpd directory')
            subprocess.getoutput('mkdir '+ self.cert_dir1)
            subprocess.getoutput('mkdir '+self.cert_dir)
            


        os.system('sudo chmod 700 /etc/httpd/ssl/private')

    def generate_certificate(self):
        """[summary]

        [description]
        """
        self.logger.info('Creating self signed Key')
        cmd = "openssl req -x509 -nodes -days 1024 -sha256 -newkey rsa:2048 " \
        "-keyout /etc/httpd/ssl/private/apache-selfsigned.key "\
        "-out /etc/httpd/ssl/apache-selfsigned.crt   -subj '/CN={}'".format(self.hostname)
        os.system(cmd)

    def restart_httpd(self):
        """[summary]

        [description]
        """
        self.logger.info('Restarting HTTPd')
        cmd = 'systemctl restart httpd'
        status, out = subprocess.getstatusoutput(cmd)
        if status == 0:
            self.logger.info('Restart of httpd success')
        else:
            self.logger.info('Restart of httpd fail')
            self.flag = 1



    def change_configuration(self):
        """[summary]

        [description]
        """

        self.logger.info('Changing configuration files')

        with open(self.apache_ssl_conf) as f:
            updated_content = f.read().replace('#DocumentRoot "/var/www/html"',
                                     'DocumentRoot "/usr/share/zabbix"')
        if updated_content:
            with open(self.apache_ssl_conf, "w") as f:
                f.write(updated_content)

        with open(self.apache_ssl_conf) as f:
            updated_content = f.read().replace('#ServerName www.example.com:443',
                                            'ServerName '+ self.hostname + ':443')

        if updated_content:
            with open(self.apache_ssl_conf, "w") as f:
                f.write(updated_content)


        with open(self.apache_ssl_conf) as f:
            updated_content = f.read().replace('SSLCertificateFile /etc/pki/tls/certs/localhost.crt',
                                    'SSLCertificateFile '+ self.certificate_path)

        if updated_content:
            with open(self.apache_ssl_conf, "w") as f:
                f.write(updated_content)

        with open(self.apache_ssl_conf) as f:
            updated_content = f.read().replace('SSLCertificateKeyFile /etc/pki/tls/private/localhost.key',
                                    'SSLCertificateKeyFile '+ self.certificate_key_path)

        if updated_content:
            with open(self.apache_ssl_conf, "w") as f:
                f.write(updated_content)

    def final_check(self):
        if self.flag == 0:
            self.logger.info("SSL Configuration Success")
            self.api_payload["StatusReason"] = "SSL Configuration Success"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[200]")
        else:
            self.logger.info("SSL Configuration Fail")
            self.api_payload["StatusReason"] = "SSL Configuration Fail"
            self.api_payload["Status"] = 2
            self.send_status.send_logs([self.api_payload])
            print("3rr0rC0d3[500]")


if __name__ == '__main__':
    zabbix = ZabbixSSLConfiguration()
    zabbix.install_yum()
    zabbix.create_directory()
    zabbix.generate_certificate()
    zabbix.change_configuration()
    zabbix.restart_httpd()
    zabbix.final_check()

