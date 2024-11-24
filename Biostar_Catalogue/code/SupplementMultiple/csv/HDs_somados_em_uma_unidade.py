import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

y_axis = "MV"
x_axis = "B_V"

cursor.execute("select SupplementMultiple.simbad_HD as HD, "
               "trim(SupplementMultiple.simbad_parallax)+0, "
               "SupplementMultiple.simbad_parallax_source, "
               "trim(SupplementMultiple_product.simbad_{y_axis})+0, "
               "trim(SupplementMultiple_product.simbad_{x_axis})+0, "
               "SupplementMultiple.simbad_SpType "
               "from Supplement, SupplementMultiple, SupplementMultiple_product "
               "where Supplement.ordinal_number = SupplementMultiple.ordinal_number_Supplement and "
               "SupplementMultiple.ordinal_number = SupplementMultiple_product.ordinal_number and "
               "Supplement.HD_Suffix like '%/%' "
               "order by cast(substring(HD,3) as unsigned) asc".format(x_axis=x_axis, y_axis=y_axis))

value = cursor.fetchall()
simbad_HD_list = []
simbad_parallax_list = []
simbad_parallax_source_list = []
simbad_MV_list = []
simbad_B_V_list = []
simbad_SpType_list = []

for (simbad_HD_value, simbad_parallax_value, simbad_parallax_source_value, simbad_MV_value, simbad_B_V_value, simbad_SpType_value) in value:
    simbad_HD_list.append(simbad_HD_value)
    simbad_parallax_list.append(simbad_parallax_value)
    simbad_parallax_source_list.append(simbad_parallax_source_value)
    simbad_MV_list.append(simbad_MV_value)
    simbad_B_V_list.append(simbad_B_V_value)
    simbad_SpType_list.append(simbad_SpType_value)

# process simbad_parallax
for i in range(len(simbad_parallax_list)):
    if simbad_parallax_list[i] is not None:
        simbad_parallax_list[i] = round(simbad_parallax_list[i], 2)
        simbad_parallax_list[i] = f"{simbad_parallax_list[i]:06.2f}"

# process MV
for i in range(len(simbad_MV_list)):
    if simbad_MV_list[i] is not None:
        sinal = None
        if simbad_MV_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        simbad_MV_list[i] = abs(simbad_MV_list[i])
        simbad_MV_list[i] = round(simbad_MV_list[i], 2)
        simbad_MV_list[i] = f"{simbad_MV_list[i]:04.2f}"
        simbad_MV_list[i] = sinal + simbad_MV_list[i]

# process B_V
for i in range(len(simbad_B_V_list)):
    if simbad_B_V_list[i] is not None:
        sinal = None
        if simbad_B_V_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        simbad_B_V_list[i] = abs(simbad_B_V_list[i])
        simbad_B_V_list[i] = round(simbad_B_V_list[i], 2)
        simbad_B_V_list[i] = f"{simbad_B_V_list[i]:04.2f}"
        simbad_B_V_list[i] = sinal + simbad_B_V_list[i]

cont = 0
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/SupplementMultiple/csv/HDs_somados_em_uma_unidade.txt", "w") as text_file:
    header = ["simbad_HD", "simbad_parallax", "simbad_parallax_source", "simbad_MV", "simbad_B_V", "simbad_SpType"]
    text_file.write("{0[0]:<10}{0[1]:<16}{0[2]:<23}{0[3]:<10}{0[4]:<11}{0[5]:<11}\n".format(header))
    for (simbad_HD, simbad_parallax, simbad_parallax_source, simbad_MV, simbad_B_V, simbad_SpType) in zip(simbad_HD_list, simbad_parallax_list, simbad_parallax_source_list, simbad_MV_list, simbad_B_V_list, simbad_SpType_list):
        if simbad_HD is None:
            simbad_HD = ""
        if simbad_parallax is None:
            simbad_parallax = ""
        if simbad_parallax_source is None:
            simbad_parallax_source = ""
        if simbad_MV is None:
            simbad_MV = ""
        if simbad_B_V is None:
            simbad_B_V = ""
        if simbad_SpType is None:
            simbad_SpType = ""
        lista = [simbad_HD[3:], simbad_parallax, simbad_parallax_source, simbad_MV, simbad_B_V, simbad_SpType]
        text_file.write("{0[0]:<10}{0[1]:<16}{0[2]:<23}{0[3]:<10}{0[4]:<11}{0[5]:<11}\n".format(lista))
        cont += 1

print("Quantidade de estrelas no arquivo: ", cont)

cursor.close()
connection.close()