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

from code.diagram.CAT1 import Mg_value

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                     password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar o diagrama CAT2_Mg_versus_Bp_minus_Rp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1_product.Bp_minus_Rp, "
               "CAT1_product.Mg "
               "from CAT1, CAT1_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP is NULL and " # nao esta na intersecao
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT1_product.Mg is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (parallax_value, Bp_minus_Rp_value, Mg_value) in value:
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5

plt.scatter(x_axis, y_axis, s=size, marker="o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT4: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(G)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT4/diagram/CAT4_Mg_versus_Bp_minus_Rp.pdf')

# Plotar, em tomato, a estrela 131156B

cursor.execute("select CAT1_product.Bp_minus_Rp, "
               "CAT1_product.Mg "
               "from CAT1, CAT1_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP is NULL and " # nao esta na intersecao
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT1_product.Mg is not NULL and "
               "CAT1.HD = '131156B'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, Mg_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

plt.scatter(x_axis, y_axis, s=size+5, marker="o", color='tomato', edgecolors = 'none', label='HD 131156B')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT4/diagram/CAT4_Mg_versus_Bp_minus_Rp.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT4_MRp_versus_Bp_minus_Rp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1_product.Bp_minus_Rp, "
               "CAT1_product.MRp "
               "from CAT1, CAT1_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP is NULL and " # nao esta na intersecao
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT1_product.MRp is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (parallax_value, Bp_minus_Rp_value, MRp_value) in value:
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

min_parallax = min(parallax_list)

plt.scatter(x_axis, y_axis, s=size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT4: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(Rp)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT4/diagram/CAT4_MRp_versus_Bp_minus_Rp.pdf')

# Plotar, em tomato, a estrela 131156B

cursor.execute("select CAT1_product.Bp_minus_Rp, "
               "CAT1_product.MRp "
               "from CAT1, CAT1_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP is NULL and " # nao esta na intersecao
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT1_product.MRp is not NULL and "
               "CAT1.HD = '131156B'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, MRp_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

plt.scatter(x_axis, y_axis, s=size+5, marker = "o", color='tomato', edgecolors = 'none', label='HD 131156B')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT4/diagram/CAT4_MRp_versus_Bp_minus_Rp.pdf')

# close matplotlib.pyplot as plt object
plt.close()

cursor.close()
connection.close()