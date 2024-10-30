import mysql.connector
# import code.functions.pyplot_HRdiagram as f

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
    ja_plotadas = []

    for (simbad_name, simbad_HD_value, parallax_value, x_value, y_value) in value:
        if simbad_name not in ja_plotadas:
            x_axis.append(x_value)
            y_axis.append(y_value)
            simbad_HD_list.append(simbad_HD_value)
            simbad_name_list.append(simbad_name)
            parallax_list.append(parallax_value)
        ja_plotadas.append(simbad_name)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    def slicedict(d):
        return {k: v for k, v in d.items() if v > 1}

    # contar quantos nomes repetidos tem na lista
    my_dict = {i: ja_plotadas.count(i) for i in ja_plotadas}
    print(slicedict(my_dict))

    plt.ylim(max(y_axis) + ymargin_bottom, min(y_axis) - ymargin_upper)
    plt.xlim(min(x_axis) - xmargin_left, max(x_axis) + xmargin_right)

    ax.set_title("{}\n{} estrelas em um raio de {:.4f} parsecs\n{:.4f} ≤ π ≤ {:.4f} (mas)".format(suptitle,
                                                                                                  len(parallax_list),
                                                                                                  1000.0/min_parallax,
                                                                                                  min_parallax,
                                                                                                  max_parallax),
                                                                                                  fontsize=6,
                                                                                                  y=1.05)
    plt.xlabel(xlabel, fontsize=6)
    plt.ylabel(ylabel, fontsize=6)

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
    plt.xticks(rotation=xrot)

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

    if 'BrightStar' in path: # a legenda desta figura em específico não foi localizada adequadamente por loc='best'
        lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='lower left')

    # configurar tamanho dos marcadores da legenda
    for handle in lgnd.legend_handles:
        handle.set_sizes([25])

    # expor legenda no axes
    frame = lgnd.get_frame()

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path, dpi=1200)

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(x_axis, y_axis):

    BrightStar_plus_Multiple = ("(select BrightStar.simbad_name, "
             "BrightStar.HD, "
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
             "(select BrightStar.simbad_name, "
             "BrightStar.HD, "
             "trim(BrightStarMultiple.simbad_parallax)+0, "
             "trim(BrightStarMultiple_product.simbad_{x_axis})+0, "
             "trim(BrightStarMultiple_product.simbad_{y_axis})+0 "
             "from BrightStar, BrightStarMultiple, BrightStarMultiple_product "
             "where BrightStar.HR = BrightStarMultiple.HR and "
             "BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
             "BrightStarMultiple_product.simbad_{x_axis} is not null and "
             "BrightStarMultiple_product.simbad_{y_axis} is not null and "
             "BrightStarMultiple.simbad_DR3 is null)".format(x_axis=x_axis, y_axis=y_axis))

    BrightStar = ("(select BrightStar.simbad_name, "
             "BrightStar.HD, "
             "trim(BrightStar.simbad_parallax)+0, "
             "trim(BrightStar_product.{x_axis})+0, "
             "trim(BrightStar_product.{y_axis})+0 "
             "from BrightStar, BrightStar_product "
             "where BrightStar.HR = BrightStar_product.HR and "
             "BrightStar_product.{x_axis} is not null and "
             "BrightStar_product.{y_axis} is not null and "
             "BrightStar.simbad_DR3 is null and "
             "BrightStar.ADS_Comp is null)".format(x_axis=x_axis, y_axis=y_axis))

    Multiple = ("select BrightStarMultiple.simbad_name, "
            "BrightStar.HD, "
            "trim(BrightStarMultiple.simbad_parallax)+0, "
            "trim(BrightStarMultiple_product.simbad_{x_axis})+0, "
            "trim(BrightStarMultiple_product.simbad_{y_axis})+0 "
            "from BrightStar, BrightStarMultiple, BrightStarMultiple_product "
            "where BrightStar.HR = BrightStarMultiple.HR and "
            "BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
            "BrightStarMultiple_product.simbad_{x_axis} is not null and "
            "BrightStarMultiple_product.simbad_{y_axis} is not null and "
            "BrightStarMultiple.simbad_DR3 is null".format(x_axis=x_axis, y_axis=y_axis))

    BrightStar_plus_Multiple = ("(select BrightStar.simbad_name, "
                                "BrightStar.HD, "
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
                                "(select BrightStarMultiple.simbad_name, "
                                "BrightStar.HD, "
                                "trim(BrightStarMultiple.simbad_parallax)+0, "
                                "trim(BrightStarMultiple_product.simbad_{x_axis})+0, "
                                "trim(BrightStarMultiple_product.simbad_{y_axis})+0 "
                                "from BrightStar, BrightStarMultiple, BrightStarMultiple_product "
                                "where BrightStar.HR = BrightStarMultiple.HR and "
                                "BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
                                "BrightStarMultiple_product.simbad_{x_axis} is not null and "
                                "BrightStarMultiple_product.simbad_{y_axis} is not null and "
                                "BrightStarMultiple.simbad_DR3 is null)".format(x_axis=x_axis, y_axis=y_axis))

    emphasis = ("select BrightStar.HD, "
             "trim(BrightStar_product.{x_axis})+0, "
             "trim(BrightStar_product.{y_axis})+0 "
             "from BrightStar, BrightStar_product "
             "where BrightStar.HR = BrightStar_product.HR and "
             "BrightStar_product.{x_axis} is not null and "
             "BrightStar_product.{y_axis} is not null and "
             "BrightStar.HD = ".format(x_axis=x_axis, y_axis=y_axis))

    return BrightStar_plus_Multiple, BrightStar, Multiple, emphasis

"""
Fazer o diagrama MV x B_V
"""
colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
hds = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

(BrightStar_plus_Multiple, BrightStar, Multiple, emphasis) = sql_query('B_V', 'MV')
diagram(cursor, Multiple, emphasis, colors, hds, '/BrightStarMultiple/pyplot_HRdiagram/jpg/MV_B_V.jpg', 0.125, 1.0, r'$B-V \; (simbad)$', r'$M(V) \; (simbad)$', 6.0, 0.20, 0.20, 2.0, 2.0, 'Objetos do Query Around (Bright Star) sem designação Gaia DR3 no Simbad', xrot=20)
diagram(cursor, BrightStar, emphasis, colors, hds, '/BrightStar/pyplot_HRdiagram/jpg/MV_B_V.jpg', 0.125, 1.0, r'$B-V$', r'$M(V)$', 6.0, 0.20, 0.20, 1.0, 2.0, 'Objetos do Bright Star com ADS_Comp vazio e sem designação Gaia DR3 no Simbad', xrot=20)
diagram(cursor, BrightStar_plus_Multiple, emphasis, colors, hds, '/BrightStar+BrightStarMultiple/pyplot_HRdiagram/jpg/MV_B_V.jpg', 0.125, 1.0, r'$B-V$', r'$M(V)$', 6.0, 0.20, 0.20, 1.0, 2.0, 'Objetos do Bright Star + Query Around sem designação Gaia DR3 no Simbad', xrot=20)

# fechar conexão com o BD
connection.close()