from flask import Flask, render_template
import mysql.connector
import math
import itertools
import matplotlib.pyplot
import numpy as np
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')

cursor = connection.cursor()

app = Flask(__name__, static_folder='/home/h/Área de trabalho/Catalogo_GAIA/static')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tabela_de_dados/")
def tabela_de_dados():
    cursor.execute("select numero_ordinal_do_registro, designation, ruwe, parallax, parallax_error, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, teff_gspphot, teff_gspphot_lower, teff_gspphot_upper, logg_gspphot, logg_gspphot_lower, logg_gspphot_upper, mh_gspphot, mh_gspphot_lower, mh_gspphot_upper, distance_gspphot, distance_gspphot_lower, distance_gspphot_upper from Source order by numero_ordinal_do_registro")
    value = cursor.fetchall()

    # não são produtos
    numero_ordinal_do_registro = []
    designation = []
    ruwe = []
    parallax = []
    parallax_error = []
    phot_g_mean_mag = []
    phot_bp_mean_mag = []
    phot_rp_mean_mag = []
    teff_gspphot = []
    teff_gspphot_lower = []
    teff_gspphot_upper = []
    logg_gspphot = []
    logg_gspphot_lower = []
    logg_gspphot_upper = []
    mh_gspphot = []
    mh_gspphot_lower = []
    mh_gspphot_upper = []
    distance_gspphot = []
    distance_gspphot_lower = []
    distance_gspphot_upper = []

    for star in value:
        numero_ordinal_do_registro.append(star[0])
        designation.append(star[1])
        ruwe.append(star[2])
        parallax.append(star[3])
        parallax_error.append(star[4])
        phot_g_mean_mag.append(star[5])
        phot_bp_mean_mag.append(star[6])
        phot_rp_mean_mag.append(star[7])
        teff_gspphot.append(star[8])
        teff_gspphot_lower.append(star[9])
        teff_gspphot_upper.append(star[10])
        logg_gspphot.append(star[11])
        logg_gspphot_lower.append(star[12])
        logg_gspphot_upper.append(star[13])
        mh_gspphot.append(star[14])
        mh_gspphot_lower.append(star[15])
        mh_gspphot_upper.append(star[16])
        distance_gspphot.append(star[17])
        distance_gspphot_lower.append(star[18])
        distance_gspphot_upper.append(star[19])


    # produtos
    indice_de_cor = []
    mg = []
    erro_de_mg = []
    mg_mais = []
    mg_menos = []
    mrp = []
    mrp_mais = []
    mrp_menos = []
    erro_de_mrp = []
    erro_de_distancia = []
    erro_de_teff = []
    erro_de_logg = []
    erro_de_mh = []

    cont = 0
    for star in value:
        indice_de_cor.append(star[6] - star[7])
        mg.append(star[5] + 5 + 5*math.log((star[3])/1000, 10))
        mg_mais.append(star[5] + 5 + 5*math.log((star[3]+star[4])/1000, 10))
        mg_menos.append(star[5] + 5 + 5 * math.log((star[3] - star[4])/1000, 10))
        erro_de_mg.append((abs(mg[cont] - mg_mais[cont]) + abs(mg[cont] - mg_menos[cont]))/2)
        mrp.append(star[7] + 5 + 5*math.log((star[3])/1000, 10))
        mrp_mais.append(star[7] + 5 + 5*math.log((star[3] + star[4])/1000, 10))
        mrp_menos.append(star[7] + 5 + 5 * math.log((star[3] - star[4])/1000, 10))
        erro_de_mrp.append((abs(mrp[cont] - mrp_mais[cont]) + abs(mrp[cont] - mrp_menos[cont]))/2)
        erro_de_distancia.append((abs(star[17] - star[18]) + abs(star[17] - star[19]))/2)
        erro_de_teff.append((abs(star[8] - star[9]) + abs(star[8] - star[10]))/2)
        erro_de_logg.append((abs(star[11] - star[12]) + abs(star[11] - star[13]))/2)
        erro_de_mh.append((abs(star[14] - star[15]) + abs(star[14] - star[16]))/2)

        cont += 1

    # exportar listas para csv

    rows = zip(numero_ordinal_do_registro, phot_g_mean_mag, parallax, phot_bp_mean_mag, phot_rp_mean_mag, mg, indice_de_cor)
    with open("/home/h/Área de trabalho/Catalogo_GAIA/dados_gaia.csv", "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    return render_template("tabela_de_dados.html", data=(numero_ordinal_do_registro, designation, ruwe, phot_g_mean_mag, phot_rp_mean_mag, indice_de_cor, mg, erro_de_mg, mrp, erro_de_mrp, distance_gspphot, erro_de_distancia, teff_gspphot, erro_de_teff, logg_gspphot, erro_de_logg, mh_gspphot, erro_de_mh), name='Tabela de Dados',zip=zip)

@app.route("/diagramas_gaia/")
def diagramas_gaia():
    cursor.execute("select parallax, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag from Source order by numero_ordinal_do_registro")
    value = cursor.fetchall()

    # não são produtos
    parallax = []
    phot_g_mean_mag = []
    phot_bp_mean_mag = []
    phot_rp_mean_mag = []

    # são produtos
    mg = []
    mrp = []
    indice_de_cor = []

    cont = 0
    for star in value:
        parallax.append(star[0])
        phot_g_mean_mag.append(star[1])
        phot_bp_mean_mag.append(star[2])
        phot_rp_mean_mag.append(star[3])

        mg.append(phot_g_mean_mag[cont] + 5 + 5*math.log((parallax[cont])/1000, 10))
        mrp.append(phot_rp_mean_mag[cont] + 5 + 5 * math.log((parallax[cont])/1000, 10))
        indice_de_cor.append(phot_bp_mean_mag[cont] - phot_rp_mean_mag[cont])
        cont += 1

    transparency = 1
    size = 1.5

    matplotlib.pyplot.scatter(indice_de_cor, mg, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(0, 4.2)
    matplotlib.pyplot.ylim(15, 0.3)
    matplotlib.pyplot.title("M(G) x índice de cor")
    matplotlib.pyplot.ylabel("M(G)")
    matplotlib.pyplot.xlabel("índice de cor")
    matplotlib.pyplot.savefig('static/images/mg_indice_de_cor.png')
    matplotlib.pyplot.clf()

    matplotlib.pyplot.scatter(indice_de_cor, mrp, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(0, 4.2)
    matplotlib.pyplot.ylim(15, 0.3)
    matplotlib.pyplot.title("M(Rp) x índice de cor")
    matplotlib.pyplot.ylabel("M(Rp)")
    matplotlib.pyplot.xlabel("índice de cor")
    matplotlib.pyplot.savefig('static/images/mrp_indice_de_cor.png')
    matplotlib.pyplot.clf()

    return render_template("diagramas_gaia.html", data=(mg, mrp, indice_de_cor), name='Diagramas GAIA', zip=zip)

@app.route("/diagramas_hipparcos/")
def diagramas_hipparcos():
    cursor.execute("select Vmag, Plx, BTmag, VTmag, B_V, numero_ordinal_do_registro from Source_Hipparcos order by numero_ordinal_do_registro")
    value = cursor.fetchall()

    # não são produtos
    Vmag = []
    Plx = []
    BTmag = []
    VTmag = []
    B_V = []
    numero_ordinal_do_registro = []

    # são produtos
    MVt = []
    MV = []
    BT_VT = []
    B_V_diagrama = []
    numero_ordinal_do_registro_diagrama = []

    cont = 0
    for star in value:
        Vmag.append(star[0])
        Plx.append(star[1])
        BTmag.append(star[2])
        VTmag.append(star[3])
        B_V.append(star[4])
        numero_ordinal_do_registro.append(star[5])

        if(Plx[cont] > 0):
            MVt.append(VTmag[cont] + 5 + 5*math.log(Plx[cont]/1000, 10))
            MV.append(Vmag[cont] + 5 + 5 * math.log(Plx[cont]/1000, 10))
            BT_VT.append(BTmag[cont] - VTmag[cont])
            B_V_diagrama.append(B_V[cont])
            numero_ordinal_do_registro_diagrama.append(numero_ordinal_do_registro[cont])

        cont += 1


    # exportar listas para csv

    rows = zip(numero_ordinal_do_registro_diagrama, MV, B_V_diagrama, MVt, BT_VT)
    with open("/home/h/Área de trabalho/Catalogo_GAIA/dados_hipparcos.csv", "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


    transparency = 1
    size = 1.5

    matplotlib.pyplot.scatter(B_V_diagrama, MV, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(-1, 6)
    matplotlib.pyplot.ylim(18, -16)
    matplotlib.pyplot.title("M(V) x B-V")
    matplotlib.pyplot.ylabel("M(V)")
    matplotlib.pyplot.xlabel("B-V")
    matplotlib.pyplot.savefig('static/images/MV_B_V.png')
    matplotlib.pyplot.clf()

    matplotlib.pyplot.scatter(BT_VT, MVt, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(-1, 7)
    matplotlib.pyplot.ylim(18, -20)
    matplotlib.pyplot.title("M(Vt) x BT-VT")
    matplotlib.pyplot.ylabel("M(Vt)")
    matplotlib.pyplot.xlabel("BT-VT")
    matplotlib.pyplot.savefig('static/images/MVt_BT_VT.png')
    matplotlib.pyplot.clf()

    return render_template("diagramas_hipparcos.html", data=(MV, B_V_diagrama, MVt, BT_VT, numero_ordinal_do_registro_diagrama), name='Diagramas Hipparcos', zip=zip)

if __name__ == "__main__":
    app.run(debug=True)