#!/usr/bin/python

import os
import sys
import json
import logging
import datetime
# import commands
import subprocess

try:
    from pyzabbix import ZabbixAPI, ZabbixAPIException
except:
    status,out=os.system('pip install pyzabbix')

#lib for https validation 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ZabbixTemplate():
    """docstring for ClassName"""
    def __init__(self, zabbix_server):
        """Constructor function
        
        
        Arguments:
            zabbix_server {string} -- hostname/url of zabbix server
        """

        self.zapi = ZabbixAPI("https://{}/zabbix".format(zabbix_server))
        self.zapi.session.verify = False


    def login(self, username, password):
        """Logiin to zabbix api using pyzabbix
        
        [description]
        """
        self.zapi.login(username, password)

        return self

 

    def add_rules(self):
        """
        : set rules for template creation
        
        [description]
        """
        self.rules = {
            'applications': {
                'createMissing': True,
            },
            'discoveryRules': {
                'createMissing': True,
                'updateExisting': True
            },
            'graphs': {
                'createMissing': True,
                'updateExisting': True
            },
            'groups': {
                'createMissing': True
            },
            'hosts': {
                'createMissing': True,
                'updateExisting': True
            },
            'images': {
                'createMissing': True,
                'updateExisting': True
            },
            'items': {
                'createMissing': True,
                'updateExisting': True
            },
            'maps': {
                'createMissing': True,
                'updateExisting': True
            },
            'screens': {
                'createMissing': True,
                'updateExisting': True
            },
            'templateLinkage': {
                'createMissing': True,
            },
            'templates': {
                'createMissing': True,
                'updateExisting': True
            },
            'templateScreens': {
                'createMissing': True,
                'updateExisting': True
            },
            'triggers': {
                'createMissing': True,
                'updateExisting': True
            },
            'valueMaps': {
                'createMissing': True,
                'updateExisting': True
            },
        }

        return self

 

    def read_template(self, filepath):
        """: Read template xml file and store in a class variable
        
        [description]
        """
        with open(filepath, 'r') as f:
            self.template = f.read()


    def create(self):
        """: Call pyzabbix to create template on the server
        
        [description]
        """
        try:
            print(self.zapi.confimport('xml', self.template, self.rules))
        except ZabbixAPIException as e:
            print(e)

#main function  
if __name__ == '__main__':
    """Main function
    script execution start from here
    :: 
    
    [description]
    """

    command_arg = sys.argv

    # zabbix_server = 'ptest0100'
    template_path = 'zbx_export_templates.xml'
    # zabbix_server = command_arg[1]
    # template_path = command_arg[2]
    
    #getting data template data from json file.
    with open('templatedata.json') as data_file:
        data = json.load(data_file)

    zabbix_server = data['ip']
    username = data['username']
    password = data['passwd']
    #template_path = ['templatepath']
    
  
    zabbix = ZabbixTemplate(zabbix_server)
    zabbix.login(username, password).add_rules()

    zabbix.read_template(template_path)
    zabbix.create()
 
