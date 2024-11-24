import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = "Supplement"
father_table_key_column = "ordinal_number"
son_table = "Supplement_product"
son_table_key_column = "ordinal_number"
y_axis = "MV"
x_axis = "B_V"

cursor.execute("select {father_table}.HD, "
               "trim({father_table}.simbad_parallax)+0, "
               "{father_table}.simbad_parallax_source, "
               "trim({father_table}.V)+0, "
               "trim({son_table}.{y_axis})+0, "
               "trim({son_table}.{x_axis})+0, "
               "{father_table}.simbad_SpType "
               "from {father_table}, {son_table} "
               "where {father_table}.{father_table_key_column} = {son_table}.{son_table_key_column} and "
               "{father_table}.simbad_DR3 is null and "
               "{father_table}.simbad_HIP is null and "
               "{father_table}.HD_Suffix is null".format(y_axis=y_axis,
                                                         x_axis=x_axis,
                                                         father_table=father_table,
                                                         father_table_key_column=father_table_key_column,
                                                         son_table=son_table,
                                                         son_table_key_column=son_table_key_column))

value = cursor.fetchall()
HD_list = []
simbad_parallax_list = []
simbad_parallax_source_list = []
V_list = []
MV_list = []
B_V_list = []
simbad_SpType_list = []

for (HD_value, simbad_parallax_value, simbad_parallax_source_value, V, MV_value, B_V_value, simbad_SpType_value) in value:
    HD_list.append(HD_value)
    simbad_parallax_list.append(simbad_parallax_value)
    simbad_parallax_source_list.append(simbad_parallax_source_value)
    V_list.append(V)
    MV_list.append(MV_value)
    B_V_list.append(B_V_value)
    simbad_SpType_list.append(simbad_SpType_value)

# process simbad_parallax
for i in range(len(simbad_parallax_list)):
    if simbad_parallax_list[i] is not None:
        simbad_parallax_list[i] = round(simbad_parallax_list[i], 2)
        simbad_parallax_list[i] = f"{simbad_parallax_list[i]:05.2f}"

# process V
for i in range(len(V_list)):
    if V_list[i] is not None:
        V_list[i] = round(V_list[i], 2)
        V_list[i] = f"{V_list[i]:04.2f}"

# process MV
for i in range(len(MV_list)):
    if MV_list[i] is not None:
        MV_list[i] = round(MV_list[i], 2)
        MV_list[i] = f"{MV_list[i]:04.2f}"

# process B_V
for i in range(len(B_V_list)):
    if B_V_list[i] is not None:
        B_V_list[i] = round(B_V_list[i], 2)
        B_V_list[i] = f"{B_V_list[i]:04.2f}"

cont = 0
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Supplement/csv/estrelas_sem_dr3_e_sem_hip.txt", "w") as text_file:
    header = ["HD", "simbad_parallax", "simbad_parallax_source", "V", "MV", "B_V", "simbad_SpType"]
    text_file.write("{0[0]:<7}{0[1]:<16}{0[2]:<23}{0[3]:<5}{0[4]:<6}{0[5]:<6}{0[6]:<13}\n".format(header))
    for (HD, simbad_parallax, simbad_parallax_source, V, MV, B_V, simbad_SpType) in zip(HD_list, simbad_parallax_list, simbad_parallax_source_list, V_list, MV_list, B_V_list, simbad_SpType_list):
        if simbad_parallax is None:
            simbad_parallax = ""
        if simbad_parallax_source is None:
            simbad_parallax_source = ""
        if V is None:
            V = ""
        if MV is None:
            MV = ""
        if B_V is None:
            B_V = ""
        if simbad_SpType is None:
            simbad_SpType = ""

        if B_V != "" and B_V[0] != "-":
            B_V = "+" + B_V

        lista = [HD[3:], simbad_parallax, simbad_parallax_source, V, MV, B_V, simbad_SpType]
        text_file.write("{0[0]:<7}{0[1]:<16}{0[2]:<23}{0[3]:<5}{0[4]:<6}{0[5]:<6}{0[6]:<13}\n".format(lista))
        cont += 1

print("Quantidade de estrelas nao plotadas: ", cont)

cursor.close()
connection.close()