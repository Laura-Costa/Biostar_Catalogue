import decimal
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
from matplotlib import style
from matplotlib.ticker import FormatStrFormatter

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
#style.use('ggplot') # esta linha muda o estilo para azul mas escuro nos bins e fundo cinza
fig, ax = plt.subplots() # novo
plt.hist(data, bins=10, edgecolor="black", rwidth=1.0, log=True)

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('e_Plx (mas)')
plt.title('π ≥ {:.1f} mas (CAT2, {} estrelas)'.format(min_Plx, len(data)))
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5f}'.format(sum(data)/len(data))))
#ax.set_xticks([3.415872057936028968014484007242]) # novo (para conferir se a linha vermelha coincide com o erro medio)
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.5f')) #novo (para conferir se a linha vermelha coincide com o erro medio)
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_ggplot_e_Plx_CAT2.pdf')
plt.close()
style.use('default')

###############################################################################################
cursor.execute("select Gaia.parallax_error, "
               "Gaia.parallax "
               "from Gaia "
               "where Gaia.parallax < 50.000 and "
               "Gaia.parallax + 3*Gaia.parallax_error >= 50.000")
value = cursor.fetchall()
print('value: ', value)
parallax_error_list = []

for (parallax_error_value, parallax_value) in value:
    parallax_error_list.append(parallax_error_value)

data = parallax_error_list
print('data: ', data)
print(max(data))
print(min(data))
#binwidth = decimal.Decimal(0)
plt.hist(data, bins=100, edgecolor="white")

plt.ylabel ('quantidade de estrelas')
plt.xlabel ('parallax_error (mas)')
plt.title('parallax_error (CAT1, {} estrela)'.format(len(data)))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.10f}'.format(np.mean(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_parallax_error_CAT1_3_sigma.pdf')
plt.close()
cursor.execute('''select Gaia.designation, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0 '''
               '''from Gaia '''
               '''where Gaia.parallax < 50.000 and '''
               '''Gaia.parallax + 3*Gaia.parallax_error >= 50.000 '''
               '''into outfile '/var/lib/mysql-files/parallax_error_CAT1_3_sigma.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')
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
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5f}'.format(np.mean(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/histograma_parallax_error_CAT1_5_sigma.pdf')
plt.close()
cursor.execute('''select Gaia.designation, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0 '''
               '''from Gaia '''
               '''where Gaia.parallax < 50.000 and '''
               '''Gaia.parallax + 5*Gaia.parallax_error >= 50.000 '''
               '''into outfile '/var/lib/mysql-files/parallax_error_CAT1_5_sigma.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')
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
cursor.execute('''select Gaia.designation, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0 '''
               '''from Gaia '''
               '''where Gaia.parallax < 50.000 and '''
               '''Gaia.parallax + 10*Gaia.parallax_error >= 50.000 '''
               '''into outfile '/var/lib/mysql-files/parallax_error_CAT1_10_sigma.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')
###############################################################################################

cursor.close()
connection.close()