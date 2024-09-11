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
plt.savefig('/home/lh/Desktop/teste.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# print(np.logspace(0.009651, 3.898048, num=10))
# print(np.logspace(-2.02, 0.6, num=150, base=10.0))

cursor.close()
connection.close()