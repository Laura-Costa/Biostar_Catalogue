import matplotlib.pyplot as plt
import matplotlib
from astropy.constants.codata2014 import alpha
from matplotlib import mlab
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.stats import norm
import numpy as np
import math

def histogram(query, cursor, suptitle, xlabel, bins, path, yfontsize, xfontsize,
              xrot=0, yrot=0,
              stdv=False, ylog=False, xlog=False, yticks_not_heights=False,
              xticks_not_edges=False, yticks_step=None, xticks_step=None,
              ylabel_ycoord=0, ylabel_xcoord=0,
              xlabel_ycoord=0, xlabel_xcoord=0,
              ylabel_fontsize=10, xlabel_fontsize=10, minortickwidth=-1):
    """
    @param cursor: permite ao Python executar comandos SQL
    @param xlabel: rótulo do eixo x e grandeza da qual se quer ver a distribuição
    @param bins: quantidade de bins que o pyplot_histogram terá
    @param path: caminho relativo a partir de output_files onde pyplot_histogram será salvo
    @param xrot: ângulo de rotação dos rótulos do eixo x em graus. Default: rot=0
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
    (bin_heights, bin_edges, _) = plt.hist(data_list, bins=bins, edgecolor='black', rwidth=7, log=ylog, zorder=2)
    if ylog:
        plt.ylabel('frequência (escala logarítmica)', fontsize=ylabel_fontsize, y=ylabel_ycoord, x=ylabel_xcoord)
    else:
        plt.ylabel('frequência', fontsize=ylabel_fontsize, y=ylabel_ycoord, x=ylabel_xcoord)

    plt.xlabel('{xlabel}'.format(xlabel=xlabel), y=xlabel_ycoord, x=xlabel_xcoord, fontsize=xlabel_fontsize)

    # rotacionar label do eixo x
    plt.xticks(rotation=xrot)

    # rotacionar label do eixo y
    plt.yticks(rotation=yrot)

    # configurar yfontsie e xfontsize
    plt.xticks(fontsize=xfontsize)
    plt.yticks(fontsize=yfontsize)

    # colocar a média e desvio padrão no pyplot_histogramylabel_ycoord= 0.45, xlabel_ycoord=-2,
    (mu, sigma) = norm.fit(data_list)
    plt.axvline(mu, color='red', linestyle='dashed', linewidth=1.0, label=str(r"$\langle\,\sigma_{\pi}\,\rangle$"))
    qtde_estrelas = len(value)

    if(stdv):
        plt.suptitle(r'%s: %i estrelas, $\sigma_{\pi}_{medio}$=%.5f (mas), desvio padrão=%.3f' %(suptitle, qtde_estrelas, mu, sigma))
        plt.axvline(mu + sigma, color='lightgreen', linestyle='dashed', linewidth=1.5, label=str(r"$\langle\,\sigma\,\rangle \pm$ desvio padrão"))
        plt.axvline(mu - sigma, color='lightgreen', linestyle='dashed', linewidth=1.5)
    else:
        # ax.set_title(r'{}: {} estrelas $\sigma_{\pi}$'.format(suptitle, qtde_estrelas), fontsize=7)
        plt.suptitle(r'%s: $%i$ estrelas, $\langle\,\sigma_{\pi}\,\rangle = %.5f \; (mas)$' % (suptitle, qtde_estrelas, mu), fontsize=7, x=0.5)
        plt.title(r'${:.4f} \; ≤ \; π \; ≤ \; {:.4f} \; (mas)$'.format(min_parallax, max_parallax), fontsize=7, x=0.5, y=1.04)

    # configurar legenda
    lgnd = plt.legend(facecolor='white', framealpha=1, shadow=True)
    frame = lgnd.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('lightgrey')

    # se o eixo y estiver em escala logarítmica, remover ticks no eixo y
    if ylog and not yticks_not_heights:
        # configurações necessárias para colocar os labels só nas alturas dos bins
        ax.tick_params(axis='y', left=False, which='minor', labelleft=False)
        # configurar largura ticks do eixo x e do eixo y
        ax.tick_params(axis='both', which='both', width=minortickwidth)

    # configurar yticks_equally_spaced
    if yticks_not_heights and ylog:
        ax.yaxis.set_major_formatter( lambda x, pos: f'{x:g}')
        ax.tick_params(axis='y', which='minor', left=False)
        ax.yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

    elif yticks_not_heights and not ylog:
        ax.set_yticks(range(0, math.ceil(bin_heights.max())+yticks_step, yticks_step))
        ax.tick_params(axis='y', which='minor', left=False)
        ax.yaxis.set_major_formatter(FormatStrFormatter("%.0f"))

    else:
        ax.set_yticks(bin_heights)
        ax.yaxis.set_major_formatter(FormatStrFormatter('%i'))

    if xticks_not_edges:
        # ax.xaxis.set_major_formatter( lambda x, pos: f'{x:g}')
        ax.set_xticks(np.arange(0, max(data_list) + xticks_step, xticks_step))
        ax.tick_params(axis='x', which='minor', left=False)
        ax.tick_params(axis='both', which='both', width=0.1)
        ax.xaxis.set_major_formatter(FormatStrFormatter("%.2f"))
    else:
        # cofigurar major ticks no eixo x do pyplot_histogram
        ax.set_xticks(bin_edges)
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    # colocar a grid
    plt.grid(color='grey', linestyle='solid', which='major', linewidth=0.2, axis='y', zorder=0)

    # salvar figura
    plt.savefig("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files{path}".format(path=path), dpi=1200)

    # fechar o matplotlib.pyplot
    plt.close()