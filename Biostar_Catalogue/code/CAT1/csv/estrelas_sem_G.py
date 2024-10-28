import mysql.connector
import pandas as pd
import os

father_table = 'CAT1'
son_table = 'CAT1_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["designation", "simbad_HD",
          "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag",
          "MG", "MG_error",
          "MBp", "MBp_error",
          "MRp", "MRp_error",
          "Bp_Rp",
          "G_Rp",
          "Bp_G"]

cursor.execute("""select {father_table}.designation, """
               """{father_table}.simbad_HD, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({father_table}.phot_bp_mean_mag)+0, """
               """trim({father_table}.phot_rp_mean_mag)+0, """
               """trim({son_table}.MG)+0, """
               """trim({son_table}.MG_error)+0, """
               """trim({son_table}.MBp)+0, """
               """trim({son_table}.MBp_error)+0, """
               """trim({son_table}.MRp)+0, """
               """trim({son_table}.MRp_error)+0, """
               """trim({son_table}.Bp_Rp)+0, """
               """trim({son_table}.G_Rp)+0, """
               """trim({son_table}.Bp_G)+0 """
               """from {father_table}, {son_table} """ 
               """where phot_g_mean_mag is null and """
               """{father_table}.designation = {son_table}.designation """
               """into outfile '/var/lib/mysql-files/estrelas_sem_G.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/estrelas_sem_G.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/csv/estrelas_sem_G.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/estrelas_sem_G.csv")