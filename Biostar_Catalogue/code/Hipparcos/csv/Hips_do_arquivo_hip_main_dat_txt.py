import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'hipparcos'
son_table = 'Hipparcos_product'

cursor.execute("select {father_table}.HIP as HIP_order "
         "from {father_table} "
         "order by cast(substring(HIP_order,4) as unsigned) asc".format(father_table=father_table))

value = cursor.fetchall()
HIP_list = []

for (HIP_value) in value:
    HIP_list.append(HIP_value)

cont = 0
print(len(HIP_list))
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/hipparcos/csv/HIP_MAIN_DAT_hips.txt", "w") as text_file:
    for (HIP,) in HIP_list:
        cont += 1
        lista = [HIP[4:]]
        text_file.write("{0[0]:<7}" # HIP
                        "\n".format(lista))

print("Quantidade de estrelas no arquivo: ", cont)

cursor.close()
connection.close()