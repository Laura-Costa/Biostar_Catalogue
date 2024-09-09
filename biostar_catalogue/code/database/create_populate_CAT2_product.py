import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar a tabela CAT2_product no BD

cursor.execute("create table CAT2_product( "
               "HIP CHAR(100) primary key, "
               "MV NUMERIC(65,30) null, "
               "MV_error NUMERIC(65,30) null, "
               "MVt NUMERIC(65,30) null, "
               "MVt_error NUMERIC(65,30) null, "
               "B_minus_V NUMERIC(65,30) null, "
               "BT_minus_VT NUMERIC(65,30) null, "
               "foreign key (HIP) references CAT2(HIP) on delete restrict)")

# Carregar dados da tabela CAT2_product

# load HIP

cursor.execute("select HIP from CAT2")
value = cursor.fetchall()

for (HIP_value,) in value:
    cursor.execute("insert into CAT2_product(HIP) values ('{}')".format(HIP_value))

# load MV

cursor.execute("select HIP, Vmag + 5 + 5 * log(10, Plx/1000.0) as MV "
               "from CAT2 "
               "where Vmag is not NULL and "
               "Plx is not NULL and "
               "Plx > 0")
value = cursor.fetchall()
for (HIP_value, MV_value) in value:
    cursor.execute("update CAT2_product set MV = {} where HIP = '{}'".format(MV_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where Vmag is NULL or "
               "Plx is NULL or "
               "Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MV = NULL where HIP = '{}'".format(HIP_value))

# load MV_error

cursor.execute("select HIP, "
               "("
               "abs((Vmag + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx + e_Plx) / 1000.0))) "
               "+ "
               "abs((Vmag  + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx - e_Plx) / 1000.0))) "
               ") / 2.0 as MV_error "
               "from CAT2 "
               "where Vmag is not NULL and "
               "Plx is not NULL and "
               "e_Plx is not NULL and "
               "Plx > 0 and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0")
value = cursor.fetchall()
for (HIP_value, MV_error_value) in value:
    cursor.execute("update CAT2_product set MV_error = {} where HIP = '{}'".format(MV_error_value, HIP_value))

cursor.execute("select HIP from CAT2 "
               "where Vmag is NULL or "
               "Plx is NULL or "
               "e_Plx is NULL or "
               "Plx <= 0 or "
               "Plx + e_Plx <= 0 or "
               "Plx - e_Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MV_error = NULL where HIP = '{}'".format(HIP_value))

# load MVt

cursor.execute("select HIP, "
               "VTmag + 5 + 5 * log(10, Plx / 1000.0) as MVt "
               "from CAT2 "
               "where VTmag is not NULL and "
               "Plx is not NULL and "
               "Plx > 0")
value = cursor.fetchall()
for (HIP_value, MVt_value) in value:
    cursor.execute("update CAT2_product set MVt = {} where HIP = '{}'".format(MVt_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where VTmag is NULL or "
               "Plx is NULL or "
               "Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MVt = NULL where HIP = '{}'".format(HIP_value))

# load MVt_error

cursor.execute("select HIP, "
               "( "
               "abs(( VTmag + 5 + 5 * log(10, Plx / 1000.0)) - (VTmag + 5 + 5 * log(10, (Plx + e_Plx) / 1000.0))) "
               "+ "
               "abs(( VTmag + 5 + 5 * log(10, Plx / 1000.0)) - (VTmag + 5 + 5 * log(10, (Plx - e_Plx) / 1000.0))) "
               ") / 2.0 as MVt_error "
               "from CAT2 "
               "where VTmag is not NULL and "
               "Plx is not NULL and "
               "e_Plx is not NULL and "
               "Plx > 0 and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0")
value = cursor.fetchall()
for (HIP_value, MVt_error_value) in value:
    cursor.execute("update CAT2_product set MVt_error = {} where HIP = '{}'".format(MVt_error_value, HIP_value))

cursor.execute("select HIP from CAT2 "
               "where VTmag is NULL or "
               "Plx is NULL or "
               "e_Plx is NULL or "
               "Plx <= 0 or "
               "Plx + e_Plx <= 0 or "
               "Plx - e_Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MVt_error = NULL where HIP = '{}'".format(HIP_value))

# load B_minus_V

cursor.execute("select HIP, "
               "B_V as B_minus_V "
               "from CAT2 "
               "where B_V is not NULL")
value = cursor.fetchall()
for (HIP_value, B_minus_V_value) in value:
    cursor.execute("update CAT2_product set B_minus_V = {} where HIP = '{}'".format(B_minus_V_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where B_V is NULL")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set B_minus_V = NULL where HIP = '{}'".format(HIP_value))

# load BT_minus_VT

cursor.execute("select HIP, "
               "BTmag - VTmag  as BT_minus_VT "
               "from CAT2 "
               "where BTmag is not NULL and "
               "VTmag is not NULL")
value = cursor.fetchall()
for (HIP_value, BT_minus_VT_value) in value:
    cursor.execute("update CAT2_product set BT_minus_VT = {} where HIP = '{}'".format(BT_minus_VT_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where BTmag is NULL or "
               "VTmag is NULL")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set BT_minus_VT = NULL where HIP = '{}'".format(HIP_value))

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()