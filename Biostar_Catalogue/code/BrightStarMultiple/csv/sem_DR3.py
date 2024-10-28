import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["simbad_name", "simbad_parallax", "simbad_parallax_source", "simbad_V", "simbad_MV", "simbad_B_V", "simbad_SpType"]

cursor.execute("""select distinct BrightStarMultiple.simbad_name, """
               """trim(BrightStarMultiple.simbad_parallax)+0, """
               """BrightStarMultiple.simbad_parallax_source, """
               """trim(BrightStarMultiple.simbad_V)+0, """
               """trim(BrightStarMultiple_product.simbad_MV)+0, """
               """trim(BrightStarMultiple_product.simbad_B_V)+0, """
               """BrightStarMultiple.simbad_SpType """
               """from BrightStar, BrightStarMultiple, BrightStarMultiple_product """
               """where BrightStar.HR = BrightStarMultiple.HR and """
               """BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and """
               """BrightStarMultiple.simbad_DR3 is null """
               """into outfile '/var/lib/mysql-files/sem_DR3.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """)

file = pd.read_csv('/var/lib/mysql-files/sem_DR3.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/sem_DR3.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/sem_DR3.csv")

header = ["simbad_name", "simbad_parallax", "simbad_parallax_source", "simbad_V", "simbad_MV", "simbad_B_V", "simbad_SpType"]

cursor.execute("""select distinct BrightStarMultiple.simbad_name, """
               """trim(BrightStarMultiple.simbad_parallax)+0, """
               """BrightStarMultiple.simbad_parallax_source, """
               """trim(BrightStarMultiple.simbad_V)+0, """
               """trim(BrightStarMultiple_product.simbad_MV)+0, """
               """trim(BrightStarMultiple_product.simbad_B_V)+0, """
               """BrightStarMultiple.simbad_SpType """
               """from BrightStar, BrightStarMultiple, BrightStarMultiple_product """
               """where BrightStar.HR = BrightStarMultiple.HR and """
               """BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and """
               """BrightStarMultiple.simbad_DR3 is null and """
               """BrightStarMultiple_product.simbad_MV is not null and """
               """BrightStarMultiple_product.simbad_B_V is not null """
               """into outfile '/var/lib/mysql-files/sem_DR3_plotted.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """)

file = pd.read_csv('/var/lib/mysql-files/sem_DR3_plotted.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/sem_DR3_plotted.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/sem_DR3_plotted.csv")