import mysql.connector
import xlsxwriter

father_table = 'CAT1'
son_table = 'CAT1_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("""select {father_table}.designation, """
               """{father_table}.simbad_HD, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({father_table}.phot_bp_mean_mag)+0, """
               """trim({father_table}.phot_rp_mean_mag)+0, """
               """trim({son_table}.MG)+0, """
               """trim({son_table}.MG_error)+0, """
               """trim({son_table}.MBp)+0, """
               """trim({son_table}.MBp_error)+0, """
               """trim({son_table}.MRp)+0, """
               """trim({son_table}.MRp_error)+0, """
               """trim({son_table}.Bp_Rp)+0, """
               """trim({son_table}.G_Rp)+0, """
               """trim({son_table}.Bp_G)+0 """
               """from {father_table}, {son_table} """ 
               """where phot_g_mean_mag is null and """
               """{father_table}.designation = {son_table}.designation""".format(father_table=father_table, son_table=son_table))
value = cursor.fetchall()

designation = []
simbad_HD = []
phot_g_mean_mag = []
phot_bp_mean_mag = []
phot_rp_mean_mag = []
MG = []
MG_error = []
MBp = []
MBp_error = []
MRp = []
MRp_error = []
Bp_Rp = []
G_Rp = []
Bp_G = []

for (designation_value, simbad_HD_value, phot_g_mean_mag_value, phot_bp_mean_mag_value,
     phot_rp_mean_mag_value, MG_value, MG_error_value, MBp_value, MBp_error_value,
     MRp_value, MRp_error_value, Bp_Rp_value, G_Rp_value, Bp_G_value) in value:
    designation.append(designation_value)
    simbad_HD.append(simbad_HD_value)
    phot_g_mean_mag.append(phot_g_mean_mag_value)
    phot_bp_mean_mag.append(phot_bp_mean_mag_value)
    phot_rp_mean_mag.append(phot_rp_mean_mag_value)
    MG.append(MG_value)
    MG_error.append(MG_error_value)
    MBp.append(MBp_value)
    MBp_error.append(MBp_error_value)
    MRp.append(MRp_value)
    MRp_error.append(MRp_error_value)
    Bp_Rp.append(Bp_Rp_value)
    G_Rp.append(G_Rp_value)
    Bp_G.append(Bp_G_value)

designation.insert(0, "designation")
simbad_HD.insert(0, "simbad_HD")
phot_g_mean_mag.insert(0, "phot_g_mean_mag")
phot_bp_mean_mag.insert(0, "phot_bp_mean_mag")
phot_rp_mean_mag.insert(0, "phot_rp_mean_mag")
MG.insert(0, "MG")
MG_error.insert(0, "MG_error")
MBp.insert(0, "MBp")
MBp_error.insert(0, "MBp_error")
MRp.insert(0, "MRp")
MRp_error.insert(0, "MRp_error")
Bp_Rp.insert(0, "Bp_Rp")
G_Rp.insert(0, "G_Rp")
Bp_G.insert(0, "Bp_G")

workbook = xlsxwriter.Workbook('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/csv/CAT1_estrelas_sem_G_e_estrelas_sem_Bp_Rp.xlsx')
sheet_sem_G = workbook.add_worksheet("sem_G")

sheet_sem_G.write_column(0, 0, designation)
sheet_sem_G.write_column(0, 1, simbad_HD)
sheet_sem_G.write_column(0, 2, phot_g_mean_mag)
sheet_sem_G.write_column(0, 3, phot_bp_mean_mag)
sheet_sem_G.write_column(0, 4, phot_rp_mean_mag)
sheet_sem_G.write_column(0, 5, MG)
sheet_sem_G.write_column(0, 6, MG_error)
sheet_sem_G.write_column(0, 7, MBp)
sheet_sem_G.write_column(0, 8, MBp_error)
sheet_sem_G.write_column(0, 9, MRp)
sheet_sem_G.write_column(0, 10, MRp_error)
sheet_sem_G.write_column(0, 11, Bp_Rp)
sheet_sem_G.write_column(0, 12, G_Rp)
sheet_sem_G.write_column(0, 13, Bp_G)

cursor.execute("""select {father_table}.designation, """
               """{father_table}.simbad_HD, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({father_table}.phot_bp_mean_mag)+0, """
               """trim({father_table}.phot_rp_mean_mag)+0, """
               """trim({son_table}.MG)+0, """
               """trim({son_table}.MG_error)+0, """
               """trim({son_table}.MBp)+0, """
               """trim({son_table}.MBp_error)+0, """
               """trim({son_table}.MRp)+0, """
               """trim({son_table}.MRp_error)+0, """
               """trim({son_table}.Bp_Rp)+0, """
               """trim({son_table}.G_Rp)+0, """
               """trim({son_table}.Bp_G)+0 """
               """from {father_table}, {son_table} """ 
               """where {son_table}.Bp_Rp is null and """
               """{father_table}.designation = {son_table}.designation""".format(father_table=father_table, son_table=son_table))
value = cursor.fetchall()

designation = []
simbad_HD = []
phot_g_mean_mag = []
phot_bp_mean_mag = []
phot_rp_mean_mag = []
MG = []
MG_error = []
MBp = []
MBp_error = []
MRp = []
MRp_error = []
Bp_Rp = []
G_Rp = []
Bp_G = []

for (designation_value, simbad_HD_value, phot_g_mean_mag_value, phot_bp_mean_mag_value,
     phot_rp_mean_mag_value, MG_value, MG_error_value, MBp_value, MBp_error_value,
     MRp_value, MRp_error_value, Bp_Rp_value, G_Rp_value, Bp_G_value) in value:
    designation.append(designation_value)
    simbad_HD.append(simbad_HD_value)
    phot_g_mean_mag.append(phot_g_mean_mag_value)
    phot_bp_mean_mag.append(phot_bp_mean_mag_value)
    phot_rp_mean_mag.append(phot_rp_mean_mag_value)
    MG.append(MG_value)
    MG_error.append(MG_error_value)
    MBp.append(MBp_value)
    MBp_error.append(MBp_error_value)
    MRp.append(MRp_value)
    MRp_error.append(MRp_error_value)
    Bp_Rp.append(Bp_Rp_value)
    G_Rp.append(G_Rp_value)
    Bp_G.append(Bp_G_value)

designation.insert(0, "designation")
simbad_HD.insert(0, "simbad_HD")
phot_g_mean_mag.insert(0, "phot_g_mean_mag")
phot_bp_mean_mag.insert(0, "phot_bp_mean_mag")
phot_rp_mean_mag.insert(0, "phot_rp_mean_mag")
MG.insert(0, "MG")
MG_error.insert(0, "MG_error")
MBp.insert(0, "MBp")
MBp_error.insert(0, "MBp_error")
MRp.insert(0, "MRp")
MRp_error.insert(0, "MRp_error")
Bp_Rp.insert(0, "Bp_Rp")
G_Rp.insert(0, "G_Rp")
Bp_G.insert(0, "Bp_G")

sheet_sem_Bp_Rp = workbook.add_worksheet("sem_Bp_Rp")

sheet_sem_Bp_Rp.write_column(0, 0, designation)
sheet_sem_Bp_Rp.write_column(0, 1, simbad_HD)
sheet_sem_Bp_Rp.write_column(0, 2, phot_g_mean_mag)
sheet_sem_Bp_Rp.write_column(0, 3, phot_bp_mean_mag)
sheet_sem_Bp_Rp.write_column(0, 4, phot_rp_mean_mag)
sheet_sem_Bp_Rp.write_column(0, 5, MG)
sheet_sem_Bp_Rp.write_column(0, 6, MG_error)
sheet_sem_Bp_Rp.write_column(0, 7, MBp)
sheet_sem_Bp_Rp.write_column(0, 8, MBp_error)
sheet_sem_Bp_Rp.write_column(0, 9, MRp)
sheet_sem_Bp_Rp.write_column(0, 10, MRp_error)
sheet_sem_Bp_Rp.write_column(0, 11, Bp_Rp)
sheet_sem_Bp_Rp.write_column(0, 12, G_Rp)
sheet_sem_Bp_Rp.write_column(0, 13, Bp_G)

workbook.close()
connection.close()
cursor.close()





