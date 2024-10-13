import mysql.connector
import pandas as pd
import os

father_table = 'BrightStar'
son_table = 'BrightStarMultiple'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["HR", "HD", "DM", "DM_Cat", "identifier", "simbad_DR1", "simbad_DR2", "simbad_DR3", "simbad_HIP", "simbad_parallax",
          "simbad_parallax_error", "simbad_B", "simbad_V"]

cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
               """{father_table}.DM_Cat, """
               """{father_table}.DM, """
               """{son_table}.identifier, """
               """{son_table}.simbad_DR1, """
               """{son_table}.simbad_DR2, """
               """{son_table}.simbad_DR3, """
               """{son_table}.simbad_HIP, """
               """trim({son_table}.simbad_parallax)+0, """
               """trim({son_table}.simbad_parallax_error)+0, """
               """trim({son_table}.simbad_B)+0, """
               """trim({son_table}.simbad_V)+0 """
               """from {father_table}, {son_table} """ 
               """where {father_table}.HR = {son_table}.HR """
               """into outfile '/var/lib/mysql-files/BrightStarMultiple.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/BrightStarMultiple.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/BrightStarMultiple.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/BrightStarMultiple.csv")