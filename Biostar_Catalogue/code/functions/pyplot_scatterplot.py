import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import math

def scatterplot(cursor, query, query_emphasis, colors, hds,
                ymargim_bottom, ymargim_upper, xmargim_bottom, xmargim_upper, xlabel, ylabel,
                y_num_labels, x_num_labels, path, suptitle, xrot=0, xlog=False, ylog=False,
                labelsize=2, y_dp = 5, x_dp = 5, fontsize=7,
                error_bars=False, lgnd_loc='best', color='black'):
    cursor.execute(query)
    value = cursor.fetchall()

    simbad_HD_list = []
    parallax_list = []
    x_axis = []
    y_axis = []

    size = 8.0

    for (simbad_HD_value, parallax_value, x_value, y_value) in value:
        parallax_list.append(parallax_value)
        if len(hds)!= 0: # hds é a lista da 18 scorpii e anãs k
            if simbad_HD_value not in hds:
                simbad_HD_list.append(simbad_HD_value)
                x_axis.append(x_value)
                y_axis.append(y_value)
        else:
            simbad_HD_list.append(simbad_HD_value)
            x_axis.append(x_value)
            y_axis.append(y_value)

    min_parallax = min(parallax_list)

    fig, ax = plt.subplots()
    ax.scatter(x_axis, y_axis, s=size, color=color, edgecolor='none', marker='o', zorder=2)
    # configurando as dimensões de axes
    plt.xlim(min(x_axis) - xmargim_bottom, max(x_axis) + xmargim_upper)
    plt.ylim(min(y_axis) - ymargim_bottom, max(y_axis) + ymargim_upper)

    plt.suptitle(suptitle, fontsize=8, horizontalalignment='center')
    plt.title("{} estrelas em um raio de {:.4f} parsecs (π ≥ {:.4f}'')".format(len(value), 1.0 / (
                min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)

    if xlog and ylog:
        max_parallax = max(x_axis)
        min_parallax_error = min(y_axis)
        max_parallax_error = max(y_axis)

        ax.set_yscale('log')
        ax.set_xscale('log')

        # aqui você configura os minor ticks do jeito que quiser
        ax.tick_params(axis='both', left=True, right=True, bottom=True, top=True, labelleft=True, labelright=True,
                       labelbottom=True, labeltop=True, which='both', labelsize=labelsize)

        # aqui você remove os major ticks e major labels que vêm por default
        ax.tick_params(axis='both', left=False, right=False, bottom=False, top=False, labelleft=False, labelright=False,
                       labelbottom=False, labeltop=False, which='major')

        # aqui você exige que apareçam os labels de minor ticks (eixo y)
        ax.yaxis.set_minor_formatter(FormatStrFormatter("%.{}f".format(y_dp)))
        ax.set_yticks(np.logspace(math.log10(min_parallax_error - 0.0),
                                  math.log10(max_parallax_error + 1.0), num=y_num_labels, base=10.0), minor=True)

        # aqui você exige que apareçam os labels de minor ticks (eixo x)
        ax.xaxis.set_minor_formatter(FormatStrFormatter("%.{}f".format(x_dp)))
        ax.set_xticks(np.logspace(math.log10(min_parallax - 1.0),
                                  math.log10(max_parallax + 1.0), num=x_num_labels, base=10.0), minor=True)

        # aqui coloca a grade partindo de minor ticks
        plt.grid(color='darkgray', linestyle='dashed', dashes=(6, 6), which='minor', linewidth=0.2)

    else:
        # definir os intervalos dos minor e major ticks, dos eixos x e eixos y
        ax.xaxis.set_major_locator(MultipleLocator(100.0))
        ax.xaxis.set_minor_locator(MultipleLocator(100.0 / 10))
        ax.yaxis.set_major_locator(MultipleLocator(100))
        ax.yaxis.set_minor_locator(MultipleLocator(100 / 10))

        # configurar labels dos major e minor ticks de ambos os eixos
        ax.tick_params(axis='both', which='both', labelsize=3, color=color, labeltop=True, top=True, labelright=True,
                       right=True, tickdir='out')

        # configurar as caracteristicas da grid
        plt.grid(color='darkgray', linestyle='dashed', dashes=(7, 7), which='major', linewidth=0.2)

    # rotacionar label do eixo x
    plt.xticks(rotation=xrot, minor=True)

    # colocar a grid atras do plot
    ax.set_axisbelow(True)

    # salvar diagrama
    plt.savefig('/home/lh/Documents/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/pyplot_scatterplot/{}'.format(path), dpi=1200)

    # marcar a HD 146233 e as 5 anãs K
    if len(hds) != 0: emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, error_bars, lgnd_loc)

    # close matplotlib.pyplot as plt object
    plt.close()


def emphasis_diagram(ax, cursor, query_emphasis, path, colors, hds, error_bars, lgnd_loc):

    for (HD_value, color) in zip(hds, colors):
        cursor.execute(query_emphasis + "'{}'".format(HD_value))
        value_emphasis = cursor.fetchall()
        print(value_emphasis)
        '''
        if error_bars:
            ax.errorbar(value_emphasis[0][1], value_emphasis[0][2], ms=3.0, color=color, mec='none', fmt='o', elinewidth=0.3, yerr=value_emphasis[0][4],
                        xerr=value_emphasis[0][3], ecolor='blue', label=value_emphasis[0][0])             
        else:'''
        if HD_value == "HD 131976" and "39mas" in path:
            ax.errorbar(value_emphasis[0][1], value_emphasis[0][2], ms=3.0, color=color, mec='none', fmt='o',
                        elinewidth=0.3, yerr=value_emphasis[0][4],
                        xerr=value_emphasis[0][3], ecolor='blue', zorder=4)
        ax.scatter(value_emphasis[0][1], value_emphasis[0][2], s=14, color=color, edgecolor='none', marker='o', zorder=4, label=value_emphasis[0][0])

    # configurar legenda
    lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc=lgnd_loc)

    # configurar tamanho dos marcadores da legenda
    for handle in lgnd.legend_handles:
        if not error_bars:
            handle.set_sizes([25])

    # expor legenda no axes
    lgnd.get_frame()

    # salvar diagrama
    plt.savefig('/home/lh/Documents/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/pyplot_scatterplot/{}'.format(path), dpi=1200)
