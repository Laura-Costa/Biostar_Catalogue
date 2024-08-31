from astroquery.simbad import Simbad
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

cursor.execute("select Hipparcos.e_Plx "
               "from Hipparcos ")
value = cursor.fetchall()

e_Plx_list = []

for (e_Plx_value,) in value:
    e_Plx_list.append(e_Plx_value)

data = e_Plx_list
binwidth = 8
erro_medio = sum(e_Plx_list)/len(e_Plx_list)
print(erro_medio)
print(np.mean(data))
plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth),
         edgecolor="white", color="blue")

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('e_Plx (mas)')
plt.title('e_Plx do CAT2')
# plt.axvline(np.mean(data))
plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=1.5, label=str(np.mean(data)))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_e_Plx_CAT2.pdf')

print(len(e_Plx_list))
print(e_Plx_list)

cursor.close()
connection.close()