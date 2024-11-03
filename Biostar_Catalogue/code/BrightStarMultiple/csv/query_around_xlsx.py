import mysql.connector
import xlsxwriter

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

# sheet plotadas
cursor.execute("""select distinct BrightStarMultiple.simbad_main_identifier, """
               """trim(BrightStarMultiple.simbad_parallax)+0, """
               """BrightStarMultiple.simbad_parallax_source, """
               """trim(BrightStarMultiple.simbad_V)+0, """
               """trim(BrightStarMultiple_product.simbad_MV)+0, """
               """trim(BrightStarMultiple_product.simbad_B_V)+0, """
               """BrightStarMultiple.simbad_SpType """
               """from BrightStarMultiple, BrightStarMultiple_product """
               """where BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and """
               """BrightStarMultiple.simbad_DR3 is null and """
               """BrightStarMultiple_product.simbad_MV is not null and """
               """BrightStarMultiple_product.simbad_B_V is not null""")

value = cursor.fetchall()

simbad_main_identifier = []
simbad_parallax = []
simbad_parallax_source = []
simbad_V = []
simbad_MV = []
simbad_B_V = []
simbad_SpType = []

for (simbad_main_identifier_value, simbad_parallax_value, simbad_parallax_source_value, simbad_V_value,
     simbad_MV_value, simbad_B_V_value, simbad_SpType_value) in value:
    simbad_main_identifier.append(simbad_main_identifier_value)
    simbad_parallax.append(simbad_parallax_value)
    simbad_parallax_source.append(simbad_parallax_source_value)
    simbad_V.append(simbad_V_value)
    simbad_MV.append(simbad_MV_value)
    simbad_B_V.append(simbad_B_V_value)
    simbad_SpType.append(simbad_SpType_value)

simbad_main_identifier.insert(0, "simbad_main_identifier")
simbad_parallax.insert(0, "simbad_parallax")
simbad_parallax_source.insert(0, "simbad_parallax_source")
simbad_V.insert(0, "simbad_V")
simbad_MV.insert(0, "simbad_MV")
simbad_B_V.insert(0, "simbad_B_V")
simbad_SpType.insert(0, "simbad_SpType")

workbook = xlsxwriter.Workbook('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/BrightStar_estrelas_do_query_around_sem_DR3.xlsx')
sheet_plotadas = workbook.add_worksheet("plotadas_no_diagrama_HR")

sheet_plotadas.write_column(0, 0, simbad_main_identifier)
sheet_plotadas.write_column(0, 1, simbad_parallax)
sheet_plotadas.write_column(0, 2, simbad_parallax_source)
sheet_plotadas.write_column(0, 3, simbad_V)
sheet_plotadas.write_column(0, 4, simbad_MV)
sheet_plotadas.write_column(0, 5, simbad_B_V)
sheet_plotadas.write_column(0, 6, simbad_SpType)

# sheet não plotadas
cursor.execute("""select distinct BrightStarMultiple.simbad_main_identifier, """
               """trim(BrightStarMultiple.simbad_parallax)+0, """
               """BrightStarMultiple.simbad_parallax_source, """
               """trim(BrightStarMultiple.simbad_V)+0, """
               """trim(BrightStarMultiple_product.simbad_MV)+0, """
               """trim(BrightStarMultiple_product.simbad_B_V)+0, """
               """BrightStarMultiple.simbad_SpType """
               """from BrightStarMultiple, BrightStarMultiple_product """
               """where BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and """
               """BrightStarMultiple.simbad_DR3 is null and """
               """(BrightStarMultiple_product.simbad_MV is null or """
               """BrightStarMultiple_product.simbad_B_V is null)""")

value = cursor.fetchall()

simbad_main_identifier = []
simbad_parallax = []
simbad_parallax_source = []
simbad_V = []
simbad_MV = []
simbad_B_V = []
simbad_SpType = []

for (simbad_main_identifier_value, simbad_parallax_value, simbad_parallax_source_value, simbad_V_value,
     simbad_MV_value, simbad_B_V_value, simbad_SpType_value) in value:
    simbad_main_identifier.append(simbad_main_identifier_value)
    simbad_parallax.append(simbad_parallax_value)
    simbad_parallax_source.append(simbad_parallax_source_value)
    simbad_V.append(simbad_V_value)
    simbad_MV.append(simbad_MV_value)
    simbad_B_V.append(simbad_B_V_value)
    simbad_SpType.append(simbad_SpType_value)

simbad_main_identifier.insert(0, "simbad_main_identifier")
simbad_parallax.insert(0, "simbad_parallax")
simbad_parallax_source.insert(0, "simbad_parallax_source")
simbad_V.insert(0, "simbad_V")
simbad_MV.insert(0, "simbad_MV")
simbad_B_V.insert(0, "simbad_B_V")
simbad_SpType.insert(0, "simbad_SpType")

sheet_plotadas = workbook.add_worksheet("nao_plotadas_no_diagrama_HR")

sheet_plotadas.write_column(0, 0, simbad_main_identifier)
sheet_plotadas.write_column(0, 1, simbad_parallax)
sheet_plotadas.write_column(0, 2, simbad_parallax_source)
sheet_plotadas.write_column(0, 3, simbad_V)
sheet_plotadas.write_column(0, 4, simbad_MV)
sheet_plotadas.write_column(0, 5, simbad_B_V)
sheet_plotadas.write_column(0, 6, simbad_SpType)

workbook.close()
connection.close()
cursor.close()