from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astroquery.simbad import Simbad
import csv

'''
Este programa faz a correspondencia entre designation, HD e HIP 
Todo registro tem designation. Pode ou nao ter HD. Pode ou nao ter HIP.
'''


# ler o arquivo designation

csv_file_path = 'designation.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    designation = []
    for row in csv_reader:
        designation.append(row[0])
print("\n Quantidade total de estrelas Gaia (23 pc): {}".format(len(designation)))


# casar designation com HD (caso haja HD correspondente)

HD = []
quantidade_de_estrelas_com_HD = 0
for id in designation:
    tab = Simbad.query_objectids(id)
    if (len([id for id in tab['ID'] if id.startswith('HD')]) == 0):
        HD.append(None)
    else:
        quantidade_de_estrelas_com_HD += 1
        HD.append([id for id in tab['ID'] if id.startswith('HD')][0][3:].strip())

print("\n Quantidade de estrelas Gaia com HD: {}".format(quantidade_de_estrelas_com_HD))

# casar designation com HIP (caso haja HIP correspondente)

HIP = []
quantidade_de_estrelas_com_HIP = 0

for id in designation:
    tab = Simbad.query_objectids(id)
    if (len([id for id in tab['ID'] if id.startswith('HIP')]) == 0):
        HIP.append(None)
    else:
        quantidade_de_estrelas_com_HIP += 1
        HIP.append([id for id in tab['ID'] if id.startswith('HIP')][0][4:])

print("\n Quantidade de estrelas Gaia com HIP: {}".format(quantidade_de_estrelas_com_HIP))


csv_file_path = 'designation_HD_HIP.csv'
with open(csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file, dialect='unix')
    for row1, row2, row3 in zip(designation, HD, HIP):
        if row2 is None and row3 is None:
            csv_writer.writerow([row1, "", ""])
        elif row2 is not None and row3 is not None:
            csv_writer.writerow([row1, row2, row3])
        elif row2 is None and row3 is not None:
            csv_writer.writerow([row1, "", row3])
        elif row2 is not None and row3 is None:
            csv_writer.writerow([row1, row2, ""])