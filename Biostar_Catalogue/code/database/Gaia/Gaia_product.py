import mysql.connector
import code.functions.database as f

# abrir a conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table = 'Gaia'
father_key_column = 'designation'
son_table = 'Gaia_product'
son_key_column = 'designation'

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table

cursor.execute("create table {son_table}( "
               "designation char(100) primary key, "
               "MRp numeric(65, 30) null, "
               "MRp_error numeric(65, 30) null, "
               "MBp numeric(65, 30) null, "
               "MBp_error numeric(65, 30) null, "
               "MG numeric(65, 30) null, "
               "MG_error numeric(65, 30) null, "
               "Bp_Rp numeric(65, 30) null, "
               "G_Rp numeric(65, 30) null, "
               "Bp_G numeric(65, 30) null, "
               "foreign key({son_key_column}) references {father_table}({father_key_column}) on delete restrict "
               ")".format(son_table=son_table,
                          son_key_column=son_key_column,
                          father_table=father_table,
                          father_key_column=father_key_column))

# load designation
cursor.execute("select designation from {father_table}".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value: # my_tuple is like ('Gaia DR3 4345775217221821312',)
    f.insert_key(cursor, son_table, son_key_column, my_tuple, 0)

# load MRp
cursor.execute("select designation, "
               "phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0) as MRp "
               "from {father_table} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_rp_mean_mag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MRp', son_key_column, my_tuple)

# load MRp_error
cursor.execute("select designation, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as MRp_error "
               "from {father_table} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_rp_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MRp_error', son_key_column, my_tuple)

# load MBp
cursor.execute("select designation, phot_bp_mean_mag + 5 + 5 * log(10, parallax/1000.0) as MBp "
               "from {father_table} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_bp_mean_mag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MBp', son_key_column, my_tuple)

# load MBp_error
cursor.execute("select designation, "
               "( "
               "abs((phot_bp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_bp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_bp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_bp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as MBp_error "
               "from {father_table} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_bp_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MBp_error', son_key_column, my_tuple)

# load MG
cursor.execute("select designation, phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as MG "
               "from {father_table} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_g_mean_mag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MG', son_key_column, my_tuple)

# load MG_error
cursor.execute("select designation, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as MG_error "
               "from {father_table} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_g_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'MG_error', son_key_column, my_tuple)

# load Bp_Rp
cursor.execute("select designation, "
               "phot_bp_mean_mag - phot_rp_mean_mag as Bp_Rp "
               "from {father_table} "
               "where phot_bp_mean_mag is not null and "
               "phot_rp_mean_mag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'Bp_Rp', son_key_column, my_tuple)

# load G_Rp
cursor.execute("select designation, "
               "phot_g_mean_mag - phot_rp_mean_mag as G_Rp "
               "from {father_table} "
               "where phot_g_mean_mag is not null and "
               "phot_rp_mean_mag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'G_Rp', son_key_column, my_tuple)

# load Bp_G
cursor.execute("select designation, "
               "phot_bp_mean_mag - phot_g_mean_mag as Bp_G "
               "from {father_table} "
               "where phot_bp_mean_mag is not null and "
               "phot_g_mean_mag is not null".format(father_table=father_table))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'Bp_G', son_key_column, my_tuple)

# certificar de que os dados foram gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()