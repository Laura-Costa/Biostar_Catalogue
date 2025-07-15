import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table = "hipparcos"
son_table = "hipparcos_product"
son_key_column = "hip"

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table

cursor.execute("create table {son_table}( "
               "hip int primary key, "
               "mv numeric(65, 30) null, "
               "e_mv numeric(65, 30) null, "
               "mvt numeric(65, 30) null, "
               "e_mvt numeric(65, 30) null, "
               "b_v numeric(65, 30) null, "
               "bt_vt numeric(65, 30) null, "
               "foreign key ({son_key_column}) references {father_table}(hip) on delete restrict "
               ")".format(son_table=son_table, father_table=father_table, son_key_column=son_key_column))

# load hip
cursor.execute("select hip from {father_table}".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value: # my_tuple is like (79672,)
    f.insert_key(cursor, son_table, son_key_column, my_tuple, 0)

# load mv
cursor.execute("select hip, "
               "vmag + 5 + 5 * log(10, plx/1000.0) as mv "
               "from {father_table} "
               "where plx is not null and "
               "plx > 0 and "
               "vmag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'mv', son_key_column, my_tuple)

# load e_mv
cursor.execute("select hip,"
               "( "
               "abs((vmag + 5 + 5 * log(10, plx/1000.0)) - (vmag + 5 + 5 * log(10, (plx + e_plx)/1000.0))) "
               "+ "
               "abs((vmag + 5 + 5 * log(10, plx/1000.0)) - (vmag + 5 + 5 * log(10, (plx - e_plx)/1000.0))) "
               ") / 2.0 as e_mv "
               "from {father_table} "
               "where plx is not null and "
               "e_plx is not null and "
               "plx > 0 and "
               "vmag is not null and "
               "plx + e_plx > 0 and "
               "plx - e_plx > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_mv', son_key_column, my_tuple)

# load mvt
cursor.execute("select hip, "
               "vtmag + 5 + 5 * log(10, plx/1000.0) as mvt "
               "from {father_table} "
               "where plx is not null and "
               "plx > 0 and "
               "vtmag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'mvt', son_key_column, my_tuple)

# load e_mvt
cursor.execute("select hip, "
               "( "
               "abs((vtmag + 5 + 5 * log(10, plx/1000.0)) - (vtmag + 5 + 5 * log(10, (plx + e_plx)/1000.0))) "
               "+"
               "abs((vtmag + 5 + 5 * log(10, plx/1000.0)) - (vtmag + 5 + 5 * log(10, (plx - e_plx)/1000.0))) "
               ") / 2.0 as e_mvt "
               "from {father_table} "
               "where plx is not null and "
               "e_plx is not null and "
               "plx > 0 and "
               "vtmag is not null and "
               "plx + e_plx > 0 and "
               "plx - e_plx > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_mvt', son_key_column, my_tuple)

# load b_v
cursor.execute("select hip,"
               "b_v "
               "from {father_table} "
               "where b_v is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'b_v', son_key_column, my_tuple)

# load bt_vt
cursor.execute("select hip, "
               "btmag - vtmag "
               "from {father_table} "
               "where btmag is not null and "
               "vtmag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'bt_vt', son_key_column, my_tuple)

# certificar-se de que os dados estao gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()