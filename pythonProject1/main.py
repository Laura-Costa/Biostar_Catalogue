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

@app.route("/gaia/")
def gaia():
    cursor.execute("select Gaia_product.record_ordinal_number, Gaia.designation, round(Gaia_product.Mg, 5), round(Gaia_product.MRp, 5), round(Gaia_product.Bp_minus_Rp, 5), round(Gaia_product.Mg_error, 5), round(Gaia_product.MRp_error, 5) from Gaia_product, Gaia where Gaia_product.record_ordinal_number = Gaia.record_ordinal_number order by Gaia_product.record_ordinal_number")
    produtos = cursor.fetchall()
    cursor.execute("select count(*) from Gaia_product")
    number_of_rows_gaia_plotted = cursor.fetchall()

    cursor.execute("select record_ordinal_number, designation, round(ra,5), round(declination, 5), round(parallax, 5), round(parallax_error, 5), round(ruwe, 5), round(phot_g_mean_mag, 5), round(phot_bp_mean_mag, 5), round(phot_rp_mean_mag, 5), round(teff_gspphot, 5), round(teff_gspphot_lower, 5), round(teff_gspphot_upper, 5), round(logg_gspphot, 5), round(logg_gspphot_lower, 5), round(logg_gspphot_upper, 5), round(mh_gspphot, 5), round(mh_gspphot_lower, 5), round(mh_gspphot_upper, 5), round(distance_gspphot, 5), round(distance_gspphot_lower, 5), round(distance_gspphot_upper, 5) from Gaia order by record_ordinal_number")
    dados = cursor.fetchall()
    cursor.execute("select count(*) from Gaia")
    number_of_rows_gaia = cursor.fetchall()

    name = ["Gaia", "Dados Plotados ({} registros)".format(number_of_rows_gaia_plotted[0][0]), "Dados do Catálogo Gaia ({} registros)".format(number_of_rows_gaia[0][0])]

    value = (produtos, dados)
    return render_template("gaia.html", data=value, name=name)

@app.route("/hipparcos/")
def hipparcos():
    cursor.execute("select Hipparcos_product.record_ordinal_number, Hipparcos.HIP, round(Hipparcos_product.MV, 5), round(Hipparcos_product.MVt, 5), round(Hipparcos_product.B_minus_V, 5), round(Hipparcos_product.BT_minus_VT, 5), round(Hipparcos_product.MV_error, 5), round(Hipparcos_product.MVt_error, 5) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and B_minus_V != 0 order by Hipparcos_product.record_ordinal_number")
    produtos_MV_versus_B_minus_V = cursor.fetchall()
    cursor.execute("select count(*) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and B_V != 0 order by Hipparcos_product.record_ordinal_number")
    number_of_rows_hipparcos_plotted_MV_versus_B_minus_V = cursor.fetchall()

    cursor.execute("select Hipparcos_product.record_ordinal_number, Hipparcos.HIP, round(Hipparcos_product.MV, 5), round(Hipparcos_product.MVt, 5), round(Hipparcos_product.B_minus_V, 5), round(Hipparcos_product.BT_minus_VT, 5), round(Hipparcos_product.MV_error, 5), round(Hipparcos_product.MVt_error, 5) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and B_minus_V = 0 order by Hipparcos_product.record_ordinal_number")
    produtos_not_plotted_MV_versus_B_minus_V = cursor.fetchall()
    cursor.execute("select count(*) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and B_minus_V = 0 order by Hipparcos_product.record_ordinal_number")
    number_of_rows_hipparcos_not_plotted_MV_versus_B_minus_V = cursor.fetchall()

    cursor.execute("select Hipparcos_product.record_ordinal_number, Hipparcos.HIP, round(Hipparcos_product.MV, 5), round(Hipparcos_product.MVt, 5), round(Hipparcos_product.B_minus_V, 5), round(Hipparcos_product.BT_minus_VT, 5), round(Hipparcos_product.MV_error, 5), round(Hipparcos_product.MVt_error, 5) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and BT_minus_VT != 0 order by Hipparcos_product.record_ordinal_number")
    produtos_MVt_versus_BT_minus_VT = cursor.fetchall()
    cursor.execute("select count(*) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and BT_minus_VT != 0 order by Hipparcos_product.record_ordinal_number")
    number_of_rows_hipparcos_plotted_MVt_versus_BT_minus_VT = cursor.fetchall()

    cursor.execute("select Hipparcos_product.record_ordinal_number, Hipparcos.HIP, round(Hipparcos_product.MV, 5), round(Hipparcos_product.MVt, 5), round(Hipparcos_product.B_minus_V, 5), round(Hipparcos_product.BT_minus_VT, 5), round(Hipparcos_product.MV_error, 5), round(Hipparcos_product.MVt_error, 5) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and BT_minus_VT = 0 order by Hipparcos_product.record_ordinal_number")
    produtos_not_plotted_MVt_versus_BT_minus_VT = cursor.fetchall()
    cursor.execute("select count(*) from Hipparcos_product, Hipparcos where Hipparcos_product.record_ordinal_number = Hipparcos.record_ordinal_number and BT_minus_VT = 0 order by Hipparcos_product.record_ordinal_number")
    number_of_rows_hipparcos_not_plotted_MVt_versus_BT_minus_VT = cursor.fetchall()

    cursor.execute("select record_ordinal_number, HIP, round(Vmag, 5), round(RAdeg, 5), round(DEdeg, 5), round(Plx, 5), round(e_Plx, 5), round(pmRA, 5), round(pmDE, 5), round(BTmag, 5), round(VTmag, 5), round(B_V, 5) from Hipparcos order by record_ordinal_number")
    dados = cursor.fetchall()
    cursor.execute("select count(*) from Hipparcos")
    number_of_rows_hipparcos = cursor.fetchall()

    name = ["Hipparcos",
            "Estrelas Plotadas no Diagrama M(V) x B-V ({} registros)".format(number_of_rows_hipparcos_plotted_MV_versus_B_minus_V[0][0]),
            "Estrelas Não Plotadas no Diagrama M(V) x B-V ({} registros)".format(number_of_rows_hipparcos_not_plotted_MV_versus_B_minus_V[0][0]),
            "Estrelas Plotadas no Diagrama M(Vt) x BT-VT ({} registros)".format(number_of_rows_hipparcos_plotted_MVt_versus_BT_minus_VT[0][0]),
            "Estrelas Não Plotadas no Diagrama M(Vt) x BT-VT ({} registros)".format(number_of_rows_hipparcos_not_plotted_MVt_versus_BT_minus_VT[0][0]),
            "Estrelas do Catálogo Hipparcos ({} registros)".format(number_of_rows_hipparcos[0][0])]

    value = (produtos_MV_versus_B_minus_V, produtos_not_plotted_MV_versus_B_minus_V, produtos_MVt_versus_BT_minus_VT, produtos_not_plotted_MVt_versus_BT_minus_VT, dados)

    return render_template("hipparcos.html", data=value, name=name)

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