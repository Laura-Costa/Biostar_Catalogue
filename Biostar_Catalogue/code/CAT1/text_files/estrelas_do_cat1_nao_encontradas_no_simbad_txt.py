import mysql.connector

father_table = 'view_CAT1'
son_table = 'Gaia_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("select {father_table}.designation as designation_order, "
               "trim({father_table}.parallax)+0, "
               "trim({father_table}.parallax_error)+0, "
               "trim({father_table}.phot_g_mean_mag)+0, "
               "trim({father_table}.phot_bp_mean_mag)+0, "
               "trim({father_table}.phot_rp_mean_mag)+0, "
               "trim({father_table}.bp_rp)+0, "
               "trim({father_table}.bp_g)+0, "
               "trim({father_table}.g_rp)+0 "
               "from {father_table}, {son_table} "
               "where {father_table}.designation = {son_table}.designation and "
               "in_simbad = 0 "
               "order by cast(substring(designation_order, 9) as unsigned) asc".format(father_table=father_table,
                                                                                       son_table=son_table))

value = cursor.fetchall()

designation_list = []
parallax_list = []
parallax_error_list = []
phot_g_mean_mag_list = []
phot_bp_mean_mag_list = []
phot_rp_mean_mag_list = []
bp_rp_list = []
bp_g_list = []
g_rp_list = []


for (designation_value,
    parallax_value, parallax_error_value,
    phot_g_mean_mag_value, phot_bp_mean_mag_value, phot_rp_mean_mag_value,
    bp_rp_value, bp_g_value, g_rp_value) in value:

    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    parallax_error_list.append(parallax_error_value)
    phot_g_mean_mag_list.append(phot_g_mean_mag_value)
    phot_bp_mean_mag_list.append(phot_bp_mean_mag_value)
    phot_rp_mean_mag_list.append(phot_rp_mean_mag_value)
    bp_rp_list.append(bp_rp_value)
    bp_g_list.append(bp_g_value)
    g_rp_list.append(g_rp_value)

# process parallax
for i in range(len(parallax_list)):
    if parallax_list[i] is not None:
        parallax_list[i] = round(parallax_list[i], 5)
        parallax_list[i] = f"{parallax_list[i]:09.5f}"

# process parallax_error
for i in range(len(parallax_error_list)):
    if parallax_error_list[i] is not None:
        parallax_error_list[i] = round(parallax_error_list[i], 5)
        parallax_error_list[i] = f"{parallax_error_list[i]:07.5f}"

# process phot_g_mean_mag
for i in range(len(phot_g_mean_mag_list)):
    if phot_g_mean_mag_list[i] is not None:
        phot_g_mean_mag_list[i] = round(phot_g_mean_mag_list[i], 5)
        phot_g_mean_mag_list[i] = f"{phot_g_mean_mag_list[i]:08.5f}"

# process phot_bp_mean_mag
for i in range(len(phot_bp_mean_mag_list)):
    if phot_bp_mean_mag_list[i] is not None:
        phot_bp_mean_mag_list[i] = round(phot_bp_mean_mag_list[i], 5)
        phot_bp_mean_mag_list[i] = f"{phot_bp_mean_mag_list[i]:08.5f}"

# process phot_rp_mean_mag
for i in range(len(phot_rp_mean_mag_list)):
    if phot_rp_mean_mag_list[i] is not None:
        phot_rp_mean_mag_list[i] = round(phot_rp_mean_mag_list[i], 5)
        phot_rp_mean_mag_list[i] = f"{phot_rp_mean_mag_list[i]:08.5f}"

with open("/output_files/CAT1/text_files/estrelas_do_cat1_nao_encontradas_no_simbad.txt", "w") as text_file:
    header = ["designation", "parallax ± parallax_error", "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag"]
    text_file.write("{0[0]:<29}" # designation
                    "{0[1]:<26}" # parallax +/- parallax_error
                    "{0[2]:<16}" # phot_g_mean_mag
                    "{0[3]:<17}" # phot_bp_mean_mag
                    "{0[4]:<0}" # phot_rp_mean_mag
                    "\n".format(header))
    for (designation, parallax, parallax_error, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag) in zip(designation_list, parallax_list, parallax_error_list, phot_g_mean_mag_list, phot_bp_mean_mag_list, phot_rp_mean_mag_list):

        if phot_g_mean_mag is None:
            phot_g_mean_mag = ""

        if phot_bp_mean_mag is None:
            phot_bp_mean_mag = ""

        if phot_rp_mean_mag is None:
            phot_rp_mean_mag = ""

        mais_ou_menos = ""
        if parallax_error != "":
            mais_ou_menos = "±"

        lista = [designation, parallax, parallax_error, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, mais_ou_menos]

        text_file.write("{0[0]:<29}" # designation
                        "{0[1]:<10}" # parallax
                        "{0[6]:<2}" # +/-
                        "{0[2]:<14}" # parallax_error
                        "{0[3]:<16}" # phot_g_mean_mag
                        "{0[4]:<17}" # phot_bp_mean_mag
                        "{0[5]:<0}" # phot_rp_mean_mag
                        "\n".format(lista))