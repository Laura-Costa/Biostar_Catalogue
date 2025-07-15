import matplotlib
import mysql.connector
import matplotlib.pyplot as plt
import decimal
import seaborn as sns
import pandas as pd
import os

from astroquery.simbad import Simbad
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh',
                                     password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar diagrama do hipparcos Hipparcos_parallax_versus_gaiaDR3_parallax.jpg

cursor.execute('''select TRIM(hipparcos.Plx)+0, '''
               '''TRIM(hipparcos.e_Plx)+0, '''
               '''TRIM(hipparcos.GaiaDR3_parallax)+0, '''
               '''TRIM(hipparcos.GaiaDR3_parallax_error)+0 ''' 
               '''from hipparcos '''
               '''where hipparcos.GaiaDR3_parallax is not null and ''' 
               '''hipparcos.GaiaDR3_parallax_error is not null and ''' 
               '''hipparcos.Plx is not null and ''' 
               '''hipparcos.e_Plx is not null ''')

value = cursor.fetchall()

x_axis = []
y_axis = []
e_Plx_list = []
GaiaDR3_parallax_error_list = []

for (Plx_value, e_Plx_value, GaiaDR3_parallax_value, GaiaDR3_parallax_error_value) in value:
    x_axis.append(GaiaDR3_parallax_value)
    y_axis.append(Plx_value)
    e_Plx_list.append(e_Plx_value)
    GaiaDR3_parallax_error_list.append(GaiaDR3_parallax_error_value)

min_parallax = min(x_axis)
print("min_parallax: ", min_parallax)

fig, ax = plt.subplots()

ax.errorbar(x_axis, y_axis, ms=2.0, color='black', mec='none', fmt='o', elinewidth=0.3, yerr=e_Plx_list, xerr=GaiaDR3_parallax_error_list, ecolor='blue')

plt.xlim(min(x_axis) - 8.0, max(x_axis) + 8.0)
plt.ylim(min(y_axis) - 100.0, max(y_axis) + 8.0)

# colocar título e rótulo dos eixos x e y
plt.suptitle("Estrelas do hipparcos que têm paralaxe no GaiaDR3", fontsize=8)
plt.title("{} estrelas em um raio de {:.4f}pc, π ≥ {:.8f}'' (paralaxe do GaiaDR3)".format(len(value), 1.0 / (min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
plt.xlabel("paralaxe GaiaDR3 (mas)", fontsize=7)
plt.ylabel("paralaxe hipparcos (mas)", fontsize=7)

# reta y = x
ax.axline((0, 0), slope=1, linewidth=0.5, label='f(x) = x', color='red')

# escala logarítmica
# ax.set_yscale('log')
# ax.set_xscale('log')

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(20/5))
ax.yaxis.set_major_locator(MultipleLocator(30))
ax.yaxis.set_minor_locator(MultipleLocator(30/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labelleft=True, left=True, labelbottom=True, bottom=True, labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=15)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)

#legenda
plt.legend(shadow=True, fontsize=7)

plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/hipparcos/pyplot_scatterplot/error_bars.jpg", dpi=1200)

cursor.close()
connection.close()