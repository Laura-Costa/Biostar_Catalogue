import decimal
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
from matplotlib import style

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

###############################################################################################
cursor.execute("select Hipparcos.e_Plx, "
               "Hipparcos.Plx "
               "from Hipparcos ")
value = cursor.fetchall()

e_Plx_list = []
Plx_list = []

for (e_Plx_value, Plx_value) in value:
    e_Plx_list.append(e_Plx_value)
    Plx_list.append(Plx_value)

min_Plx = min(Plx_list)

# data = [erro/decimal.Decimal(1000.0) for erro in e_Plx_list]
data = e_Plx_list
print(data)
print(max(data))
print(min(data))
binwidth = decimal.Decimal(9)
plt.hist(data, bins=np.arange(min(data), max(data), binwidth), edgecolor="white")

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('e_Plx (mas)')
plt.title('π ≥ {:.1f} mas (CAT2, {} estrelas)'.format(min_Plx, len(data)))
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5}'.format(sum(data)/len(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_e_Plx_CAT2.pdf')
plt.close()

###############################################################################################

###############################################################################################
cursor.execute("select Hipparcos.e_Plx, "
               "Hipparcos.Plx "
               "from Hipparcos ")
value = cursor.fetchall()

e_Plx_list = []
Plx_list = []

for (e_Plx_value, Plx_value) in value:
    e_Plx_list.append(e_Plx_value)
    Plx_list.append(Plx_value)

min_Plx = min(Plx_list)

data = e_Plx_list
style.use('ggplot')
plt.hist(data, bins=10, edgecolor="black", color='blue', rwidth=1.0, log=True)

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('e_Plx (mas)')
plt.title('π ≥ {:.1f} mas (CAT2, {} estrelas)'.format(min_Plx, len(data)))
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5}'.format(sum(data)/len(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_ggplot_e_Plx_CAT2.pdf')
plt.close()
style.use('default')

###############################################################################################
cursor.execute("select Gaia.parallax_error, "
               "Gaia.parallax "
               "from Gaia "
               "where Gaia.parallax < 50.000 and "
               "Gaia.parallax + 5*Gaia.parallax_error >= 50.000")
value = cursor.fetchall()
print('value: ', value)
parallax_error_list = []

for (parallax_error_value, parallax_value) in value:
    parallax_error_list.append(parallax_error_value)

data = parallax_error_list
print('data: ', data)
print(max(data))
print(min(data))
binwidth = decimal.Decimal(0.005)
plt.hist(data, bins=len(data), edgecolor="white", log=True)

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('parallax_error (mas)')
plt.title('parallax_error (CAT1, {} estrelas)'.format(len(data)))
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5}'.format(np.mean(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_parallax_error_CAT1_5_sigma.pdf')
plt.close()
###############################################################################################

###############################################################################################
cursor.execute("select Gaia.parallax_error, "
               "Gaia.parallax "
               "from Gaia "
               "where Gaia.parallax < 50.000 and "
               "Gaia.parallax + 10*Gaia.parallax_error >= 50.000")
value = cursor.fetchall()
print('value: ', value)
parallax_error_list = []

for (parallax_error_value, parallax_value) in value:
    parallax_error_list.append(parallax_error_value)

data = parallax_error_list
print('data: ', data)
print(max(data))
print(min(data))
binwidth = decimal.Decimal(0.048)
plt.hist(data, bins=np.arange(min(data), max(data), binwidth), edgecolor="white", log=True)

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('parallax_error (mas)')
plt.title('π < 50.000 mas & π ≥ 50.000 + 10σ mas (CAT1, {} estrelas)'.format(len(data)))
#plt.title('parallax_error (CAT1)')
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5}'.format(np.mean(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_parallax_error_CAT1_10_sigma.pdf')
plt.close()
###############################################################################################

cursor.close()
connection.close()