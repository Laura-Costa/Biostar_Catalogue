import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("drop database if exists Biostar_Catalogue")
cursor.execute("create database Biostar_Catalogue")

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.close()
connection.close()