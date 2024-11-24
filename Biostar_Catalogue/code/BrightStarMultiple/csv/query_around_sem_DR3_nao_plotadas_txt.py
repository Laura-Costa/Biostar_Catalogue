import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("select distinct BrightStarMultiple.simbad_main_identifier, "
               "trim(BrightStarMultiple.simbad_parallax)+0, "
               "BrightStarMultiple.simbad_parallax_source, "
               "trim(BrightStarMultiple_product.simbad_MV)+0 as MV, "
               "trim(BrightStarMultiple_product.simbad_B_V)+0, "
               "BrightStarMultiple.simbad_SpType "
               "from BrightStarMultiple, BrightStarMultiple_product "
               "where BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
               "BrightStarMultiple.simbad_DR3 is null and "
               "( "
               "BrightStarMultiple_product.simbad_MV is null or "
               "BrightStarMultiple_product.simbad_B_V is null "
               ") "
               "order by MV desc")

value = cursor.fetchall()
identifier_list = []
simbad_parallax_list = []
simbad_parallax_source_list = []
MV_list = []
B_V_list = []
simbad_SpType_list = []

for (identifier_value, simbad_parallax_value, simbad_parallax_source_value, MV_value, B_V_value, simbad_SpType_value) in value:
    identifier_list.append(identifier_value)
    simbad_parallax_list.append(simbad_parallax_value)
    simbad_parallax_source_list.append(simbad_parallax_source_value)
    MV_list.append(MV_value)
    B_V_list.append(B_V_value)
    simbad_SpType_list.append(simbad_SpType_value)

# process simbad_parallax
for i in range(len(simbad_parallax_list)):
    if simbad_parallax_list[i] is not None:
        simbad_parallax_list[i] = round(simbad_parallax_list[i], 2)
        simbad_parallax_list[i] = f"{simbad_parallax_list[i]:06.2f}"

# process MV
for i in range(len(MV_list)):
    if MV_list[i] is not None:
        MV_list[i] = round(MV_list[i], 2)
        MV_list[i] = f"{MV_list[i]:04.2f}"

# process B_V
for i in range(len(B_V_list)):
    if B_V_list[i] is not None:
        sinal = None
        if B_V_list[i] >= 0:
            sinal = "+"
        B_V_list[i] = round(B_V_list[i], 2)
        B_V_list[i] = f"{B_V_list[i]:04.2f}"
        if sinal is not None:
            B_V_list[i] = sinal + B_V_list[i]

cont = 0
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/query_around_estrelas_nao_plotadas_MV_B_V.txt", "w") as text_file:
    header = ["identifier", "simbad_parallax", "simbad_parallax_source", "MV", "B_V", "simbad_SpType"]
    text_file.write("{0[0]:<33}{0[1]:<16}{0[2]:<23}{0[3]:<5}{0[4]:<6}{0[5]:<0}\n".format(header))
    for (identifier, simbad_parallax, simbad_parallax_source, MV, B_V, simbad_SpType) in zip(identifier_list, simbad_parallax_list, simbad_parallax_source_list, MV_list, B_V_list, simbad_SpType_list):
        print(identifier)
        if simbad_parallax is None:
            simbad_parallax = ""
        if simbad_parallax_source is None:
            simbad_parallax_source = ""
        if MV is None:
            MV = ""
        if B_V is None:
            B_V = ""
        if simbad_SpType is None:
            simbad_SpType = ""
        lista = [identifier, simbad_parallax, simbad_parallax_source, MV, B_V, simbad_SpType]
        text_file.write("{0[0]:<33}{0[1]:<16}{0[2]:<23}{0[3]:<5}{0[4]:<6}{0[5]:<0}\n".format(lista))
        cont += 1

print("Quantidade de estrelas nao plotadas: ", cont)

cursor.close()
connection.close()