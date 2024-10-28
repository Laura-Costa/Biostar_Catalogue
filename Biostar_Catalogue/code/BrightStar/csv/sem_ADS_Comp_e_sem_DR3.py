import mysql.connector
import pandas as pd
import os

father_table = 'BrightStar'
son_table = 'BrightStar_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["HR", "HD", "simbad_parallax", "simbad_parallax_source", "V", "MV", "B_V", "Name", "simbad_SpType", "simbad_name"]

cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
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
               """{father_table}.ADS_Comp is null and  """
               """{father_table}.simbad_DR3 is null """
               """into outfile '/var/lib/mysql-files/estrelas_sem_ADS_Comp_e_sem_DR3.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/estrelas_sem_ADS_Comp_e_sem_DR3.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/estrelas_sem_ADS_Comp_e_sem_DR3.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/estrelas_sem_ADS_Comp_e_sem_DR3.csv")

cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
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
               """{father_table}.ADS_Comp is null and  """
               """{father_table}.simbad_DR3 is null and """
               """{son_table}.MV is not null and """
               """{son_table}.B_V is not null """
               """into outfile '/var/lib/mysql-files/estrelas_sem_ADS_Comp_e_sem_DR3_plotted.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/estrelas_sem_ADS_Comp_e_sem_DR3_plotted.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/estrelas_sem_ADS_Comp_e_sem_DR3_plotted.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/estrelas_sem_ADS_Comp_e_sem_DR3_plotted.csv")