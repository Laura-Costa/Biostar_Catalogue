import xlsxwriter
import mysql.connector

father_table = 'CAT1'
son_table = 'CAT1_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

header = ["designation", "simbad_HD",
          "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag",
          "MG", "MG_error",
          "MBp", "MBp_error",
          "MRp", "MRp_error",
          "Bp_Rp",
          "G_Rp",
          "Bp_G"]

cursor.execute("""select {father_table}.designation, """
               """{father_table}.simbad_HD, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({father_table}.phot_bp_mean_mag)+0, """
               """trim({father_table}.phot_rp_mean_mag)+0 """
               """from {father_table} """ 
               """where {father_table}.parallax >= 50.000 """.format(father_table=father_table))
value = cursor.fetchall()

designation = []
simbad_HD = []
phot_g_mean_mag = []
phot_bp_mean_mag = []
phot_rp_mean_mag = []

for (designation_value, simbad_HD_value, phot_g_mean_mag_value, phot_bp_mean_mag_value, phot_rp_mean_mag_value) in value:
    designation.append(designation_value)
    simbad_HD.append(simbad_HD_value)
    phot_g_mean_mag.append(phot_g_mean_mag_value)
    phot_bp_mean_mag.append(phot_bp_mean_mag_value)
    phot_rp_mean_mag.append(phot_rp_mean_mag)

designation.insert(0, "designation")
simbad_HD.insert(0, "simbad_HD")
phot_g_mean_mag.insert(0, "phot_g_mean_mag")

workbook = xlsxwriter.Workbook('/home/lh/Desktop/hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column(0, 0, designation)
worksheet.write_column(0, 1, simbad_HD)
worksheet.write_column(0, 2, phot_g_mean_mag)

workbook.close()