import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar o diagrama BrightStar_MV_versus_B_minus_V.pdf

cursor.execute("select TRIM(BrightStar.simbad_parallax) + 0, "
               "TRIM(BrightStar.B_V) + 0, "
               "TRIM(BrightStar.V + 5 + 5*log(10, BrightStar.simbad_parallax/1000.0))+0 as MV "
               "from BrightStar "
               "where BrightStar.simbad_parallax is not null and "
               "BrightStar.B_V is not null and "
               "BrightStar.V is not null ")
value = cursor.fetchall()

x_axis = []
y_axis = []
parallax_list = []

for (simbad_parallax_value, B_V_value, MV_value) in value:
    parallax_list.append(simbad_parallax_value)
    x_axis.append(B_V_value)
    y_axis.append(MV_value)

min_simbad_parallax = min(parallax_list)
print(min_simbad_parallax)

size = 1.5
fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o')

plt.xlim(min(x_axis) - 0.15, max(x_axis) + 0.15)
plt.ylim(max(y_axis) + 0.2, min(y_axis) - 0.2)
fig.suptitle("Bright Star Catalogue: ${}$ estrelas em um raio de ${:.4f}$pc $(π ≥ {:.7f}'')$".format(len(value), 1.0 / (min_simbad_parallax / 1000.0), min_simbad_parallax / 1000.0), fontsize=8)
plt.xlabel("$B-V$ (mag)", fontsize=7)
plt.ylabel("$M(V)$ (mag)", fontsize=7)

# definir os intervalos dos minor e major ticks, dos eixos x e eixos y
ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.xaxis.set_minor_locator(MultipleLocator(0.25/9))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(1/9))

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
plt.savefig('/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/BrightStar/diagram/BrightStar_MV_versus_B_minus_V.pdf')

# close matplotlib.pyplot as plt object
plt.close()

cursor.close()
connection.close()