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

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                     password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar o diagrama CAT2_MV_versus_B_minus_V.pdf

cursor.execute("select CAT2.Plx, "
               "CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT2_product.MV is not NULL")
value = cursor.fetchall()

Plx_list = []
x_axis = []
y_axis = []

for (Plx_value, B_minus_V_value, MV_value) in value:
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT2: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_MV_versus_B_minus_V.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT2_product.MV is not NULL and "
               "CAT2.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (B_minus_V_value, MV_value) in value:
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

plt.scatter(x_axis, y_axis, s = size+5, marker = "o", color='deepskyblue', edgecolors = 'none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_MV_versus_B_minus_V.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT2_MVt_versus_BT_minus_VT.pdf

cursor.execute("select CAT2.Plx, "
               "CAT2_product.BT_minus_VT, "
               "CAT2_product.MVt "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.BT_minus_VT is not NULL and "
               "CAT2_product.MVt is not NULL")
value = cursor.fetchall()

Plx_list = []
x_axis = []
y_axis = []

for (Plx_value, BT_minus_VT_value, MVt_value) in value:
    Plx_list.append(Plx_value)
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

min_Plx = min(Plx_list)

plt.scatter(x_axis, y_axis, s = size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT2: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("BT - VT")
plt.ylabel("M(Vt)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_MVt_versus_BT_minus_VT.pdf')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select CAT2_product.BT_minus_VT, "
               "CAT2_product.MVt "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.BT_minus_VT is not NULL and "
               "CAT2_product.MVt is not NULL and "
               "CAT2.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (BT_minus_VT_value, MVt_value) in value:
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

plt.scatter(x_axis, y_axis, s = size+5, marker = "o", color='deepskyblue', edgecolors = 'none', label='HD 146233')

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_MVt_versus_BT_minus_VT.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar diagrama do CAT2 Plx_versus_parallax_simbad.pdf

cursor.execute('''select TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax)+0 as simbad_parallax, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax_error)+0 '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and ''' 
               '''(designation_DR3 is not null or '''
               '''designation_DR2 is not null or '''
               '''designation_DR1 is not null) and ''' 
               '''CAT2.Plx is not null and ''' 
               '''CAT2_DR1_DR2_DR3.simbad_parallax is not null ''')

value = cursor.fetchall()

x_axis = []
y_axis = []
e_Plx_list = []
simbad_parallax_error_list = []

for (Plx_value, e_Plx_value, simbad_parallax_value, simbad_parallax_error_value) in value:
    x_axis.append(simbad_parallax_value)
    y_axis.append(Plx_value)
    e_Plx_list.append(e_Plx_value)
    simbad_parallax_error_list.append(simbad_parallax_error_value)

min_parallax = min(x_axis)

fig, ax = plt.subplots()
ax.errorbar(x_axis, y_axis, ms=size, color='black', mec='none', fmt='o', elinewidth=0.1, yerr=e_Plx_list, xerr=simbad_parallax_error_list, ecolor='blue')

plt.xlim(min(x_axis) - 8.0, max(x_axis) + 8.0)
plt.ylim(min(y_axis) - 100.0, max(y_axis) + 8.0)

# colocar título e rótulo dos eixos x e y
plt.suptitle("Estrelas do CAT2 que têm designação Gaia DR1, DR2 ou DR3 no Simbad", fontsize=8)
plt.title("{} estrelas em um raio de {:.4f}pc, π ≥ {:.8f}'' (paralaxe do Simbad)".format(len(value), 1.0 / (min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
plt.xlabel("paralaxe Simbad (mas)", fontsize=7)
plt.ylabel("paralaxe Hipparcos (mas)", fontsize=7)

# reta y = x
# ax.axline((0, 0), slope=1, linewidth=0.001, label='f(x) = y', color='red')

# escala logarítmica
# ax.set_yscale('log')
# ax.set_xscale('log')

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(20/5))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.set_minor_locator(MultipleLocator(20/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labelleft=True, left=True, labelbottom=True, bottom=True, labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)

#legenda
# plt.legend(shadow=True, fontsize=7)

plt.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/Plx_versus_parallax_simbad.pdf")

# Criar diagrama do CAT2 error_division_versus_simbad_parallax.pdf

cursor.execute('''select TRIM(CAT2.e_Plx/CAT2_DR1_DR2_DR3.simbad_parallax_error)+0, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax)+0 as simbad_parallax '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and ''' 
               '''(designation_DR3 is not null or '''
               '''designation_DR2 is not null or '''
               '''designation_DR1 is not null) and ''' 
               '''CAT2_DR1_DR2_DR3.simbad_parallax is not null and '''
               '''CAT2_DR1_DR2_DR3.simbad_parallax_error is not null''')

value = cursor.fetchall()

x_axis = []
y_axis = []

for (error_division_value, simbad_parallax_value) in value:
    x_axis.append(simbad_parallax_value)
    y_axis.append(error_division_value)

min_parallax = min(x_axis)

fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - 8.0, max(x_axis) + 8.0)
plt.ylim(min(y_axis) - 100.0, max(y_axis) + 100.0)

# colocar título e rótulo dos eixos x e y
plt.suptitle("Estrelas do CAT2 que têm designação Gaia DR1, DR2 ou DR3 no Simbad", fontsize=8)
plt.title("{} estrelas em um raio de ${:.4f}pc, π ≥ {:.8f}$'' (paralaxe do Simbad)".format(len(value), 1.0 / (min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
plt.xlabel("paralaxe Simbad (mas)", fontsize=7)
plt.ylabel("$σ_π({HIP})/σ_π({Simbad})$ (mas)", fontsize=7)

# escala logarítmica
# ax.set_yscale('log')
# ax.set_xscale('log')

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(15))
ax.xaxis.set_minor_locator(MultipleLocator(15/5))
ax.yaxis.set_major_locator(MultipleLocator(150))
ax.yaxis.set_minor_locator(MultipleLocator(150/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labelleft=True, left=True, labelbottom=True, bottom=True, labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)

#legenda
#plt.legend(shadow=True, fontsize=7)

plt.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/error_division_versus_simbad_parallax.pdf")

# Criar diagrama do CAT2 e_Plx_versus_Plx.pdf

cursor.execute('''select TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(CAT2.Plx)+0 '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and ''' 
               '''(designation_DR3 is null) and ''' 
               '''CAT2.e_Plx is not null and ''' 
               '''CAT2.Plx is not null ''')

value = cursor.fetchall()

x_axis = []
y_axis = []

for (e_Plx_value, Plx_value) in value:
    x_axis.append(Plx_value)
    y_axis.append(e_Plx_value)

min_parallax = min(x_axis)

fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - 5.0, max(x_axis) + 5.0)
plt.ylim(min(y_axis) - 1.0, max(y_axis) + 1.0)

# colocar título e rótulo dos eixos x e y
plt.suptitle("Estrelas do CAT2 que não têm designação Gaia DR3 no Simbad", fontsize=8)
plt.title("{} estrelas em um raio de {:.4f}pc, π ≥ {:.4f}''".format(len(value), 1.0 / (min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
plt.xlabel("Plx (mas)", fontsize=7)
plt.ylabel("e_Plx (mas)", fontsize=7)

# escala logarítmica
# ax.set_yscale('log')
# ax.set_xscale('log')

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_minor_locator(MultipleLocator(20/5))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(5/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labelleft=True, left=True, labelbottom=True, bottom=True, labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)

#legenda
#plt.legend(shadow=True, fontsize=7)

plt.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/e_Plx_versus_Plx.pdf")

# Criar diagrama do CAT2 e_Plx_versus_Vmag.pdf

matplotlib.style.use('default') # voltar para o estilo default

cursor.execute('''select TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0 '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and ''' 
               '''(designation_DR3 is null) and ''' 
               '''CAT2.e_Plx is not null and ''' 
               '''CAT2.Plx is not null and ''' 
               '''CAT2.Vmag is not null ''')

value = cursor.fetchall()

x_axis = []
y_axis = []
Plx_list = []

for (Vmag_value, Plx_value, e_Plx_value) in value:
    x_axis.append(Vmag_value)
    y_axis.append(e_Plx_value)
    Plx_list.append(Plx_value)

min_parallax = min(Plx_list)

fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - 0.3, max(x_axis) + 0.3)
plt.ylim(min(y_axis) - 4.0, max(y_axis) + 4.5)

# colocar título e rótulo dos eixos x e y
plt.suptitle("Estrelas do CAT2 que não têm designação Gaia DR3 no Simbad", fontsize=8)
plt.title("{} estrelas em um raio de {:.4f}pc, π ≥ {:.4f}''".format(len(value), 1.0 / (min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
plt.xlabel("Vmag (mag)", fontsize=7)
plt.ylabel("e_Plx (mas)", fontsize=7)

# escala logarítmica
# ax.set_yscale('log')
# ax.set_xscale('log')

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.5/5))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(5/5))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labelleft=True, left=True, labelbottom=True, bottom=True, labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)

#legenda
#plt.legend(shadow=True, fontsize=7)

plt.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/e_Plx_versus_Vmag.pdf")

# Criar o diagrama CAT2_errors.pdf

cursor.execute("select CAT2.e_Plx, "
               "CAT2.Plx "
               "from CAT2 ")
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

plt.xlim(min(x_axis) - decimal.Decimal(1.5), max(x_axis) + decimal.Decimal(1.5))
plt.ylim(min(y_axis) - decimal.Decimal(6), max(y_axis) + decimal.Decimal(6))
fig.suptitle("CAT2: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("e_Plx (mas)", fontsize=7)
plt.ylabel("Plx (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.set_minor_locator(MultipleLocator(10))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=0)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='darkgrey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_errors.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT2_errors_logarithmic_scale.pdf

cursor.execute("select CAT2.e_Plx, "
               "CAT2.Plx "
               "from CAT2 ")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (e_Plx_value, Plx_value) in value:
    x_axis.append(e_Plx_value)
    y_axis.append(Plx_value)
min_Plx = min(y_axis)

fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')
ax.set_yscale('log')
ax.set_xscale('log')
ax.tick_params(labelsize=3)
ax.set_yticks([39, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 772.33])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set_xticks([0.38, 10, 114.46])
ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(100.0))

plt.xlim(min(x_axis) - decimal.Decimal(0.1), max(x_axis) + decimal.Decimal(100))
plt.ylim(min(y_axis) - decimal.Decimal(6), max(y_axis) + decimal.Decimal(100))
fig.suptitle("CAT2: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("e_Plx (mas)", fontsize=7)
plt.ylabel("Plx (mas)", fontsize=7)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_errors_logarithmic_scale.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# a seguir, são feitos diagramas com seaborn
# fazer diagramas da distribuicao de erros do CAT2
cursor.execute('''select TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(CAT2.Plx)+0 '''
               '''from CAT2 '''
               '''into outfile '/var/lib/mysql-files/CAT2_ePlx_Plx.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

df = pd.read_table("/var/lib/mysql-files/CAT2_ePlx_Plx.csv", sep=',', header=None, names=['e_Plx', 'Plx'])
# print(df.describe())
os.remove("/var/lib/mysql-files/CAT2_ePlx_Plx.csv")

# Create a Simple Scatter Plot
scatter_plot = sns.scatterplot(x=df['Plx'], y=df['e_Plx'], s=3, color='black', edgecolor='none')
scatter_plot.set_xlabel('Plx (mas)', fontsize=10)
scatter_plot.set_ylabel('e_Plx (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_errors_sns.pdf")
plt.close()

# Logarithmic Scale
scatter_plot = sns.scatterplot(x=df['Plx'], y=df['e_Plx'], s=3, color='black', edgecolor='none')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('Plx (mas)', fontsize=10)
scatter_plot.set_ylabel('e_Plx (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_errors_logarithmic_scale_sns.pdf")
plt.close()

# Create a Simple Scatter Plot (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['Plx'], y=df['e_Plx'], s=3, color='black', edgecolor='none')
scatter_plot.set_xlabel('Plx (mas)', fontsize=10)
scatter_plot.set_ylabel('e_Plx (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_errors_sns_apr.pdf")
plt.close()

# Logarithmic Scale (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['Plx'], y=df['e_Plx'], s=3, color='black', edgecolor='none')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('Plx (mas)', fontsize=10)
scatter_plot.set_ylabel('e_Plx (mas)', fontsize=10)
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_errors_logarithmic_scale_sns_apr.pdf")
plt.close()

# a seguir, histograma da distribuição dos erros no CAT2

matplotlib.style.use('default') # voltar para o estilo default

cursor.execute("select CAT2.e_Plx, "
               "CAT2.Plx "
               "from CAT2 ")
value = cursor.fetchall()

e_Plx_list = []
Plx_list = []

for (e_Plx_value, Plx_value) in value:
    e_Plx_list.append(e_Plx_value)
    Plx_list.append(Plx_value)

min_Plx = min(Plx_list)

data = e_Plx_list
fig, ax = plt.subplots() # novo
plt.hist(data, bins=10, edgecolor="black", rwidth=1.0, log=True)

plt.ylabel ('frequência')
plt.xlabel ('e_Plx (mas)')
plt.suptitle("Distribuição de erros do CAT2")
plt.title('π ≥ {:.1f} mas ({} estrelas)'.format(min_Plx, len(data)))
plt.axvline(sum(data)/len(data), color='red', linestyle='dashed', linewidth=1.5, label=str('{:.5f}'.format(sum(data)/len(data))))
#ax.set_xticks([3.415872057936028968014484007242]) # novo (para conferir se a linha vermelha coincide com o erro medio)
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.5f')) #novo (para conferir se a linha vermelha coincide com o erro medio)
plt.legend(loc='upper right')
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/CAT2_histogram_e_Plx.pdf')
plt.close()

cursor.close()
connection.close()