import matplotlib.pyplot as plt
import matplotlib
from astropy.constants.codata2014 import alpha
from matplotlib import mlab
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.stats import norm
import numpy as np
import math

def histogram(query, cursor, xlabel, bins, path, yfontsize, xfontsize, rot=0, stdv=False, log=False, yticks_equally_spaced=False,
              xticks_not_edges=False):
    """
    @param cursor: permite ao Python executar comandos SQL
    @param xlabel: rótulo do eixo x e grandeza da qual se quer ver a distribuição
    @param bins: quantidade de bins que o pyplot_histogram terá
    @param path: caminho relativo a partir de output_files onde pyplot_histogram será salvo
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
    (bin_heights, bin_edges, _) = plt.hist(data_list, bins=bins, edgecolor=None, rwidth=7, log=log, zorder=2)
    plt.ylabel('frequência')
    plt.xlabel('{xlabel}'.format(xlabel=xlabel))
    plt.title('{:.4f} ≤ π ≤ {:.4f} mas ({} estrelas)'.format(min_parallax, max_parallax, len(value)))


    # rotacionar label do eixo x
    plt.xticks(rotation=rot)

    # configurar yfontsie e xfotsize
    plt.xticks(fontsize=xfontsize)
    plt.yticks(fontsize=yfontsize)

    # colocar o média e desvio padrão no pyplot_histogram
    (mu, sigma) = norm.fit(data_list)
    plt.axvline(mu, color='red', linestyle='dashed', linewidth=1.0, label=str(r"$\sigma_{medio}$"))
    if(stdv):
        plt.suptitle(r'Histograma de %s: $\sigma_{medio}$=%.5f, desvio padrão=%.3f' %(xlabel, mu, sigma))
        plt.axvline(mu + sigma, color='lightgreen', linestyle='dashed', linewidth=1.5, label=str(r"$\sigma_{medio} \pm$ desvio padrão"))
        plt.axvline(mu - sigma, color='lightgreen', linestyle='dashed', linewidth=1.5)
    else:
        plt.suptitle(r'Histograma de %s: $\sigma_{medio}$ = %.5f' % (xlabel, mu))

    # configurar legenda
    lgnd = plt.legend(facecolor='white', framealpha=1, shadow=True)
    frame = lgnd.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('lightgrey')

    # se eixo y estiver em escala logarítmica, remover ticks no eixo y
    if log and not yticks_equally_spaced:
        # configurações necessárias para colocar os labels só nas alturas dos bins
        ax.tick_params(axis='y', left=False, which='minor', labelleft=False)
        # configurar largura ticks do eixo x e do eixo y
        ax.tick_params(axis='both', which='both', width=0.1)



    # colocar major ticks no eixo y do pyplot_histogram
    # ax.set_yticks(bin_heights)
    # ax.yaxis.set_major_formatter(FormatStrFormatter('%i'))

    # configurar yticks_equally_spaced
    if(yticks_equally_spaced):
        ax.yaxis.set_major_formatter( lambda x, pos: f'{x:g}')
        ax.tick_params(axis='y', which='minor', left=False)
        #ax.set_ylim(ymin=min(data_list))
        # aqui você configura os minor ticks do jeito que quiser
        #ax.tick_params(axis='y', left=True, right=True, bottom=True, top=True, labelleft=True, labelright=True,
        #               labelbottom=True, labeltop=True, which='minor', labelsize=2)

        # aqui você remove os major ticks e major labels que vêm por default
        #ax.tick_params(axis='y', left=False, right=False, bottom=False, top=False, labelleft=False, labelright=False,
        #               labelbottom=False, labeltop=False, which='major')

        ax.yaxis.set_major_formatter(FormatStrFormatter("%.0f"))
        #ax.set_yticks(np.logspace(math.log10(min(bin_heights) - 0.0),
        #                          math.log10(max(bin_heights) + 1.0), num=50, base=10.0), minor=True)
    else:
        # colocar major ticks no eixo y do pyplot_histogram
        ax.set_yticks(bin_heights)
        ax.yaxis.set_major_formatter(FormatStrFormatter('%i'))

    if(xticks_not_edges):
        ax.xaxis.set_major_formatter( lambda x, pos: f'{x:g}')
        ax.tick_params(axis='x', which='minor', left=False)
        ax.xaxis.set_major_formatter(FormatStrFormatter("%if"))
    else:
        # cofigurar major ticks no eixo x do pyplot_histogram
        ax.set_xticks(bin_edges)
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    # colocar a grid
    plt.grid(color='grey', linestyle='solid', which='major', linewidth=0.1, axis='y', zorder=0)

    # salvar figura
    plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files{path}".format(path=path))

    # fechar p matplotlib.pyplot
    plt.close()


