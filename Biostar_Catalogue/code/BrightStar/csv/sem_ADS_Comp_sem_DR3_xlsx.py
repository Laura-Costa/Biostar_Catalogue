import mysql.connector
import xlsxwriter

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'BrightStar'
son_table = 'BrightStar_product'

# sheet plotadas
cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
               """trim({father_table}.simbad_parallax)+0, """
               """{father_table}.simbad_parallax_source, """
               """trim({father_table}.V)+0, """
               """trim({son_table}.MV)+0, """
               """trim({father_table}.B_V)+0, """
               """{father_table}.Name, """
               """{father_table}.simbad_SpType, """
               """{father_table}.simbad_main_identifier """
               """from {father_table}, {son_table} """
               """where {father_table}.HR = {son_table}.HR and """
               """{father_table}.ADS_Comp is null and  """
               """{father_table}.simbad_DR3 is null and """
               """{son_table}.MV is not null and """
               """{son_table}.B_V is not null""".format(father_table=father_table, son_table=son_table))

value = cursor.fetchall()

HR = []
HD = []
simbad_parallax = []
simbad_parallax_source = []
V = []
MV = []
B_V = []
Name = []
simbad_SpType = []
simbad_main_identifier = []

for (HR_value, HD_value, simbad_parallax_value, simbad_parallax_source_value, V_value, MV_value, B_V_value,
     Name_value, simbad_SpType_value, simbad_main_identifier_value) in value:
    HR.append(HR_value)
    HD.append(HD_value)
    simbad_parallax.append(simbad_parallax_value)
    simbad_parallax_source.append(simbad_parallax_source_value)
    V.append(V_value)
    MV.append(MV_value)
    B_V.append(B_V_value)
    Name.append(Name_value)
    simbad_SpType.append(simbad_SpType_value)
    simbad_main_identifier.append(simbad_main_identifier_value)

HR.insert(0, "HR")
HD.insert(0, "HD")
simbad_parallax.insert(0, "simbad_parallax")
simbad_parallax_source.insert(0, "simbad_parallax_source")
V.insert(0, "V")
MV.insert(0, "MV")
B_V.insert(0, "B_V")
Name.insert(0, "Name")
simbad_SpType.insert(0, "simbad_SpType")
simbad_main_identifier.insert(0, "simbad_main_identifier")

workbook = xlsxwriter.Workbook('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/BrightStar_estrelas_sem_ADS_Comp_e_sem_DR3.xlsx')
sheet_plotadas = workbook.add_worksheet("plotadas_no_diagrama_HR")

sheet_plotadas.write_column(0, 0, HR)
sheet_plotadas.write_column(0, 1, HD)
sheet_plotadas.write_column(0, 2, simbad_parallax)
sheet_plotadas.write_column(0, 3, simbad_parallax_source)
sheet_plotadas.write_column(0, 4, V)
sheet_plotadas.write_column(0, 5, MV)
sheet_plotadas.write_column(0, 6, B_V)
sheet_plotadas.write_column(0, 7, Name)
sheet_plotadas.write_column(0, 8, simbad_SpType)
sheet_plotadas.write_column(0, 9, simbad_main_identifier)

# sheet não plotadas
cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
               """trim({father_table}.simbad_parallax)+0, """
               """{father_table}.simbad_parallax_source, """
               """trim({father_table}.V)+0, """
               """trim({son_table}.MV)+0, """
               """trim({father_table}.B_V)+0, """
               """{father_table}.Name, """
               """{father_table}.simbad_SpType, """
               """{father_table}.simbad_main_identifier """
               """from {father_table}, {son_table} """
               """where {father_table}.HR = {son_table}.HR and """
               """{father_table}.ADS_Comp is null and  """
               """{father_table}.simbad_DR3 is null and """
               """({son_table}.MV is null or """
               """{son_table}.B_V is null)""".format(father_table=father_table, son_table=son_table))

value = cursor.fetchall()

HR = []
HD = []
simbad_parallax = []
simbad_parallax_source = []
V = []
MV = []
B_V = []
Name = []
simbad_SpType = []
simbad_main_identifier = []

for (HR_value, HD_value, simbad_parallax_value, simbad_parallax_source_value, V_value, MV_value, B_V_value,
     Name_value, simbad_SpType_value, simbad_main_identifier_value) in value:
    HR.append(HR_value)
    HD.append(HD_value)
    simbad_parallax.append(simbad_parallax_value)
    simbad_parallax_source.append(simbad_parallax_source_value)
    V.append(V_value)
    MV.append(MV_value)
    B_V.append(B_V_value)
    Name.append(Name_value)
    simbad_SpType.append(simbad_SpType_value)
    simbad_main_identifier.append(simbad_main_identifier_value)

HR.insert(0, "HR")
HD.insert(0, "HD")
simbad_parallax.insert(0, "simbad_parallax")
simbad_parallax_source.insert(0, "simbad_parallax_source")
V.insert(0, "V")
MV.insert(0, "MV")
B_V.insert(0, "B_V")
Name.insert(0, "Name")
simbad_SpType.insert(0, "simbad_SpType")
simbad_main_identifier.insert(0, "simbad_main_identifier")

sheet_plotadas = workbook.add_worksheet("nao_plotadas_no_diagrama_HR")

sheet_plotadas.write_column(0, 0, HR)
sheet_plotadas.write_column(0, 1, HD)
sheet_plotadas.write_column(0, 2, simbad_parallax)
sheet_plotadas.write_column(0, 3, simbad_parallax_source)
sheet_plotadas.write_column(0, 4, V)
sheet_plotadas.write_column(0, 5, MV)
sheet_plotadas.write_column(0, 6, B_V)
sheet_plotadas.write_column(0, 7, Name)
sheet_plotadas.write_column(0, 8, simbad_SpType)
sheet_plotadas.write_column(0, 9, simbad_main_identifier)
'''
# sheet sem HD
cursor.execute("""select {father_table}.HR, """
               """{father_table}.HD, """
               """trim({father_table}.simbad_parallax)+0, """
               """{father_table}.simbad_parallax_source, """
               """trim({father_table}.V)+0, """
               """trim({son_table}.MV)+0, """
               """trim({father_table}.B_V)+0, """
               """{father_table}.Name, """
               """{father_table}.simbad_SpType, """
               """{father_table}.simbad_name """
               """from {father_table}, {son_table} """
               """where {father_table}.HR = {son_table}.HR and """
               """{father_table}.HD is null""".format(father_table=father_table, son_table=son_table))

value = cursor.fetchall()

HR = []
HD = []
simbad_parallax = []
simbad_parallax_source = []
V = []
MV = []
B_V = []
Name = []
simbad_SpType = []
simbad_name = []

for (HR_value, HD_value, simbad_parallax_value, simbad_parallax_source_value, V_value, MV_value, B_V_value,
     Name_value, simbad_SpType_value, simbad_name_value) in value:
    HR.append(HR_value)
    HD.append(HD_value)
    simbad_parallax.append(simbad_parallax_value)
    simbad_parallax_source.append(simbad_parallax_source_value)
    V.append(V_value)
    MV.append(MV_value)
    B_V.append(B_V_value)
    Name.append(Name_value)
    simbad_SpType.append(simbad_SpType_value)
    simbad_name.append(simbad_name_value)

HR.insert(0, "HR")
HD.insert(0, "HD")
simbad_parallax.insert(0, "simbad_parallax")
simbad_parallax_source.insert(0, "simbad_parallax_source")
V.insert(0, "V")
MV.insert(0, "MV")
B_V.insert(0, "B_V")
Name.insert(0, "Name")
simbad_SpType.insert(0, "simbad_SpType")
simbad_name.insert(0, "simbad_main_identifier")

sheet_plotadas = workbook.add_worksheet("sem_HD")

sheet_plotadas.write_column(0, 0, HR)
sheet_plotadas.write_column(0, 1, HD)
sheet_plotadas.write_column(0, 2, simbad_parallax)
sheet_plotadas.write_column(0, 3, simbad_parallax_source)
sheet_plotadas.write_column(0, 4, V)
sheet_plotadas.write_column(0, 5, MV)
sheet_plotadas.write_column(0, 6, B_V)
sheet_plotadas.write_column(0, 7, Name)
sheet_plotadas.write_column(0, 8, simbad_SpType)
sheet_plotadas.write_column(0, 9, simbad_name)
'''
workbook.close()
connection.close()
cursor.close()