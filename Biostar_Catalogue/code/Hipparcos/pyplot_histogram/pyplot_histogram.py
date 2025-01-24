import code.functions.pyplot_histogram as f
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Hipparcos'

"""
Histograma de sigma pi
para as estrelas do Hipparcos 
"""

query = ("select trim({father_table}.Plx)+0, "
         "trim({father_table}.e_Plx)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.Plx > 0.0 and "
         "{father_table}.simbad_DR3 is null "
         ")".format(father_table=father_table))

f.histogram(query, cursor, 'Hipparcos', r'$\sigma_{\pi} \; (mas)$', 3,
            '/Hipparcos/pyplot_histogram/jpg/Hipparcos_Plx_log.jpg',
            yfontsize=8.0, xfontsize=8.0,
            ylog=True, xlog=True,
            xrot=0, yrot=0,
            ylabel_ycoord= 0.45, ylabel_xcoord=-2,
            xlabel_ycoord= 0.5 , xlabel_xcoord=0.5,
            ylabel_fontsize=8.0, xlabel_fontsize=8.0,
            minortickwidth=1)

f.histogram(query, cursor, "CAT1",  r'$\sigma_{\pi} \; (mas)$', 9,
            '/Hipparcos/pyplot_histogram/jpg/Hipparcos_Plx.jpg',
            yfontsize=8.0, xfontsize=8.0,
            xrot=0, yrot=0,
            ylabel_ycoord= 0.45, ylabel_xcoord=-2,
            xlabel_ycoord= 0.5 , xlabel_xcoord=0.5,
            ylabel_fontsize=8.0, xlabel_fontsize=8.0,
            minortickwidth=1,
            yticks_not_heights=True, yticks_step=1000)

cursor.close()
connection.close()