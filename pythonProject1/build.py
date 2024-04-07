import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp, (abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as Mg_error, (abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as MRp_error from Gaia order by record_ordinal_number")
value = cursor.fetchall()

add_row = ("INSERT INTO Gaia_product "
              "(record_ordinal_number, Mg, MRp, Bp_minus_Rp, Mg_error, MRp_error) "
              "VALUES (%(record_ordinal_number)s, %(Mg)s, %(MRp)s, %(Bp_minus_Rp)s, %(Mg_error)s, %(MRp_error)s)")

for registro in value:
    data_row = {
        'record_ordinal_number': registro[0],
        'Mg': registro[1],
        'MRp': registro[2],
        'Bp_minus_Rp': registro[3],
        'Mg_error': registro[4],
        'MRp_error': registro[5],
    }
    cursor.execute(add_row, data_row)

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT, (abs(Vmag + 5 + 5*log(10, Plx/1000) - (Vmag + 5 + 5*log(10, (Plx+e_Plx)/1000))) + abs(Vmag + 5 + 5*log(10, Plx/1000) - (Vmag + 5 + 5*log(10, (Plx-e_Plx)/1000))))/2 as MV_error, (abs(VTmag + 5 + 5*log(10, Plx/1000) - (VTmag + 5 + 5*log(10, (Plx+e_Plx)/1000))) + abs(VTmag + 5 + 5*log(10, Plx/1000) - (VTmag + 5 + 5*log(10, (Plx-e_Plx)/1000))))/2 as MVt_error from Hipparcos where Plx > 0 order by record_ordinal_number")
value = cursor.fetchall()

add_row = ("INSERT INTO Hipparcos_product "
              "(record_ordinal_number, MV, MVt, B_minus_V, BT_minus_VT, MV_error, MVt_error) "
              "VALUES (%(record_ordinal_number)s, %(MV)s, %(MVt)s, %(B_minus_V)s, %(BT_minus_VT)s, %(MV_error)s, %(MVt_error)s)")

for registro in value:
    data_row = {
        'record_ordinal_number': registro[0],
        'MV': registro[1],
        'MVt': registro[2],
        'B_minus_V': registro[3],
        'BT_minus_VT': registro[4],
        'MV_error': registro[5],
        'MVt_error': registro[6],
    }
    cursor.execute(add_row, data_row)

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from Gaia order by record_ordinal_number")
value = cursor.fetchall()

eixox = []
for registro in value:
    eixox.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(parallax) from Gaia")
minima_paralaxe = cursor.fetchall()

transparency = 1
size = 1.5
plt.scatter(eixox, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(G)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/mg_versus_Bp_minus_Rp.png')
plt.clf()

plt.scatter(eixox, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Rp)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/mrp_versus_Bp_minus_Rp.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where B_V != 0 order by record_ordinal_number")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(Plx) from Hipparcos where B_V != 0")
minima_paralaxe = cursor.fetchall()

transparency = 1
size = 1.5
plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/mv_versus_b_minus_v_plx_greater_or_iqual_0.039.png')
plt.clf()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where BTmag - VTmag != 0 order by record_ordinal_number")
value = cursor.fetchall()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(Plx) from Hipparcos where BTmag - VTmag != 0")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/mvt_versus_bt_minus_vt_plx_greater_or_iqual_0.039.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.1 and B_V != 0 order by record_ordinal_number")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.1 and B_V != 0")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, 0.3)
plt.title("HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π > {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/mv_versus_b_minus_v_plx_greater_0.1.png')
plt.clf()


cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.1 and BTmag - VTmag != 0 order by record_ordinal_number")
value = cursor.fetchall()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])


cursor.execute("select MIN(Plx) from Hipparcos where (Plx / 1000) > 0.1 and BTmag - VTmag != 0")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, 0.3)
plt.title("HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π > {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/mvt_versus_bt_minus_vt_plx_greater_0.1.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.05 and B_V != 0 order by record_ordinal_number")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.05 and B_V != 0")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π > {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/mv_versus_b_minus_v_plx_greater_0.05.png')
plt.clf()


cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.05 and BTmag - VTmag != 0 order by record_ordinal_number")
value = cursor.fetchall()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.05 and BTmag - VTmag != 0 ")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π > {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-RT")
plt.savefig('static/img/mvt_versus_bt_minus_vt_plx_greater_0.05.png')
plt.clf()

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()




connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number_gaia, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from matched order by record_ordinal_number_gaia")
value = cursor.fetchall()

eixox = []
for registro in value:
    eixox.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(parallax) from matched")
minima_paralaxe = cursor.fetchall()

transparency = 1
size = 1.5
plt.scatter(eixox, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA ∩ HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(G)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/gaia_intersection_hipparcos_mg_versus_Bp_minus_Rp.png')
plt.clf()

plt.scatter(eixox, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA ∩ HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Rp)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/gaia_intersection_hipparcos_mrp_versus_Bp_minus_Rp.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()


connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number_hipparcos, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from matched where (Plx/1000) > 0 and B_V != 0 order by record_ordinal_number_hipparcos")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(parallax) from matched where (Plx/1000) > 0 and B_V != 0")
minima_paralaxe = cursor.fetchall()

transparency = 1
size = 1.5


plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA ∩ HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/gaia_intersection_hipparcos_mv_versus_b_minus_v_plx_greater_0.png')
plt.clf()


cursor.execute("select record_ordinal_number_hipparcos, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from matched where (Plx/1000) > 0 and BTmag - VTmag != 0 order by record_ordinal_number_hipparcos")
value = cursor.fetchall()


eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(parallax) from matched where (Plx/1000) > 0 and BTmag - VTmag != 0")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA ∩ HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/gaia_intersection_hipparcos_mvt_versus_bt_minus_vt_plx_greater_0.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()



##
connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where B_V != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(Plx) from Hipparcos where B_V != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched)")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -2)
plt.title("HIPPARCOS — GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/hipparcos_minus_gaia_mv_versus_b_minus_v_plx_greater_or_iqual_0.039.png')
plt.clf()


cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where BTmag - VTmag != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(Plx) from Hipparcos where BTmag - VTmag != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched)")
minima_paralaxe = cursor.fetchall()


plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -2)
plt.title("HIPPARCOS — GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/hipparcos_minus_gaia_mvt_versus_bt_minus_vt_plx_greater_or_iqual_0.039.png')
plt.clf()

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()

##



connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.05 and B_V != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.05 and B_V != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched)")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS — GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/hipparcos_minus_gaia_mv_versus_b_minus_v_plx_greater_0.05.png')
plt.clf()


cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.05 and BTmag - VTmag != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.05 and BTmag - VTmag != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched)")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS — GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/hipparcos_minus_gaia_mvt_versus_bt_minus_vt_plx_greater_0.05.png')
plt.clf()

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()













connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.1 and B_V != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.1 and B_V != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched)")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, 0.3)
plt.title("HIPPARCOS — GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/hipparcos_minus_gaia_mv_versus_b_minus_v_plx_greater_0.1.png')
plt.clf()



cursor.execute("select record_ordinal_number, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_minus_V, BTmag - VTmag as BT_minus_VT from Hipparcos where (Plx/1000) > 0.1 and BTmag - VTmag != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(Plx) from Hipparcos where (Plx/1000) > 0.1 and BTmag - VTmag != 0 and record_ordinal_number not in (select record_ordinal_number_hipparcos from matched)")
minima_paralaxe = cursor.fetchall()

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, 0.3)
plt.title("HIPPARCOS — GAIA: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/hipparcos_minus_gaia_mvt_versus_bt_minus_vt_plx_greater_0.1.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()






connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select record_ordinal_number, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from Gaia where record_ordinal_number not in (select record_ordinal_number_gaia from matched) order by record_ordinal_number")
value = cursor.fetchall()

eixox = []
for registro in value:
    eixox.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

cursor.execute("select MIN(parallax) from Gaia where record_ordinal_number not in (select record_ordinal_number_gaia from matched)")
minima_paralaxe = cursor.fetchall()

transparency = 1
size = 1.5
plt.scatter(eixox, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA — HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(G)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/gaia_minus_hipparcos_mg_versus_Bp_minus_Rp.png')
plt.clf()

plt.scatter(eixox, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA — HIPPARCOS: {} estrelas em um raio de {:.2f}pc (π ≥ {:.3f}'')".format(len(value), 1/(minima_paralaxe[0][0]/1000) , minima_paralaxe[0][0]/1000))
plt.ylabel("M(Rp)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/gaia_minus_hipparcos_mrp_versus_Bp_minus_Rp.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()