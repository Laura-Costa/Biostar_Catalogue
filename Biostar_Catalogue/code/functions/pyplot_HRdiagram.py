import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

def diagram(cursor, query, query_emphasis, colors, HDs, name, xgap, ygap, xlabel, ylabel, size, xmargin, ymargin_upper, ymargin_bottom):

    fig, ax = plt.subplots()
    cursor.execute(query)

    value = cursor.fetchall()
    x_axis = []
    y_axis = []
    parallax_list = []

    for (simbad_HD_value, parallax_value, Bp_Rp_value, MRp_value) in value:
        parallax_list.append(parallax_value)
        if simbad_HD_value not in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134'):
            x_axis.append(Bp_Rp_value)
            y_axis.append(MRp_value)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    plt.xlim(min(x_axis) - xmargin, max(x_axis) + xmargin)
    plt.ylim(max(y_axis) + ymargin_bottom, min(y_axis) - ymargin_upper)
    fig.suptitle("CAT1: {} estrelas ({:.4f} ≤ π ≤ {:.4f})".format(len(value), min_parallax, max_parallax))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # definir os intervalos de major e minor ticks
    ax.xaxis.set_major_locator(MultipleLocator(xgap))
    ax.xaxis.set_minor_locator(MultipleLocator(xgap/10))
    ax.yaxis.set_major_locator(MultipleLocator(ygap))
    ax.yaxis.set_minor_locator(MultipleLocator(ygap/10))

    # configurar labels do major e minor ticks de ambos os eixos
    ax.tick_params(axis='both', which='both', labelsize=3, color='black', labeltop=True, top=True,
                                                                          labelright=True, right=True,
                                                                          tickdir='out')

    # rotacionar label do eixo x
    plt.xticks(rotation=0)

    # configurar uma grid atrás do plot
    plt.grid(color='grey', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.05)

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/pyplot_HRdiagram/' + name, dpi=1200)

    # marcar a HD 146233 e as 5 anãs K
    emphasis_diagram(ax, cursor, query_emphasis, name, colors, HDs, size)

    # fechar plt
    plt.close()

def emphasis_diagram(ax, cursor, query_emphasis, name, colors, HDs, size):

    for (HD_value, color) in zip(HDs, colors):
        cursor.execute(query_emphasis + "'{}'".format(HD_value))
        value_emphasis = cursor.fetchall()
        ax.scatter(value_emphasis[0][1], value_emphasis[0][2], s=size, color=color, edgecolor='none', marker='o', zorder=2, label=value_emphasis[0][0])

    # configurar legenda
    lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='best')

    # configurar tamanho dos marcadores da legenda
    for handle in lgnd.legend_handles:
        handle.set_sizes([25])

    # expor legenda no axes
    frame = lgnd.get_frame()

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/pyplot_HRdiagram/' + name, dpi=1200)
