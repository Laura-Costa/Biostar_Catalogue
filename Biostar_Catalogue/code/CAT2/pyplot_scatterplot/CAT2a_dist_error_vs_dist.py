import mysql.connector
import code.functions.pyplot_HRdiagram as f
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FormatStrFormatter)

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(y_axis, x_axis):
    father_table = 'Gaia'
    son_table = 'Gaia_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "{father_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "( "
             "distance_gspphot <= 20.000 "
             ")".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "{father_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

"""
fazer o diagrama de distance_gspphot_error x distance_gspphot_20pc
"""

colors = ['red', 'lime', 'deepskyblue']
HDs = ['HD 4628', 'HD 32147', 'HD 146233']

(query, query_emphasis) = sql_query('distance_gspphot_error', 'distance_gspphot')
f.diagram(cursor, query, query_emphasis, colors, HDs, 'CAT2/pyplot_scatterplot/#/CAT2a_sigma_dist_vs_dist.#',
          2.0, 0.5,
          r'$dist$', r'$σ(dist)$', 8,
          1.0, 1.0, 0.1, 0.1,
          'CAT2a', xrot=0, minortickwidth=1.0, majortickwidth=1.3, dp=1,
          axeslabelsize=10, lgnd_loc="upper left")

# fechar a conexão com o BD
connection.close()