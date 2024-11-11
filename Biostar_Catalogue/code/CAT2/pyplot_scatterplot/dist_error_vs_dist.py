import mysql.connector
import code.functions.pyplot_HRdiagram as f
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FormatStrFormatter)

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
hds = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def diagram(cursor, query, query_emphasis, colors, hds, path, xgap, ygap, xlabel, ylabel, markersize, xmargin_left, xmargin_right, ymargin_upper, ymargin_bottom, suptitle, xrot=0, redx=-1, redy=-1, error_bars=False, minortickwidth=0.5, majortickwidth=0.5, dp = -1, axeslabelsize=6):

    fig, ax = plt.subplots()
    cursor.execute(query)

    value = cursor.fetchall()
    x_axis = []
    y_axis = []


    for (x_value, y_value) in value:
        x_axis.append(x_value)
        y_axis.append(y_value)
    """
    # reta y = x
    ax.axline((0, 0), slope=1, linewidth=0.5, color='red', label='y = x') # label='f(x) = x',
    """

    ax.scatter(x_axis, y_axis, s=markersize, color='black', edgecolor='none', marker='o', zorder=3)


    plt.ylim(min(y_axis) - ymargin_bottom, max(y_axis) + ymargin_upper)
    plt.xlim(min(x_axis) - xmargin_left, max(x_axis) + xmargin_right)


    ax.set_title("{}: {} estrelas ".format(suptitle,len(value), fontsize=7.5, y=1.07))
    plt.xlabel(xlabel, fontsize=axeslabelsize)
    plt.ylabel(ylabel, fontsize=axeslabelsize)

    # definir os intervalos de major e minor ticks
    ax.xaxis.set_major_locator(MultipleLocator(xgap))
    ax.xaxis.set_minor_locator(MultipleLocator(xgap/5))
    ax.yaxis.set_major_locator(MultipleLocator(ygap))
    ax.yaxis.set_minor_locator(MultipleLocator(ygap/5))

    # configurar ambos os axis (xaxis e yaxis) com labels com dp (decimal_places) casas decimais
    if dp != -1:
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.{}f'.format(dp)))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.{}f'.format(dp)))

    # configurar labels do major e minor ticks de ambos os eixos
    ax.tick_params(axis='both', which='both', labelsize=8, color='black', labeltop=True, top=True,
                                                                          labelright=True, right=True,
                                                                          tickdir='out')

    # configurar largura dos minor ticks dos eixos x e y
    ax.tick_params(axis='both', which='minor', width=minortickwidth)

    # configurar largura dos major ticks dos eixos x e y
    ax.tick_params(axis='both', which='major', width=majortickwidth)

    # rotacionar label do eixo x
    plt.xticks(rotation=0)

    # configurar uma major grid atrás do plot
    plt.grid(color='gray', linestyle='dashed', dashes=(2, 2), which='major', linewidth=0.4, zorder=1)

    # configurar uma minor grid atrás do plot
    plt.grid(color='lightgrey', linestyle='dashed', dashes=(2,2), which='minor', linewidth=0.1, zorder=1)

    # rotacionar label do eixo x
    plt.xticks(rotation=xrot)

    # salvar a figura em várias extensões diferentes
    for ext in ['jpg', 'eps', 'pdf', 'jpeg', 'svg', 'png']:
        temp_path = path.replace("#", ext)
        plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + temp_path, dpi=1200)

    # fechar plt
    plt.close()

def sql_query(y_axis, x_axis):
    father_table = 'Gaia'
    son_table = 'Gaia_product'

    query = ("select trim({father_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "{father_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "( "
             "distance_gspphot <= 20.000 "
             "or "
             "(distance_gspphot > 20.000 and (distance_gspphot - distance_gspphot_error <= 20.000)) "
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
fazer o diagrama de distance_gspphot_error x distance_gspphot

(query, query_emphasis) = sql_query('distance_gspphot_error', 'distance_gspphot')
diagram(cursor, query, query_emphasis, colors, [], 'CAT2/pyplot_scatterplot/#/sigma_dist_vs_dist.#',
          1000.0, 1000.0,
          r'$dist$', r'$σ(dist)$', 8,
          500.0, 500.0, 500.0, 500.0,
          'CAT2', xrot=10, minortickwidth=1.0, majortickwidth=1.3, dp=0,
          axeslabelsize=10)
"""

"""
fazer o diagrama de distance_gspphot_error x phot_g_mean_mag
"""
(query, query_emphasis) = sql_query('distance_gspphot_error', 'phot_g_mean_mag')
diagram(cursor, query, query_emphasis, colors, [], 'CAT2/pyplot_scatterplot/#/sigma_dist_vs_G.#',
          1.0, 1000.0,
          r'$G$', r'$σ(dist)$', 8,
          0.5, 0.5, 500.0, 500.0,
          'CAT2', xrot=0, minortickwidth=1.0, majortickwidth=1.3, dp=0,
          axeslabelsize=10)

# fechar a conexão com o BD
connection.close()