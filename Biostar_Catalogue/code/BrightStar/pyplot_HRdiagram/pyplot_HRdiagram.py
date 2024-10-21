import mysql.connector
import code.functions.pyplot_HRdiagram as f

"""
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

def diagram(cursor, query, query_emphasis, colors, hds, path, xgap, ygap, xlabel, ylabel, size, xmargin_left, xmargin_right, ymargin_upper, ymargin_bottom, suptitle, xrot=0):

    fig, ax = plt.subplots()
    cursor.execute(query)

    value = cursor.fetchall()
    x_axis = []
    y_axis = []
    simbad_HD_list = []
    parallax_list = []
    simbad_name_list = []

    for (simbad_name, simbad_HD_value, parallax_value, x_value, y_value) in value:
        parallax_list.append(parallax_value)
        if len(hds) != 0: # hds é a lista da 18 scorpi e das anãs k
            if simbad_HD_value not in hds:
                x_axis.append(x_value)
                y_axis.append(y_value)
                simbad_HD_list.append(simbad_HD_value)
                simbad_name_list.append(simbad_name)
        else:
            x_axis.append(x_value)
            y_axis.append(x_value)
            simbad_HD_list.append(simbad_HD_value)
            simbad_name_list.append(simbad_name)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    plt.ylim(max(y_axis) + ymargin_bottom, min(y_axis) - ymargin_upper)
    plt.xlim(min(x_axis) - xmargin_left, max(x_axis) + xmargin_right)

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

    # rotacionar label do eixo x
    plt.xticks(rotation=xrot)

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path, dpi=1200)

    # marcar a HD 146233 e as 5 anãs K
    if len(hds) != 0: emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, size)

    # fechar plt
    plt.close()

def emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, size):

    for (HD_value, color) in zip(hds, colors):
        cursor.execute(query_emphasis + "'{}'".format(HD_value))
        value_emphasis = cursor.fetchall()
        ax.scatter(value_emphasis[0][1], value_emphasis[0][2], s=10, color=color, edgecolor='none', marker='o', zorder=3, label=value_emphasis[0][0])

    # configurar legenda
    lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='best')

    if path == '/BrightStarSupplement/pyplot_HRdiagram/simbad_MV_simbad_B_V.jpg': # a legenda desta figura em específico não foi localizada adequadamente por loc='best'
        lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='lower right')

    # configurar tamanho dos marcadores da legenda
    for handle in lgnd.legend_handles:
        handle.set_sizes([25])

    # expor legenda no axes
    frame = lgnd.get_frame()

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path, dpi=1200)
"""
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(x_axis, y_axis):

    query = ("(select BrightStar.HD, "
             "trim(BrightStar.simbad_parallax)+0, "
             "trim(BrightStar_product.{x_axis})+0, "
             "trim(BrightStar_product.{y_axis})+0 "
             "from BrightStar, BrightStar_product "
             "where BrightStar.HR = BrightStar_product.HR and "
             "BrightStar_product.{x_axis} is not null and "
             "BrightStar_product.{y_axis} is not null and "
             "BrightStar.simbad_DR3 is null and "
             "BrightStar.ADS_Comp is null) "
             "union all "
             "select BrightStar.HD, "
             "trim(BrightStarMultiple.simbad_paralax)+0, "
             "trim(BrightStarMultiple_product.{x_axis})+0, "
             "trim(BrightStarMultiple_product.{y_axis})+0, "
             "from BrightStar, BrightStarMultiple, BrightStarMultiple_product "
             "where BrightStar.HR = BrightStarMultiple.HR and "
             "BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
             "BrightStarMultiple_product.{x_axis} is not null and "
             "BrightStarMultiple_product.{y_axis} is not null and "
             "BrightStarMultiple.simbad_DR3 is not null".format(x_axis=x_axis, y_axis=y_axis))

    query_emphasis = ("(select BrightStar.HD, "
             "trim(BrightStar.simbad_parallax)+0, "
             "trim(BrightStar_product.{x_axis})+0, "
             "trim(BrightStar_product.{y_axis})+0 "
             "from BrightStar, BrightStar_product "
             "where BrightStar.HR = BrightStar_product.HR and "
             "BrightStar_product.{x_axis} is not null and "
             "BrightStar_product.{y_axis} is not null".format(x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

"""
Fazer o diagrama MV x B_V
"""
colors = ['deepskyblue', 'red', 'magenta', 'lime', 'gold', 'chocolate']
hds = ['HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134']

(query, query_emphasis) = sql_query('B_V', 'MV')
f.diagram(cursor, query, query_emphasis, colors, hds, '/BrightStar/pyplot_HRdiagram/MV_B_V.svg', 0.125, 1.0, r'$B-V$', r'$M(V)$', 6.0, 0.20, 2.0, 2.0, 'Objetos do Bright Star sem designação Gaia DR3 no Simbad')

"""
Fazer o diagrama simbad_MV x simbad_B_V 
"""
colors = ['deepskyblue', 'red', 'lime', 'gold', 'chocolate']
hds = ['HD 146233', 'HD 4628', 'HD 32147', 'HD 191408', 'HD 219134']

(query, query_emphasis) = sql_query('simbad_B_V', 'simbad_MV')
f.diagram(cursor, query, query_emphasis, colors, hds, '/BrightStar/pyplot_HRdiagram/simbad_MV_simbad_B_V.svg', 0.125, 1.0, r'$B-V$ (simbad)', r'$M(V)$ (simbad)', 6.0, 0.20, 2.0, 2.0, 'Objetos do Bright Star sem designação Gaia DR3 no Simbad')

# fechar conexão com o BD
connection.close()