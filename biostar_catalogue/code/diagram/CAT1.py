from xxsubtype import bench
from astroquery.simbad import Simbad
import mysql.connector
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import decimal
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar o diagrama CAT1_errors_logarithmic_scale.pdf

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 ")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (e_Plx_value, Plx_value) in value:
    x_axis.append(e_Plx_value)
    y_axis.append(Plx_value)
min_Plx = min(y_axis)

fig, ax = plt.subplots()
transparency = 1
size = 1.5

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')
ax.set_yscale('log')
ax.set_xscale('log')
ax.tick_params(labelsize=3)

plt.xlim(min(x_axis) - decimal.Decimal(0.0), max(x_axis) + decimal.Decimal(0.0))
plt.ylim(min(y_axis) - decimal.Decimal(1.0), max(y_axis) + decimal.Decimal(10.0))
fig.suptitle("CAT1: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("parallax_error (mas)", fontsize=7)
plt.ylabel("parallax (mas)", fontsize=7)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_errors_logarithmic_scale.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT1_errors.pdf

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 ")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (e_Plx_value, Plx_value) in value:
    x_axis.append(e_Plx_value)
    y_axis.append(Plx_value)
min_Plx = min(y_axis)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - decimal.Decimal(0.02), max(x_axis) + decimal.Decimal(0.02))
plt.ylim(min(y_axis) - decimal.Decimal(5.0), max(y_axis) + decimal.Decimal(5.0))
fig.suptitle("CAT1: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("parallax_error (mas)", fontsize=7)
plt.ylabel("parallax (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.3))
ax.xaxis.set_minor_locator(MultipleLocator(0.3/5))
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.set_minor_locator(MultipleLocator(10))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='darkgrey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_errors.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# a seguir, são feitos diagramas com seaborn
# fazer diagramas da distribuicao de erros do CAT1
cursor.execute('''select TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.parallax)+0 '''
               '''from CAT1 '''
               '''into outfile '/var/lib/mysql-files/CAT1_parallaxerror_parallax.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

df = pd.read_table("/var/lib/mysql-files/CAT1_parallaxerror_parallax.csv", sep=',', header=None, names=['parallax_error', 'parallax'])
# print(df.describe())
os.remove("/var/lib/mysql-files/CAT1_parallaxerror_parallax.csv")

# Create a Simple Scatter Plot
scatter_plot = sns.scatterplot(x=df['parallax'], y=df['parallax_error'], s=3, color='black', edgecolor='none')
scatter_plot.set_xlabel('parallax (mas)', fontsize=10)
scatter_plot.set_ylabel('parallax_error (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_errors_sns.pdf")
plt.close()

# Logarithmic Scale
scatter_plot = sns.scatterplot(x=df['parallax'], y=df['parallax_error'], s=3, color='black', edgecolor='none')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('parallax (mas)', fontsize=10)
scatter_plot.set_ylabel('parallax_error (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_errors_logarithmic_scale_sns.pdf")
plt.close()

# Create a Simple Scatter Plot (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['parallax'], y=df['parallax_error'], s=3, color='black', edgecolor='none')
scatter_plot.set_xlabel('parallax (mas)', fontsize=10)
scatter_plot.set_ylabel('parallax_error (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_errors_sns_apr.pdf")
plt.close()

# Create a Simple Scatter Plot (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['parallax'], y=df['parallax_error'], s=3, color='black', edgecolor='none')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('parallax (mas)', fontsize=10)
scatter_plot.set_ylabel('parallax_error (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_errors_logarithmic_scale_sns_apr.pdf")
plt.close()

# a seguir, histograma da distribuição dos erros no CAT1

matplotlib.style.use('default') # voltar para o estilo default

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 "
               "where (CAT1.parallax < 50.000) and "
               "(CAT1.parallax + (1)*CAT1.parallax_error >= 50.000)")
value = cursor.fetchall()
parallax_error_list = []
parallax_list = []
for (parallax_error_value, parallax_value) in value:
    parallax_error_list.append(parallax_error_value)
    parallax_list.append(parallax_value)

data = parallax_error_list
min_parallax = min(parallax_list)
print(parallax_list)
#print('data: ', data)
#print(max(data))
#print(min(data))

binwidth = decimal.Decimal(0.5)
plt.hist(data, bins=23, edgecolor="white", log=True)

plt.ylabel ('frequência')
plt.xlabel ('parallax_error (mas)')
plt.suptitle("Distribuição de erros do CAT1")
plt.title('π<50.0 & π+σ≥50.0 ({} estrelas)'.format(len(data)))
# plt.axvline(np.mean(data))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5f}'.format(np.mean(data))))
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1/diagram/CAT1_histogram_parallax_error_1_sigma.pdf')
plt.close()

cursor.close()
connection.close()