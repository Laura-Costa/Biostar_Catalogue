from xxsubtype import bench
from astroquery.simbad import Simbad
import mysql.connector
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import decimal
import numpy as np
from matplotlib.ticker import FormatStrFormatter

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_edited.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.HD, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.Bt_minus_VT, "
               "Hipparcos_product.MV, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
HD_list = []
Plx_list = []
x_axis = []
BT_minus_VT_list = []
y_axis = []
MVt_list = []

for (HIP_value, HD_value, Plx_value, B_minus_V_value, BT_minus_VT_value, MV_value, MVt_value) in value:
    HIP_list.append(HIP_value)
    HD_list.append(HD_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    BT_minus_VT_list.append(BT_minus_VT_value)
    y_axis.append(MV_value)
    MVt_list.append(MVt_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
#plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))

plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")

# Colorindo as AFG
AFG = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal('4.82'):
        blue = plt.scatter([x], [y], s=size, marker=".", edgecolors='blue', alpha=transparency)
        AFG += (str(HIP),)

# Colorindo as anãs brancas
anas_brancas = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y >= decimal.Decimal(5.91)*decimal.Decimal(x) + decimal.Decimal(9.27):
        dodgerblue = plt.scatter([x], [y], s=size, marker=".", edgecolors='dodgerblue', alpha=transparency)
        anas_brancas += (str(HIP),)

# Colorindo as estrelas sem classificação
sem_classificacao = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal(5.91)*decimal.Decimal(x) + decimal.Decimal(9.27) and y >= decimal.Decimal(5.68)*decimal.Decimal(x) + decimal.Decimal(3.9):
        black = plt.scatter([x], [y], s=size, marker=".", edgecolors='black', alpha=transparency)
        sem_classificacao += (str(HIP),)

# Colorindo as GK
GK = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal(5.68)*decimal.Decimal(x) + decimal.Decimal(3.9) and y >= 4.82 and y <= decimal.Decimal(-5.26)*decimal.Decimal(x) + decimal.Decimal(14.842):
        coral = plt.scatter([x], [y], s=size, marker=".", edgecolors='coral', alpha=transparency)
        GK += (str(HIP),)

# Colorindo as anãs vermelhas
anas_vermelhas = ()
for (HIP, HD, Plx, x, BT_minus_VT, y, MVt) in zip(HIP_list, HD_list, Plx_list, x_axis, BT_minus_VT_list, y_axis, MVt_list):
    if y <= decimal.Decimal(5.68)*decimal.Decimal(x) + decimal.Decimal(3.9) and y >= 4.82 and y >= decimal.Decimal(-5.26)*decimal.Decimal(x) + decimal.Decimal(14.842):
        red = plt.scatter([x], [y], s=size, marker=".", edgecolors='red', alpha=transparency)
        anas_vermelhas += (str(HIP),)

# equação da reta que passa pelo Sol
# y = 4.82
plt.axhline(y = 4.82, color = 'gray', linestyle=':', linewidth=1)

# equação da reta que isola as anãs brancas
# y = 5.91*x + 9.27
plt.plot([-0.4, 1], [6.9, 5.91*(1) + 9.27], color='gray', linestyle=':', linewidth=1)

# equação da reta que isola as estrelas não classificadas
# y = 5.68*x + 3.9
plt.plot([0.17, 1.9], [5.68*(0.17) + 3.9, 14.7], color='gray', linestyle=':', linewidth=1)

# equação da reta que isola as anãs vermelhas
# y = -5.26*x + 14.842
plt.plot([1, 1.9], [-5.26*(1) + 14.842, -5.26*(1.9) + 14.842], color='gray', linestyle=':', linewidth=1)

# Marcando o Sol
yellow = plt.scatter([0.65], [4.82], s=30, marker="o", color='yellow', edgecolors='gold', alpha=1)

# Legenda
plt.legend((yellow, blue, coral, red, dodgerblue, black),
           ('Sol', 'AFG ({} estrelas)'.format(len(AFG)), 'GK ({} estrelas)'.format(len(GK)), 'anãs vermelhas ({} estrelas)'.format(len(anas_vermelhas)), 'anãs brancas ({} estrelas)'.format(len(anas_brancas)), 'sem classificação ({} estrelas)'.format(len(sem_classificacao))),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=6)

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_edited.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_showing_gaia.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis_temp = []
y_axis_temp = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis_temp.append(B_minus_V_value)
    y_axis_temp.append(MV_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.xlim(min(x_axis_temp) - decimal.Decimal(0.2), max(x_axis_temp) + decimal.Decimal(0.2))
plt.ylim(max(y_axis_temp) + decimal.Decimal(0.5), min(y_axis_temp) - decimal.Decimal(0.5))

# Separar os dados das estrelas que têm designação mas não estão no catálogo 1
x_axis_gaia = []
y_axis_gaia = []
pop_axis = []
hips_com_designacao = ()
for i in range(len(HIP_list)):
    tab = Simbad.query_objectids("HIP " + str(HIP_list[i]))
    ids = [id for id in tab['ID'] if id.startswith('Gaia')]
    if len(ids) != 0:
        hips_com_designacao += (str(HIP_list[i]),)
        # print(ids)
        # se esse if é True, entao a estrela com identificador HIP_list[i] tem designation, ela está no Gaia com distancia maior do que 23pc
        x_axis_gaia.append(x_axis_temp[i])
        y_axis_gaia.append(y_axis_temp[i])
        pop_axis.append(i)
x_axis = []
y_axis = []
for i in range(len(x_axis_temp)):
    if i not in pop_axis:
        x_axis.append(x_axis_temp[i])
        y_axis.append(y_axis_temp[i])

black = plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
lightcoral = plt.scatter(x_axis_gaia, y_axis_gaia, s = size, marker = ".", edgecolors = 'lightcoral', alpha = transparency)
plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.legend((lightcoral, black),
           ('Estrelas com designação Gaia ({} estrelas)'.format(len(x_axis_gaia)), 'Estrelas sem designação Gaia ({} estrelas)'.format(len(x_axis))),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=6)

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_showing_gaia.pdf')

# close matplotlib.pyplot as plt object
plt.close()
###########################
# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_ticks.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)
min_Plx = min(Plx_list)

fig, ax = plt.subplots()
transparency = 1
size = 1.5
ax.scatter(x_axis, y_axis, s=0.3, color='black')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
ax.set_title("M(V) x B-V", fontsize=7)
fig.suptitle("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("B - V", fontsize=7)
plt.ylabel("M(V)", fontsize=7)

# tentar colocar nos dois eixos o mesmo tamanho entre os majorticks
print("tentar colocar nos dois eixos o mesmo tamanho entre os majorticks", (decimal.Decimal(0.5)*(abs(min(x_axis)) + abs(max(x_axis))))/(abs(min(y_axis)) + abs(max(y_axis))))

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.125))
ax.xaxis.set_minor_locator(MultipleLocator(0.03125))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# para colocar label no minor axis também
# ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
# ax.yaxis.set_minor_formatter(FormatStrFormatter("%.1f"))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='major', labelsize=3)
# ax.tick_params(axis='both', which='minor', labelsize=2.5, labelcolor='dimgray')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='darkgrey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_ticks.pdf')

# close matplotlib.pyplot as plt object
plt.close()
###########################

###########################
# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_colors.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)
min_Plx = min(Plx_list)

fig, ax = plt.subplots()
transparency = 1
size = 1.5

# definindo as cores
colors = x_axis

# mudar a cor atras do plot
ax.set_facecolor('black')

# criando um cmap customizado
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["blue", "lightblue", "white", "yellow" , "orange", "red", "red", "red", "red", "red", "red", "red"])

ax.scatter(x_axis, y_axis, s=0.3, c=colors, cmap=cmap)

# tentar consertar o gradiente de cores no diagrama
# plt.clim(-0.375, 1.750)

# definindo a barra de cor
# cbar = ax.colorbar(orientation="horizontal", shrink=0.5, extend="both", format="%.3f", aspect=40)
# cbar.ax.tick_params(labelsize=3)
# cbar.set_label(label="índice de cor", size=5)

plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
# ax.set_title("M(V) x B-V", fontsize=7)
fig.suptitle("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("B - V", fontsize=7)
plt.ylabel("M(V)", fontsize=7)

# tentar colocar nos dois eixos o mesmo tamanho entre os majorticks
# print("tentar colocar nos dois eixos o mesmo tamanho entre os majorticks", (decimal.Decimal(0.5)*(abs(min(x_axis)) + abs(max(x_axis))))/(abs(min(y_axis)) + abs(max(y_axis))))

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.125))
ax.xaxis.set_minor_locator(MultipleLocator(0.03125))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# para colocar label no minor axis também
# ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
# ax.yaxis.set_minor_formatter(FormatStrFormatter("%.1f"))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="dimgray", labeltop=True, top=True, labelright=True, right=True, tickdir='out')
# ax.tick_params(axis='both', which='minor', labelsize=2.5, labelcolor='dimgray')

# rotacionar label do eixo x
plt.xticks(rotation=45)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='dimgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_colors.pdf')

# close matplotlib.pyplot as plt object
plt.close()
###########################

########################################################################################################
# Criar o diagrama Hipparcos_errors.pdf numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos.e_Plx, "
               "Hipparcos.Plx "
               "from Hipparcos ")
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

ax.scatter(x_axis, y_axis, s=0.3, color='black')

plt.xlim(min(x_axis) - decimal.Decimal(1.5), max(x_axis) + decimal.Decimal(1.5))
plt.ylim(min(y_axis) - decimal.Decimal(6), max(y_axis) + decimal.Decimal(6))
fig.suptitle("Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
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
ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='darkgrey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_errors.pdf')

# close matplotlib.pyplot as plt object
plt.close()
########################################################################################################

########################################################################################################
# Criar o diagrama Hipparcos_errors_logarithmic_scale.pdf numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos.e_Plx, "
               "Hipparcos.Plx "
               "from Hipparcos ")
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

ax.scatter(x_axis, y_axis, s=0.3, color='black')
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
fig.suptitle("Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("e_Plx (mas)", fontsize=7)
plt.ylabel("Plx (mas)", fontsize=7)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_errors_logarithmic_scale.pdf')

# close matplotlib.pyplot as plt object
plt.close()
########################################################################################################
########################################################################################################
# Criar o diagrama Gaia_errors_logarithmic_scale.pdf numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia.parallax_error, "
               "Gaia.parallax "
               "from Gaia ")
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

ax.scatter(x_axis, y_axis, s=0.3, color='black')
ax.set_yscale('log')
ax.set_xscale('log')
ax.tick_params(labelsize=3)

plt.xlim(min(x_axis) - decimal.Decimal(0.0), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(min(y_axis) - decimal.Decimal(0.0), max(y_axis) + decimal.Decimal(100.0))
fig.suptitle("Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("parallax_error (mas)", fontsize=7)
plt.ylabel("parallax (mas)", fontsize=7)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Gaia_errors_logarithmic_scale.pdf')

# close matplotlib.pyplot as plt object
plt.close()
########################################################################################################

########################################################################################################
# Criar o diagrama Gaia_errors.pdf numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia.parallax_error, "
               "Gaia.parallax "
               "from Gaia ")
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

ax.scatter(x_axis, y_axis, s=0.3, color='black')

plt.xlim(min(x_axis) - decimal.Decimal(0.02), max(x_axis) + decimal.Decimal(0.02))
plt.ylim(min(y_axis) - decimal.Decimal(5.0), max(y_axis) + decimal.Decimal(5.0))
fig.suptitle("Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("parallax_error (mas)", fontsize=7)
plt.ylabel("parallax (mas)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.1/5))
ax.yaxis.set_major_locator(MultipleLocator(50))
ax.yaxis.set_minor_locator(MultipleLocator(10))

# configurar labels dos major e minor ticks de ambos os eixos
ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True, right=True, tickdir='out')

# rotacionar label do eixo x
plt.xticks(rotation=0)

# colocar a grid atras do plot
ax.set_axisbelow(True)

# deixar o axes com aspecto quadrado
ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='darkgrey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Gaia_errors.pdf')

# close matplotlib.pyplot as plt object
plt.close()
########################################################################################################

# Make sure data is committed to the database
connection.commit()

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_white_dwarfs.csv
anas_brancas = ",".join(anas_brancas)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_white_dwarfs_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % anas_brancas)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_unknown.csv
sem_classificacao = ",".join(sem_classificacao)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_unknown_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % sem_classificacao)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_AFG.csv
AFG = ",".join(AFG)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_AFG_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % AFG)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_GK.csv
GK = ",".join(GK)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_GK_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % GK)

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_red_dwarfs.csv
anas_vermelhas = ",".join(anas_vermelhas)
cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''Hipparcos.BD, '''
               '''Hipparcos.CoD, '''
               '''Hipparcos.CPD, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''Hipparcos.SpType '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_red_dwarfs_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % anas_vermelhas)

cursor.close()
connection.close()