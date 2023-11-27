from flask import Flask, render_template
import mysql.connector
import math
#import itertools
import matplotlib.pyplot
#import numpy as np
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='IC2023ic*')

cursor = connection.cursor()

app = Flask(__name__, static_folder='/home/h/Área de trabalho/Catalogo_GAIA/static')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tabela_de_dados_gaia/")
def tabela_de_dados_gaia():
    cursor.execute("select * from Source_Gaia order by numero_ordinal_do_registro")
    value = cursor.fetchall()

    return render_template("tabela_de_dados_gaia.html", data=value, name='Tabela de Dados Gaia')

@app.route("/tabela_de_dados_hipparcos/")
def tabela_de_dados_hipparcos():
    cursor.execute("select * from Source_Hipparcos order by numero_ordinal_do_registro")
    value = cursor.fetchall()

    return render_template("tabela_de_dados_hipparcos.html", data=value, name='Tabela de Dados Hipparcos')

@app.route("/diagramas_gaia/")
def diagramas_gaia():
    cursor.execute("drop table Produto_Gaia")
    cursor.execute("create table Produto_Gaia (ra double not null, declination double not null, Mg double not null, MRp double not null, Bp_menos_Rp double not null, primary key (ra, declination), foreign key (ra, declination) references Source_Gaia(ra, declination))")
    cursor.execute("select numero_ordinal_do_registro, ra, declination, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_menos_Rp, (abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_Mg, (abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_MRp from Source_Gaia order by numero_ordinal_do_registro")
    value = cursor.fetchall()

    for registro in value:
        ra = registro[1]
        declination = registro[2]
        Mg = registro[3]
        MRp = registro[4]
        Bp_menos_Rp = registro[5]
        erro_de_Mg = registro[6]
        erro_de_MRp = registro[7]
        cursor.execute("insert into Produto_Gaia values ({}, {}, {}, {}, {})".format(ra, declination, Mg, MRp, Bp_menos_Rp))

    '''
    transparency = 1
    size = 1.5

    matplotlib.pyplot.scatter(indice_de_cor, mg, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(0, 4.2)
    matplotlib.pyplot.ylim(15, 0.3)
    matplotlib.pyplot.title("GAIA: {} estrelas dentro de 20pc".format(cont))
    matplotlib.pyplot.ylabel("M(G)")
    matplotlib.pyplot.xlabel("BP-RP")
    matplotlib.pyplot.savefig('static/images/mg_indice_de_cor.png')
    matplotlib.pyplot.clf()

    matplotlib.pyplot.scatter(indice_de_cor, mrp, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(0, 4.2)
    matplotlib.pyplot.ylim(15, 0.3)
    matplotlib.pyplot.title("GAIA: {} estrelas dentro de 20pc".format(cont))
    matplotlib.pyplot.ylabel("M(Rp)")
    matplotlib.pyplot.xlabel("BP-RP")
    matplotlib.pyplot.savefig('static/images/mrp_indice_de_cor.png')
    matplotlib.pyplot.clf()
    '''
    return render_template("diagramas_gaia.html", data=([3], [3], [3]), name='Diagramas GAIA', zip=zip)


@app.route("/diagramas_hipparcos/")
def diagramas_hipparcos():
    cursor.execute("select Vmag, Plx, BTmag, VTmag, B_V, numero_ordinal_do_registro from Source_Hipparcos order by numero_ordinal_do_registro")
    value = cursor.fetchall()
    '''
    transparency = 1
    size = 1.5

    matplotlib.pyplot.scatter(B_V_diagrama, MV, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(-1, 3)
    matplotlib.pyplot.ylim(18, -5)
    matplotlib.pyplot.title("Hipparcos: {} estrelas (π ≥ {}′′)".format(qtde_de_registros_usados, paralaxe_minima))
    matplotlib.pyplot.ylabel("M(V)")
    matplotlib.pyplot.xlabel("B-V")
    matplotlib.pyplot.savefig('static/images/MV_B_V.png')
    matplotlib.pyplot.clf()

    matplotlib.pyplot.scatter(BT_VT, MVt, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(-1, 3)
    matplotlib.pyplot.ylim(18, -5)
    matplotlib.pyplot.title("Hipparcos: {} estrelas (π ≥ {}′′)".format(qtde_de_registros_usados, paralaxe_minima))
    matplotlib.pyplot.ylabel("M(Vt)")
    matplotlib.pyplot.xlabel("BT-VT")
    matplotlib.pyplot.savefig('static/images/MVt_BT_VT.png')
    matplotlib.pyplot.clf()
    '''
    return render_template("diagramas_hipparcos.html", data=([2], [2], [2], [2], [2]), name='Diagramas Hipparcos', zip=zip)

if __name__ == "__main__":
    app.run(debug=True)