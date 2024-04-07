from flask import Flask, render_template
import mysql.connector
import math
import matplotlib.pyplot
import csv


connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tabela_de_dados_gaia/")
def tabela_de_dados_gaia():
    cursor.execute("select record_ordinal_number, designation, round(ra,3), round(declination, 3), round(parallax, 3), round(parallax_error, 3), round(ruwe, 3), round(phot_g_mean_mag, 3), round(phot_bp_mean_mag, 3), round(phot_rp_mean_mag, 3), round(teff_gspphot, 3), round(teff_gspphot_lower, 3), round(teff_gspphot_upper, 3), round(logg_gspphot, 3), round(logg_gspphot_lower, 3), round(logg_gspphot_upper, 3), round(mh_gspphot, 3), round(mh_gspphot_lower, 3), round(mh_gspphot_upper, 3), round(distance_gspphot, 3), round(distance_gspphot_lower, 3), round(distance_gspphot_upper, 3) from Gaia order by record_ordinal_number")
    value = cursor.fetchall()

    return render_template("tabela_de_dados_gaia.html", data=value, name='Tabela de Dados Gaia')

@app.route("/tabela_de_dados_hipparcos/")
def tabela_de_dados_hipparcos():
    cursor.execute("select record_ordinal_number, HIP, round(Vmag, 3), round(RAdeg, 3), round(DEdeg, 3), round(Plx, 3), round(e_Plx, 3), round(pmRA, 3), round(pmDE, 3), round(BTmag, 3), round(VTmag, 3), round(B_V, 3) from Hipparcos order by record_ordinal_number limit 1774")
    value = cursor.fetchall()

    return render_template("tabela_de_dados_hipparcos.html", data=value, name='Tabela de Dados Hipparcos')

@app.route("/diagramas_gaia/")
def diagramas_gaia():
    cursor.execute("select record_ordinal_number, round(Mg, 3), round(MRp, 3), round(Bp_minus_Rp, 3), round(Mg_error, 4), round(MRp_error, 4) from Gaia_product order by record_ordinal_number")
    value = cursor.fetchall()
    return render_template("diagramas_gaia.html", data=value, name='Diagramas GAIA')

@app.route("/diagramas_hipparcos/")
def diagramas_hipparcos():
    cursor.execute("select round(record_ordinal_number, 3), round(MV, 3), round(MVt, 3), round(B_minus_V, 3), round(BT_minus_VT, 3), round(MV_error, 4), round(MVt_error, 4) from Hipparcos_product order by record_ordinal_number limit 1774")
    value = cursor.fetchall()
    return render_template("diagramas_hipparcos.html", data=value, name='Diagramas Hipparcos')

@app.route("/gaia_intersection_hipparcos/")
def gaia_intersection_hipparcos():
    cursor.execute("select record_ordinal_number_gaia, designation, round(ra,3), round(RAdeg, 3), round(declination, 3), round(DEdeg, 3), round(parallax, 3), round(parallax_error, 3), round(ruwe, 3), round(phot_g_mean_mag, 3), round(phot_bp_mean_mag, 3), round(phot_rp_mean_mag, 3), round(teff_gspphot, 3), round(teff_gspphot_lower, 3), round(teff_gspphot_upper, 3), round(logg_gspphot, 3), round(logg_gspphot_lower, 3), round(logg_gspphot_upper, 3), round(mh_gspphot, 3), round(mh_gspphot_lower, 3), round(mh_gspphot_upper, 3), round(distance_gspphot, 3), round(distance_gspphot_lower, 3), round(distance_gspphot_upper, 3), record_ordinal_number_hipparcos, HIP, round(Vmag, 3), round(Plx, 3), round(e_Plx, 3), round(pmRA, 3), round(pmDE, 3), round(BTmag, 3), round(VTmag, 3), round(B_V, 3) from matched")
    value = cursor.fetchall()
    return render_template("gaia_intersection_hipparcos.html", data=value, name='Gaia ∩ Hipparcos')


@app.route("/hipparcos_minus_gaia/")
def hipparcos_minus_gaia():
    cursor.execute("select record_ordinal_number, HIP, round(Vmag, 3), round(RAdeg, 3), round(DEdeg, 3), round(Plx, 3), round(e_Plx, 3), round(pmRA, 3), round(pmDE, 3), round(BTmag, 3), round(VTmag, 3), round(B_V, 3) from Hipparcos where Hipparcos.record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) limit 2000")
    value = cursor.fetchall()
    return render_template("hipparcos_minus_gaia.html", data=value, name='Hipparcos — Gaia')

@app.route("/gaia_minus_hipparcos/")
def gaia_minus_hipparcos():
    cursor.execute("select record_ordinal_number, designation, round(ra,3), round(declination, 3), round(parallax, 3), round(parallax_error, 3), round(ruwe, 3), round(phot_g_mean_mag, 3), round(phot_bp_mean_mag, 3), round(phot_rp_mean_mag, 3), round(teff_gspphot, 3), round(teff_gspphot_lower, 3), round(teff_gspphot_upper, 3), round(logg_gspphot, 3), round(logg_gspphot_lower, 3), round(logg_gspphot_upper, 3), round(mh_gspphot, 3), round(mh_gspphot_lower, 3), round(mh_gspphot_upper, 3), round(distance_gspphot, 3), round(distance_gspphot_lower, 3), round(distance_gspphot_upper, 3) from Gaia where record_ordinal_number not in (select record_ordinal_number_gaia from matched) order by record_ordinal_number limit 2000")
    value = cursor.fetchall()
    return render_template("gaia_minus_hipparcos.html", data=value, name='Gaia — Hipparcos')

if __name__ == "__main__":
    app.run(debug=True)