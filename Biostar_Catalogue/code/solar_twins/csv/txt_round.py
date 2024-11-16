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
        if cont != 9:
            stringHD += "'HD {}', ".format(line.rstrip())
        else:
            stringHD += "'HD {}')".format(line.rstrip())

cursor.execute("""select {father_table}.simbad_HD, """
               """{father_table}.simbad_HIP, """
               """round({father_table}.parallax,4), """
               """round({father_table}.parallax_error, 4), """
               """round({father_table}.phot_g_mean_mag, 4), """
               """round({son_table}.MG, 4), """
               """round({son_table}.MG_error, 4), """
               """round({father_table}.phot_bp_mean_mag, 4), """
               """round({son_table}.MBp, 4), """
               """round({son_table}.MBp_error, 4), """
               """round({father_table}.phot_rp_mean_mag, 4), """
               """round({son_table}.MRp, 4), """
               """round({son_table}.MRp_error, 4), """
               """round({father_table}.bp_rp, 4), """
               """round({father_table}.bp_g, 4), """
               """round({father_table}.g_rp, 4), """
               """round({father_table}.ruwe, 4), """
               """{father_table}.phot_variable_flag, """
               """{father_table}.non_single_star, """
               """round({father_table}.distance_gspphot, 4), """
               """round({father_table}.distance_gspphot_lower, 4), """
               """round({father_table}.distance_gspphot_upper, 4), """
               """round({son_table}.distance_gspphot_error, 4), """
               """round({father_table}.azero_gspphot, 4), """
               """round({father_table}.azero_gspphot_lower, 4), """
               """round({father_table}.azero_gspphot_upper, 4), """
               """round({son_table}.azero_gspphot_error, 4) """
               """from {father_table}, {son_table} """
               """where {father_table}.designation = {son_table}.designation and """
               """(simbad_HD is not null and """
               """simbad_HD in {stringHD}) """
               """order by cast(substring(simbad_HD,3) as unsigned) asc""".format(father_table=father_table,
                                                   son_table=son_table, stringHD=stringHD))

value = cursor.fetchall()

simbad_HD_list = []
simbad_HIP_list = []
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

for (simbad_HD_value, simbad_HIP_value, parallax_value, parallax_error_value,
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
    simbad_HIP_list.append(simbad_HIP_value)
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
    parallax_list[i] = f"{parallax_list[i]:07.4f}"

# process parallax_error
for i in range(len(parallax_error_list)):
    parallax_error_list[i] = f"{parallax_error_list[i]:06.4f}"

# process phot_g_mean_mag
for i in range(len(phot_g_mean_mag_list)):
    phot_g_mean_mag_list[i] = f"{phot_g_mean_mag_list[i]:06.4f}"

# process MG
for i in range(len(MG_list)):
    MG_list[i] = f"{MG_list[i]:06.4f}"

# process MG_error
for i in range(len(MG_error_list)):
    MG_error_list[i] = f"{MG_error_list[i]:06.4f}"

# process phot_bp_mean_mag
for i in range(len(phot_bp_mean_mag_list)):
    phot_bp_mean_mag_list[i] = f"{phot_bp_mean_mag_list[i]:06.4f}"

# process MBp
for i in range(len(MBp_list)):
    MBp_list[i] = f"{MBp_list[i]:06.4f}"

# process MBp_error
for i in range(len(MBp_error_list)):
    MBp_error_list[i] = f"{MBp_error_list[i]:06.4f}"

# process phot_rp_mean_mag
for i in range(len(phot_rp_mean_mag_list)):
    phot_rp_mean_mag_list[i] = f"{phot_rp_mean_mag_list[i]:06.4f}"

# process MRp
for i in range(len(MRp_list)):
    MRp_list[i] = f"{MRp_list[i]:06.4f}"

# process MRp_error
for i in range(len(MRp_error_list)):
    MRp_error_list[i] = f"{MRp_error_list[i]:06.4f}"

# process bp_rp
for i in range(len(bp_rp_list)):
    bp_rp_list[i] = f"{bp_rp_list[i]:06.4f}"

# process bp_g
for i in range(len(bp_g_list)):
    bp_g_list[i] = f"{bp_g_list[i]:06.4f}"

# process g_rp
for i in range(len(g_rp_list)):
    g_rp_list[i] = f"{g_rp_list[i]:06.4f}"

# process ruwe
for i in range(len(ruwe_list)):
    ruwe_list[i] = f"{ruwe_list[i]:07.4f}"

# process distance_gspphot
for i in range(len(distance_gspphot_list)):
    distance_gspphot_list[i] = f"{distance_gspphot_list[i]:07.4f}"

# process distance_gspphot_error
for i in range(len(distance_gspphot_error_list)):
    distance_gspphot_error_list[i] = f"{distance_gspphot_error_list[i]:06.4f}"

# process azero_gspphot
for i in range(len(azero_gspphot_list)):
    azero_gspphot_list[i] = f"{azero_gspphot_list[i]:06.4f}"

print(azero_gspphot_error_list)
# process azero_gspphot_error
for i in range(len(azero_gspphot_error_list)):
    azero_gspphot_error_list[i] = f"{azero_gspphot_error_list[i]:06.4f}"

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/solar_twins/csv/gemeas_solares_valores_arredondados.txt", "w") as text_file:
    header = ["HD", "HIP", "parallax",
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
                    "{0[1]:<7}" # HIP
                    "{0[2]:<17}" # parallax 
                    "{0[3]:<7}"
                    "{0[4]:<16}"
                    "{0[5]:<7}"
                    "{0[6]:<16}"
                    "{0[7]:<7}"
                    "{0[8]:<16}"
                    "{0[9]:<7}"
                    "{0[10]:<7}"
                    "{0[11]:<7}"
                    "{0[12]:<8}"
                    "{0[13]:<19}"
                    "{0[14]:<16}"
                    "{0[15]:<17}"
                    "{0[16]:<20}\n".format(header))

    for (HD, HIP, parallax, parallax_error,
         G, MG, MG_error,
         Bp, MBp, MBp_error,
         Rp, MRp, MRp_error,
         Bp_Rp, Bp_G, G_Rp,
         ruwe,
         phot_variable_flag,
         non_single_star,
         distance_gspphot, distance_gspphot_error,
         azero_gspphot, azero_gspphot_error) in zip(simbad_HD_list, simbad_HIP_list, parallax_list, parallax_error_list,
                                                    phot_g_mean_mag_list, MG_list, MG_error_list,
                                                    phot_bp_mean_mag_list, MBp_list, MBp_error_list,
                                                    phot_rp_mean_mag_list, MRp_list, MRp_error_list,
                                                    bp_rp_list, bp_g_list, g_rp_list,
                                                    ruwe_list,
                                                    phot_variable_flag_list,
                                                    non_single_star_list,
                                                    distance_gspphot_list, distance_gspphot_error_list,
                                                    azero_gspphot_list, azero_gspphot_error_list):
        lista = [HD[3:], HIP[4:], parallax, parallax_error,
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
                        "{0[1]:<7}" # HIP
                        "{0[2]:<8}" # parallax
                        "{0[23]:<2}" # simbolo
                        "{0[3]:<7}" # parallax_error
                        "{0[4]:<7}"
                        "{0[5]:<7}"
                        "{0[23]:<2}"
                        "{0[6]:<7}"
                        "{0[7]:<7}"
                        "{0[8]:<7}"
                        "{0[23]:<2}"
                        "{0[9]:<7}"
                        "{0[10]:<7}"
                        "{0[11]:<7}"
                        "{0[23]:<2}"
                        "{0[12]:<7}"
                        "{0[13]:<7}"
                        "{0[14]:<7}"
                        "{0[15]:<7}"
                        "{0[16]:<8}"
                        "{0[17]:<19}"
                        "{0[18]:<16}"
                        "{0[19]:<8}"
                        "{0[23]:<2}"
                        "{0[20]:<7}"
                        "{0[21]:<7}"
                        "{0[23]:<2}"
                        "{0[22]:<20}\n".format(lista))