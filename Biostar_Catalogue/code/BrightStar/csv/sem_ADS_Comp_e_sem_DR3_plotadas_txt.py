import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'BrightStar'
son_table = 'BrightStar_product'

cursor.execute("select {father_table}.HD as HD, "
               "trim({father_table}.simbad_parallax)+0, "
               "{father_table}.simbad_parallax_source, "
               "trim({son_table}.MV)+0, "
               "trim({father_table}.B_V)+0, "
               "{father_table}.simbad_SpType "
               "from {father_table}, {son_table} "
               "where {father_table}.HR = {son_table}.HR and "
               "{father_table}.ADS_Comp is null and  "
               "{father_table}.simbad_DR3 is null and "
               "{son_table}.MV is not null and "
               "{son_table}.B_V is not null "
               "order by cast(substring(HD,3) as unsigned) asc".format(father_table=father_table, son_table=son_table))

value = cursor.fetchall()
HD_list = []
simbad_parallax_list = []
simbad_parallax_source_list = []
MV_list = []
B_V_list = []
simbad_SpType_list = []

for (HD_value, simbad_parallax_value, simbad_parallax_source_value, MV_value, B_V_value, simbad_SpType_value) in value:
    HD_list.append(HD_value)
    simbad_parallax_list.append(simbad_parallax_value)
    simbad_parallax_source_list.append(simbad_parallax_source_value)
    MV_list.append(MV_value)
    B_V_list.append(B_V_value)
    simbad_SpType_list.append(simbad_SpType_value)

# process simbad_parallax
for i in range(len(simbad_parallax_list)):
    simbad_parallax_list[i] = round(simbad_parallax_list[i], 2)
    simbad_parallax_list[i] = f"{simbad_parallax_list[i]:05.2f}"

# process MV
for i in range(len(MV_list)):
    sinal = None
    if MV_list[i] < 0:
        sinal = "-"
    else:
        sinal = "+"

    MV_list[i] = abs(MV_list[i])
    MV_list[i] = round(MV_list[i], 2)
    MV_list[i] = f"{MV_list[i]:05.2f}"
    if sinal != None:
        MV_list[i] = sinal + MV_list[i]

# process B_V
for i in range(len(B_V_list)):
    sinal = None
    if B_V_list[i] >= 0:
        sinal = "+"
    B_V_list[i] = round(B_V_list[i], 2)
    B_V_list[i] = f"{B_V_list[i]:04.2f}"
    if sinal is not None:
        B_V_list[i] = sinal + B_V_list[i]

cont = 0
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/estrelas_plotadas_MV_B_V.txt", "w") as text_file:
    header = ["HD", "simbad_parallax", "simbad_parallax_source", "MV", "B_V", "simbad_SpType"]
    text_file.write("{0[0]:<7}{0[1]:<16}{0[2]:<23}{0[3]:<7}{0[4]:<6}{0[5]:<0}\n".format(header))
    for (HD, simbad_parallax, simbad_parallax_source, MV, B_V, simbad_SpType) in zip(HD_list, simbad_parallax_list, simbad_parallax_source_list, MV_list, B_V_list, simbad_SpType_list):
        if simbad_SpType is None:
            simbad_SpType = ""

        lista = [HD[3:], simbad_parallax, simbad_parallax_source, MV, B_V, simbad_SpType]
        text_file.write("{0[0]:<7}{0[1]:<16}{0[2]:<23}{0[3]:<7}{0[4]:<6}{0[5]:<0}\n".format(lista))
        cont += 1

print("Quantidade de estrelas plotadas: ", cont)

cursor.close()
connection.close()