import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

stringHIP = "("

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/stars_in_hip_main_dat_with_Dr3_at_Simbad.txt") as file:
    cont = 0
    for line in file:
        cont += 1
        if cont != 114072:
            stringHIP += "'HIP {}', ".format(line.rstrip())
        else:
            stringHIP += "'HIP {}')".format(line.rstrip())

father_table = 'hipparcos'

"""
Histograma de sigma pi
para as estrelas do hipparcos 
sem numero DR3 no Simbad
"""

query = ("select trim({father_table}.Plx)+0, "
         "trim({father_table}.e_Plx)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.Plx > 0.0 and "
         "{father_table}.e_Plx is not null and "
         "{father_table}.HIP not in {stringHIP} "
         ")".format(father_table=father_table, stringHIP=stringHIP))

cursor.execute(query)
value = cursor.fetchall()

e_Plx_list = []

for (Plx_value, e_Plx_value) in value:
    e_Plx_list.append(e_Plx_value)

dataframe = pd.DataFrame(data=e_Plx_list, columns=['e_Plx'])
print(dataframe)

####################
# Histograma duplo:
####################
add = 2.0
fig, (lin, log) = plt.subplots(1, 2, figsize=(6.4+add, 4.8+add))

'''configuração dos ticks'''
xgap = 20
ygap = 20
x_minor_gap = 4
y_minor_gap = 2

# definir os intervalos de major e minor ticks
lin.xaxis.set_major_locator(MultipleLocator(xgap))
lin.xaxis.set_minor_locator(MultipleLocator(xgap / x_minor_gap))
lin.yaxis.set_major_locator(MultipleLocator(ygap))
lin.yaxis.set_minor_locator(MultipleLocator(ygap / y_minor_gap))

# configurar largura dos minor ticks dos eixos x e y
minortickwidth = 1.3
minor_length = 2.8
lin.tick_params(axis='both', which='minor', width=minortickwidth, length=minor_length)

# configurar largura dos major ticks dos eixos x e y
majortickwidth = 1.3
major_length = 5.0
lin.tick_params(axis='both', which='major', width=majortickwidth, length=major_length)

'''Histograma linear'''
dataframe['e_Plx'].hist(grid=False, bins='auto', histtype='step', edgecolor='blue', ax=lin)

'''configuração dos ticks'''
xgap = 20
x_minor_gap = 4

# definir os intervalos de major e minor ticks
log.xaxis.set_major_locator(MultipleLocator(xgap))
log.xaxis.set_minor_locator(MultipleLocator(xgap / x_minor_gap))

# configurar largura dos minor ticks dos eixos x e y
minortickwidth = 1.3
minor_length = 2.8
log.tick_params(axis='both', which='minor', width=minortickwidth, length=minor_length)

# configurar largura dos major ticks dos eixos x e y
majortickwidth = 1.3
major_length = 5.0

'''Histograma logaritmico'''
log.tick_params(axis='both', which='major', width=majortickwidth, length=major_length)

dataframe['e_Plx'].hist(grid=False, bins='auto', histtype='step', edgecolor='darkgreen', log=True, ax=log)
plt.suptitle(r'Estrelas HIP sem número DR3 no Simbad: ${}$'.format(len(e_Plx_list)), fontsize=10, x=0.5)
plt.title(r'Histogramas de $\sigma_{\pi}$', fontsize=10, y=1.05, x=-0.1)
lin.set_xlabel(r'$\sigma_{\pi} \; [mas]$')
lin.set_ylabel(r'$N$')
log.set_xlabel(r'$\sigma_{\pi} \; [mas]$')
log.set_ylabel(r'$N$')
plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/hipparcos/pandas_histogram/jpg/histogramas2.jpg", dpi=1200)

plt.close()

cursor.close()
connection.close()