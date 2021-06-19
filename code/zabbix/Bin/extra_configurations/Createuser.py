#File Name:- Zabbix_agentinstall_Linux.py
#Service Name:- 
#Purpose: To install agent on linux and add it to hosts
#Author Name: 
#Create Date: 03/May/2019
#Modifed By:- 
#Last Modify Date: 
#Current Version: 1.1
#Summary of Last Change: N/A
#Arguments: Global.txt file present in Input folder is a mandate
import sys
import logging
import os,datetime,commands,json
status,out=commands.getstatusoutput('pip install pyzabbix')
import subprocess
from pyzabbix import ZabbixAPI, ZabbixAPIException
status,Host=commands.getstatusoutput('hostname -s')
Host=Host.strip()
status,HostIP=commands.getstatusoutput('hostname -I')
HostIP=HostIP.strip()

vip = sys.argv[1]
zapi = ZabbixAPI("http://{}/zabbix".format(vip))

zapi.login("Admin","zabbix")
tlookup=[]

grouplookup = zapi.hostgroup.get(filter=({'name':"Linux servers"}))
# elem=grouplookup.pop()
usergroups=["Command Center Team","Platform Team","Unix","Windows","Backup","Storage","Network","Database","ITSM"]
usrtogrp={}
for grp in usergroups:
	d=zapi.usergroup.create({"name":grp,"rights":{"permission":3,"id":grouplookup[0]["groupid"]}})
	usrtogrp[grp]=d["usrgrpids"][0]
print(usrtogrp)

users=["akhil-k","priyanka.ja","satyam.s","monika_n","gauravbha","prateek_srivastava"]

for usr in users:
	print(zapi.user.create({"alias":usr,"passwd":"Zabbix@123","type":"3","usrgrps":[{"usrgrpid":7}]}))
