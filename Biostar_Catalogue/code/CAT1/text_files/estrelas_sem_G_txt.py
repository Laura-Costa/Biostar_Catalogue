import mysql.connector

father_table = 'gaia'
son_table = 'Gaia_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("select {father_table}.designation as designation_order, "
               "trim({father_table}.parallax)+0, "
               "trim({father_table}.parallax_error)+0, "
               "trim({father_table}.phot_bp_mean_mag)+0, "
               "trim({father_table}.phot_rp_mean_mag)+0, "
               "trim({father_table}.bp_rp)+0 "
               "from {father_table}, {son_table} "
               "where {father_table}.designation = {son_table}.designation and "
               "{father_table}.parallax + 3*{father_table}.parallax_error >= 50.000 and "
               "{father_table}.phot_g_mean_mag is null "
               "order by cast(substring(designation_order, 9) as unsigned) asc".format(father_table=father_table,
                                                                                       son_table=son_table))

value = cursor.fetchall()

designation_list = []
parallax_list = []
parallax_error_list = []
phot_bp_mean_mag_list = []
phot_rp_mean_mag_list = []
bp_rp_list = []


for (designation_value,
    parallax_value, parallax_error_value,
    phot_bp_mean_mag_value, phot_rp_mean_mag_value,
    bp_rp_value) in value:

    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    parallax_error_list.append(parallax_error_value)
    phot_bp_mean_mag_list.append(phot_bp_mean_mag_value)
    phot_rp_mean_mag_list.append(phot_rp_mean_mag_value)
    bp_rp_list.append(bp_rp_value)

# process parallax
for i in range(len(parallax_list)):
    if parallax_list[i] is not None:
        parallax_list[i] = round(parallax_list[i], 5)
        parallax_list[i] = f"{parallax_list[i]:09.5f}"

# process parallax_error
for i in range(len(parallax_error_list)):
    if parallax_error_list[i] is not None:
        parallax_error_list[i] = round(parallax_error_list[i], 5)
        parallax_error_list[i] = f"{parallax_error_list[i]:7.5f}"

# process phot_bp_mean_mag
for i in range(len(phot_bp_mean_mag_list)):
    if phot_bp_mean_mag_list[i] is not None:
        phot_bp_mean_mag_list[i] = round(phot_bp_mean_mag_list[i], 5)
        phot_bp_mean_mag_list[i] = f"{phot_bp_mean_mag_list[i]:7.5f}"

# process phot_rp_mean_mag
for i in range(len(phot_rp_mean_mag_list)):
    if phot_rp_mean_mag_list[i] is not None:
        phot_rp_mean_mag_list[i] = round(phot_rp_mean_mag_list[i], 5)
        phot_rp_mean_mag_list[i] = f"{phot_rp_mean_mag_list[i]:08.5f}"

# process bp_rp
for i in range(len(bp_rp_list)):
    if bp_rp_list[i] is not None:
        bp_rp_list[i] = round(bp_rp_list[i], 5)
        bp_rp_list[i] = f"{bp_rp_list[i]:7.5f}"

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/text_files/estrelas_sem_G.txt", "w") as text_file:
    header = ["designation", "parallax ± parallax_error",
              "phot_bp_mean_mag", "phot_rp_mean_mag",
              "bp_rp"]
    text_file.write("{0[0]:<29}" # designation
                    "{0[1]:<26}" # parallax ± parallax_error
                    "{0[2]:<17}" # phot_bp_mean_mag
                    "{0[3]:<17}" # phot_rp_mean_mag
                    "{0[4]:<0}" # bp_rp
                    "\n".format(header))
    for (designation, parallax, parallax_error, phot_bp_mean_mag, phot_rp_mean_mag, bp_rp) in zip(designation_list, parallax_list, parallax_error_list, phot_bp_mean_mag_list, phot_rp_mean_mag_list, bp_rp_list):

        if parallax is None:
            parallax = ""

        if parallax_error is None:
            parallax_error = ""

        mais_ou_menos = ""
        if parallax_error != "":
            mais_ou_menos = "±"

        if phot_bp_mean_mag is None:
            phot_bp_mean_mag = ""

        if phot_rp_mean_mag is None:
            phot_rp_mean_mag = ""

        if bp_rp is None:
            bp_rp = ""

        lista = [designation, parallax, mais_ou_menos, parallax_error, phot_bp_mean_mag, phot_rp_mean_mag, bp_rp]

        text_file.write("{0[0]:<29}" # designation
                        "{0[1]:<10}" # parallax
                        "{0[2]:<2}" # sinal
                        "{0[3]:<14}" # parallax_error
                        "{0[4]:<17}" # phot_bp_mean_mag
                        "{0[5]:<17}" # phot_rp_mean_mag
                        "{0[6]:<0}" # bp_rp
                        "\n".format(lista))