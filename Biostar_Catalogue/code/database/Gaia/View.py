import mysql.connector

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

cursor.execute("drop view if exists view_CAT1")
cursor.execute("drop view if exists view_CAT2")

cursor.execute("create view view_CAT1 as "
               "select "
               "Gaia.designation, "
               "Gaia.right_ascension, "
               "Gaia.declination, "
               "Gaia.parallax, "
               "Gaia.parallax_error, "
               "Gaia.pm, "
               "Gaia.pmra, "
               "Gaia.pmdec, "
               "Gaia.ruwe, "
               "Gaia.phot_variable_flag, "
               "Gaia.non_single_star, "
               "Gaia.phot_g_mean_mag, "
               "Gaia.phot_bp_mean_mag, "
               "Gaia.phot_rp_mean_mag, "
               "Gaia.bp_rp, "
               "Gaia.bp_g, "
               "Gaia.g_rp, "
               "Gaia.teff_gspphot, "
               "Gaia.teff_gspphot_lower, "
               "Gaia.teff_gspphot_upper, "
               "Gaia.logg_gspphot, "
               "Gaia.logg_gspphot_lower, "
               "Gaia.logg_gspphot_upper, "
               "Gaia.mh_gspphot, "
               "Gaia.mh_gspphot_lower, "
               "Gaia.mh_gspphot_upper, "
               "Gaia.distance_gspphot, "
               "Gaia.distance_gspphot_lower, "
               "Gaia.distance_gspphot_upper, "
               "Gaia.azero_gspphot, " 
               "Gaia.azero_gspphot_lower, "
               "Gaia.azero_gspphot_upper "
               "from Gaia, Gaia_product "
               "where "
               "Gaia.designation = Gaia_product.designation and "
               "( "
               "(parallax >= 50.00 and phot_g_mean_mag is not null) or "
               "(parallax >= 50.00 and phot_g_mean_mag is null and MRp < 8.0) or " # condição para incluir a estrela 'Gaia DR3 5443030200460964480'
               "(parallax < 50.00 and MG <= 9.08) " # condição que seleciona as 3 estrelas da "borda" de 3*sigmas 
               ")")

cursor.execute("create view view_CAT2 as "
               "select "
               "Gaia.designation, "
               "Gaia.right_ascension, "
               "Gaia.declination, "
               "Gaia.parallax, "
               "Gaia.parallax_error, "
               "Gaia.pm, "
               "Gaia.pmra, "
               "Gaia.pmdec, "
               "Gaia.ruwe, "
               "Gaia.phot_variable_flag, "
               "Gaia.non_single_star, "
               "Gaia.phot_g_mean_mag, "
               "Gaia.phot_bp_mean_mag, "
               "Gaia.phot_rp_mean_mag, "
               "Gaia.bp_rp, "
               "Gaia.bp_g, "
               "Gaia.g_rp, "
               "Gaia.teff_gspphot, "
               "Gaia.teff_gspphot_lower, "
               "Gaia.teff_gspphot_upper, "
               "Gaia.logg_gspphot, "
               "Gaia.logg_gspphot_lower, "
               "Gaia.logg_gspphot_upper, "
               "Gaia.mh_gspphot, "
               "Gaia.mh_gspphot_lower, "
               "Gaia.mh_gspphot_upper, "
               "Gaia.distance_gspphot, "
               "Gaia.distance_gspphot_lower, "
               "Gaia.distance_gspphot_upper, "
               "Gaia.azero_gspphot, " 
               "Gaia.azero_gspphot_lower, "
               "Gaia.azero_gspphot_upper "
               "from Gaia, Gaia_product "
               "where "
               "Gaia.designation = Gaia_product.designation and "
               "distance_gspphot <= 20.0000 or "
               "( "
               "distance_gspphot > 20.0000 and (distance_gspphot - distance_gspphot_error <= 20.0000) " 
               ")")

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o banco de dados
connection.close()