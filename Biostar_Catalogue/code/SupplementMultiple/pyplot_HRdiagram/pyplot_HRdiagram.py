import mysql.connector
import code.functions.pyplot_HRdiagram as f

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator, FormatStrFormatter)

def diagram(cursor, query, query_emphasis, colors, hds, path, xgap, ygap, xlabel, ylabel, markersize,
            xmargin_left, xmargin_right, ymargin_upper, ymargin_bottom, suptitle, xrot=0, x_minor_gap=5,
            y_minor_gap=5, dp=2, minortickwidth=1.0, majortickwidth=1.3, xy_labels_fontsize=10, ticklabelsize=10):

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

    ax.scatter(x_axis, y_axis, s=markersize, color='black', edgecolor='none', marker='o', zorder=2)

    def slicedict(d):
        return {k: v for k, v in d.items() if v > 1}

    # contar quantos nomes repetidos tem na lista
    my_dict = {i: ja_plotadas.count(i) for i in ja_plotadas}
    print(slicedict(my_dict))

    plt.ylim(max(y_axis) + ymargin_bottom, min(y_axis) - ymargin_upper)
    plt.xlim(min(x_axis) - xmargin_left, max(x_axis) + xmargin_right)

    ax.set_title("{}: {} estrelas em um raio de {:.4f} parsecs\n{:.4f} ≤ π ≤ {:.4f} (mas)".format(suptitle,
                                                                                                  len(parallax_list),
                                                                                                  1000.0/min_parallax,
                                                                                                  min_parallax,
                                                                                                  max_parallax),
                                                                                                  fontsize=7.5,
                                                                                                  y=1.07)
    plt.xlabel(xlabel, fontsize=xy_labels_fontsize)
    plt.ylabel(ylabel, fontsize=xy_labels_fontsize)

    # definir os intervalos de major e minor ticks
    ax.xaxis.set_major_locator(MultipleLocator(xgap))
    ax.xaxis.set_minor_locator(MultipleLocator(xgap/x_minor_gap))
    ax.yaxis.set_major_locator(MultipleLocator(ygap))
    ax.yaxis.set_minor_locator(MultipleLocator(ygap/y_minor_gap))

    ax.xaxis.set_major_formatter(FormatStrFormatter('%.{}f'.format(dp)))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.{}f'.format(dp)))

    # configurar labels do major e minor ticks de ambos os eixos
    ax.tick_params(axis='both', which='both', labelsize=ticklabelsize, color='black', labeltop=True, top=True,
                                                                          labelright=True, right=True,
                                                                          tickdir='out')

    # configurar largura dos minor ticks dos eixos x e y
    ax.tick_params(axis='both', which='minor', width=minortickwidth)

    # configurar largura dos major ticks dos eixos x e y
    ax.tick_params(axis='both', which='major', width=majortickwidth)

    # rotacionar label do eixo x
    plt.xticks(rotation=xrot)

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

    # marcar a HD 146233 e as 5 anãs K
    if len(hds) != 0: emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, markersize)

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
    lgnd.get_frame()

    # salvar a figura em várias extensões diferentes
    for ext in ['jpg', 'eps', 'pdf', 'jpeg', 'svg', 'png']:
        temp_path = path.replace("#", ext)
        plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + temp_path, dpi=1200)

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(x_axis, y_axis):

    SupplementMultiple_letter = ("select SupplementMultiple.simbad_main_identifier, "
            "Supplement.HD, "
            "trim(SupplementMultiple.simbad_parallax)+0, "
            "trim(SupplementMultiple_product.simbad_{x_axis})+0, "
            "trim(SupplementMultiple_product.simbad_{y_axis})+0 "
            "from Supplement, SupplementMultiple, SupplementMultiple_product "
            "where Supplement.ordinal_number = SupplementMultiple.ordinal_number_Supplement and "
            "SupplementMultiple.ordinal_number = SupplementMultiple_product.ordinal_number and "
            "SupplementMultiple_product.simbad_{x_axis} is not null and "
            "SupplementMultiple_product.simbad_{y_axis} is not null and "
            "SupplementMultiple.simbad_DR3 is null and Supplement.HD_Suffix not like '%/%'".format(x_axis=x_axis, y_axis=y_axis))
            # nenhuma estrela proveniente de uma estrela com / no HD_Suffix do Supplement
            # tem os requisitos necessarios para ser plotada
            # de modo que a restricao que exige que o HD_Suffix nao tenha /
            # (ou seja, so tenha letras) poderia ser retirada

    emphasis = ("select BrightStar.HD, "
             "trim(BrightStar_product.{x_axis})+0, "
             "trim(BrightStar_product.{y_axis})+0 "
             "from BrightStar, BrightStar_product "
             "where BrightStar.HR = BrightStar_product.HR and "
             "BrightStar_product.{x_axis} is not null and "
             "BrightStar_product.{y_axis} is not null and "
             "BrightStar.HD = ".format(x_axis=x_axis, y_axis=y_axis))

    return SupplementMultiple_letter, emphasis

"""
Fazer o diagrama MV x B_V
"""
colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
hds = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

(SupplementMultiple, emphasis) = sql_query('B_V', 'MV')

diagram(cursor, SupplementMultiple, emphasis, colors, hds, 'SupplementMultiple/pyplot_HRdiagram/#/query_around_MV_B_V.#',
          0.20, 3.0,
          r'$B-V$', r'$M(V)$', 13.0,
          0.05, 0.35, 0.50, 2.0,
          'Supplement (query around)', xrot=0, minortickwidth=1.0, majortickwidth=1.3, dp=1,
          xy_labels_fontsize=10,
          x_minor_gap=2, y_minor_gap=10)

# fechar conexão com o BD
connection.close()