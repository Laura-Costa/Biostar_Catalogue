import mysql.connector
import code.functions.database as f

# abrir a conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table = 'gaia'
father_key_column = 'source_id'
son_table = 'gaia_product'
son_key_column = 'source_id'

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table

cursor.execute("create table {son_table}( "
               "{son_key_column} bigint primary key, "
               "mrp numeric(65, 30) null, "
               "e_mrp numeric(65, 30) null, "
               "mbp numeric(65, 30) null, "
               "e_mbp numeric(65, 30) null, "
               "mg numeric(65, 30) null, "
               "e_mg numeric(65, 30) null, "
               "e_distance_gspphot numeric(65, 30) null, "
               "e_azero_gspphot numeric(65, 30) null, "
               "vt_alpha numeric(65, 30) null, "
               "vt_delta numeric(65, 30) null, "
               "u numeric(65, 30) null, "
               "v numeric(65, 30) null, "
               "w numeric(65, 30) null, "
               "foreign key({son_key_column}) references {father_table}({father_key_column}) on delete restrict "
               ")".format(son_table=son_table,
                          son_key_column=son_key_column,
                          father_table=father_table,
                          father_key_column=father_key_column))

# load source_id
cursor.execute("select {father_key_column} from {father_table}".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value: # my_tuple is like (4345775217221821312,)
    f.insert_key(cursor, son_table, son_key_column, my_tuple, 0)

# load mrp
cursor.execute("select {father_key_column}, "
               "phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0) as mrp "
               "from {father_table} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_rp_mean_mag is not null".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'mrp', son_key_column, my_tuple)

# load e_mrp
cursor.execute("select {father_key_column}, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as e_mrp "
               "from {father_table} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_rp_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_mrp', son_key_column, my_tuple)

# load mbp
cursor.execute("select {father_key_column}, "
               "phot_bp_mean_mag + 5 + 5 * log(10, parallax/1000.0) as mbp "
               "from {father_table} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_bp_mean_mag is not null".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'mbp', son_key_column, my_tuple)

# load e_mbp
cursor.execute("select {father_key_column}, "
               "( "
               "abs((phot_bp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_bp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_bp_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_bp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as e_mbp "
               "from {father_table} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_bp_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_mbp', son_key_column, my_tuple)

# load mg
cursor.execute("select {father_key_column}, "
               "phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as mg "
               "from {father_table} "
               "where parallax is not null and "
               "parallax > 0 and "
               "phot_g_mean_mag is not null".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'mg', son_key_column, my_tuple)

# load e_mg
cursor.execute("select {father_key_column}, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error)/1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax/1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error)/1000.0))) "
               ") / 2.0 as e_mg "
               "from {father_table} "
               "where parallax is not null and "
               "parallax_error is not null and "
               "parallax > 0 and "
               "phot_g_mean_mag is not null and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_mg', son_key_column, my_tuple)

# load e_distance_gspphot
cursor.execute("select {father_key_column}, "
               "(1.0/2.0)*(distance_gspphot_upper - distance_gspphot_lower) as e_distance_gspphot "
               "from {father_table} "
               "where distance_gspphot_upper is not null and "
               "distance_gspphot_lower is not null".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_distance_gspphot', son_key_column, my_tuple)

# load e_azero_gspphot
cursor.execute("select {father_key_column}, "
               "(1.0/2.0)*(azero_gspphot_upper - azero_gspphot_lower) as e_azero_gspphot "
               "from {father_table} "
               "where azero_gspphot_upper is not null and "
               "azero_gspphot_lower is not null".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'e_azero_gspphot', son_key_column, my_tuple)

# load vt_alpha
cursor.execute("select {father_key_column}, "
               "(4.74057*(pmra/1000.0)*cos(declination))/(parallax/1000.0) as vt_alpha "
               "from {father_table} "
               "where pmra is not null and "
               "declination is not null and "
               "parallax is not null and "
               "parallax != 0".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'vt_alpha', son_key_column, my_tuple)

# load vt_delta
cursor.execute("select {father_key_column}, "
               "(4.74057*(pmdec/1000.0))/(parallax/1000.0) as vt_delta "
               "from {father_table} "
               "where pmdec is not null and "
               "parallax is not null and "
               "parallax != 0".format(father_table=father_table, father_key_column=father_key_column))
value = cursor.fetchall()
for my_tuple in value:
    f.update_product(cursor, son_table, 'vt_delta', son_key_column, my_tuple)

# load u, v e w (radial velocity from Gaia DR3)
cursor.execute("select {father_table}.{father_key_column}, "
               "{father_table}.right_ascension, "
               "{father_table}.declination, "
               "{father_table}.radial_velocity, "
               "{son_table}.vt_alpha, "
               "{son_table}.vt_delta "
               "from {father_table}, {son_table} "
               "where {father_table}.{father_key_column} = {son_table}.{son_key_column} and "
               "{father_table}.right_ascension is not null and "
               "{father_table}.declination is not null and "
               "{father_table}.radial_velocity is not null and "
               "{son_table}.vt_alpha is not null and "
               "{son_table}.vt_delta is not null".format(father_table=father_table, father_key_column=father_key_column,
                                                         son_table=son_table, son_key_column=son_key_column))
value = cursor.fetchall()
for (source_id, ra, dec, vr, vt_alpha, vt_delta) in value:
    (u, v, w) = f.strassen(ra, dec, vr, vt_alpha, vt_delta)
    f.update_product(cursor, son_table, 'u', son_key_column, (source_id, u))
    f.update_product(cursor, son_table, 'v', son_key_column, (source_id, v))
    f.update_product(cursor, son_table, 'w', son_key_column, (source_id, w))

# load u, v e w (radial velocity from Simbad)
cursor.execute("select {father_table}.{father_key_column}, "
               "{father_table}.right_ascension, "
               "{father_table}.declination, "
               "simbad.radial_velocity, "
               "{son_table}.vt_alpha, "
               "{son_table}.vt_delta "
               "from {father_table}, {son_table}, simbad "
               "where {father_table}.{father_key_column} = {son_table}.{son_key_column} and "
               "{father_table}.{father_key_column} = simbad.source_id and "
               "{father_table}.right_ascension is not null and "
               "{father_table}.declination is not null and "
               "simbad.radial_velocity is not null and "
               "{son_table}.vt_alpha is not null and "
               "{son_table}.vt_delta is not null and "
               "{father_table}.radial_velocity is null".format(father_table=father_table, father_key_column=father_key_column,
                                                         son_table=son_table, son_key_column=son_key_column))
value = cursor.fetchall()
for (source_id, ra, dec, vr, vt_alpha, vt_delta) in value:
    (u, v, w) = f.strassen(ra, dec, vr, vt_alpha, vt_delta)
    f.update_product(cursor, son_table, 'u', son_key_column, (source_id, u))
    f.update_product(cursor, son_table, 'v', son_key_column, (source_id, v))
    f.update_product(cursor, son_table, 'w', son_key_column, (source_id, w))

# certificar de que os dados foram gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()