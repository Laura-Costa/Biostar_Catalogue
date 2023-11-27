import mysql.connector


connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='IC2023ic*')
cursor = connection.cursor()

cursor.execute("create table Produto_Gaia(numero_ordinal_do_registro int primary key,Mg double not null,MRp double not null,Bp_menos_Rp double not null,erro_de_mg double not null,erro_de_MRp double not null,foreign key (numero_ordinal_do_registro) references Source_Gaia(numero_ordinal_do_registro) on delete restrict)")
cursor.execute("select numero_ordinal_do_registro, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_menos_Rp, (abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_Mg, (abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_MRp from Source_Gaia order by numero_ordinal_do_registro")
value = cursor.fetchall()

add_row = ("INSERT INTO Produto_Gaia "
              "(numero_ordinal_do_registro, Mg, MRp, Bp_menos_Rp, erro_de_Mg, erro_de_MRp) "
              "VALUES (%(numero_ordinal_do_registro)s, %(Mg)s, %(MRp)s, %(Bp_menos_Rp)s, %(erro_de_Mg)s, %(erro_de_MRp)s)")



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

connection = mysql.connector.connect(host='localhost', port='3306', database='catalogo_gaia', user='helena', password='IC2023ic*')
cursor = connection.cursor()

cursor.execute("create table Produto_Hipparcos(numero_ordinal_do_registro int primary key,MV double not null,MVt double not null,B_menos_V double not null,BT_menos_VT double not null,foreign key (numero_ordinal_do_registro) references Source_Hipparcos(numero_ordinal_do_registro) on delete restrict)")
cursor.execute("select numero_ordinal_do_registro, phot_g_mean_mag + 5 + 5*log(10, parallax/1000) as Mg, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) as MRp, phot_bp_mean_mag - phot_rp_mean_mag as Bp_menos_Rp, (abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_g_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_g_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_Mg, (abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax+parallax_error)/1000))) + abs(phot_rp_mean_mag + 5 + 5*log(10, parallax/1000) - (phot_rp_mean_mag + 5 + 5*log(10, (parallax-parallax_error)/1000))))/2 as erro_de_MRp from Source_Gaia order by numero_ordinal_do_registro")
value = cursor.fetchall()

add_row = ("INSERT INTO Produto_Gaia "
              "(numero_ordinal_do_registro, Mg, MRp, Bp_menos_Rp, erro_de_Mg, erro_de_MRp) "
              "VALUES (%(numero_ordinal_do_registro)s, %(Mg)s, %(MRp)s, %(Bp_menos_Rp)s, %(erro_de_Mg)s, %(erro_de_MRp)s)")



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