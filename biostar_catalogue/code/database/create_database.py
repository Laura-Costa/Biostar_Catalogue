import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("drop database if exists biostar_catalogue")
cursor.execute("create database biostar_catalogue")

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.close()
connection.close()