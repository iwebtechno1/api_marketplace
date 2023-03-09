# import pyodbc
# from flask import Flask,jsonify,request,render_template
# # from flask import Flask, jsonify, request
# # from flask_restful import Resource, Api

# # database connection
# pyodbc.drivers()
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=IUMSDemo;DATABASE=GTU_TEST;UID=iweb;PWD=passwd@1')
# cursor = conn.cursor()
# # cursor.execute('SELECT * FROM M_USER') 

# # storing loginid and password in a variable to convert it into list later on 
# loginid_not_list=cursor.execute('SELECT [LOGIN_ID] FROM M_USER')
# password_not_list=cursor.execute('SELECT [PASSWORD] FROM M_USER')
# # for i in cursor:
# #     print(i)

# # storing loginid and password in list 
# loginid_database=list(loginid_not_list)
# password_database=list(password_not_list)

# # # function to authenticate 
# # def authenticate(self, loginid_fromapp, loginid_database, password_fromapp, password_database):
# #     if(loginid_fromapp in loginid_database):
# #         if(password_fromapp in password_database):
# #             print("Logged in successfully")
# #         else:
# #             print("Your password is wrongly entered please try again")
# #     else:
# #         print("Please enter correct id")

import pyodbc
from flask import Flask,jsonify,request,render_template

class Database():
    def __init__(self):
        self.__connection = pyodbc.connect('DRIVER={SQL Server};SERVER=IUMSDemo;DATABASE=GTU_TEST;UID=iweb;PWD=passwd@1')

    def select_records(self,statement):
        cursor = self.__connection.cursor()
        cursor.execute(statement)
        return cursor.fetchall()

    def __del__(self):
        self.__connection.close()