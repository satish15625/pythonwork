# coding=utf-8
import requests,json,os,sys

class sendstatus():

	def __init__(self,path = (os.environ["Admin_Root"]+"/zabbix/Input/global.json")):
		self.Admin_Root = os.environ["Admin_Root"]
		self.env_variables_file = ""
		# self.runtimeVariable = self.Admin_Root+"/iDeploy/working/runtimeVariables.json"
		with open(path) as f:
			self.env_variables_file = json.load(f)
		self.api_user = self.env_variables_file["connection_details"]['api_username']
		self.api_paasword = self.env_variables_file["connection_details"]['api_password']
		self.auth_url = "http://{url}/api/ansible/authenticate".format(url=self.env_variables_file["connection_details"]['url'])
		self.status_url = "http://{url}/api/ansible/UpdateDeploymentStatus".format(url=self.env_variables_file["connection_details"]['url'])
		self.logs_url = "http://{url}/api/ansible/DeploymentStatusLog".format(url=self.env_variables_file["connection_details"]['url'])
		r = requests.post(self.auth_url,
			data = json.dumps({"Username":self.api_user,"Password":self.api_paasword}),
			headers={"Content-Type": "application/json"})
		self.data=json.loads(r.content)
		

	def authenticate(self):

		r = requests.post(self.auth_url,
			data = json.dumps({"Username":self.api_user,"Password":self.api_paasword}),
			headers={"Content-Type": "application/json"})
		self.data=json.loads(r.content)
		# with open(self.runtimeVariable,'w') as file:
		# 	token = json.dump(data,file)
 
	def send_status(self,dict_data):
		
		r=requests.post(self.status_url, data=json.dumps(dict_data),headers={"Content-Type": "application/json","Authorization":"Bearer " +self.data["token"]})

	def send_logs(self,dict_data):
		
		r=requests.post(self.logs_url, data=json.dumps(dict_data),headers={"Content-Type": "application/json","Authorization":"Bearer " +self.data["token"]})

