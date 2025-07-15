import mysql.connector

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

cursor.execute("drop view if exists view_CAT1")

cursor.execute("create view view_CAT1 as "
               "select source_id, "
               "designation, "
               "hip, "
               "right_ascension, "
               "declination, "
               "parallax, "
               "parallax_error, "
               "pm, "
               "pmra, "
               "pmdec, "
               "ruwe, "
               "phot_variable_flag, "
               "non_single_star,"
               "phot_g_mean_mag, "
               "phot_bp_mean_mag, "
               "phot_rp_mean_mag, "
               "bp_rp, "
               "bp_g, "
               "g_rp, "
               "teff_gspphot, "
               "teff_gspphot_lower, "
               "teff_gspphot_upper, "
               "logg_gspphot, "
               "logg_gspphot_lower, "
               "logg_gspphot_upper, "
               "mh_gspphot, "
               "mh_gspphot_lower, "
               "mh_gspphot_upper, "
               "distance_gspphot, "
               "distance_gspphot_lower, "
               "distance_gspphot_upper, "
               "azero_gspphot, "
               "azero_gspphot_lower, "
               "azero_gspphot_upper, "
               "radial_velocity, "
               "radial_velocity_error "               
               "from gaia "
               "where "
               "(parallax + 3 * parallax_error >= 50.00)")

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o banco de dados
connection.close()