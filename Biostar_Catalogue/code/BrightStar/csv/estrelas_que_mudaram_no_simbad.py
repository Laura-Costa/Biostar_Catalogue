import mysql.connector

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

# pegar as estrelas atuais no banco de dados
cursor.execute("select trim(substring(HD, 3)) "
               "from BrightStar "
               "where ADS_Comp is null and "
               "simbad_DR3 is null and "
               "simbad_parallax is not null and "
               "B_V is not null and "
               "V is not null")

value = cursor.fetchall()
hd_list = []
for (hd_value,) in value:
    hd_list.append(hd_value)

hds_que_mudaram_no_simbad = []
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/estrelas_plotadas_MV_B_V.txt") as file:
    next(file) # pular o header
    for line in file:
        line = line.split(" ")
        hd = line[0]

        if hd not in hd_list:
            hds_que_mudaram_no_simbad.append(hd)
    file.close()

hds_que_mudaram_no_simbad = list(map(int, hds_que_mudaram_no_simbad))
hds_que_mudaram_no_simbad.sort()
print(hds_que_mudaram_no_simbad)

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStar/csv/estrelas_que_mudaram_no_simbad_MV_B_V.txt", "w") as file:
    for hd in hds_que_mudaram_no_simbad:
        file.write("{}\n".format(hd))
    file.close()





###############################################################################################################
# pegar as estrelas atuais resultantes do query around sem simbad_DR3, com simbad_parallax, simbad_B e simbad_V
###############################################################################################################
cursor.execute("select distinct simbad_main_identifier "
               "from BrightStarMultiple "
               "where simbad_DR3 is null and "
               "simbad_parallax is not null and "
               "simbad_B is not null and "
               "simbad_V is not null")

value = cursor.fetchall()
simbad_main_identifier_list = []

for (simbad_main_identifier_value, ) in value:
    simbad_main_identifier_list.append(simbad_main_identifier_value)

simbad_main_identifiers_que_mudaram_no_simbad = []
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/query_around_estrelas_plotadas_MV_B_V.txt") as file:
    next(file) # pular o header
    for line in file:
        line = line[0:12]
        simbad_main_identifier = line.strip()

        if simbad_main_identifier not in simbad_main_identifier_list:
            simbad_main_identifiers_que_mudaram_no_simbad.append(simbad_main_identifier)
    file.close()

print(simbad_main_identifiers_que_mudaram_no_simbad)

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/query_around_estrelas_que_mudaram_no_simbad_MV_B_V.txt", "w") as file:
    for simbad_main_identifier in simbad_main_identifiers_que_mudaram_no_simbad:
        file.write("{}\n".format(simbad_main_identifier))
    file.close()



cursor.close()
connection.close()