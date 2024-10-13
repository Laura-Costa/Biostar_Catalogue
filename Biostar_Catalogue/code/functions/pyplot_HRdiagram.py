import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

def diagram(cursor, query, query_emphasis, colors, hds, path, xgap, ygap, xlabel, ylabel, size, xmargin, ymargin_upper, ymargin_bottom, suptitle, xrot=0):

    fig, ax = plt.subplots()
    cursor.execute(query)

    value = cursor.fetchall()
    x_axis = []
    y_axis = []
    parallax_list = []

    for (simbad_HD_value, parallax_value, Bp_Rp_value, MRp_value) in value:
        parallax_list.append(parallax_value)
        if len(hds) != 0:
            if simbad_HD_value not in hds:
                x_axis.append(Bp_Rp_value)
                y_axis.append(MRp_value)
        else:
            x_axis.append(Bp_Rp_value)
            y_axis.append(MRp_value)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    plt.xlim(min(x_axis) - xmargin, max(x_axis) + xmargin)
    plt.ylim(max(y_axis) + ymargin_bottom, min(y_axis) - ymargin_upper)
    ax.set_title("{}\n{} estrelas em um raio de {:.4f} parsecs\n{:.4f} ≤ π ≤ {:.4f} (mas)".format(suptitle, len(value), 1000.0/min_parallax, min_parallax, max_parallax), fontsize=7, y=1.04)
    plt.xlabel(xlabel, fontsize=7)
    plt.ylabel(ylabel, fontsize=7)

    # definir os intervalos de major e minor ticks
    ax.xaxis.set_major_locator(MultipleLocator(xgap))
    ax.xaxis.set_minor_locator(MultipleLocator(xgap/10))
    ax.yaxis.set_major_locator(MultipleLocator(ygap))
    ax.yaxis.set_minor_locator(MultipleLocator(ygap/10))

    # configurar labels do major e minor ticks de ambos os eixos
    ax.tick_params(axis='both', which='both', labelsize=3, color='black', labeltop=True, top=True,
                                                                          labelright=True, right=True,
                                                                          tickdir='out', width=0.1)

    # colocar o label x=1.7 em vermelho
    print(plt.gca())

    # rotacionar label do eixo x
    plt.xticks(rotation=0)

    # configurar uma grid atrás do plot
    plt.grid(color='grey', linestyle='dashed', dashes=(7,7), which='major', linewidth=0.1)

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
        ax.scatter(value_emphasis[0][1], value_emphasis[0][2], s=size, color=color, edgecolor='none', marker='o', zorder=2, label=value_emphasis[0][0])

    # configurar legenda
    lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='best')

    if path == '/BrightStarSupplement/pyplot_HRdiagram/simbad_MV_simbad_B_V.svg': # a legenda desta figura em específico não foi localizada adequadamente por loc='best'
        lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='lower right')

    # configurar tamanho dos marcadores da legenda
    for handle in lgnd.legend_handles:
        handle.set_sizes([25])

    # expor legenda no axes
    frame = lgnd.get_frame()

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path, dpi=1200)
