import decimal
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

###############################################################################################
cursor.execute("select Hipparcos.e_Plx "
               "from Hipparcos ")
value = cursor.fetchall()

e_Plx_list = []

for (e_Plx_value,) in value:
    e_Plx_list.append(e_Plx_value)

data = [erro/decimal.Decimal(1000.0) for erro in e_Plx_list]
print(data)
print(max(data))
print(min(data))
binwidth = decimal.Decimal(0.01)
plt.hist(data, bins=np.arange(min(data), max(data), binwidth),
         edgecolor="white")

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('e_Plx (arcsec)')
plt.title('e_Plx (CAT2)')
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str(np.mean(data)))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_e_Plx_CAT2.pdf')
plt.close()
###############################################################################################

# cria os subplots
fig, axes = plt.subplots(figsize=(50, 25))

# plot
axes.hist(data, edgecolor="white", color="blue")
axes.set_xlim((min(data)-decimal.Decimal(0.001), max(data)+decimal.Decimal(0.001)))

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma2_e_Plx_CAT2.pdf')
plt.close()
###############################################################################################

###############################################################################################
cursor.execute("select Gaia.parallax_error, "
               "Gaia.parallax "
               "from Gaia "
               "where Gaia.parallax < 50.000 and "
               "Gaia.parallax + Gaia.parallax_error >= 50.000")
value = cursor.fetchall()
print('value: ', value)
parallax_error_list = []

for (parallax_error_value, parallax_value) in value:
    parallax_error_list.append(parallax_error_value)

data = [erro/decimal.Decimal(1000.0) for erro in parallax_error_list]
print('data: ', data)
print(max(data))
print(min(data))
binwidth = decimal.Decimal(0.01)
plt.hist(data, bins=np.arange(min(data), max(data), binwidth),
         edgecolor="white")

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('parallax_error (arcsec)')
plt.title('parallax_error (CAT1)')
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str(np.mean(data)))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_parallax_error_CAT1.pdf')
plt.close()
###############################################################################################

cursor.close()
connection.close()