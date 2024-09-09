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

# Criar o diagrama CAT3_Mg_versus_MV.pdf

cursor.execute("select CAT1_product.Mg, "
               "CAT1.parallax, "
               "CAT2_product.MV "
               "from CAT2_product, CAT1, CAT1_product "
               "where CAT1.HIP = CAT2_product.HIP and "
               "CAT1.designation = CAT1_product.designation and "
               "CAT1_product.Mg is not NULL and "
               "CAT2_product.MV is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (Mg_value, parallax_value, MV_value) in value:
    parallax_list.append(parallax_value)
    y_axis.append(Mg_value)
    x_axis.append(MV_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(min(y_axis) - decimal.Decimal(0.5), max(y_axis) + decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.5f}pc (π ≥ {:.5f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.ylabel("M(G)")
plt.xlabel("M(V)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_Mg_versus_MV.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT1_product.Mg, "
               "CAT2_product.MV "
               "from CAT2_product, CAT1, CAT1_product "
               "where CAT1.HIP = CAT2_product.HIP and "
               "CAT1.designation = CAT1_product.designation and "
               "CAT1_product.Mg is not NULL and "
               "CAT2_product.MV is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Mg_value, MV_value) in value:
    y_axis.append(Mg_value)
    x_axis.append(MV_value)

plt.scatter(x_axis, y_axis, s = size+5, marker = "o", edgecolors = 'none', color='deepskyblue', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_Mg_versus_MV.pdf')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama CAT3_phot_g_mean_mag_versus_Vmag.pdf

cursor.execute("select CAT1.phot_g_mean_mag, "
               "CAT1.parallax, "
               "CAT2.Vmag "
               "from CAT1, CAT2 "
               "where CAT1.HIP = CAT2.HIP and "
               "CAT1.phot_g_mean_mag is not NULL and "
               "CAT2.Vmag is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (phot_g_mean_mag_value, parallax_value, Vmag_value) in value:
    parallax_list.append(parallax_value)
    y_axis.append(Vmag_value)
    x_axis.append(phot_g_mean_mag_value)

min_parallax = min(parallax_list)

plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(min(y_axis) - decimal.Decimal(0.5), max(y_axis) + decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("phot_g_mean_mag")
plt.ylabel("Vmag")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_phot_g_mean_mag_versus_Vmag.pdf')

# Plotar, em deepskyblue, a estrela HD146233

cursor.execute("select CAT1.phot_g_mean_mag, "
               "CAT2.Vmag "
               "from CAT1, CAT2 "
               "where CAT1.HIP = CAT2.HIP and "
               "CAT2.Vmag is not NULL and "
               "CAT1.phot_g_mean_mag is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (phot_g_mean_mag_value, Vmag_value) in value:
    x_axis.append(phot_g_mean_mag_value)
    y_axis.append(Vmag_value)

plt.scatter(x_axis, y_axis, s=size+5, marker="o", color='deepskyblue', edgecolors='none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_phot_g_mean_mag_versus_Vmag.pdf')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama CAT3_Mg_versus_Bp_minus_Rp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1_product.Bp_minus_Rp, "
               "CAT1_product.Mg "
               "from CAT1_product, CAT1, CAT2 "
               "where CAT1_product.designation = CAT1.designation and "
               "CAT1.HIP = CAT2.HIP and "
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

plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(G)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_Mg_versus_Bp_minus_Rp.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT1_product.Bp_minus_Rp, "
               "CAT1_product.Mg "
               "from CAT1_product, CAT1, CAT2 "
               "where CAT1_product.designation = CAT1.designation and "
               "CAT1.HIP = CAT2.HIP and "
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT1_product.Mg is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, Mg_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

plt.scatter(x_axis, y_axis, s=size+5, marker="o", color='deepskyblue', edgecolors='none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_Mg_versus_Bp_minus_Rp.pdf')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama CAT3_MRp_versus_Bp_minus_Rp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1_product.Bp_minus_Rp, "
               "CAT1_product.MRp "
               "from CAT1_product, CAT1, CAT2 "
               "where CAT1_product.designation = CAT1.designation and "
               "CAT1.HIP = CAT2.HIP and "
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

plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(Rp)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MRp_versus_Bp_minus_Rp.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT1_product.Bp_minus_Rp, "
               "CAT1_product.MRp "
               "from CAT1_product, CAT1, CAT2 "
               "where CAT1_product.designation = CAT1.designation and "
               "CAT1.HIP = CAT2.HIP and "
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT1_product.MRp is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, MRp_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

plt.scatter(x_axis, y_axis, s=size+5, marker="o", color='deepskyblue', edgecolors='none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MRp_versus_Bp_minus_Rp.pdf')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama CAT3_MVt_versus_MRp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1_product.MRp, "
               "CAT2_product.MVt "
               "from CAT1, CAT1_product, CAT2_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP = CAT2_product.HIP and "
               "CAT1_product.MRp is not NULL and "
               "CAT2_product.MVt is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (parallax_value, MRp_value, MVt_value) in value:
    parallax_list.append(parallax_value)
    x_axis.append(MRp_value)
    y_axis.append(MVt_value)

min_parallax = min(parallax_list)

plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("M(Rp)")
plt.ylabel("M(Vt)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MVt_versus_MRp.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT1_product.MRp, "
               "CAT2_product.MVt "
               "from CAT1, CAT1_product, CAT2_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP = CAT2_product.HIP and "
               "CAT1_product.MRp is not NULL and "
               "CAT2_product.MVt is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (MRp_value, MVt_value) in value:
    x_axis.append(MRp_value)
    y_axis.append(MVt_value)

plt.scatter(x_axis, y_axis, s=size+5, marker = "o", color='deepskyblue', edgecolors = 'none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MVt_versus_MRp.pdf')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama CAT3_Bt_minus_Vt_versus_Bp_minus_Rp.pdf

cursor.execute("select CAT1.parallax, "
               "CAT1_product.Bp_minus_Rp, "
               "CAT2_product.BT_minus_VT "
               "from CAT1, CAT1_product, CAT2_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP = CAT2_product.HIP and "
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT2_product.BT_minus_VT is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (parallax_value, Bp_minus_Rp, BT_minus_VT) in value:
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp)
    y_axis.append(BT_minus_VT)

min_parallax = min(parallax_list)

plt.scatter(x_axis, y_axis, s=size, marker="o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp-Rp")
plt.ylabel("Bt-Vt")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_Bt_minus_Vt_versus_Bp_minus_Rp.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT1_product.Bp_minus_Rp, "
               "CAT2_product.BT_minus_VT "
               "from CAT1, CAT1_product, CAT2_product "
               "where CAT1.designation = CAT1_product.designation and "
               "CAT1.HIP = CAT2_product.HIP and "
               "CAT1_product.Bp_minus_Rp is not NULL and "
               "CAT2_product.BT_minus_VT is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp, BT_minus_VT) in value:
    x_axis.append(Bp_minus_Rp)
    y_axis.append(BT_minus_VT)

plt.scatter(x_axis, y_axis, s=size+5, marker = "o", color='deepskyblue', edgecolors='none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_Bt_minus_Vt_versus_Bp_minus_Rp.pdf')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama CAT3_MV_versus_B_minus_V.pdf

cursor.execute("select CAT1.parallax, "
               "CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT1, CAT2_product "
               "where CAT1.HIP = CAT2_product.HIP and "
               "CAT2_product.MV is not NULL and "
               "CAT2_product.B_minus_V is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (parallax_value, B_minus_V_value, MV_value) in value:
    parallax_list.append(parallax_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

min_parallax = min(parallax_list)

plt.scatter(x_axis, y_axis, s=size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MV_versus_B_minus_V.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT1, CAT2_product "
               "where CAT1.HIP = CAT2_product.HIP and "
               "CAT2_product.MV is not NULL and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (B_minus_V_value, MV_value) in value:
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

plt.scatter(x_axis, y_axis, s=size+5, marker="o", color='deepskyblue', edgecolors = 'none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MV_versus_B_minus_V.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT3_MVt_versus_Bt_minus_Vt.pdf

cursor.execute("select CAT1.parallax, "
               "CAT2_product.BT_minus_VT, "
               "CAT2_product.MVt "
               "from CAT1, CAT2_product "
               "where CAT1.HIP = CAT2_product.HIP and "
               "CAT2_product.BT_minus_VT is not NULL and "
               "CAT2_product.MVt is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (parallax_value, BT_minus_VT_value, MVt_value) in value:
    parallax_list.append(parallax_value)
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

min_parallax = min(parallax_list)

plt.scatter(x_axis, y_axis, s=size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT3: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bt - Vt")
plt.ylabel("M(Vt)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MVt_versus_Bt_minus_Vt.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT2_product.BT_minus_VT, "
               "CAT2_product.MVt "
               "from CAT1, CAT2_product "
               "where CAT1.HIP = CAT2_product.HIP and "
               "CAT2_product.BT_minus_VT is not NULL and "
               "CAT2_product.MVt is not NULL and "
               "CAT1.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (BT_minus_VT_value, MVt_value) in value:
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

plt.scatter(x_axis, y_axis, s=size+5, marker="o", color='deepskyblue', edgecolors='none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT3/diagram/CAT3_MVt_versus_Bt_minus_Vt.pdf')

# close matplotlib.pyplot as plt object
plt.close()

cursor.close()
connection.close()