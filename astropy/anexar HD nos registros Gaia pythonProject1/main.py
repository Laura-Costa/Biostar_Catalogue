from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astroquery.simbad import Simbad
import csv

# 

csv_file_path = 'designation.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    designation = []
    for row in csv_reader:
        designation.append(row[0])
print("\n Quantidade total de estrelas: {}".format(len(designation)))
#print(designation)

HD = []
quantidade_de_estrelas_com_HD = 0
for id in designation:
    tab = Simbad.query_objectids(id)
    if (len([id for id in tab['ID'] if id.startswith('HD')]) == 0):
        HD.append(None)
    else:
        quantidade_de_estrelas_com_HD += 1
        HD.append([id for id in tab['ID'] if id.startswith('HD')][0][3:].strip())

print("\n Quantidade de estrelas com HD: {}".format(quantidade_de_estrelas_com_HD))


#print(len(HD))

#soma = 0
#for row in HD:
#    if row is None:
#        continue
#    print(int(row))
#    soma += 1
#print(soma)


csv_file_path = 'HD.csv'
print(HD)
with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file, dialect='unix')
    for row1, row2 in zip(HD, designation):
        if row1 is None:
            csv_writer.writerow(["", row2])
        else:
            csv_writer.writerow([row1, row2])
