import math

import mysql.connector
import matplotlib
import matplotlib.pyplot as plt
from cryptography.hazmat.backends.openssl import backend
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import decimal
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import os

from code.diagram.CAT1 import transparency

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar o diagrama CAT1a_errors.pdf

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 "
               "where CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))")
value = cursor.fetchall()

x_axis = []
y_axis = []

size = 1.5

for (parallax_error_value, parallax_value) in value:
    y_axis.append(parallax_error_value)
    x_axis.append(parallax_value)
min_Plx = min(x_axis)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - decimal.Decimal(8.0), max(x_axis) + decimal.Decimal(8.0))
plt.ylim(min(y_axis) - decimal.Decimal(0.05), max(y_axis) + decimal.Decimal(0.05))
fig.suptitle("CAT1a: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("parallax (mas)", fontsize=7)
plt.ylabel("parallax_error (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(15))
ax.xaxis.set_minor_locator(MultipleLocator(15/5))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_parallax_error_versus_parallax.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT1a_parallax_error_versus_parallax_log_scale.pdf

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 "
               "where CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))")
value = cursor.fetchall()

x_axis = []
y_axis = []

size = 1.5

for (parallax_error_value, parallax_value) in value:
    y_axis.append(parallax_error_value)
    x_axis.append(parallax_value)
min_Plx = min(x_axis)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')
ax.set_yscale('log')
ax.set_xscale('log')

plt.xlim(min(x_axis) - decimal.Decimal(0.0), max(x_axis) + decimal.Decimal(0.0))
plt.ylim(min(y_axis) - decimal.Decimal(0.0), max(y_axis) + decimal.Decimal(0.0))
fig.suptitle("CAT1a: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("parallax (mas)", fontsize=7)
plt.ylabel("parallax_error (mas)", fontsize=7)

# remover minor e major ticks da escala logarítmica do eixo y e do eixo x
ax.tick_params(axis='both', left=False, labelleft=True, labelbottom=False, bottom=False, right=False, top=False, which='both')

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
#ax.xaxis.set_major_locator(MultipleLocator(15))
#ax.xaxis.set_minor_locator(MultipleLocator(15/5))
#ax.yaxis.set_major_locator(MultipleLocator(0.1))
#ax.yaxis.set_minor_locator(MultipleLocator(0.1/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", tickdir='out')

ax.yaxis.set_major_formatter(lambda x, pos: f'{x:g}')
ax.set_ylim(ymin=0.009651)
#ax.set_yticks(np.logspace(0.009651, 3.898048))


# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_parallax_error_versus_parallax_log_scale.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT1a_parallax_error_versus_parallax_log_scale.pdf

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 "
               "where CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))")
value = cursor.fetchall()

x_axis = []
y_axis = []

size = 1.5

for (parallax_error_value, parallax_value) in value:
    y_axis.append(parallax_error_value)
    x_axis.append(parallax_value)
min_parallax = min(x_axis)
max_parallax = max(x_axis)
min_parallax_error = min(y_axis)
max_parallax_error = max(y_axis)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)
ax.set_yscale('log')
ax.set_xscale('log')

# configurando as dimensões de axes
plt.xlim(min(x_axis) - decimal.Decimal(0.001), max(x_axis) + decimal.Decimal(15.0))
plt.ylim(min(y_axis) - decimal.Decimal(0.001), max(y_axis) + decimal.Decimal(0.5))

# colocar título e rótulo dos eixos x e y
plt.suptitle("CAT1a: σ(π) versus π em escala logarítmica", fontsize=8)
plt.title("{} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)), fontsize=5)
plt.xlabel("parallax (mas)", fontsize=7)
plt.ylabel("parallax_error (mas)", fontsize=7)

# aqui você configura os minor ticks do jeito que quiser
ax.tick_params(axis='both', left=True, right=True, bottom=True, top=True,labelleft=True, labelright=True, labelbottom=True, labeltop=True, which='both', labelsize=2)

# aqui você remove os major ticks e major labels que vêm por default
ax.tick_params(axis='both', left=False, right=False, bottom=False, top=False, labelleft=False, labelright=False, labelbottom=False, labeltop=False, which='major')

# aqui você exige que apareçam os labels de minor ticks (eixo y)
ax.yaxis.set_minor_formatter(FormatStrFormatter("%.5f"))
ax.set_yticks(np.logspace(math.log10(min_parallax_error - decimal.Decimal(0.0)), math.log10(max_parallax_error + decimal.Decimal(1.0)), num=50, base=10.0), minor=True)

# rotacionar label do eixo x
plt.xticks(rotation=45, minor=True)

# aqui você exige que apareçam os labels de minor ticks (eixo x)
ax.xaxis.set_minor_formatter(FormatStrFormatter("%.5f"))
ax.set_xticks(np.logspace(math.log10(min_parallax - decimal.Decimal(1.0)), math.log10(max_parallax + decimal.Decimal(1.0)), num=60, base=10.0), minor=True)

# aqui coloca a grade partindo de minor ticks
plt.grid(color='lightgray', linestyle='dashed', dashes=(1,1), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_parallax_error_versus_parallax_log_scale.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT1a_parallax_error_versus_phot_g_mean_mag.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1.parallax_error, "
               "CAT1.phot_g_mean_mag "
               "from CAT1 "
               "where (CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))) and "
               "CAT1.phot_g_mean_mag is not null")
value = cursor.fetchall()

x_axis = []
y_axis = []
parallax_list = []

for (parallax_value, parallax_error_value, phot_g_mean_mag_value) in value:
    parallax_list.append(parallax_value)
    y_axis.append(parallax_error_value)
    x_axis.append(phot_g_mean_mag_value)
min_Plx = min(parallax_list)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - decimal.Decimal(0.5), max(x_axis) + decimal.Decimal(0.5))
plt.ylim(min(y_axis) - decimal.Decimal(0.05), max(y_axis) + decimal.Decimal(0.05))
fig.suptitle("CAT1a: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("phot_g_mean_mag (mag)", fontsize=7)
plt.ylabel("parallax_error (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.5/5))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_parallax_error_versus_phot_g_mean_mag.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT1a_parallax_error_versus_Bp_minus_Rp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1.parallax_error, "
               "CAT1_product.Bp_minus_Rp "
               "from CAT1, CAT1_product "
               "where CAT1.designation = CAT1_product.designation and "
               "(CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))) and "
               "CAT1_product.Bp_minus_Rp is not null")
value = cursor.fetchall()

x_axis = []
y_axis = []
parallax_list = []

for (parallax_value, parallax_error_value, Bp_minus_Rp_value) in value:
    parallax_list.append(parallax_value)
    y_axis.append(parallax_error_value)
    x_axis.append(Bp_minus_Rp_value)
min_Plx = min(parallax_list)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - decimal.Decimal(0.15), max(x_axis) + decimal.Decimal(0.15))
plt.ylim(min(y_axis) - decimal.Decimal(0.05), max(y_axis) + decimal.Decimal(0.05))
fig.suptitle("CAT1a: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("Bp-Rp (mag)", fontsize=7)
plt.ylabel("parallax_error (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.15))
ax.xaxis.set_minor_locator(MultipleLocator(0.15/5))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_parallax_error_versus_Bp_minus_Rp.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT1a_MG_error_versus_phot_g_mean_mag.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1.phot_g_mean_mag, "
               "CAT1_product.Mg_error "
               "from CAT1, CAT1_product "
               "where CAT1.designation = CAT1_product.designation and "
               "(CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))) and "
               "CAT1.phot_g_mean_mag is not null and "
               "CAT1_product.Mg_error is not null")
value = cursor.fetchall()

x_axis = []
y_axis = []
parallax_list = []

for (parallax_value, phot_g_mean_mag_value, Mg_error_value) in value:
    parallax_list.append(parallax_value)
    x_axis.append(phot_g_mean_mag_value)
    y_axis.append(Mg_error_value)
min_Plx = min(parallax_list)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - decimal.Decimal(0.15), max(x_axis) + decimal.Decimal(0.15))
plt.ylim(min(y_axis) - decimal.Decimal(0.002), max(y_axis) + decimal.Decimal(0.002))
fig.suptitle("CAT1a: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("phot_g_mean_mag (mag)", fontsize=7)
plt.ylabel("M(G) error (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.5/5))
ax.yaxis.set_major_locator(MultipleLocator(0.005))
ax.yaxis.set_minor_locator(MultipleLocator(0.005/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_MG_error_versus_phot_g_mean_mag.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# criar histograma CAT1a_histogram_parallax_error_log_scale.pdf

matplotlib.style.use('default') # voltar para o estilo default

cursor.execute("select CAT1.parallax_error, "
               "CAT1.parallax "
               "from CAT1 "
               "where CAT1.parallax >= 50.00 or "
               "(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00))")
value = cursor.fetchall()

parallax_error_list = []
parallax_list = []

for (parallax_error_value, parallax_value) in value:
    parallax_error_list.append(parallax_error_value)
    parallax_list.append(parallax_value)

min_Plx = min(parallax_list)

data = parallax_error_list
fig, ax = plt.subplots() # novo
(bin_heights, bin_edges, _) = plt.hist(data, bins=4, edgecolor="black", rwidth=1.0, log=True, zorder=2)

# remover minor ticks da escala logarítmica do eixo y
ax.tick_params(axis='y', left=False, which='minor')

# rotacionar label do eixo x
plt.yticks(rotation=0)

plt.ylabel ('quantidade')
plt.xlabel ('parallax_error (mas)')
plt.suptitle("Distribuição de erros do CAT1a em escala logarítmica")
plt.title('π ≥ {:.1f} mas ({} estrelas)'.format(min_Plx, len(data)))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('média: {:.6f}'.format(sum(data)/len(data))))

# colocar os ticks no eixo x do histograma
ax.set_xticks(bin_edges)
ax.xaxis.set_major_formatter(FormatStrFormatter('%.6f'))

# colocar major ticks no eixo y do histograma
ax.set_yticks(bin_heights)
ax.yaxis.set_major_formatter(FormatStrFormatter('%i'))

# colocar a grid
plt.grid(color='lightgrey', linestyle='solid', which='major', linewidth=1.0, axis='y', zorder=0)

# framealpha: opacidade do frame da legenda (1 é opaco, 0 é transparente)
legenda = plt.legend(loc='upper right', facecolor='white', framealpha=1, shadow=True)
frame = legenda.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('lightgrey')

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1a/diagram/CAT1a_histogram_parallax_error_log_scale.pdf')
plt.close()

# para confirmar o erro medio usando pandas
cursor.execute('''select TRIM(CAT1.parallax_error)+0 '''
               '''from CAT1 '''
               '''where CAT1.parallax >= 50.00 or '''
               '''(CAT1.parallax < 50.00 and (CAT1.parallax + CAT1.parallax_error >= 50.00)) '''
               '''into outfile '/var/lib/mysql-files/CAT1a_parallax_error.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

df = pd.read_table("/var/lib/mysql-files/CAT1a_parallax_error.csv", sep=',', header=None, names=['parallax_error'])
os.remove("/var/lib/mysql-files/CAT1a_parallax_error.csv")

cursor.close()
connection.close()