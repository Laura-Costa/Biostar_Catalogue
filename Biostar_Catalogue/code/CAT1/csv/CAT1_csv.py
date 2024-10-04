import mysql.connector
import pandas as pd
import os

father_table = 'Gaia30pc'
son_table = 'Gaia30pc_product'
brother_table = 'Hipparcos'
nephew_table = 'Hipparcos_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["designation", "simbad_HD", "ra", "dec", "parallax", "parallax_error", "pm", "pmra", "pmdec", "ruwe",
          "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag",
          "teff_gspphot", "teff_gspphot_lower", "teff_gspphot_upper",
          "logg_gspphot", "logg_gspphot_lower", "logg_gspphot_upper",
          "mh_gspphot", "mh_gspphot_lower", "mh_gspphot_upper",
          "distance_gspphot", "distance_gspphot_lower", "distance_gspphot_upper",
          "MG", "MG_error",
          "MBp", "MBp_error",
          "MRp", "MRp_error",
          "Bp_Rp",
          "G_Rp",
          "Bp_G"]

cursor.execute("""select {father_table}.designation, """
               """{father_table}.simbad_HD, """
               """trim({father_table}.right_ascension)+0, """
               """trim({father_table}.declination)+0, """
               """trim({father_table}.parallax)+0, """
               """trim({father_table}.parallax_error)+0, """
               """trim({father_table}.pm)+0, """
               """trim({father_table}.pmra)+0, """
               """trim({father_table}.pmdec)+0, """
               """trim({father_table}.ruwe)+0, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({father_table}.phot_bp_mean_mag)+0, """
               """trim({father_table}.phot_rp_mean_mag)+0, """
               """trim({father_table}.teff_gspphot)+0, """
               """trim({father_table}.teff_gspphot_lower)+0, """
               """trim({father_table}.teff_gspphot_upper)+0, """
               """trim({father_table}.logg_gspphot)+0, """
               """trim({father_table}.logg_gspphot_lower)+0, """
               """trim({father_table}.logg_gspphot_upper)+0, """
               """trim({father_table}.mh_gspphot)+0, """
               """trim({father_table}.mh_gspphot_lower)+0, """
               """trim({father_table}.mh_gspphot_upper)+0, """
               """trim({father_table}.distance_gspphot)+0, """
               """trim({father_table}.distance_gspphot_lower)+0, """
               """trim({father_table}.distance_gspphot_upper)+0, """
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
               """where (phot_rp_mean_mag is null or phot_bp_mean_mag is null or phot_g_mean_mag is null) and """
               """( """
               """{father_table}.parallax >= 50.00 """
               """or """
               """((parallax < 50.00) and (parallax+3*parallax_error >= 50.00)) """ 
               """) and """
               """{father_table}.designation = {son_table}.designation """
               """into outfile '/var/lib/mysql-files/estrelas_sem_Rp_Bp_G.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(father_table=father_table,
                                               son_table=son_table))

file = pd.read_csv('/var/lib/mysql-files/estrelas_sem_Rp_Bp_G.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/csv/estrelas_sem_Rp_Bp_G.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/estrelas_sem_Rp_Bp_G.csv")
