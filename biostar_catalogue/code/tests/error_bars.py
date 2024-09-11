import mysql.connector
import pandas as pd
import os
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar diagrama do CAT2 Plx_versus_parallax_simbad.pdf

cursor.execute('''select TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax)+0 as simbad_parallax, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax_error)+0 '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and ''' 
               '''(designation_DR3 is not null or '''
               '''designation_DR2 is not null or '''
               '''designation_DR1 is not null) ''')

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

plt.errorbar(x_axis, y_axis, yerr=e_Plx_list, fmt='o')
plt.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/diagram/Plx_versus_parallax_simbad.pdf")

cursor.close()
connection.close()