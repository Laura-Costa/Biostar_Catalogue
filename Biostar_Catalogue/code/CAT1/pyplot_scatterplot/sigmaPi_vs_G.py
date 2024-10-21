import mysql.connector
import code.functions.pyplot_HRdiagram as f
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def diagram(cursor, query, query_emphasis, colors, hds, path, xgap, ygap, xlabel, ylabel, size, xmargin_left, xmargin_right, ymargin_upper, ymargin_bottom, suptitle, xrot=0, redx=-1, redy=-1):

    fig, ax = plt.subplots()
    cursor.execute(query)

    value = cursor.fetchall()
    x_axis = []
    y_axis = []
    simbad_HD_list = []
    parallax_list = []

    for (simbad_HD_value, parallax_value, Bp_Rp_value, MRp_value) in value:
        parallax_list.append(parallax_value)
        if len(hds) != 0: # hds é a lista da 18 scorpi e das anãs k
            if simbad_HD_value not in hds:
                x_axis.append(Bp_Rp_value)
                y_axis.append(MRp_value)
                simbad_HD_list.append(simbad_HD_value)
        else:
            x_axis.append(Bp_Rp_value)
            y_axis.append(MRp_value)
            simbad_HD_list.append(simbad_HD_value)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    plt.ylim(-0.19034899200000002 + 1.1, 4.69095)
    plt.xlim(2.4807318 + 1.1, 21.158179999999998)

    ax.set_title("{}\n{} estrelas em um raio de {:.4f} parsecs\n{:.4f} ≤ π ≤ {:.4f} (mas)".format(suptitle, len(value), 1000.0/min_parallax, min_parallax, max_parallax), fontsize=7, y=1.04)
    plt.xlabel(xlabel, fontsize=7)
    plt.ylabel(ylabel, fontsize=7)

    # definir os intervalos de major e minor ticks
    ax.xaxis.set_major_locator(MultipleLocator(xgap))
    ax.xaxis.set_minor_locator(MultipleLocator(xgap/5))
    ax.yaxis.set_major_locator(MultipleLocator(ygap))
    ax.yaxis.set_minor_locator(MultipleLocator(ygap/5))

    # configurar labels do major e minor ticks de ambos os eixos
    ax.tick_params(axis='both', which='both', labelsize=3, color='black', labeltop=True, top=True,
                                                                          labelright=True, right=True,
                                                                          tickdir='out', width=0.5)

    # rotacionar label do eixo x
    plt.xticks(rotation=0)

    # configurar uma major grid atrás do plot
    plt.grid(color='#aeaeae', linestyle='dashed', dashes=(2, 2), which='major', linewidth=0.1)

    # configurar uma minor grid atrás do plot
    plt.grid(color='lightgrey', linestyle='dashed', dashes=(2,2), which='minor', linewidth=0.1)

    # grid vermelha em Bp-Rp=1.500 e M(G)=7
    if 'MG_Bp_Rp' in path and redx != -1 and redy != -1:
        # a = [tick.gridline for tick in ax.xaxis.get_minor_ticks()] # para se quiser a linha partindo do minor tick
        a = ax.get_xgridlines()
        b = a[redx]
        b.set_color('red')
        b.set_linewidth(0.6)

        a = ax.get_ygridlines()
        b = a[redy]
        b.set_color('red')
        b.set_linewidth(0.6)


    # rotacionar label do eixo x
    plt.xticks(rotation=xrot)

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path, dpi=1200)

    # marcar a HD 146233 e as 5 anãs K
    if len(hds) != 0: f.emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, size)

    # fechar plt
    plt.close()

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis):
    father_table = 'CAT1'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({father_table}.{y_axis})+0 "
             "from {father_table} "
             "where {father_table}.{x_axis} is not null and "
             "{father_table}.{y_axis} is not null".format(father_table=father_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({father_table}.{y_axis})+0 "
                      "from {father_table} "
                      "where {father_table}.{x_axis} is not null and "
                      "{father_table}.{y_axis} is not null and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

def sql_query_zoom(y_axis, x_axis):
    father_table = 'CAT1'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({father_table}.{y_axis})+0 "
             "from {father_table} "
             "where {father_table}.{x_axis} is not null and "
             "{father_table}.{y_axis} is not null and "
             "{father_table}.{y_axis} > 1.00".format(father_table=father_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({father_table}.{y_axis})+0 "
                      "from {father_table} "
                      "where {father_table}.{x_axis} is not null and "
                      "{father_table}.{y_axis} is not null and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

"""
fazer o diagrama de M(Rp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('parallax_error', 'phot_g_mean_mag')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_scatterplot/jpg/parallax_error_G.jpg', 1.25, 0.5, r'$G$', r'$σ(π)$', 2.0, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('parallax_error', 'phot_g_mean_mag')
diagram(cursor, query, query_emphasis, colors, [],'CAT1/pyplot_scatterplot/jpg/parallax_error_G_ampliado.jpg', 1.25, 0.5, r'$G$', 'σ(π)', 6.0, 0.20, 0.20, 0.20, 0.20, 'CAT1: estrelas com σ(π) > 1.0 (mas)')

# fechar a conexão com o BD
connection.close()