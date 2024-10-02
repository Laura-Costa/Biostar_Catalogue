import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import math

def scatterplot(cursor, query, ymargim_bottom, ymargim_upper, xmargim_bottom, xmargim_upper, xlabel, ylabel, path, suptitle, xrot=0, xlog=False, ylog=False):
    cursor.execute(query)
    value = cursor.fetchall()

    x_axis = []
    y_axis = []

    size = 1.5

    for (parallax_error_value, parallax_value) in value:
        y_axis.append(parallax_error_value)
        x_axis.append(parallax_value)
    min_parallax = min(x_axis)

    fig, ax = plt.subplots()

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    # configurando as dimensões de axes
    plt.xlim(min(x_axis) - xmargim_bottom, max(x_axis) + xmargim_upper)
    plt.ylim(min(y_axis) - ymargim_bottom, max(y_axis) + ymargim_upper)

    plt.suptitle(suptitle, fontsize=8, horizontalalignment='center')
    plt.title("{} estrelas em um raio de {:.4f} parsecs (π ≥ {:.4f}'')".format(len(value), 1.0 / (
                min_parallax / 1000.0), min_parallax / 1000.0), fontsize=5)
    plt.xlabel(xlabel, fontsize=7)
    plt.ylabel(ylabel, fontsize=7)

    if xlog and ylog:
        max_parallax = max(x_axis)
        min_parallax_error = min(y_axis)
        max_parallax_error = max(y_axis)

        ax.set_yscale('log')
        ax.set_xscale('log')

        # aqui você configura os minor ticks do jeito que quiser
        ax.tick_params(axis='both', left=True, right=True, bottom=True, top=True, labelleft=True, labelright=True,
                       labelbottom=True, labeltop=True, which='both', labelsize=2)

        # aqui você remove os major ticks e major labels que vêm por default
        ax.tick_params(axis='both', left=False, right=False, bottom=False, top=False, labelleft=False, labelright=False,
                       labelbottom=False, labeltop=False, which='major')

        # aqui você exige que apareçam os labels de minor ticks (eixo y)
        ax.yaxis.set_minor_formatter(FormatStrFormatter("%.5f"))
        ax.set_yticks(np.logspace(math.log10(min_parallax_error - 0.0),
                                  math.log10(max_parallax_error + 1.0), num=50, base=10.0), minor=True)

        # aqui você exige que apareçam os labels de minor ticks (eixo x)
        ax.xaxis.set_minor_formatter(FormatStrFormatter("%.5f"))
        ax.set_xticks(np.logspace(math.log10(min_parallax - 1.0),
                                  math.log10(max_parallax + 1.0), num=60, base=10.0), minor=True)

        # aqui coloca a grade partindo de minor ticks
        plt.grid(color='darkgray', linestyle='dashed', dashes=(6, 6), which='minor', linewidth=0.2)

    else:
        # definir os intervalos dos minor e major ticks, dos eixos x e eixos y
        ax.xaxis.set_major_locator(MultipleLocator(50.0))
        ax.xaxis.set_minor_locator(MultipleLocator(50.0 / 10))
        ax.yaxis.set_major_locator(MultipleLocator(0.5))
        ax.yaxis.set_minor_locator(MultipleLocator(0.5 / 10))

        # configurar labels dos major e minor ticks de ambos os eixos
        ax.tick_params(axis='both', which='both', labelsize=3, color="black", labeltop=True, top=True, labelright=True,
                       right=True, tickdir='out')

        # configurar as caracteristicas da grid
        plt.grid(color='darkgray', linestyle='dashed', dashes=(7, 7), which='major', linewidth=0.2)

    # rotacionar label do eixo x
    plt.xticks(rotation=xrot, minor=True)

    # colocar a grid atras do plot
    ax.set_axisbelow(True)



    # salvar diagrama
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/pyplot_scatterplot/{}'.format(path))

    # close matplotlib.pyplot as plt object
    plt.close()
