import mysql.connector

father_table = 'Gaia'
son_table = 'Gaia_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

stringHD = "("

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/solar_twins.txt") as file:
    cont = 0
    for line in file:
        cont += 1
        if cont != 5:
            stringHD += "'HD {}', ".format(line.rstrip())
        else:
            stringHD += "'HD {}')".format(line.rstrip())

cursor.execute("""select {father_table}.simbad_HD, """
               """trim({father_table}.parallax)+0, """
               """trim({father_table}.parallax_error)+0, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({son_table}.MG)+0, """
               """trim({son_table}.MG_error)+0, """
               """trim({father_table}.phot_bp_mean_mag)+0, """
               """trim({son_table}.MBp)+0, """
               """trim({son_table}.MBp_error)+0, """
               """trim({father_table}.phot_rp_mean_mag)+0, """
               """trim({son_table}.MRp)+0, """
               """trim({son_table}.MRp_error)+0, """
               """trim({father_table}.bp_rp)+0, """
               """trim({father_table}.bp_g)+0, """
               """trim({father_table}.g_rp)+0, """
               """trim({father_table}.ruwe)+0, """
               """{father_table}.phot_variable_flag, """
               """{father_table}.non_single_star, """
               """trim({father_table}.distance_gspphot)+0, """
               """trim({father_table}.distance_gspphot_lower)+0, """
               """trim({father_table}.distance_gspphot_upper)+0, """
               """trim({son_table}.distance_gspphot_error)+0, """
               """trim({father_table}.azero_gspphot)+0, """
               """trim({father_table}.azero_gspphot_lower)+0, """
               """trim({father_table}.azero_gspphot_upper)+0, """
               """trim({son_table}.azero_gspphot_error)+0 """
               """from {father_table}, {son_table} """
               """where {father_table}.designation = {son_table}.designation and """
               """(simbad_HD is not null and """
               """simbad_HD in {stringHD}) """
               """order by simbad_HD asc""".format(father_table=father_table,
                                                   son_table=son_table, stringHD=stringHD))

value = cursor.fetchall()

simbad_HD_list = []
parallax_list = []
parallax_error_list = []
phot_g_mean_mag_list = []
MG_list = []
MG_error_list = []
phot_bp_mean_mag_list = []
MBp_list = []
MBp_error_list = []
phot_rp_mean_mag_list = []
MRp_list = []
MRp_error_list = []
bp_rp_list = []
bp_g_list = []
g_rp_list = []
ruwe_list = []
phot_variable_flag_list = []
non_single_star_list = []
distance_gspphot_list = []
distance_gspphot_lower_list = []
distance_gspphot_upper_list = []
distance_gspphot_error_list = []
azero_gspphot_list = []
azero_gspphot_lower_list = []
azero_gspphot_upper_list = []
azero_gspphot_error_list = []

for (simbad_HD_value, parallax_value, parallax_error_value,
    phot_g_mean_mag_value, MG_value, MG_error_value,
    phot_bp_mean_mag_value, MBp_value, MBp_error_value,
    phot_rp_mean_mag_value, MRp_value, MRp_error_value,
    bp_rp_value, bp_g_value, g_rp_value,
    ruwe_value,
    phot_variable_flag_value,
    non_single_star_value,
    distance_gspphot_value, distance_gspphot_lower_value, distance_gspphot_upper_value, distance_gspphot_error_value,
    azero_gspphot_value, azero_gspphot_lower_value, azero_gspphot_upper_value, azero_gspphot_error_value) in value:

    simbad_HD_list.append(simbad_HD_value)
    parallax_list.append(parallax_value)
    parallax_error_list.append(parallax_error_value)
    phot_g_mean_mag_list.append(phot_g_mean_mag_value)
    MG_list.append(MG_value)
    MG_error_list.append(MG_error_value)
    phot_bp_mean_mag_list.append(phot_bp_mean_mag_value)
    MBp_list.append(MBp_value)
    MBp_error_list.append(MBp_error_value)
    phot_rp_mean_mag_list.append(phot_rp_mean_mag_value)
    MRp_list.append(MRp_value)
    MRp_error_list.append(MRp_error_value)
    bp_rp_list.append(bp_rp_value)
    bp_g_list.append(bp_g_value)
    g_rp_list.append(g_rp_value)
    ruwe_list.append(ruwe_value)
    phot_variable_flag_list.append(phot_variable_flag_value)
    non_single_star_list.append(non_single_star_value)
    distance_gspphot_list.append(distance_gspphot_value)
    distance_gspphot_lower_list.append(distance_gspphot_lower_value)
    distance_gspphot_upper_list.append(distance_gspphot_upper_value)
    distance_gspphot_error_list.append(distance_gspphot_error_value)
    azero_gspphot_list.append(azero_gspphot_value)
    azero_gspphot_lower_list.append(azero_gspphot_lower_value)
    azero_gspphot_upper_list.append(azero_gspphot_upper_value)
    azero_gspphot_error_list.append(azero_gspphot_error_value)

# process parallax
for i in range(len(parallax_list)):
    parallax_list[i] = round(parallax_list[i], 4)
    parallax_list[i] = f"{parallax_list[i]:07.4f}"

# process parallax_error
for i in range(len(parallax_error_list)):
    parallax_error_list[i] = round(parallax_error_list[i], 4)
    parallax_error_list[i] = f"{parallax_error_list[i]:06.4f}"

# process phot_g_mean_mag
for i in range(len(phot_g_mean_mag_list)):
    phot_g_mean_mag_list[i] = round(phot_g_mean_mag_list[i], 4)
    phot_g_mean_mag_list[i] = f"{phot_g_mean_mag_list[i]:06.4f}"

# process MG
for i in range(len(MG_list)):
    MG_list[i] = round(MG_list[i], 4)
    MG_list[i] = f"{MG_list[i]:06.4f}"

# process MG_error
for i in range(len(MG_error_list)):
    MG_error_list[i] = round(MG_error_list[i], 4)
    MG_error_list[i] = f"{MG_error_list[i]:06.4f}"

# process phot_bp_mean_mag
for i in range(len(phot_bp_mean_mag_list)):
    phot_bp_mean_mag_list[i] = round(phot_bp_mean_mag_list[i], 4)
    phot_bp_mean_mag_list[i] = f"{phot_bp_mean_mag_list[i]:06.4f}"

# process MBp
for i in range(len(MBp_list)):
    MBp_list[i] = round(MBp_list[i], 4)
    MBp_list[i] = f"{MBp_list[i]:06.4f}"

# process MBp_error
for i in range(len(MBp_error_list)):
    MBp_error_list[i] = round(MBp_error_list[i], 4)
    MBp_error_list[i] = f"{MBp_error_list[i]:06.4f}"

# process phot_rp_mean_mag
for i in range(len(phot_rp_mean_mag_list)):
    phot_rp_mean_mag_list[i] = round(phot_rp_mean_mag_list[i], 4)
    phot_rp_mean_mag_list[i] = f"{phot_rp_mean_mag_list[i]:06.4f}"

# process MRp
for i in range(len(MRp_list)):
    MRp_list[i] = round(MRp_list[i], 4)
    MRp_list[i] = f"{MRp_list[i]:06.4f}"

# process MRp_error
for i in range(len(MRp_error_list)):
    MRp_error_list[i] = round(MRp_error_list[i], 4)
    MRp_error_list[i] = f"{MRp_error_list[i]:06.4f}"

# process bp_rp
for i in range(len(bp_rp_list)):
    bp_rp_list[i] = round(bp_rp_list[i], 4)
    bp_rp_list[i] = f"{bp_rp_list[i]:06.4f}"

# process bp_g
for i in range(len(bp_g_list)):
    bp_g_list[i] = round(bp_g_list[i], 4)
    bp_g_list[i] = f"{bp_g_list[i]:06.4f}"

# process g_rp
for i in range(len(g_rp_list)):
    g_rp_list[i] = round(g_rp_list[i], 4)
    g_rp_list[i] = f"{g_rp_list[i]:06.4f}"

# process ruwe
for i in range(len(ruwe_list)):
    ruwe_list[i] = round(ruwe_list[i], 4)
    ruwe_list[i] = f"{ruwe_list[i]:07.4f}"

# process distance_gspphot
for i in range(len(distance_gspphot_list)):
    distance_gspphot_list[i] = round(distance_gspphot_list[i], 4)
    distance_gspphot_list[i] = f"{distance_gspphot_list[i]:07.4f}"

# process distance_gspphot_upper
for i in range(len(distance_gspphot_upper_list)):
    distance_gspphot_upper_list[i] = round(distance_gspphot_upper_list[i], 4)
    distance_gspphot_upper_list[i] = f"{distance_gspphot_upper_list[i]:07.4f}"

# process distance_gspphot_lower
for i in range(len(distance_gspphot_lower_list)):
    distance_gspphot_lower_list[i] = round(distance_gspphot_lower_list[i], 4)
    distance_gspphot_lower_list[i] = f"{distance_gspphot_lower_list[i]:07.4f}"

# process distance_gspphot_error
for i in range(len(distance_gspphot_error_list)):
    distance_gspphot_error_list[i] = round(distance_gspphot_error_list[i], 4)
    distance_gspphot_error_list[i] = f"{distance_gspphot_error_list[i]:06.4f}"

# process azero_gspphot
for i in range(len(azero_gspphot_list)):
    azero_gspphot_list[i] = round(azero_gspphot_list[i], 4)
    azero_gspphot_list[i] = f"{azero_gspphot_list[i]:06.4f}"

# process azero_gspphot_upper
for i in range(len(azero_gspphot_upper_list)):
    azero_gspphot_upper_list[i] = round(azero_gspphot_upper_list[i], 4)
    azero_gspphot_upper_list[i] = f"{azero_gspphot_upper_list[i]:07.4f}"

# process azero_gspphot_lower
for i in range(len(azero_gspphot_lower_list)):
    azero_gspphot_lower_list[i] = round(azero_gspphot_lower_list[i], 4)
    azero_gspphot_lower_list[i] = f"{azero_gspphot_lower_list[i]:07.4f}"

print(azero_gspphot_error_list)
# process azero_gspphot_error
for i in range(len(azero_gspphot_error_list)):
    azero_gspphot_error_list[i] = round(azero_gspphot_error_list[i], 5)
    azero_gspphot_error_list[i] = f"{azero_gspphot_error_list[i]:07.5f}"

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/solar_twins/csv/gemeas_solares.txt", "w") as text_file:
    header = ["HD", "parallax",
              "G", "MG",
              "Bp", "MBp",
              "Rp", "MRp",
              "Bp_Rp", "Bp_G", "G_Rp",
              "ruwe",
              "phot_variable_flag",
              "non_single_star",
              "distance_gspphot",
              "azero_gspphot"]

    """
    Header
    """
    text_file.write("{0[0]:<7}" # HD
                    "{0[1]:<17}" # parallax +/- erro
                    "{0[2]:<7}"
                    "{0[3]:<16}"
                    "{0[4]:<7}"
                    "{0[5]:<16}"
                    "{0[6]:<7}"
                    "{0[7]:<16}"
                    "{0[8]:<7}"
                    "{0[9]:<7}"
                    "{0[10]:<7}"
                    "{0[11]:<8}"
                    "{0[12]:<19}"
                    "{0[13]:<16}"
                    "{0[14]:<17}"
                    "{0[15]:<20}\n".format(header))

    for (HD, parallax, parallax_error,
         G, MG, MG_error,
         Bp, MBp, MBp_error,
         Rp, MRp, MRp_error,
         Bp_Rp, Bp_G, G_Rp,
         ruwe,
         phot_variable_flag,
         non_single_star,
         distance_gspphot, distance_gspphot_error,
         azero_gspphot, azero_gspphot_error) in zip(simbad_HD_list, parallax_list, parallax_error_list,
                                                    phot_g_mean_mag_list, MG_list, MG_error_list,
                                                    phot_bp_mean_mag_list, MBp_list, MBp_error_list,
                                                    phot_rp_mean_mag_list, MRp_list, MRp_error_list,
                                                    bp_rp_list, bp_g_list, g_rp_list,
                                                    ruwe_list,
                                                    phot_variable_flag_list,
                                                    non_single_star_list,
                                                    distance_gspphot_list, distance_gspphot_error_list,
                                                    azero_gspphot_list, azero_gspphot_error_list):
        lista = [HD[3:], parallax, parallax_error,
                 G, MG, MG_error,
                 Bp, MBp, MBp_error,
                 Rp, MRp, MRp_error,
                 Bp_Rp, Bp_G, G_Rp,
                 ruwe,
                 phot_variable_flag,
                 non_single_star,
                 distance_gspphot, distance_gspphot_error,
                 azero_gspphot, azero_gspphot_error, "±"]

        """
        Dados
        """
        text_file.write("{0[0]:<7}" # HD
                        "{0[1]:<8}" # parallax
                        "{0[22]:<2}" # simbolo
                        "{0[2]:<7}" # parallax_error
                        "{0[3]:<7}"
                        "{0[4]:<7}"
                        "{0[22]:<2}"
                        "{0[5]:<7}"
                        "{0[6]:<7}"
                        "{0[7]:<7}"
                        "{0[22]:<2}"
                        "{0[8]:<7}"
                        "{0[9]:<7}"
                        "{0[10]:<7}"
                        "{0[22]:<2}"
                        "{0[11]:<7}"
                        "{0[12]:<7}"
                        "{0[13]:<7}"
                        "{0[14]:<7}"
                        "{0[15]:<8}"
                        "{0[16]:<19}"
                        "{0[17]:<16}"
                        "{0[18]:<8}"
                        "{0[22]:<2}"
                        "{0[19]:<7}"
                        "{0[20]:<7}"
                        "{0[22]:<2}"
                        "{0[21]:<20}\n".format(lista))