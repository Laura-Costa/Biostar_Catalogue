import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar a tabela CAT1_product no BD

cursor.execute("create table CAT1_product("
               "designation CHAR(100) primary key,"
               "Mg NUMERIC(65,30) null,"
               "Mg_error NUMERIC(65,30) null,"
               "MRp NUMERIC(65,30) null,"
               "MRp_error NUMERIC(65,30) null,"
               "Bp_minus_Rp NUMERIC(65,30) null,"
               "foreign key (designation) references CAT1(designation) on delete restrict)")

# Carregar dados da tabela CAT1_product

# load designation

cursor.execute("select designation from CAT1")
value = cursor.fetchall()

for (designation_value,) in value:
    cursor.execute("insert into CAT1_product(designation) values('{}')".format(designation_value))

# load Mg

cursor.execute("select designation, phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as Mg "
               "from CAT1 "
               "where phot_g_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax > 0")
value = cursor.fetchall()
for (designation_value, Mg_value) in value:
    cursor.execute("update CAT1_product set Mg = {} where designation = '{}'".format(Mg_value, designation_value))

cursor.execute("select designation from CAT1 "
               "where phot_g_mean_mag is NULL or "
               "parallax is NULL and "
               "parallax <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set Mg = NULL where designation = '{}'".format(designation_value))

# load Mg_error

cursor.execute("select designation, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2.0 as Mg_error "
               "from CAT1 "
               "where phot_g_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL and "
               "parallax > 0 and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0")
value = cursor.fetchall()
for (designation_value, Mg_error_value) in value:
    cursor.execute("update CAT1_product set Mg_error = {} where designation = '{}'".format(Mg_error_value, designation_value))

cursor.execute("select designation "
               "from CAT1 "
               "where phot_g_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL or "
               "parallax <= 0 or "
               "parallax + parallax_error <= 0 or "
               "parallax - parallax_error <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set Mg_error = NULL where designation = '{}'".format(designation_value))

# load MRp

cursor.execute("select designation, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000.0) as MRp "
               "from CAT1 "
               "where phot_rp_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax > 0")
value = cursor.fetchall()
for (designation_value, MRp_value) in value:
    cursor.execute("update CAT1_product set MRp = {} where designation = '{}'".format(MRp_value, designation_value))

cursor.execute("select designation "
               "from CAT1 "
               "where phot_rp_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set MRp = NULL where designation = '{}'".format(designation_value))

# load MRp_error

cursor.execute("select designation, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2.0 as MRp_error "
               "from CAT1 "
               "where phot_rp_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL and "
               "parallax > 0 and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0")
value = cursor.fetchall()
for (designation_value, MRp_error_value) in value:
    cursor.execute("update CAT1_product set MRp_error = {} where designation = '{}'".format(MRp_error_value, designation_value))

cursor.execute("select designation from CAT1 "
               "where phot_rp_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL or "
               "parallax <= 0 or "
               "parallax + parallax_error <= 0 or "
               "parallax - parallax_error <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set MRp_error = NULL where designation = '{}'".format(designation_value))

# load Bp_minus_Rp

cursor.execute("select designation, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from CAT1 "
               "where phot_bp_mean_mag is not NULL and phot_rp_mean_mag is not NULL")
value = cursor.fetchall()
for (designation_value, Bp_minus_Rp_value) in value:
    cursor.execute("update CAT1_product set Bp_minus_Rp = {} where designation = '{}'".format(Bp_minus_Rp_value, designation_value))

cursor.execute("select designation "
               "from CAT1 "
               "where phot_bp_mean_mag is NULL or "
               "phot_rp_mean_mag is NULL")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set Bp_minus_Rp = NULL where designation = '{}'".format(designation_value))

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()