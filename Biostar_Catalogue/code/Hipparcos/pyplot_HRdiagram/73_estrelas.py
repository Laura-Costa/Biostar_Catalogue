import mysql.connector
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

linewidths = 2
axislinewidths = 2
lenticks = 6

rc('font', family='sans-serif', size=15)
rc('xtick.major', size=lenticks)
rc('xtick.minor', size=lenticks * 2 / 3)
rc('ytick.minor', size=lenticks)
rc('ytick.minor', size=lenticks * 2 /3)
rc('lines', linewidth=linewidths)
rc('lines', linewidth=axislinewidths)

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

path = '/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/73_estrelas.txt'
_73_stars = "("

with open(path) as file:

    print('file opened successfully')
    cont = 0
    nrows = sum( 1 for line in file if '--' not in line and 'HIP' not in line)

    # reset to the beginning of the file
    file.seek(0)

    for line in file:

      if '--' in line or 'HIP' in line:
        continue

      cont += 1
      if cont != nrows:
          _73_stars += "{}, ".format(line.rstrip())
      else:
          _73_stars += "{})".format(line.rstrip())
    file.close()

def plot_colored_stars(axis, x, y):

  # map the HD of the 6 k-dwarfs to their HIPs and plot colors
  k_dwarfs = {
              '4628':['3765', 'red'],
              '16160':['12114', 'magenta'],
              '32147':['23311', 'lime'],
              '146233':['79672', 'deepskyblue'],
              '191408':['99461', 'gold'],
              '219134':['114622', 'chocolate']
             }

  for hd in k_dwarfs.keys():

    query = ("SELECT hip." + x + ", "
            "hip." + y + " "
            "FROM public_hipparcos_product AS hip "
            "WHERE hip.hip IN (" + k_dwarfs[hd][0] + ") AND "
            "hip." + x + " IS NOT NULL AND "
            "hip." + y + " IS NOT NULL "
            )

    cursor.execute(query)
    value = cursor.fetchall()

    # stars without data do not go to legend
    print(len(value[0]))
    if len(value[0]) != 2:
      continue

    axis.scatter([value[0][0]], [value[0][1]], s=size, c=k_dwarfs[hd][1], label='HD ' + hd)

# main

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,7))
size = 100.0
fontsize = 10

# hrd - v versus b_v

query = (
         "SELECT hip.mv, "
         "hip.b_v "
         "FROM public_hipparcos_product as hip "
         "WHERE hip.mv IS NOT NULL AND "
         "hip.b_v IS NOT NULL AND "
         "hip.hip IN " + _73_stars
        )

cursor.execute(query)
value = cursor.fetchall()

for (b_v, mv) in value:
    ax1.scatter([b_v], [mv], s=size, c='black')

n1 = len(value)

plot_colored_stars(ax1, 'b_v', 'mv')

# set text label

ax1.set_xlabel(r'$(B-V) \; [mag]$')
ax1.set_ylabel(r'$M_V \; [mag]$')
ax1.set_title('{} stars'.format(n1))
ax1.invert_yaxis()

# show legend on diagram
lgnd = ax1.legend(loc='lower left', fontsize=fontsize, shadow=True)

# increase legend circles size
for handle in lgnd.legend_handles:
  handle.set_sizes([80])

plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/pyplot_HRdiagram/jpg/diagramas.jpg', dpi=1200)

# fechar o cursor
cursor.close()

# fechar a conexão
connection.close()