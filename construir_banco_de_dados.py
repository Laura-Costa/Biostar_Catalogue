import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("drop table if exists Produto_Gaia")
cursor.execute("create table Produto_Gaia(numero_ordinal_do_registro int primary key,Mg double not null,MRp double not null,Bp_menos_Rp double not null,erro_de_mg double not null,erro_de_MRp double not null,foreign key (numero_ordinal_do_registro) references Source_Gaia(numero_ordinal_do_registro) on delete cascade)")
cursor.execute("select numero_ordinal_do_registro, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_menos_Rp, (abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_Mg, (abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_MRp from Source_Gaia order by numero_ordinal_do_registro")
value = cursor.fetchall()

add_row = ("INSERT INTO Produto_Gaia "
              "(numero_ordinal_do_registro, Mg, MRp, Bp_menos_Rp, erro_de_Mg, erro_de_MRp) "
              "VALUES (%(numero_ordinal_do_registro)s, %(Mg)s, %(MRp)s, %(Bp_menos_Rp)s, %(erro_de_Mg)s, %(erro_de_MRp)s)")

#print(value)
for registro in value:
    data_row = {
        'numero_ordinal_do_registro': registro[0],
        'Mg': registro[1],
        'MRp': registro[2],
        'Bp_menos_Rp': registro[3],
        'erro_de_Mg': registro[4],
        'erro_de_MRp': registro[5],
    }
    cursor.execute(add_row, data_row)

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("drop table if exists Produto_Hipparcos")
cursor.execute("create table Produto_Hipparcos(numero_ordinal_do_registro int primary key, MV double not null, MVt double not null, B_menos_V double not null, BT_menos_VT double not null, erro_de_MV double not null, erro_de_MVt double not null, foreign key (numero_ordinal_do_registro) references Source_Hipparcos(numero_ordinal_do_registro) on delete cascade)")
cursor.execute("select numero_ordinal_do_registro, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_menos_V, BTmag - VTmag as BT_menos_VT, (abs(Vmag + 5 + 5*log(10, Plx/1000) - (Vmag + 5 + 5*log(10, (Plx+e_Plx)/1000))) + abs(Vmag + 5 + 5*log(10, Plx/1000) - (Vmag + 5 + 5*log(10, (Plx-e_Plx)/1000))))/2 as erro_de_MV, (abs(VTmag + 5 + 5*log(10, Plx/1000) - (VTmag + 5 + 5*log(10, (Plx+e_Plx)/1000))) + abs(VTmag + 5 + 5*log(10, Plx/1000) - (VTmag + 5 + 5*log(10, (Plx-e_Plx)/1000))))/2 as erro_de_MVt from Source_Hipparcos where Plx > 0 order by numero_ordinal_do_registro")
value = cursor.fetchall()

add_row = ("INSERT INTO Produto_Hipparcos "
              "(numero_ordinal_do_registro, MV, MVt, B_menos_V, BT_menos_VT, erro_de_MV, erro_de_MVt) "
              "VALUES (%(numero_ordinal_do_registro)s, %(MV)s, %(MVt)s, %(B_menos_V)s, %(BT_menos_VT)s, %(erro_de_MV)s, %(erro_de_MVt)s)")

for registro in value:
    data_row = {
        'numero_ordinal_do_registro': registro[0],
        'MV': registro[1],
        'MVt': registro[2],
        'B_menos_V': registro[3],
        'BT_menos_VT': registro[4],
        'erro_de_MV': registro[5],
        'erro_de_MVt': registro[6],
    }
    cursor.execute(add_row, data_row)

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()


connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')
cursor = connection.cursor()

'''
cursor.execute("drop table if exists Diagrama_Gaia")
cursor.execute("drop table if exists Produto_Gaia_e_plotado_em")
cursor.execute("create table Diagrama_Gaia(codigo char(100) not null, diagrama blob not null, descricao char(100), primary key (codigo));")
cursor.execute("create table Produto_Gaia_e_plotado_em(parallax double not null, numero_ordinal_do_registro int not null, codigo char(100) not null, primary key (parallax, numero_ordinal_do_registro, codigo), foreign key (numero_ordinal_do_registro) references Produto_Gaia(numero_ordinal_do_registro), foreign key (codigo) references Diagrama_Gaia(codigo) on delete cascade)")
'''

#cursor.execute("select numero_ordinal_do_registro, MG, MRp, Bp_menos_Rp from Produto_Gaia")
cursor.execute("select numero_ordinal_do_registro, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_menos_Rp from Source_Gaia order by numero_ordinal_do_registro")
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


transparency = 1
size = 1.5
plt.scatter(eixox, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA: {} estrelas em um raio de 23pc".format(len(value)))
plt.ylabel("M(G)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/mg_indice_de_cor.png')
plt.clf()

plt.scatter(eixox, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(0, 4.2)
plt.ylim(15, 0.3)
plt.title("GAIA: {} estrelas em um raio de 23pc".format(len(value)))
plt.ylabel("M(Rp)")
plt.xlabel("Bp-Rp")
plt.savefig('static/img/mrp_indice_de_cor.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')
cursor = connection.cursor()

# gráficos Hipparcos
cursor.execute("select numero_ordinal_do_registro, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_menos_V, BTmag - VTmag as BT_menos_VT from Source_Hipparcos where (Plx/1000) > 0 and B_V != 0 and BTmag - VTmag != 0 order by numero_ordinal_do_registro")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

transparency = 1
size = 1.5
plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 7)
plt.ylim(15, -20)
plt.title("HIPPARCOS: {} estrelas(π > 0'')".format(len(value)))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/mv_b_v_0.png')
plt.clf()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 7)
plt.ylim(15, -20)
plt.title("HIPPARCOS: {} estrelas (π > 0'')".format(len(value)))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/mvt_bt_vt_0.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("select numero_ordinal_do_registro, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_menos_V, BTmag - VTmag as BT_menos_VT from Source_Hipparcos where (Plx/1000) > 0.1 and B_V != 0 and BTmag - VTmag != 0 order by numero_ordinal_do_registro")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, 0.3)
plt.title("HIPPARCOS: {} estrelas em um raio de 10pc (π > 0.1'')".format(len(value)))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/mv_b_v_01.png')
plt.clf()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, 0.3)
plt.title("HIPPARCOS: {} estrelas em um raio de 10pc (π > 0.1'')".format(len(value)))
plt.ylabel("M(Vt)")
plt.xlabel("BT-VT")
plt.savefig('static/img/mvt_bt_vt_01.png')
plt.clf()

connection.commit()
cursor.close()
connection.close()


connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute(
    "select numero_ordinal_do_registro, Vmag + 5 + 5*log(10, Plx/1000) as MV, VTmag + 5 + 5*log(10, Plx/1000) as MVt, B_V as B_menos_V, BTmag - VTmag as BT_menos_VT from Source_Hipparcos where (Plx/1000) > 0.05 and B_V != 0 and BTmag - VTmag != 0 order by numero_ordinal_do_registro")
value = cursor.fetchall()

eixox1 = []
for registro in value:
    eixox1.append(registro[3])

eixoy1 = []
for registro in value:
    eixoy1.append(registro[1])

plt.scatter(eixox1, eixoy1, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS: {} estrelas em um raio de 20pc (π > 0.05'')".format(len(value)))
plt.ylabel("M(V)")
plt.xlabel("B-V")
plt.savefig('static/img/mv_b_v_005.png')
plt.clf()

eixox2 = []
for registro in value:
    eixox2.append(registro[4])

eixoy2 = []
for registro in value:
    eixoy2.append(registro[2])

plt.scatter(eixox2, eixoy2, s=size, marker=".", edgecolors='black', alpha=transparency)
plt.xlim(-1, 2.5)
plt.ylim(15, -1)
plt.title("HIPPARCOS: {} estrelas em um raio de 20pc (π > 0.05'')".format(len(value)))
plt.ylabel("M(Vt)")
plt.xlabel("BT-RT")
plt.savefig('static/img/mvt_bt_vt_005.png')
plt.clf()

# Make sure data is committed to the database
connection.commit()
cursor.close()
connection.close()