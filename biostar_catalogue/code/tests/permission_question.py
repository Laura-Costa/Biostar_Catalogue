import mysql.connector
import pandas as pd
"""
connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023')
cursor = connection.cursor()


cursor.execute('''select TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(Hipparcos.Plx)+0 '''
               '''from Hipparcos '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_ePlx_Plx_sem_header.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

cursor.close()
connection.close()
"""

header_list = ["e_Plx", "Plx"]
file = pd.read_csv("/var/lib/mysql-files/Hipparcos_ePlx_Plx_sem_header.csv")
file.to_csv("/home/lh/Desktop/Hipparcos_ePlx_Plx.csv", header=header_list, index=False)
