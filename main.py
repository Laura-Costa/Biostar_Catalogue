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
    cursor.execute("select * from Produto_Gaia")
    value = cursor.fetchall()

    return render_template("diagramas_gaia.html", data=value, name='Diagramas GAIA')


@app.route("/diagramas_hipparcos/")
def diagramas_hipparcos():
    cursor.execute("select * from Produto_Hipparcos")
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
    return render_template("diagramas_hipparcos.html", data=value, name='Diagramas Hipparcos')

if __name__ == "__main__":
    app.run(debug=True)