
import os
import sys
import time
import logging
import threading
import commands
import json
import shutil
import io
import re

class ToolDeployer():


    def __init__(self):

        self.tool_name = 'zabbix'
        self.version = '5.0'
        self.Admin_Root = os.environ["Admin_Root"]
        self.log_file = self.Admin_Root+"/iDeploy/tools/{tool}/logs/{tool_name}_log.txt".format(
                        tool = self.tool_name+"_"+self.version, tool_name = self.tool_name)

        logging.basicConfig(filename=self.log_file, format='%(asctime)s %(message)s',
                            filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.dt = time.strftime("%Y:%m:%d-%H:%M:%S")
        self.logger.info("deployement Started on "+self.dt)
        self.ini_file = self.Admin_Root+"/iDeploy/tools/{tool}/Ansible-Playbooks/ansible_host.ini".format(tool = self.tool_name+"_"+self.version)
        self.extra_vars = ' --extra-vars "@{root}/iDeploy/working/{tool}/zabbix_extra_vars.yml"'.format(
                    root=self.Admin_Root,tool=self.tool_name)
        self.error_identifier_dict = {"3rr0rC0d3[500]":[], "3rr0rC0d3[001]":[], "3rr0rC0d3[200]":[], "NA" : []}
    def load_inventory(self):

        self.logger.info("Load inventory in JSON format "+self.dt)
        inventory = open(self.Admin_Root+'/iDeploy/working/'+self.tool_name+'/inventory.json','r')
        self.inventory = json.loads(inventory.read())
        self.logger.info("Successfully Loaded inventory in JSON format "+self.dt)

    def update_global_vars(self):

        global_json_ideploy =  open(self.Admin_Root+"/iDeploy/common/globalVariables.json","r").read()
        global_json_ideploy = json.loads(global_json_ideploy)

        inventory = open(self.Admin_Root+'/iDeploy/working/'+self.tool_name+'/inventory.json','r')
        inventory = json.loads(inventory.read())

        global_file_tool = open(self.Admin_Root  + "/iDeploy/tools/zabbix_5.0/zabbix/Input/global_template.json","r").read()
        global_file_tool = global_file_tool.replace("<<api_url>>",global_json_ideploy['url'])
        global_file_tool = global_file_tool.replace("<<api_usr>>",global_json_ideploy['api_username'])
        global_file_tool = global_file_tool.replace("<<api_pwd>>",global_json_ideploy['api_password'])
        global_file_tool = global_file_tool.replace("<<environment>>",inventory["Environment"])

        f = io.open(self.Admin_Root + "/iDeploy/tools/zabbix_5.0/zabbix/Input/global.json","w+",encoding='utf8')
        f.write(global_file_tool)
        f.close()



    def ansible_writer(self):

        self.logger.info("Ansible writer started")
        inventory_dict = {}
        for component in self.inventory["components"].keys():
            if "primary" in self.inventory["components"][component]["servers"].keys():
                inventory_dict["Primary_" + component + "_" + self.tool_name.title()] = \
                self.inventory["components"][component]["servers"]["primary"]
            if "secondary" in self.inventory["components"][component]["servers"].keys():
                inventory_dict["Secondary_" + component + "_" + self.tool_name.title()] = \
                self.inventory["components"][component]["servers"]["secondary"]
        inventory_string = ""
        for i in inventory_dict.keys():
            inventory_string += '\n[' + str(i) + ']\n'
            for j in inventory_dict[i]:
                inventory_string += str(j) + "\n"
        f = open(self.ini_file, "w")
        f.write(inventory_string)


    def credentials(self):

        self.logger.info("Load Credentials as extra vars "+self.dt)
        original_path =  "{root}/iDeploy/working/{tool}/zabbix_extra_vars.yml".format(root=self.Admin_Root,tool=self.tool_name)
        target_path = self.Admin_Root+"/iDeploy/tools/zabbix_5.0/zabbix/Input/zabbix_extra_vars.yml"
        shutil.copyfile(original_path, target_path)
        self.extra_vars = ' --extra-vars "@{root}/iDeploy/tools/zabbix_5.0/zabbix/Input/zabbix_extra_vars.yml"'.format(
                    root=self.Admin_Root,tool=self.tool_name)
        # print(self.extra_vars)
        self.logger.info("Loaded Credentials as extra vars "+self.dt)

    def code_finder(self,output):

        self.logger.info("Finding code in output started")
        output =  re.findall(r'"3rr0rC0d3.*"', str(output))
        output = " ".join(output).replace('"','')

        if output.find("3rr0rC0d3[001]") != -1:
            return ["1","Fail: Python Error","3rr0rC0d3[001]"]
        elif output.find("3rr0rC0d3[500]") != -1:
            return ["1","Fail: Problem Found","3rr0rC0d3[500]"]
        elif output.find("3rr0rC0d3[200]") != -1:
            return ["0","Pass: No issues","3rr0rC0d3[200]"] 
        else:
            return ["1","Fail: No know error code found"+output,"NA"]
        

    def call_ansible_role(self, role_name, server, ):

        rolepath = "{root}/iDeploy/tools/{tool_ver}/Ansible-Playbooks/roles/{role}".format(root=self.Admin_Root,
                        tool_ver=self.tool_name+"_"+self.version, role=role_name)
        command  = 'ansible -i {} {} --e interaction_id=78uj -m include_role -a name={} {}'.format(self.ini_file,
                                                                                server, rolepath, self.extra_vars)
        print("Role Command :",command)
    
        self.logger.info(command)
        status,output = commands.getstatusoutput(command)
        result = self.code_finder(str(output))
        self.error_identifier_dict[result[2]].append([role_name,server,result[1]]) 


    def call_ansible_playbook(self, playbook_name):

        playbook_path = "{root}/iDeploy/tools/{tool_ver}/Ansible-Playbooks/{playbook}".format(root=self.Admin_Root,
                        tool_ver=self.tool_name+"_"+self.version, playbook=playbook_name)
        # print("playbook_path",playbook_path)
        command = "ansible-playbook -i {} --e interaction_id=78uj {} {}".format(self.ini_file, playbook_path, self.extra_vars)
        print(command)
        status,output = commands.getstatusoutput(command)
        self.logger.info(command)
        #self.logger.info("Ansible Playbook Called Successfully "+self.dt)

    def rollback(self):
        self.logger.info('Rollback Initiated')
        rollback_script_dict = [

            ["Primary_Core_Zabbix" , "zabbix_core_rollback"],
            ["Secondary_Core_Zabbix" , "zabbix_core_rollback"],
            ["Primary_DB_Zabbix" , "zabbix_db_rollback"],
            ["Secondary_DB_Zabbix" ,"zabbix_db_rollback"],
            ["Primary_DB_Proxy_Zabbix" , "zabbix_db_proxy_rollback"],
            ["Secondary_DB_Proxy_Zabbix" , "zabbix_db_proxy_rollback"],
            ["Primary_Proxy_Zabbix" , "zabbix_proxy_rollback"],
            ["Secondary_Proxy_Zabbix" , "zabbix_proxy_rollback"]
        ]
        threads = []

        for i in rollback_script_dict:
            self.call_ansible_role( i[1],i[0])
            

    def alert_and_copy(self):
        self.call_ansible_role("zabbix_alerts_primary","localhost")
        self.call_ansible_role("zabbix_alerts_secondary","localhost")
        # Copying scripts
        self.call_ansible_playbook("zabbix_script_copy_ha.yml")    

    def precheck(self):

        precheck_script_dict = {
            "zabbix_db_pre_primary" : "Primary_DB_Zabbix",
            "zabbix_db_pre_secondary" : "Secondary_DB_Zabbix",
            "zabbix_core_precheck_primary" : "Primary_Core_Zabbix",
            "zabbix_core_precheck_secondary" : "Secondary_Core_Zabbix",
            "zabbix_proxy_precheck_primary" : "Primary_Proxy_Zabbix",
            "zabbix_proxy_precheck_secondary" : "Secondary_Proxy_Zabbix",
            "zabbix_db_proxy_precheck_primary" : "Primary_DB_Proxy_Zabbix",
            "zabbix_db_proxy_precheck_secondary" : "Secondary_DB_Proxy_Zabbix",
        }
        self.logger.info('Test zabbix ha Preecheck function called')
        threads = []

        for i in precheck_script_dict:
            t =  threading.Thread(target = self.call_ansible_role, args = (i, precheck_script_dict[i],))
            threads.append(t)
            t.start()

        for index, thread in enumerate(threads):
            thread.join()

        if len(self.error_identifier_dict["3rr0rC0d3[500]"]) > 0:
            self.logger.info("Exiting due to failed precheck")
            sys.exit()

        #self.logger.info('zabbix sa Preecheck function called')

    def installation(self):
        db_install_dict = {
            "zabbix_db_install_primary" : "Primary_DB_Zabbix",
            "zabbix_db_install_secondary" : "Secondary_DB_Zabbix",
            "zabbix_core_install_sa": "Primary_Core_Zabbix",
            "zabbix_core_install_secondary":"Secondary_Core_Zabbix",
            "zabbix_proxy_sa": "Primary_Proxy_Zabbix",
            "zabbix_proxy_secondary": "Secondary_Proxy_Zabbix"
        }

        threads = []

        for i in db_install_dict:
            t =  threading.Thread(target = self.call_ansible_role, args = (i, db_install_dict[i],))
            threads.append(t)
            t.start()

        for index, thread in enumerate(threads):
            thread.join()

        self.call_ansible_role("zabbix_db_proxy_install_primary", "Primary_DB_Proxy_Zabbix")
        self.call_ansible_role("zabbix_db_proxy_install_secondary","Secondary_DB_Proxy_Zabbix")

        if len(self.error_identifier_dict["3rr0rC0d3[500]"]) > 0:
            self.rollback()
            sys.exit()


    def configuration(self):
        config_dict =[ {
                        "role" : "zabbix_db_config_primary",
                        "host" : "Primary_DB_Zabbix"
                    },
                    {
                        "role" : "zabbix_db_config_secondary",
                        "host" : "Secondary_DB_Zabbix"
                    },
                    {   
                        "role" : "zabbix_mysql_DB_Master_Config",
                        "host" : "Primary_DB_Zabbix"
                    },
                    {   
                        "role" : "zabbix_mysql_DB_Slave_Config",
                        "host" : "Secondary_DB_Zabbix"
                    },
                    #--------------------------------------------------------
                    # {   
                    #     "role" : "zabbix_db_ha_config_primary",
                    #     "host" : "Primary_DB_Zabbix"
                    # },
                    # {   
                    #     "role" : "zabbix_db_ha_config_secondary",
                    #     "host" : "Secondary_DB_Zabbix"
                    # },
                    #---------------------------------------------------
                    {
                        "role": "zabbix_db_proxy_config_primary",
                        "host": "Primary_DB_Proxy_Zabbix"
                    },
                    {
                        "role": "zabbix_db_proxy_config_secondary",
                        "host": "Secondary_DB_Proxy_Zabbix"
                    },
                    {
                        "role": "zabbix_core_config_sa",
                        "host": "Primary_Core_Zabbix"
                    },
                    {
                        "role": "zabbix_core_config_secondary",
                        "host": "Secondary_Core_Zabbix"
                    },
                    {
                        "role": "zabbix_core_config_secondary",
                        "host": "Primary_Core_Zabbix"
                    },
                    {
                        "role": "zabbix_core_config_sa",
                        "host": "Secondary_Core_Zabbix"
                    },

                    {
                        "role": "zabbix_proxy_config_sa",
                        "host": "Primary_Proxy_Zabbix"
                    },
                    {
                        "role": "zabbix_proxy_config_secondary",
                        "host": "Secondary_Proxy_Zabbix"
                    },
                    {
                        "role": "zabbix_ssl_configuration",
                        "host": "Primary_Core_Zabbix"
                    },
                    {
                        "role": "zabbix_ssl_configuration_secondary",
                        "host": "Secondary_Core_Zabbix"
                    }
                    ]

        for configuration in config_dict:
            role = configuration['role']
            host = configuration['host']
            self.call_ansible_role(role, host)

        if len(self.error_identifier_dict["3rr0rC0d3[500]"]) > 0:
            #self.rollback()
            sys.exit()

    def ha_configuration(self):
        """
        This function is going to calll ansible role to configure Zabbix DB HA
        Master-Master configuration 
        Retunring earlt since this is not in use for now
        """

        configuration_ha_list = [
            {
                "role" : "zabbix_copyone",
                "hostname" : "Primary_Core_Zabbix"
            },
            {
                "role" : "zabbix_copysecond",
                "hostname" : "Secondary_Core_Zabbix"
            },
            {
                "role" : "zabbix_cluster",
                "hostname" : "Primary_Core_Zabbix"
            },
            {
                "role" : "zabbix_cluster",
                "hostname" : "Secondary_Core_Zabbix"
            },
            {
                "role" : "zabbix_first",
                "hostname" : "Primary_Core_Zabbix"
            }]

        for configuration in configuration_ha_list:
            role_name = configuration['role']
            host_name = configuration['hostname']
            self.call_ansible_role(role_name, host_name)



    def extra_configuration(self):
        config_dict = [
            
            {
                "role": "zabbix_onboarding",
                "host": "Primary_Core_Zabbix"
            },
            {
                "role": "zabbix_create_group_sa",
                "host": "Primary_Core_Zabbix"
            },
            {
                "role": "zabbix_create_group_secondary",
                "host": "Secondary_Core_Zabbix"
            },
            {
                "role": "zabbix_create_user_sa",
                "host": "Primary_Core_Zabbix"
            },
            {
                "role": "zabbix_create_user_secondary",
                "host": "Secondary_Core_Zabbix"
            },
            {
                "role": "zabbix_smtp_sa",
                "host": "Primary_Core_Zabbix"
            },

            {
                "role": "zabbix_smtp_secondary",
                "host": "Secondary_Core_Zabbix"
            },
            
            {
                "role": "zabbix_change_admin",
                "host": "Primary_DB_Zabbix"
            },
            {
                "role": "zabbix_change_admin_secondary",
                "host": "Secondary_DB_Zabbix"
            },
            {
                "role": "zabbix_heartbeat",
                "host": "Primary_Proxy_Zabbix"
            },
            {
                "role": "zabbix_heartbeat_secondary",
                "host": "Secondary_Core_Zabbix"
            },
            ###   Zabbix Ha Proxy Roles
            {
<<<<<<< HEAD
                "role": "zabbix_import_template_primary",
                "host": "Primary_Core_Zabbix"
            },
	        {
                "role": "zabbix_import_template_secondary",
                "host": "Secondary_Core_Zabbix"
            },
	        {
                "role": "zabbix_update_host_primary",
                "host": "Primary_Core_Zabbix"
            },
	        {
                "role": "zabbix_update_host_secondary",
                "host": "Secondary_Core_Zabbix"
=======
                "role": "zabbix_ha_proxy_primary",
                "host": "Primary_Core_Zabbix"
>>>>>>> 2d4642ad750d67525202852910eca39ce3ec8f75
            },
            ###   Zabbix Ha Proxy Roles
            {
<<<<<<< HEAD
                "role": "zabbix_ha_proxy_primary",
=======
                "role": "zabbix_trigger_action,",
>>>>>>> 2d4642ad750d67525202852910eca39ce3ec8f75
                "host": "Primary_Core_Zabbix"
            },
            {
                "role": "zabbix_ha_proxy_secondary",
                "host": "Secondary_Core_Zabbix"
            }
<<<<<<< HEAD
            {
                "role": "zabbix_trigger_action_primary,",
                "host": "Primary_Core_Zabbix"
            },
            {
                "role": "zabbix_trigger_action_secondary,",
                "host": "Secondary_Core_Zabbix"
            }
            
=======
>>>>>>> 2d4642ad750d67525202852910eca39ce3ec8f75


        ]

        for configuration in config_dict:
            role = configuration['role']
            host = configuration['host']
            self.call_ansible_role(role, host)


    def post_check(self):
        post_dict = {
            "zabbix_db_postcheck" : "Primary_DB_Zabbix",
            "zabbix_db_postcheck_secondary" : "Secondary_DB_Zabbix",
            "zabbix_db_proxy_postcheck" : "Primary_DB_Proxy_Zabbix",
            "zabbix_db_proxy_postcheck_secondary" : "Secondary_DB_Proxy_Zabbix",
            "zabbix_proxy_postcheck" : "Primary_Proxy_Zabbix",
            "zabbix_proxy_postcheck_secondary" : "Secondary_Proxy_Zabbix"

        }

        threads = []

        for i in post_dict:
            t =  threading.Thread(target = self.call_ansible_role, args = (i, post_dict[i],))
            threads.append(t)
            t.start()

        for index, thread in enumerate(threads):
            thread.join()
        # moved below checks ,due to bi-dir port connection at same time via multithread
        post_dict_seq = [

                        {
                            "role": "zabbix_core_postcheck",
                            "host": "Primary_Core_Zabbix"
                        },
                        {
                             "role": "zabbix_core_postcheck_secondary",
                             "host": "Secondary_Core_Zabbix"
                        }
                        ]
        for post in post_dict_seq:
            role = post['role']
            host = post['host']
            self.call_ansible_role(role, host)

    def zabbix_agent(self):

        zbx_agent = {
            "zabbix_agent": ["Primary_DB_Zabbix","Primary_DB_Proxy_Zabbix","Primary_Proxy_Zabbix"],
            "zabbix_agent_secondary": ["Secondary_DB_Zabbix","Secondary_DB_Proxy_Zabbix","Secondary_Proxy_Zabbix"]
        }

        threads = []
        for x in zbx_agent:
            for element in zbx_agent[x]:
                # print element
                th = threading.Thread(target=self.call_ansible_role, args=(x, element,))
                threads.append(th)
                th.start()

        for index1, thread in enumerate(threads):
            # print self_threads
            thread.join()



if __name__ == '__main__':

    zabbix = ToolDeployer()
    zabbix.load_inventory()
    zabbix.update_global_vars()
    zabbix.ansible_writer()
    zabbix.credentials()
<<<<<<< HEAD
    zabbix.rollback()
    #zabbix.alert_and_copy()
    #zabbix.precheck()
    #zabbix.installation()
    #zabbix.configuration()
    #zabbix.ha_configuration()
    #zabbix.extra_configuration()
    #zabbix.zabbix_agent()
    #zabbix.post_check()
    
=======
    #zabbix.rollback()
    # zabbix.alert_and_copy()
    # zabbix.precheck()
    zabbix.installation()
    zabbix.configuration()
    zabbix.ha_configuration()
    zabbix.extra_configuration()
    zabbix.zabbix_agent()
    zabbix.post_check()
    
>>>>>>> 2d4642ad750d67525202852910eca39ce3ec8f75
