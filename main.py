from flask import Flask, render_template
import mysql.connector
import math
import itertools
import matplotlib.pyplot
import numpy as np

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')

cursor = connection.cursor()

app = Flask(__name__, static_folder='/home/h/PycharmProjects/Catalogo_GAIA/static')
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
        mg.append(star[5] + 5 + 5*math.log(1000*star[3], 10))
        mg_mais.append(star[5] + 5 + 5*math.log(1000*(star[3]+star[4]), 10))
        mg_menos.append(star[5] + 5 + 5 * math.log(1000 * (star[3] - star[4]), 10))
        erro_de_mg.append(((mg[cont] - mg_mais[cont]) + (mg[cont] - mg_menos[cont]))/2)
        mrp.append(star[7] + 5 + 5*math.log(1000*star[3], 10))
        mrp_mais.append(star[7] + 5 + 5*math.log(1000*(star[3] + star[4]), 10))
        mrp_menos.append(star[7] + 5 + 5 * math.log(1000 * (star[3] - star[4]), 10))
        erro_de_mrp.append(((mrp[cont] - mrp_mais[cont]) + (mrp[cont] - mrp_menos[cont]))/2)
        erro_de_distancia.append(((star[17] - star[18]) + (star[17] - star[19]))/2)
        erro_de_teff.append(((star[8] - star[9]) + (star[8] - star[10]))/2)
        erro_de_logg.append(((star[11] - star[12]) + (star[11] - star[13]))/2)
        erro_de_mh.append(((star[14] - star[15]) + (star[14] - star[16]))/2)

        cont += 1
    return render_template("tabela_de_dados.html", data=(numero_ordinal_do_registro, designation, ruwe, phot_g_mean_mag, phot_rp_mean_mag, indice_de_cor, mg, erro_de_mg, mrp, erro_de_mrp, distance_gspphot, erro_de_distancia, teff_gspphot, erro_de_teff, logg_gspphot, erro_de_logg, mh_gspphot, erro_de_mh), name='Tabela de Dados',zip=zip)

@app.route("/diagramas/")
def diagramas():
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

        mg.append(phot_g_mean_mag[cont] + 5 + 5*math.log(1000*parallax[cont], 10))
        mrp.append(phot_rp_mean_mag[cont] + 5 + 5 * math.log(1000 * parallax[cont], 10))
        indice_de_cor.append(phot_bp_mean_mag[cont] - phot_rp_mean_mag[cont])
        cont += 1

    transparency = 1
    size = 1.5

    matplotlib.pyplot.scatter(indice_de_cor, mg, s=size, marker=".", edgecolors='black', alpha=transparency)
    matplotlib.pyplot.xlim(0, 4)
    matplotlib.pyplot.ylim(45, 30)
    matplotlib.pyplot.savefig('static/images/mg_indice_de_cor.png')

    return render_template("diagramas.html", data=(mg, mrp, indice_de_cor), name='Diagramas', zip=zip)

if __name__ == "__main__":
    app.run(debug=True)