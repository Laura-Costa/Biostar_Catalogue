import mysql.connector
import code.functions.xlsx as f
import pandas as pd
import os

father_table = 'Gaia'
son_table = 'Gaia_product'

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
               """trim({father_table}.bp_rp)+0, """
               """trim({father_table}.g_rp)+0, """
               """trim({father_table}.bp_g)+0 """
               """from {father_table}, {son_table} """ 
               """where {father_table}.parallax >= 50.000 and """
               """{father_table}.designation = {son_table}.designation """
               """into outfile '/var/lib/mysql-files/CAT1_20pc.csv' CHARACTER SET utf8mb4 """ 
               """fields terminated by ',' optionally enclosed by '"' escaped by '' """
               """lines terminated by '\r\n' """.format(father_table=father_table, son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/CAT1_20pc.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/text_files/CAT1_20pc.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/CAT1_20pc.csv")

""" fazer o arquivo com o tipo xlsx """

query_nucleo = ("select {father_table}.designation, "
                "{father_table}.simbad_HD, "
                "{father_table}.simbad_HIP, "
                "trim({father_table}.parallax)+0, "
                "trim({father_table}.parallax_error)+0, "
                "trim({father_table}.phot_g_mean_mag)+0, "
                "trim({father_table}.phot_bp_mean_mag)+0, "
                "trim({father_table}.phot_rp_mean_mag)+0, "
                "trim({son_table}.MG)+0, "
                "trim({son_table}.MG_error)+0, "
                "trim({son_table}.MBp)+0, "
                "trim({son_table}.MBp_error)+0, "
                "trim({son_table}.MRp)+0, "
                "trim({son_table}.MRp_error)+0, "
                "trim({father_table}.bp_rp)+0, "
                "trim({father_table}.g_rp)+0, "
                "trim({father_table}.bp_g)+0 "
                "from {father_table}, {son_table} " 
                "where {father_table}.parallax >= 50.000 and "
                "{father_table}.designation = {son_table}.designation ".format(father_table=father_table, son_table=son_table))

query_borda = ("select {father_table}.designation, "
               "{father_table}.simbad_HD, "
               "{father_table}.simbad_HIP, "
               "trim({father_table}.parallax)+0, "
               "trim({father_table}.parallax_error)+0, "
               "trim({father_table}.phot_g_mean_mag)+0, "
               "trim({father_table}.phot_bp_mean_mag)+0, "
               "trim({father_table}.phot_rp_mean_mag)+0, "
               "trim({son_table}.MG)+0, "
               "trim({son_table}.MG_error)+0, "
               "trim({son_table}.MBp)+0, "
               "trim({son_table}.MBp_error)+0, "
               "trim({son_table}.MRp)+0, "
               "trim({son_table}.MRp_error)+0, "
               "trim({father_table}.bp_rp)+0, "
               "trim({father_table}.g_rp)+0, "
               "trim({father_table}.bp_g)+0 "
               "from {father_table}, {son_table} " 
               "where {father_table}.parallax < 50.000 and "
               "{father_table}.parallax + 3*{father_table}.parallax_error >= 50.000 and "
               "{father_table}.designation = {son_table}.designation ".format(father_table=father_table, son_table=son_table))

# declarar as variáveis que serão passadas para a função
headers = ['designation', 'simbad_HD', 'simbad_HIP',
           'parallax', 'parallax_error',
           'phot_g_mean_mag', 'phot_bp_mean_mag', 'phot_rp_mean_mag',
           'MG', 'MG_error',
           'MBp', 'MBp_error',
           'MRp', 'MRp_error',
           'bp_rp', 'g_rp', 'bp_g']
path = 'CAT1/text_files/CAT1.xlsx'
sheets = ["nucleo_de_20pc", "borda_de_3sigmas"]
queries = [query_nucleo, query_borda]
f.xlsx(cursor, queries, headers, path, sheets)


connection.close()
cursor.close()