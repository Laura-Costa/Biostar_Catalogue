import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table = 'BrightStarMultiple'
father_key_column = 'ordinal_number'
son_table = 'BrightStarMultiple_product'
son_key_column = 'ordinal_number'

# apagar a table son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table
cursor.execute("create table {son_table}( "
               "{son_key_column} int primary key, "
               "simbad_MV numeric(65, 30) null, "
               "simbad_MV_error numeric(65, 30) null, "
               "simbad_B_V numeric(65, 30) null, "
               "foreign key({son_key_column}) references {father_table}({father_key_column}) on delete restrict)".format(son_table=son_table,
                                                                                                                         son_key_column=son_key_column,
                                                                                                                         father_table=father_table,
                                                                                                                         father_key_column=father_key_column))

# load son_key_column
cursor.execute("select {father_key_column} from {father_table}".format(father_key_column=father_key_column,
                                                                       father_table=father_table))
value = cursor.fetchall()
for my_tuple in value: # my_tuple is like (1,)
    f.insert_key(cursor, son_table, son_key_column, my_tuple, 0)

# load simbad_MV
cursor.execute("select {father_key_column}, "
               "simbad_V + 5 + 5 * log(10, simbad_parallax / 1000.0) as simbad_MV "
               "from {father_table} "
               "where simbad_parallax is not null and "
               "simbad_parallax > 0 and "
               "simbad_V is not null".format(father_key_column=father_key_column, father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'simbad_MV', son_key_column, my_tuple)

# load simbad_MV_error
cursor.execute("select {father_key_column}, "
               "( "
               "abs((simbad_V + 5 + 5 * log(10, simbad_parallax/1000.0)) - (simbad_V + 5 + 5 * log(10, (simbad_parallax + simbad_parallax_error)/1000.0))) "
               "+ "
               "abs((simbad_V + 5 + 5 * log(10, simbad_parallax/1000.0)) - (simbad_V + 5 + 5 * log(10, (simbad_parallax - simbad_parallax_error)/1000.0))) "
               ") / 2.0 as simbad_MV_error "
               "from {father_table} "
               "where simbad_parallax is not null and "
               "simbad_parallax_error is not null and "
               "simbad_parallax > 0 and "
               "simbad_V is not null and "
               "simbad_parallax + simbad_parallax_error > 0 and "
               "simbad_parallax - simbad_parallax_error > 0".format(father_key_column=father_key_column,
                                                                    father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'simbad_MV_error', son_key_column, my_tuple)

# load simbad_B_V
cursor.execute("select {father_key_column}, "
               "(simbad_B - simbad_V) as simbad_B_V "
               "from {father_table} "
               "where simbad_B is not null and "
               "simbad_V is not null".format(father_key_column=father_key_column, father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'simbad_B_V', son_key_column, my_tuple)

# certificar-se de que os dados foram gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()