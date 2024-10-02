import mysql.connector
import pandas as pd
import os

father_table = 'Gaia30pc'
son_table = 'Gaia30pc_product'
brother_table = 'Hipparcos'
nephew_table = 'Hipparcos_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["DR3", "DR2", "DR1", "HIP", "HD", "BD", "CoD", "CPD", "right_ascension", "declination", "parallax", "parallax_error",
          "phot_g_mean_mag", "MG", "MG_error", "phot_bp_mean_mag", "MBp", "MBp_error", "phot_rp_mean_mag", "MRp", "MRp_error",
          "distance_gspphot", "Plx", "e_Plx", "Vmag", "MV", "MV_error", "VTmag", "MVt", "MVt_error", "BTmag", "B_V",
          "Bt_Vt"]

cursor.execute("""select {father_table}.designation, """
               """{brother_table}.simbad_DR2, """
               """{brother_table}.simbad_DR1, """
               """{brother_table}.HIP, """
               """{father_table}.simbad_HD, """
               """{brother_table}.BD, """
               """{brother_table}.CoD, """
               """{brother_table}.CPD, """
               """{father_table}.right_ascension, """
               """{father_table}.declination, """
               """{father_table}.parallax, """
               """{father_table}.parallax_error, """
               """{father_table}.phot_g_mean_mag, """
               #"""{son_table}.MG, """
               #"""{son_table}.MG_error, """
               """{father_table}.phot_bp_mean_mag, """
               #"""{son_table}.MBp, """
               #"""{son_table}.MBp_error, """
               """{father_table}.phot_rp_mean_mag, """
               #"""{son_table}.MRp, """
               #"""{son_table}.MRp_error, """
               """{father_table}.distance_gspphot, """
               """{brother_table}.Plx, """
               """{brother_table}.e_Plx, """
               """{brother_table}.Vmag, """
               #"""{nephew_table}.MV, """
               #"""{nephew_table}.MV_error, """
               """{brother_table}.VTmag, """
               #"""{nephew_table}.MVt, """
               #"""{nephew_table}.MVt_error, """
               """{brother_table}.BTmag """ #,
               #"""{nephew_table}.B_V, """
               #"""{nephew_table}.Bt_Vt """
               """from {father_table}, {brother_table} """ #, {son_table}, {nephew_table} """
               """where """
               """( """
               """{father_table}.designation = {son_table}.designation and """
               """{father_table}.HIP is null and """
               """({father_table}.phot_rp_mean_mag is null or {father_table}.phot_bp_mean_mag is null or {father_table}.phot_g_mean_mag is null) """
               """) """
               """or """
               """( """
               """{father_table}.designation = {son_table}.designation and """
               """{father_table}.HIP is not null and """
               """{father_table}.HIP = {brother_table}.HIP and """
               """({father_table}.phot_rp_mean_mag is null or {father_table}.phot_bp_mean_mag is null or {father_table}.phot_g_mean_mag is null) """
               """) """ 
               """into outfile '/var/lib/mysql-files/estrelas_sem_Rp_Bp_G.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               brother_table=brother_table,
                                               son_table=son_table,
                                               nephew_table=nephew_table))

file = pd.read_csv('/var/lib/mysql-files/estrelas_sem_Rp_Bp_G.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/csv/estrelas_sem_Rp_Bp_G.csv", header=header, index=False)
os.remove("/var/lib/mysql-files/estrelas_sem_Rp_Bp_G.csv")
