import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

header_list = ["HR", "Name", "HD", "HD_Suffix", "V", "B_V", "SpType"]

# Criando o arquivo BrightStar_without_designation_gaia_DR3_in_Simbad.csv

cursor.execute('''select BrightStar.HR, '''
               '''BrightStar.Name, '''
               '''BrightStar.HD, '''
               '''BrightStar.HD_Suffix, '''
               '''BrightStar.V, '''
               '''BrightStar.B_V, '''
               '''BrightStar.SpType '''
               '''from BrightStar '''
               '''where BrightStar.simbad_designation_DR3 is null '''
               '''order by BrightStar.B_V desc '''
               '''into outfile '/var/lib/mysql-files/BrightStar_without_designation_gaia_DR3_in_Simbad.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/BrightStar_without_designation_gaia_DR3_in_Simbad.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/BrightStar/csv/BrightStar_without_designation_gaia_DR3_in_Simbad.csv", header=header_list, index=False)
os.remove("/var/lib/mysql-files/BrightStar_without_designation_gaia_DR3_in_Simbad.csv")

cursor.close()
connection.close()