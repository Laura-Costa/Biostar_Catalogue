import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table = "Hipparcos"
son_table = "Hipparcos_product"
son_key_column = "HIP"

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table

cursor.execute("create table {son_table}( "
               "HIP char(100) primary key, "
               "MV numeric(65, 30) null, "
               "MV_error numeric(65, 30) null, "
               "MVt numeric(65, 30) null, "
               "MVt_error numeric(65, 30) null, "
               "B_V numeric(65, 30) null, "
               "Bt_Vt numeric(65, 30) null, "
               "foreign key ({son_key_column}) references {father_table}(HIP) on delete restrict "
               ")".format(son_table=son_table, father_table=father_table, son_key_column=son_key_column))

# load HIP
cursor.execute("select HIP from {father_table}".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value: # my_tuple is like ('HIP 79672',)
    f.insert_key(cursor, son_table, son_key_column, my_tuple, 0)

# load MV
cursor.execute("select HIP, "
               "Vmag + 5 + 5 * log(10, Plx/1000.0) as MV "
               "from {father_table} "
               "where Plx is not null and "
               "Plx > 0 and "
               "Vmag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MV', son_key_column, my_tuple)

# load MV_error
cursor.execute("select HIP,"
               "( "
               "abs((Vmag + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx + e_Plx)/1000.0))) "
               "+ "
               "abs((Vmag + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx - e_Plx)/1000.0))) "
               ") / 2.0 as MV_error "
               "from {father_table} "
               "where Plx is not null and "
               "e_Plx is not null and "
               "Plx > 0 and "
               "Vmag is not null and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MV_error', son_key_column, my_tuple)

# load MVt
cursor.execute("select HIP, "
               "VTmag + 5 + 5 * log(10, Plx/1000.0) as MVt "
               "from {father_table} "
               "where Plx is not null and "
               "Plx > 0 and "
               "VTmag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MVt', son_key_column, my_tuple)

# load MVt_error
cursor.execute("select HIP, "
               "( "
               "abs((VTmag + 5 + 5 * log(10, Plx/1000.0)) - (VTmag + 5 + 5 * log(10, (Plx + e_Plx)/1000.0))) "
               "+"
               "abs((VTmag + 5 + 5 * log(10, Plx/1000.0)) - (VTmag + 5 + 5 * log(10, (Plx - e_Plx)/1000.0))) "
               ") / 2.0 as MVt_error "
               "from {father_table} "
               "where Plx is not null and "
               "e_Plx is not null and "
               "Plx > 0 and "
               "VTmag is not null and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MVt_error', son_key_column, my_tuple)

# load B_V
cursor.execute("select HIP,"
               "B_V "
               "from {father_table} "
               "where B_V is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'B_V', son_key_column, my_tuple)

# load BT_VT
cursor.execute("select HIP, "
               "BTmag - VTmag "
               "from {father_table} "
               "where BTmag is not null and "
               "VTmag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'Bt_Vt', son_key_column, my_tuple)

# certificar-se de que os dados estao gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()