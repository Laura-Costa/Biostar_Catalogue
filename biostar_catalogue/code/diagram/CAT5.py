import matplotlib
import mysql.connector
import matplotlib.pyplot as plt
import decimal

from astroquery.simbad import Simbad
from matplotlib.ticker import MultipleLocator

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                     password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

def AFG():
    connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                         password='ic2023', allow_local_infile=True)
    cursor = connection.cursor()
    cursor.execute("select CAT2_product.HIP, "
                   "CAT2_product.B_minus_V, "
                   "CAT2_product.MV "
                   "from CAT2_product, CAT2 "
                   "where CAT2_product.HIP = CAT2.HIP and "
                   "CAT2_product.HIP not in ( "
                   "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
                   "CAT2_product.B_minus_V is not NULL and "
                   "CAT2_product.MV is not NULL")
    value = cursor.fetchall()
    HIP_AFG = ()
    AFG_x_axis = []
    AFG_y_axis = []
    for (HIP_value, B_minus_V_value, MV_value) in value:
        if MV_value <= decimal.Decimal('4.82'):
            HIP_AFG += (HIP_value,)
            AFG_x_axis.append(B_minus_V_value)
            AFG_y_axis.append(MV_value)
    cursor.close()
    connection.close()
    return [HIP_AFG, AFG_x_axis, AFG_y_axis]

def anas_brancas():
    connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                         password='ic2023', allow_local_infile=True)
    cursor = connection.cursor()
    cursor.execute("select CAT2_product.HIP, "
                   "CAT2_product.B_minus_V, "
                   "CAT2_product.MV "
                   "from CAT2_product, CAT2 "
                   "where CAT2_product.HIP = CAT2.HIP and "
                   "CAT2_product.HIP not in ( "
                   "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
                   "CAT2_product.B_minus_V is not NULL and "
                   "CAT2_product.MV is not NULL")
    value = cursor.fetchall()
    HIP_anas_brancas = ()
    anas_brancas_x_axis = []
    anas_brancas_y_axis = []
    for (HIP_value, B_minus_V_value, MV_value) in value:
        if MV_value >= decimal.Decimal(5.91) * B_minus_V_value + decimal.Decimal(9.27):
            HIP_anas_brancas += (HIP_value,)
            anas_brancas_x_axis.append(B_minus_V_value)
            anas_brancas_y_axis.append(MV_value)
    cursor.close()
    connection.close()
    return [HIP_anas_brancas, anas_brancas_x_axis, anas_brancas_y_axis]

def sem_classificacao():
    connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                         password='ic2023', allow_local_infile=True)
    cursor = connection.cursor()
    cursor.execute("select CAT2_product.HIP, "
                   "CAT2_product.B_minus_V, "
                   "CAT2_product.MV "
                   "from CAT2_product, CAT2 "
                   "where CAT2_product.HIP = CAT2.HIP and "
                   "CAT2_product.HIP not in ( "
                   "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
                   "CAT2_product.B_minus_V is not NULL and "
                   "CAT2_product.MV is not NULL")
    value = cursor.fetchall()
    HIP_sem_classificacao = ()
    sem_classificacao_x_axis = []
    sem_classificacao_y_axis = []
    for (HIP_value, B_minus_V_value, MV_value) in value:
        if MV_value <= decimal.Decimal(5.91) * B_minus_V_value + decimal.Decimal(9.27) and MV_value >= decimal.Decimal(5.68) * B_minus_V_value + decimal.Decimal(3.9):
            HIP_sem_classificacao += (HIP_value,)
            sem_classificacao_x_axis.append(B_minus_V_value)
            sem_classificacao_y_axis.append(MV_value)
    cursor.close()
    connection.close()
    return [HIP_sem_classificacao, sem_classificacao_x_axis, sem_classificacao_y_axis]

def GK():
    connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                         password='ic2023', allow_local_infile=True)
    cursor = connection.cursor()
    cursor.execute("select CAT2_product.HIP, "
                   "CAT2_product.B_minus_V, "
                   "CAT2_product.MV "
                   "from CAT2_product, CAT2 "
                   "where CAT2_product.HIP = CAT2.HIP and "
                   "CAT2_product.HIP not in ( "
                   "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
                   "CAT2_product.B_minus_V is not NULL and "
                   "CAT2_product.MV is not NULL")
    value = cursor.fetchall()
    HIP_GK = ()
    GK_x_axis = []
    GK_y_axis = []
    for (HIP_value, B_minus_V_value, MV_value) in value:
        if MV_value <= decimal.Decimal(5.68) * B_minus_V_value + decimal.Decimal(3.9) and MV_value >= 4.82 and MV_value <= decimal.Decimal(-5.26) * B_minus_V_value + decimal.Decimal(14.842):
            HIP_GK += (HIP_value,)
            GK_x_axis.append(B_minus_V_value)
            GK_y_axis.append(MV_value)
    cursor.close()
    connection.close()
    return [HIP_GK, GK_x_axis, GK_y_axis]

def anas_vermelhas():
    connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh',
                                         password='ic2023', allow_local_infile=True)
    cursor = connection.cursor()
    cursor.execute("select CAT2_product.HIP, "
                   "CAT2_product.B_minus_V, "
                   "CAT2_product.MV "
                   "from CAT2_product, CAT2 "
                   "where CAT2_product.HIP = CAT2.HIP and "
                   "CAT2_product.HIP not in ( "
                   "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
                   "CAT2_product.B_minus_V is not NULL and "
                   "CAT2_product.MV is not NULL")
    value = cursor.fetchall()
    HIP_anas_vermelhas = ()
    anas_vermelhas_x_axis = []
    anas_vermelhas_y_axis = []
    for (HIP_value, B_minus_V_value, MV_value) in value:
        if MV_value <= decimal.Decimal(5.68) * B_minus_V_value + decimal.Decimal(3.9) and MV_value >= 4.82 and MV_value >= decimal.Decimal(-5.26) * B_minus_V_value + decimal.Decimal(14.842):
            HIP_anas_vermelhas += (HIP_value,)
            anas_vermelhas_x_axis.append(B_minus_V_value)
            anas_vermelhas_y_axis.append(MV_value)
    cursor.close()
    connection.close()
    return [HIP_anas_vermelhas, anas_vermelhas_x_axis, anas_vermelhas_y_axis]

# Criar o diagrama CAT5_MV_versus_B_minus_V.pdf

cursor.execute("select CAT2.Plx, "
               "CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT2_product, CAT2 "
               "where CAT2.HIP = CAT2_product.HIP and "
               "CAT2_product.HIP not in ( "
               "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
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
plt.scatter(x_axis, y_axis, s=size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT5: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/diagram/CAT5_MV_versus_B_minus_V.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT5_MVt_versus_BT_minus_VT.pdf

cursor.execute("select CAT2.Plx, "
               "CAT2_product.BT_minus_VT, "
               "CAT2_product.MVt "
               "from CAT2, CAT2_product "
               "where CAT2.HIP = CAT2_product.HIP and "
               "CAT2_product.HIP not in ( "
               "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
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

plt.scatter(x_axis, y_axis, s=size, marker = "o", color='black', edgecolors = 'none')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("CAT5: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("Bt - Vt")
plt.ylabel("M(Vt)")
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/diagram/CAT5_MVt_versus_BT_minus_VT.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT5_MV_versus_B_minus_V_edited.pdf

cursor.execute("select CAT2.Plx "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.HIP not in ( "
               "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT2_product.MV is not NULL")
value = cursor.fetchall()

Plx_list = []

for (Plx_value,) in value:
    Plx_list.append(Plx_value)

min_Plx = min(Plx_list)

plt.xlim(-0.3990, 3.7000)
plt.ylim(14.7491, -1.1312)

# equação da reta que passa pelo Sol
# y = 4.82
plt.axhline(y=4.82, color='gray', linestyle=':', linewidth=0.01, zorder=1)

# equação da reta que isola as anãs brancas
# y = 5.91*x + 9.27
plt.plot([-0.4, 1], [6.9, 5.91 * (1) + 9.27], color='gray', linestyle=':', linewidth=0.01, zorder=1)

# equação da reta que isola as estrelas não classificadas
# y = 5.68*x + 3.9
plt.plot([0.17, 1.9], [5.68 * (0.17) + 3.9, 14.7], color='gray', linestyle=':', linewidth=0.01, zorder=1)

# equação da reta que isola as anãs vermelhas
# y = -5.26*x + 14.842
plt.plot([1, 1.9], [-5.26 * (1) + 14.842, -5.26 * (1.9) + 14.842], color='gray', linestyle=':', linewidth=0.01, zorder=1)

# Marcando o Sol
plt.scatter([0.65], [4.82], s=30, marker="o", color='yellow', edgecolors='gold', label="Sol", zorder=2)

plt.title("CAT5: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")

# Colorindo as AFG
(HIP_AFG, x_axis, y_axis) = AFG()
plt.scatter(x_axis, y_axis, s=size, color='blue', edgecolor='none', marker="o", label="AFG ({} estrelas)".format(len(HIP_AFG)))

# Colorindo as anas brancas
(HIP_anas_brancas, x_axis, y_axis) = anas_brancas()
plt.scatter(x_axis, y_axis, s=size, color='dodgerblue', edgecolor='none', marker="o", label="anãs brancas ({} estrelas)".format(len(HIP_anas_brancas)))

# Colorindo as sem classificação
(HIP_sem_classificacao, x_axis, y_axis) = sem_classificacao()
plt.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker="o", label="sem classificação ({} estrelas)".format(len(HIP_sem_classificacao)))

# Colorindo as GK
(HIP_GK, x_axis, y_axis) = GK()
plt.scatter(x_axis, y_axis, s=size, color='coral', edgecolor='none', marker="o", label="GK ({} estrelas)".format(len(HIP_GK)))

# Colorindo as anãs vermelhas
(HIP_anas_vermelhas, x_axis, y_axis) = anas_vermelhas()
plt.scatter(x_axis, y_axis, s=size, color='red', edgecolor='none', marker="o", label="anãs vermelhas ({} estrelas)".format(len(HIP_anas_vermelhas)))

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=7)

# Fazer com que os marcadores da legenda tenham o mesmo tamanho
for handle in lgnd.legend_handles:
    handle.set_sizes([30])

# Expor legenda na figura
frame = lgnd.get_frame()

# Salvar figura
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/diagram/CAT5_MV_versus_B_minus_V_edited.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT5_MV_versus_B_minus_V_showing_gaia_dr3.pdf

cursor.execute("select CAT2_product.HIP, "
               "CAT2.Plx, "
               "CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.HIP not in ( "
               "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT2_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis_temp = [] # lista temporaria para nao plotar o mesmo ponto duas vezes
y_axis_temp = [] # lista temporaria para nao plotar o mesmo ponto duas vezes

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis_temp.append(B_minus_V_value)
    y_axis_temp.append(MV_value)

min_Plx = min(Plx_list)

plt.xlim(min(x_axis_temp) - decimal.Decimal(0.2), max(x_axis_temp) + decimal.Decimal(0.2))
plt.ylim(max(y_axis_temp) + decimal.Decimal(0.5), min(y_axis_temp) - decimal.Decimal(0.5))

# Separar os dados das estrelas que têm Gaia DR3 mas não estão no CAT1
x_axis_gaia_dr3 = []
y_axis_gaia_dr3 = []
hips_com_designacao_dr3 = ()
indices_com_gaia_dr3 = []

for i in range(len(HIP_list)):
    tab = Simbad.query_objectids(HIP_list[i])
    if tab is not None:
        ids = [id for id in tab['ID'] if id.startswith('Gaia DR3')]
        if len(ids) != 0:
            hips_com_designacao_dr3 += (HIP_list[i],)
            # se esse if é True, entao a estrela com identificador HIP_list[i] tem designation Gaia DR3,
            # ela pode estar no Gaia DR3 com paralaxe menor do que 43.47826086956522 (mas) ou
            # nãp possuir paralaxe no Gaia DR3
            x_axis_gaia_dr3.append(x_axis_temp[i])
            y_axis_gaia_dr3.append(y_axis_temp[i])
            indices_com_gaia_dr3.append(i) # esses índices i tem Gaia DR3
x_axis = [] # cor black
y_axis = [] # cor black
for i in range(len(x_axis_temp)):
    if i not in indices_com_gaia_dr3: # nao plotar em black o ponto que sera plotado em red
        x_axis.append(x_axis_temp[i])
        y_axis.append(y_axis_temp[i])

plt.scatter(x_axis, y_axis, s = size, marker = "o", edgecolors = 'none', color='black', label='Estrelas sem designação Gaia DR3 no Simbad ({} estrelas)'.format(len(x_axis)))
plt.scatter(x_axis_gaia_dr3, y_axis_gaia_dr3, s = size, marker = "o", edgecolors = 'none', color='red', label='Estrelas com designação Gaia DR3 no Simbad ({} estrelas)'.format(len(x_axis_gaia_dr3)))
plt.title("CAT5: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")

# Legenda
lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='upper right', markerscale=3)

# Expor legenda na figura
frame = lgnd.get_frame()

plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/diagram/CAT5_MV_versus_B_minus_V_showing_gaia_dr3.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT5_MV_versus_B_minus_V_ticks.pdf

cursor.execute("select CAT2_product.HIP, "
               "CAT2.Plx, "
               "CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.HIP not in ( "
               "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT2_product.MV is not NULL")
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
ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
ax.set_title("M(V) x B-V", fontsize=7)
fig.suptitle("CAT5: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
plt.xlabel("B - V", fontsize=7)
plt.ylabel("M(V)", fontsize=7)

# tentar colocar nos eixos x e y o mesmo espacamento entre os majorticks
# print("tentar colocar nos dois eixos o mesmo espacamento entre os majorticks", (decimal.Decimal(0.5)*(abs(min(x_axis)) + abs(max(x_axis))))/(abs(min(y_axis)) + abs(max(y_axis))))

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
# ax.set_box_aspect(1)

# configurar as caracteristicas da grid
plt.grid(color='darkgrey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)
# plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='minor', linewidth=0.2)

# salvar diagrama
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/diagram/CAT5_MV_versus_B_minus_V_ticks.pdf')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama CAT5_MV_versus_B_minus_V_colors.pdf

cursor.execute("select CAT2_product.HIP, "
               "CAT2.Plx, "
               "CAT2_product.B_minus_V, "
               "CAT2_product.MV "
               "from CAT2_product, CAT2 "
               "where CAT2_product.HIP = CAT2.HIP and "
               "CAT2_product.HIP not in ( "
               "select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) and "
               "CAT2_product.B_minus_V is not NULL and "
               "CAT2_product.MV is not NULL")
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

# definindo as cores
colors = x_axis

# mudar a cor atras do plot
ax.set_facecolor('black')

# criando um cmap customizado
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["blue", "lightblue", "white", "yellow" , "orange", "red", "red", "red", "red", "red", "red", "red"])

ax.scatter(x_axis, y_axis, s=3, c=colors, cmap=cmap, edgecolor='none')

# tentar consertar o gradiente de cores no diagrama
# plt.clim(-0.375, 1.750)

# definindo a barra de cor
# cbar = ax.colorbar(orientation="horizontal", shrink=0.5, extend="both", format="%.3f", aspect=40)
# cbar.ax.tick_params(labelsize=3)
# cbar.set_label(label="índice de cor", size=5)

plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
# ax.set_title("M(V) x B-V", fontsize=7) # comentado porque ficou muito proximo dos upper ticks
fig.suptitle("CAT5: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)), fontsize=8)
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
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/diagram/CAT5_MV_versus_B_minus_V_colors.pdf')

# close matplotlib.pyplot as plt object
plt.close()

cursor.close()
connection.close()