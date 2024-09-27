import mysql.connector
import code.database.functions as f

# abrir a conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table_name = 'Gaia50pc'
son_table_name = 'Gaia50pc_product'
son_column_key_name = 'designation'

# apagar a tabela son_table_name caso ela já exista
cursor.execute("drop table if exists {son_table_name}".format(son_table_name=son_table_name))

# criar a tabela son_table_name

cursor.execute("create table {son_table_name}( "
               "designation char(100) primary key, "
               "MG numeric(65, 30) null, "
               "MG_error numeric(65, 30) null, "
               "MRp numeric(65, 30) null, "
               "MRp_error numeric(65, 30), "
               "Bp_Rp numeric(65, 30) null, "
               "foreign key (designation) references {father_table_name}(designation) on delete restrict "
               ")".format(son_table_name=son_table_name, father_table_name=father_table_name))

# load designation
cursor.execute("select designation from {father_table_name}".format(father_table_name=father_table_name))
value = cursor.fetchall()
for my_tuple in value: # my_tuple is like ('Gaia DR3 4345775217221821312',)
    f.insert_key(cursor, son_table_name, son_column_key_name, my_tuple, 0)

# load MG
cursor.execute("select designation, phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as MG "
               "from {father_table_name} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_g_mean_mag is not null".format(father_table_name=father_table_name))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table_name, 'MG', son_column_key_name, my_tuple)

# load MG_error
cursor.execute("select designation, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as MG_error "
               "from {father_table_name} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_g_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table_name=father_table_name))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table_name, 'MG_error', son_column_key_name, my_tuple)

# load MRp
cursor.execute("select designation, phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0) as MRp "
               "from {father_table_name} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_rp_mean_mag is not null".format(father_table_name=father_table_name))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table_name, 'MRp', son_column_key_name, my_tuple)

# load MRp_error
cursor.execute("select designation, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as MRp_error "
               "from {father_table_name} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_rp_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table_name=father_table_name))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table_name, 'MRp_error', son_column_key_name, my_tuple)

# load Bp_Rp
cursor.execute("select designation, "
               "phot_bp_mean_mag - phot_rp_mean_mag as Bp_Rp "
               "from {father_table_name} "
               "where phot_bp_mean_mag is not null and "
               "phot_rp_mean_mag is not null".format(father_table_name=father_table_name))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table_name, 'Bp_Rp', son_column_key_name, my_tuple)

# certificar de que os dados foram gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()