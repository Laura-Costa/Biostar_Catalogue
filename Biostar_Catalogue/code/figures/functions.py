import matplotlib.pyplot as plt
import matplotlib
from astropy.constants.codata2014 import alpha
from matplotlib import mlab
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.stats import norm

def histogram(query, cursor, xlabel, bins, path, rot=0, log=False):
    """
    @param cursor: permite ao Python executar comandos SQL
    @param xlabel: rótulo do eixo x e grandeza da qual se quer ver a distribuição
    @param bins: quantidade de bins que o histograma terá
    @param path: caminho relativo a partir de output_files onde histograma será salvo
    @param rot: ângulo de rotação dos rótulos do eixo x em graus. Default: rot=0
    @return: none
    """
    matplotlib.style.use('default') # retirar qualquer configuração prévia de estilo

    cursor.execute(query)
    value = cursor.fetchall()
    parallax_list = []
    data_list = []

    for (parallax_value, data_value) in value:
        parallax_list.append(parallax_value)
        data_list.append(data_value)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    fig, ax = plt.subplots()
    (bin_heights, bin_edges, _) = plt.hist(data_list, bins=bins, edgecolor='black', rwidth=1, log=log, zorder=2)
    plt.ylabel('frequência')
    plt.xlabel('{xlabel}'.format(xlabel=xlabel))
    plt.title('{:.4f} ≤ π ≤ {:.4f} mas ({} estrelas)'.format(min_parallax, max_parallax, len(value)))


    # rotacionar label do eixo x
    plt.xticks(rotation=rot, fontsize=5)
    plt.yticks(fontsize=5)

    # colocar o média e desvio padrão no histograma
    (mu, sigma) = norm.fit(data_list)
    plt.suptitle(r'$\mathrm{Histograma\ de\ %s:}\ \mu=%.3f,\ \sigma=%.3f$' %(xlabel, mu, sigma))
    plt.axvline(mu + sigma, color='lightgreen', linestyle='dashed', linewidth=1.5, label=str(r"$\mu \pm \sigma$"))
    plt.axvline(mu - sigma, color='lightgreen', linestyle='dashed', linewidth=1.5)
    plt.axvline(mu, color='red', linestyle='dashed', linewidth=1.5, label=str(r"$\mu$"))

    # configurar legenda
    lgnd = plt.legend(facecolor='white', framealpha=1, shadow=True)
    frame = lgnd.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('lightgrey')

    # se eixo y estiver em escala logarítmica, remover ticks no eixo y
    if log:
        ax.tick_params(axis='y', left=False, which='minor')

    # colocar major ticks no eixo x do histograma
    ax.set_xticks(bin_edges)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.4f'))

    # colocar major ticks no eixo y do histograma
    ax.set_yticks(bin_heights)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%i'))

    # colocar a grid
    plt.grid(color='lightgrey', linestyle='solid', which='major', linewidth=1.0, axis='y', zorder=0)

    # salvar figura
    plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files{path}".format(path=path))

    # fechar p matplotlib.pyplot
    plt.close()

def diagram(cursor, query, query_emphasis, name, xgap, ygap, xlabel, ylabel, size, xmargin, ymargin):
    cursor.execute(query)
    value = cursor.fetchall()
    x_axis = []
    y_axis = []
    parallax_list = []

    for (parallax_value, Bp_Rp_value, MRp_value) in value:
        parallax_list.append(parallax_value)
        x_axis.append(Bp_Rp_value)
        y_axis.append(MRp_value)

    min_parallax = min(parallax_list)
    max_parallax = max(parallax_list)

    fig, ax = plt.subplots()

    ax.scatter(x_axis, y_axis, s=size, color='black', edgecolor='none', marker='o', zorder=2)

    cursor.execute(query_emphasis)
    value_emphasis = cursor.fetchall()

    if len(value_emphasis) != 0:

        color = ['red', 'deepskyblue', 'goldenrod', 'purple', 'blue', 'darkgreen', 'lime', 'orange', 'magenta']

        for ((id, x_value, y_value), color) in zip(value_emphasis, color):
            ax.scatter([x_value], [y_value], s=7, color=color, edgecolor='none', marker='o', zorder=2, label=id)

        # configurar legenda
        lgnd = plt.legend(scatterpoints=1, shadow=True, fontsize=5, loc='best')

        # configurar tamanho dos marcadores da legenda
        for handle in lgnd.legend_handles:
            handle.set_sizes([40])

        # expor legenda no axes
        frame = lgnd.get_frame()

    plt.xlim(min(x_axis) - xmargin, max(x_axis) + xmargin)
    plt.ylim(max(y_axis) + ymargin, min(y_axis) - ymargin)
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
    plt.xticks(rotation=0   )

    # configurar uma grid atrás do plot
    plt.grid(color='lightgray', linestyle='dashed', dashes=(5,5), which='major', linewidth=0.2)

    # salvar a figura
    plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/diagramas_HR/' + name)



