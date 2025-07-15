import mysql.connector

father_table = 'gaia'
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

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/solar_twins/csv/gemeas_solares.txt", "w") as text_file:
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
                    "{0[2]:<33}" # parallax
                    "{0[3]:<10}" # G
                    "{0[4]:<43}" # MG
                    "{0[5]:<10}" # Bp
                    "{0[6]:<42}" # MBp
                    "{0[7]:<10}" # Rp
                    "{0[8]:<43}" # MRp
                    "{0[9]:<11}" # Bp_Rp
                    "{0[10]:<11}" # Bp_G
                    "{0[11]:<11}" # G_Rp
                    "{0[12]:<11}" # ruwe
                    "{0[13]:<20}" # phot_variable_flag
                    "{0[14]:<16}" # non_single_star
                    "{0[15]:<31}" # distance_gspphot
                    "{0[16]:<20}" # azero_gspphot
                    "\n".format(header))

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
        text_file.write("{0[0]:<7}"  # HD
                        "{0[1]:<7}"  # HIP
                        "{0[2]:<19}" # parallax
                        "{0[23]:<2}" # sinal
                        "{0[3]:<12}"  # parallax_error
                        "{0[4]:<10}"  # G
                        "{0[5]:<19}"  #  MG
                        "{0[23]:<2}" # sinal
                        "{0[6]:<22}" # MG_error
                        "{0[7]:<10}" # Bp
                        "{0[8]:<18}" # MBp
                        "{0[23]:<2}" # sinal
                        "{0[9]:<22}" # MBp_error
                        "{0[10]:<10}" # Rp
                        "{0[11]:<19}" # MRp
                        "{0[23]:<2}" # sinal
                        "{0[12]:<22}" # MRp_error
                        "{0[13]:<11}" # Bp_Rp
                        "{0[14]:<11}" # Bp_G
                        "{0[15]:<11}" # G_Rp
                        "{0[16]:<11}" # ruwe
                        "{0[17]:<20}" # phot_variable_flag
                        "{0[18]:<16}" # non_single_star
                        "{0[19]:<8}" # distance_gspphot
                        "{0[23]:<2}" # sinal
                        "{0[20]:<21}" # distance_gspphot_error
                        "{0[21]:<7}" # azero_gspphot
                        "{0[23]:<2}" # sinal
                        "{0[22]:<21}" # azero_gspphot_error
                        "\n".format(lista))