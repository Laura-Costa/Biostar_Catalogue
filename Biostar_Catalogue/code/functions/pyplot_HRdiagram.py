import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

list_HD = []

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/211_stars.txt") as file:
    for line in file:
        list_HD.append("HD {}".format(line.rstrip()))

def diagram(cursor, query, query_emphasis, colors, hds, path, xgap, ygap, xlabel, ylabel, size, xmargin_left, xmargin_right, ymargin_upper, ymargin_bottom, suptitle, xrot=0, redx=-1, redy=-1, error_bars=False):

    fig, ax = plt.subplots()
    cursor.execute(query)

    value = cursor.fetchall()
    x_axis = []
    y_axis = []
    simbad_HD_list = []
    parallax_list = []
    x_error_list = []
    y_error_list = []

    if not error_bars:
        for (simbad_HD_value, parallax_value, x_value, y_value) in value:
            parallax_list.append(parallax_value)
            if len(hds) != 0: # hds é a lista da 18 scorpi e das anãs k
                if simbad_HD_value not in hds:
                    x_axis.append(x_value)
                    y_axis.append(y_value)
                    simbad_HD_list.append(simbad_HD_value)
            else:
                x_axis.append(x_value)
                y_axis.append(x_value)
                simbad_HD_list.append(simbad_HD_value)
    elif error_bars:
        for (simbad_HD_value, parallax_value, x_value, y_value, x_error_value, y_error_value) in value:
            parallax_list.append(parallax_value)
            if len(hds) != 0: # hds é a lista da 18 scorpi e das anãs k
                if simbad_HD_value not in hds:
                    x_axis.append(x_value)
                    y_axis.append(y_value)
                    simbad_HD_list.append(simbad_HD_value)
                    x_error_list.append(x_error_value)
                    y_error_list.append(y_error_value)
            else:
                x_axis.append(x_value)
                y_axis.append(y_value)
                simbad_HD_list.append(simbad_HD_value)
                x_error_list.append(x_error_value)
                y_error_list.append(y_error_value)

        # reta y = x
        ax.axline((0, 0), slope=1, linewidth=0.5, color='red', label='f(x) = x') # label='f(x) = x',

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    if 'LNA' in path:
        for (simbad_HD_value, x, y) in zip(simbad_HD_list, x_axis, y_axis):
            if x <= 1.500 and y <= 9.00 and simbad_HD_value not in list_HD:
                ax.scatter([x], [y], s=size, color='black', edgecolor='none', marker='o', zorder=2)
            else:
                ax.scatter([x], [y], s=size, color='#95a5a6', edgecolor='none', marker='o', zorder=2)
    elif not error_bars:
        ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)
    elif error_bars:
        ax.errorbar(x_axis, y_axis, ms=2.0, color='black', mec='none', fmt='o', elinewidth=0.3, yerr=y_error_list,
                    xerr=x_error_list, ecolor='blue', zorder=2)

    if "HR" in path: # Se o diagrama é HR, o eixo y é invertido
        plt.ylim(max(y_axis) + ymargin_bottom, min(y_axis) - ymargin_upper)
    else:
        plt.ylim(min(y_axis) - ymargin_bottom, max(y_axis) + ymargin_upper)
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
    if len(hds) != 0: emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, error_bars, size)

    # fechar plt
    plt.close()

def emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, error_bars, size):

    for (HD_value, color) in zip(hds, colors):
        cursor.execute(query_emphasis + "'{}'".format(HD_value))
        value_emphasis = cursor.fetchall()
        '''
        if error_bars:
            ax.errorbar(value_emphasis[0][1], value_emphasis[0][2], ms=4.0, color=color, mec='none', fmt='o', elinewidth=0.3, yerr=value_emphasis[0][4],
                        xerr=value_emphasis[0][3], ecolor='blue', label=value_emphasis[0][0])             
        else:
        '''
        ax.scatter(value_emphasis[0][1], value_emphasis[0][2], s=10, color=color, edgecolor='none', marker='o', zorder=3, label=value_emphasis[0][0])

    # configurar legenda
    lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='best')

    if path == '/BrightStarSupplement/pyplot_HRdiagram/simbad_MV_simbad_B_V.jpg': # a legenda desta figura em específico não foi localizada adequadamente por loc='best'
        lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='lower right')

    # configurar tamanho dos marcadores da legenda
    for handle in lgnd.legend_handles:
        if not error_bars:
            handle.set_sizes([25])

    # expor legenda no axes
    frame = lgnd.get_frame()

    # mudar o tamanho da figura em polegadas
    # plt.gcf().set_size_inches(10.40, 8.80)

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path, dpi=1200)
