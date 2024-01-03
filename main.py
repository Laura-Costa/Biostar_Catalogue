from flask import Flask, render_template
import mysql.connector
import math
#import itertools
import matplotlib.pyplot
#import numpy as np
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')

cursor = connection.cursor()
# app = Flask(__name__, static_folder='/home/h/"Área de trabalho"/Catalogo_GAIA/static/static')
app = Flask(__name__)
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
    cursor.execute("select numero_ordinal_do_registro, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_menos_Rp, (abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_Mg, (abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_MRp from Source_Gaia order by numero_ordinal_do_registro")
    value = cursor.fetchall()
    return render_template("diagramas_gaia.html", data=value, name='Diagramas GAIA')

@app.route("/diagramas_hipparcos/")
def diagramas_hipparcos():
    cursor.execute("select numero_ordinal_do_registro, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_menos_V, BTmag - VTmag as BT_menos_VT, (abs(Vmag + 5 + 5*log(10, Plx/1000) - (Vmag + 5 + 5*log(10, (Plx+e_Plx)/1000))) + abs(Vmag + 5 + 5*log(10, Plx/1000) - (Vmag + 5 + 5*log(10, (Plx-e_Plx)/1000))))/2 as erro_de_MV, (abs(VTmag + 5 + 5*log(10, Plx/1000) - (VTmag + 5 + 5*log(10, (Plx+e_Plx)/1000))) + abs(VTmag + 5 + 5*log(10, Plx/1000) - (VTmag + 5 + 5*log(10, (Plx-e_Plx)/1000))))/2 as erro_de_MVt from Source_Hipparcos where Plx > 0 order by numero_ordinal_do_registro")
    value = cursor.fetchall()
    return render_template("diagramas_hipparcos.html", data=value, name='Diagramas Hipparcos')

if __name__ == "__main__":
    app.run(debug=True)
