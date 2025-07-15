import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'gaia'
son_table = 'Gaia_product'

stringHD = "("

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/solar_twins.txt") as file:
    cont = 0
    for line in file:
        cont += 1
        if cont != 9:
            stringHD += "'HD {}', ".format(line.rstrip())
        else:
            stringHD += "'HD {}')".format(line.rstrip())

query = ("""select substring({father_table}.simbad_HD, 4), """
        """substring({father_table}.simbad_HIP, 5), """
        """{father_table}.parallax, """
        """{father_table}.parallax_error, """
        """{father_table}.phot_g_mean_mag, """
        """{son_table}.MG, """
        """{son_table}.MG_error, """
        """{father_table}.phot_bp_mean_mag, """
        """{son_table}.MBp, """
        """{son_table}.MBp_error, """
        """{father_table}.phot_rp_mean_mag, """
        """{son_table}.MRp, """
        """{son_table}.MRp_error, """
        """{father_table}.bp_rp, """
        """{father_table}.bp_g, """
        """{father_table}.g_rp, """
        """{father_table}.ruwe, """
        """{father_table}.phot_variable_flag, """
        """{father_table}.non_single_star, """
        """{father_table}.distance_gspphot, """
        """{father_table}.distance_gspphot_lower, """
        """{father_table}.distance_gspphot_upper, """
        """{son_table}.distance_gspphot_error, """
        """{father_table}.azero_gspphot, """
        """{father_table}.azero_gspphot_lower, """
        """{father_table}.azero_gspphot_upper, """
        """{son_table}.azero_gspphot_error """
        """from {father_table}, {son_table} """
        """where {father_table}.designation = {son_table}.designation and """
        """(simbad_HD is not null and """
        """simbad_HD in {stringHD}) """
        """order by cast(substring(simbad_HD,3) as unsigned) asc""".format(father_table=father_table,
                                                   son_table=son_table, stringHD=stringHD))

header = ["HD",
          "HIP",
          "parallax",
          "parallax_error",
          "phot_g_mean_mag",
          "MG",
          "MG_error",
          "phot_bp_mean_mag",
          "MBp",
          "MBp_error",
          "phot_rp_mean_mag",
          "MRp",
          "MRp_error",
          "bp_rp",
          "bp_g",
          "g_rp",
          "ruwe",
          "phot_variable_flag",
          "non_single_star",
          "distance_gspphot",
          "distance_gspphot_lower",
          "distance_gspphot_upper",
          "distance_gspphot_error",
          "azero_gspphot",
          "azero_gspphot_lower",
          "azero_gspphot_upper",
          "azero_gspphot_error"]

path = "solar_twins/csv/gemeas_solares.xlsx"
queries = [query]

# def xlsx(cursor, query, header, path, sheets):
f.xlsx(cursor, queries, header, path, ["gemeas_solares"])

cursor.close()
connection.close()