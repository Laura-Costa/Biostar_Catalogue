import mysql.connector
import pandas as pd
import os

father_table = 'BrightStar'
son_table = 'BrightStar_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["HR", "HD", "simbad_DR3", "simbad_parallax", "simbad_parallax_source", "V", "MV", "B_V", "Name", "simbad_SpType", "simbad_name"]

cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
               """{father_table}.simbad_DR3, """
               """trim({father_table}.simbad_parallax)+0, """
               """{father_table}.simbad_parallax_source, """
               """trim({father_table}.V)+0, """
               """trim({son_table}.MV)+0, """
               """trim({father_table}.B_V)+0, """
               """{father_table}.Name, """
               """{father_table}.simbad_SpType, """
               """{father_table}.simbad_name """
               """from {father_table}, {son_table} """
               """where {father_table}.HR = {son_table}.HR and """
               """{father_table}.HD is null """
               """into outfile '/var/lib/mysql-files/estrelas_sem_HD.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/estrelas_sem_HD.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/estrelas_sem_HD.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/estrelas_sem_HD.csv")