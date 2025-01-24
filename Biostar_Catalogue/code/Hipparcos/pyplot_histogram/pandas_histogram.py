import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Hipparcos'

"""
Histograma de sigma pi
para as estrelas do Hipparcos 
sem numero DR3 no Simbad
"""

query = ("select trim({father_table}.Plx)+0, "
         "trim({father_table}.e_Plx)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.Plx > 0.0 and "
         "{father_table}.simbad_DR3 is null "
         ")".format(father_table=father_table))

cursor.execute(query)
value = cursor.fetchall()

e_Plx_list = []

for (Plx_value, e_Plx_value) in value:
    e_Plx_list.append(e_Plx_value)

dataframe = pd.DataFrame(data=e_Plx_list, columns=['e_Plx'])
print(dataframe)

"""
# Histograma linear:
dataframe['e_Plx'].hist(grid=False, bins='auto', histtype='step', edgecolor='indigo')
plt.suptitle(r'Estrelas HIP sem número DR3 no Simbad: ${}$'.format(len(e_Plx_list)), fontsize=7, x=0.5)
plt.title(r'Histograma de $\sigma_{\pi}$', fontsize=7, y=1.05, x=0.5)
plt.xlabel(r'$\sigma_{\pi} \; [mas]$')
plt.ylabel('frequência')
plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/pandas_histogram/jpg/hist_lin.jpg", dpi=1200)

# Histograma logaritmico:
dataframe['e_Plx'].hist(grid=False, bins='auto', histtype='step', edgecolor='indigo', log=True)
plt.suptitle(r'Estrelas HIP sem número DR3 no Simbad: ${}$'.format(len(e_Plx_list)), fontsize=7, x=0.5)
plt.title(r'Histograma de $\sigma_{\pi}$', fontsize=7, y=1.05, x=0.5)
plt.xlabel(r'$\sigma_{\pi} \; [mas]$')
plt.ylabel('frequência')
plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/pandas_histogram/jpg/hist_log.jpg", dpi=1200)
"""

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
plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/pandas_histogram/jpg/histogramas.jpg", dpi=1200)

plt.close()

####################
# Histograma duplo alpha:
####################
add = 1.5
fig, (lin, log) = plt.subplots(1, 2, figsize=(6.4+add, 4.8+add))



dataframe['e_Plx'].hist(grid=False, bins='auto', alpha=0.2, color='blue', edgecolor='blue', ax=lin)
dataframe['e_Plx'].hist(grid=False, bins='auto', alpha=0.2, color='green', edgecolor='darkgreen', log=True, ax=log)
plt.suptitle(r'Estrelas HIP sem número DR3 no Simbad: ${}$'.format(len(e_Plx_list)), fontsize=9, x=0.5)
plt.title(r'Histogramas de $\sigma_{\pi}$', fontsize=9, y=1.05, x=-0.1)
lin.set_xlabel(r'$\sigma_{\pi} \; [mas]$')
lin.set_ylabel('frequência')
log.set_xlabel(r'$\sigma_{\pi} \; [mas]$')
log.set_ylabel('frequência')



plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/pandas_histogram/jpg/histogramas_alpha.jpg", dpi=1200)

plt.close()

cursor.close()
connection.close()