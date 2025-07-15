import mysql.connector
import database

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

son_table = 'gaia'
father_table = 'hipparcos'
column_key_name = 'source_id'

# apagar a tabela table_name caso ela já exista
cursor.execute("drop table if exists {}".format(son_table))

# criar a tabela table_name
cursor.execute("create table {son_table}( "
               "source_id bigint primary key, "
               "designation char(100) null, "
               "hip int null, "
               "right_ascension decimal(65, 30) null, "
               "declination decimal(65, 30) null, "
               "parallax decimal(65, 30) null, "
               "parallax_error decimal(65, 30) null, "
               "pm decimal(65, 30) null, "
               "pmra decimal(65, 30) null, "
               "pmdec decimal(65, 30) null, "
               "ruwe decimal(65, 30) null, "
               "phot_variable_flag char(100) null, "
               "non_single_star int null,"
               "phot_g_mean_mag decimal(65, 30) null, "
               "phot_bp_mean_mag decimal(65, 30) null, "
               "phot_rp_mean_mag decimal(65, 30) null, "
               "bp_rp decimal(65, 30) null, "
               "bp_g decimal(65, 30) null, "
               "g_rp decimal(65, 30) null, "
               "teff_gspphot decimal(65, 30) null, "
               "teff_gspphot_lower decimal(65, 30) null, "
               "teff_gspphot_upper decimal(65, 30) null, "
               "logg_gspphot decimal(65, 30) null, "
               "logg_gspphot_lower decimal(65, 30) null, "
               "logg_gspphot_upper decimal(65, 30) null, "
               "mh_gspphot decimal(65, 30) null, "
               "mh_gspphot_lower decimal(65, 30) null, "
               "mh_gspphot_upper decimal(65, 30) null, "
               "distance_gspphot decimal(65, 30) null, "
               "distance_gspphot_lower decimal(65, 30) null, "
               "distance_gspphot_upper decimal(65, 30) null, "
               "azero_gspphot decimal(65, 30) null, "
               "azero_gspphot_lower decimal(65, 30) null, "
               "azero_gspphot_upper decimal(65, 30) null, "
               "radial_velocity decimal(65, 30) null, "
               "radial_velocity_error decimal(65, 30) null, "
               "foreign key(hip) references {father_table}(hip) on delete restrict)".format(son_table=son_table,
                                                                                            father_table=father_table))

# carregar os dados de table_name.csv na tabela table_name
with open("/home/lh/Documents/biostar_catalogue/code/database/input/gaia.csv", "r") as csv_file:

    next(csv_file) # pular a linha do header do csv

    for line in csv_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        line = line.split(",")

        # load designation
        database.insert_key(cursor, son_table, column_key_name, line, 0)
        lastrowid = line[0].strip() # .strip() para retirar os espaços vazios do source_id

        columns_names_and_indexes = [('designation', 1),
                                     ('right_ascension', 2), ('declination', 3),
                                     ('parallax', 4), ('parallax_error', 5),
                                     ('pm', 6), ('pmra', 7), ('pmdec', 8),
                                     ('ruwe', 9), ('phot_variable_flag', 10), ('non_single_star', 11),
                                     ('phot_g_mean_mag', 12), ('phot_bp_mean_mag', 13), ('phot_rp_mean_mag', 14),
                                     ('bp_rp', 15), ('bp_g', 16), ('g_rp', 17),
                                     ('teff_gspphot', 18), ('teff_gspphot_lower', 19), ('teff_gspphot_upper', 20),
                                     ('logg_gspphot', 21), ('logg_gspphot_lower', 22), ('logg_gspphot_upper', 23),
                                     ('mh_gspphot', 24), ('mh_gspphot_lower', 25), ('mh_gspphot_upper', 26),
                                     ('distance_gspphot', 27), ('distance_gspphot_lower', 28), ('distance_gspphot_upper', 29),
                                     ('azero_gspphot', 30), ('azero_gspphot_lower', 31), ('azero_gspphot_upper', 32),
                                     ('radial_velocity', 33), ('radial_velocity_error', 34)]
        for(column_name, index) in columns_names_and_indexes:
            database.update_table(cursor, son_table, column_name, line, index, column_key_name, lastrowid)

csv_file.close()

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()