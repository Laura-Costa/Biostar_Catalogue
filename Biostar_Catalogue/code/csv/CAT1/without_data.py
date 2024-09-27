import mysql.connector
import pandas as pd
import os

father_table = 'Gaia50pc'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["designation", "HIP", "simbad_HIP", "simbad_HD", "in_Simbad", "right_ascension", "declination", "parallax", "parallax_error",
          "pm", "pmra", "pmdec", "ruwe", "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag", "teff_gspphot", "teff_gspphot_lower",
          "teff_gspphot_upper", "logg_gspphot", "logg_gspphot_lower", "logg_gspphot_upper", "mh_gspphot", "mh_gspphot_lower",
          "mh_gspphot_upper", "distance_gspphot", "distance_gspphot_lower", "distance_gspphot_upper"]

# criar o arquivo without_Rp_Bp_G.csv

cursor.execute("""select designation, """
               """HIP, """
               """simbad_HIP, """
               """simbad_HD, """
               """in_Simbad, """
               """right_ascension, """
               """declination, """
               """parallax, """
               """parallax_error, """
               """pm, """
               """pmra, """
               """pmdec, """
               """ruwe, """
               """phot_g_mean_mag, """
               """phot_bp_mean_mag, """
               """phot_rp_mean_mag, """
               """teff_gspphot, """
               """teff_gspphot_lower, """
               """teff_gspphot_upper, """
               """logg_gspphot, """
               """logg_gspphot_lower, """
               """logg_gspphot_upper, """
               """mh_gspphot, """
               """mh_gspphot_lower, """
               """mh_gspphot_upper, """
               """distance_gspphot, """
               """distance_gspphot_lower, """
               """distance_gspphot_upper """
               """from {father_table} """
               """where (phot_g_mean_mag is null or """
               """phot_bp_mean_mag is null or """
               """phot_rp_mean_mag is null) and """ 
               """( """ 
               """parallax >= 50.00 or (parallax < 50.00 and (parallax+3*parallax_error) >= 50.00) """
               """) """
               """into outfile '/var/lib/mysql-files/without_Rp_Bp_G.csv' """
               """fields optionally enclosed by '"' terminated by ',' lines terminated by '\n' """.format(father_table=father_table))

file = pd.read_csv('/var/lib/mysql-files/without_Rp_Bp_G.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/csv/without_Rp_Bp_G.csv", header=header, index=False)
os.remove('/var/lib/mysql-files/without_Rp_Bp_G.csv')