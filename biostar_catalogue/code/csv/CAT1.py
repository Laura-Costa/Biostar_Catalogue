import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

header_list = ["designation", "HIP", "HD", "ra", "declination", "parallax", "parallax_error", "pm", "pmra",
               "pmdec", "ruwe", "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag", "teff_gspphot",
               "teff_gspphot_lower", "teff_gspphot_upper", "logg_gspphot", "logg_gspphot_lower",
               "logg_gspphot_upper", "mh_gspphot", "mh_gspphot_lower", "mh_gspphot_upper", "distance_gspphot",
               "distance_gspphot_lower", "distance_gspphot_upper", "Mg", "Mg_error", "MRp", "MRp_error", "Bp_minus_Rp"]

# Criando o arquivo CAT1.csv

cursor.execute('''select CAT1.designation, '''
               '''CAT1.HIP, '''
               '''CAT1.HD, '''
               '''TRIM(CAT1.ra)+0, '''
               '''TRIM(CAT1.declination)+0, '''
               '''TRIM(CAT1.parallax)+0, '''
               '''TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.pm)+0, '''
               '''TRIM(CAT1.pmra)+0, '''
               '''TRIM(CAT1.pmdec)+0, '''
               '''TRIM(CAT1.ruwe)+0, '''
               '''TRIM(CAT1.phot_g_mean_mag)+0, '''
               '''TRIM(CAT1.phot_bp_mean_mag)+0, '''
               '''TRIM(CAT1.phot_rp_mean_mag)+0, '''
               '''TRIM(CAT1.teff_gspphot)+0, '''
               '''TRIM(CAT1.teff_gspphot_lower)+0, '''
               '''TRIM(CAT1.teff_gspphot_upper)+0, '''
               '''TRIM(CAT1.logg_gspphot)+0, '''
               '''TRIM(CAT1.logg_gspphot_lower)+0, '''
               '''TRIM(CAT1.logg_gspphot_upper)+0, '''
               '''TRIM(CAT1.mh_gspphot)+0, '''
               '''TRIM(CAT1.mh_gspphot_lower)+0, '''
               '''TRIM(CAT1.mh_gspphot_upper)+0, '''
               '''TRIM(CAT1.distance_gspphot)+0, '''
               '''TRIM(CAT1.distance_gspphot_lower)+0, '''
               '''TRIM(CAT1.distance_gspphot_upper)+0, '''
               '''TRIM(CAT1_product.Mg)+0, '''
               '''TRIM(CAT1_product.Mg_error)+0, '''
               '''TRIM(CAT1_product.MRp)+0, '''
               '''TRIM(CAT1_product.MRp_error)+0, '''
               '''TRIM(CAT1_product.Bp_minus_Rp)+0 '''
               '''from CAT1, CAT1_product '''
               '''where CAT1.designation = CAT1_product.designation '''
               '''order by CAT1.parallax asc '''
               '''into outfile '/var/lib/mysql-files/CAT1.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT1.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/csv/CAT1.csv", header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT1.csv")

cursor.close()
connection.close()