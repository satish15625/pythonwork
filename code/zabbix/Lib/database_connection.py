#********************************************************************************
#*File Name:- database_connection.py
#*Service Name:- Functions to connect to database,Fetch Data and Update Data
#*Purpose:Functions to connect to database,Fetch Data and Update Data
#*Author Name: Priyanka Jain
#*Create Date:
#*Modify By:- Sankar
#*Last Modify Date: 26-Sep
#*Current Version:1.0
#*Summary of Last Change: Added return for validation
#********************************************************************************

import sys
import os
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Input')
sys.path.insert(0, os.environ['Admin_Root'] + '/zabbix/Variables')

import logging
import mysql.connector
from mysql.connector import errorcode


def Fun_Fetch_Data(mySQLconnection,query):		#Function to Fetch Data from database
	sql_select_Query = query												
	cursor = mySQLconnection.cursor()
	cursor.execute(sql_select_Query)
	records = cursor.fetchall()
	return (records)

	
def Fun_Update_Data(user,password,database,host,query,logfile):		#Function to Update Data in database
	mySQLconnection=Fun_Database_Connection(user,password,database,host,logfile)
	sql_update_Query = query
	# print(sql_update_Query)
	cursor = mySQLconnection.cursor()
	cursor.execute(sql_update_Query)
	mySQLconnection.commit()
	
def Fun_Database_Connection(user,password,database,host,logfile):
	logging.info('Creating Database connection')			#Function to create connection with database
	# user,password,database,host=Fun_Read_Creds(logfile)
	# print( user,password,database)
	try:
		
		cnx = mysql.connector.connect(user=user,password=password,
									database=database,
									auth_plugin='mysql_native_password',host=host)
		logging.info('Database Connected')
		# print ("connected")
		return cnx
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			# print("Something is wrong with your user name or password")
			logging.warning('Something is wrong with your user name or password')
			return 'false'

		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			# print("Database does not exist")
			logging.warning('Database does not exist')
			return 'false'
		else:
			# print(err)
			logging.critical('Error:'+str(err))
			return 'false'


def Fun_Execute(mySQLconnection,query):
	try:
		cursor = mySQLconnection.cursor()
		cursor.execute(query)
		return 'true'
	except Exception as e:
		logging.warning('Execution failed:'+str(e))
		return 'false'

#added by sankar
def Fun_Close(mySQLconnection):
	try:
		mySQLconnection.close()
		return 'true'
	except Exception as e:
		logging.warning('Closing connection failed: '+str(e))
		return 'false'








