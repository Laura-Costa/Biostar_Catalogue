from astroquery.simbad import Simbad
import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

son_table = 'Gaia30pc'
father_table = 'Hipparcos'
column_key_name = 'designation'

# apagar a tabela table_name caso ela já exista
cursor.execute("drop table if exists {}".format(son_table))

# criar a tabela table_name
cursor.execute("create table {son_table}( "
               "designation char(100) primary key, "
               "HIP char(100) null, "
               "simbad_HIP char(100) null, "
               "simbad_HD char(100) null, "
               "in_simbad bool null, "
               "right_ascension numeric(65, 30) null, "
               "declination numeric(65, 30) null, "
               "parallax numeric(65, 30) null, "
               "parallax_error numeric(65, 30) null, "
               "pm numeric(65, 30) null, "
               "pmra numeric(65, 30) null, "
               "pmdec numeric(65, 30) null, "
               "ruwe numeric(65, 30) null, "
               "phot_g_mean_mag numeric(65, 30) null, "
               "phot_bp_mean_mag numeric(65, 30) null, "
               "phot_rp_mean_mag numeric(65, 30) null, "
               "teff_gspphot numeric(65, 30) null, "
               "teff_gspphot_lower numeric(65, 30) null, "
               "teff_gspphot_upper numeric(65, 30) null, "
               "logg_gspphot numeric(65, 30) null, "
               "logg_gspphot_lower numeric(65, 30) null, "
               "logg_gspphot_upper numeric(65, 30) null, "
               "mh_gspphot numeric(65, 30) null, "
               "mh_gspphot_lower numeric(65, 30) null, "
               "mh_gspphot_upper numeric(65, 30) null, "
               "distance_gspphot numeric(65, 30) null, "
               "distance_gspphot_lower numeric(65, 30) null, "
               "distance_gspphot_upper numeric(65, 30) null, "
               "foreign key(HIP) references {father_table}(HIP) on delete restrict)".format(son_table=son_table,
                                                                                            father_table=father_table))

# carregar os dados de table_name.csv na tabela table_name
with open("input_files/Gaia30pc.csv", "r") as csv_file:

    next(csv_file) # pular a linha do header do csv

    for line in csv_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        line = line.split(",")

        if len(line[3].strip()) == 0 or float(line[3].strip()) < (1.0/30)*1000:
            continue # pular os registros que não têm paralaxe ou têm paralaxe menor do que (1/30)*1000

        # load designation
        f.insert_key(cursor, son_table, column_key_name, line, 0)
        lastrowid = line[0].strip() # .strip() para retirar os espaços vazios da designation

        # load HIP
        cursor.execute("update {son_table} set {son_table}.HIP = {son_table}.simbad_HIP "
                       "where {son_table}.simbad_HIP in (select {father_table}.HIP from {father_table})".format(son_table=son_table,
                                                                                                                father_table=father_table))

        # load simbad_HIP
        tab = Simbad.query_objectids(lastrowid)
        f.simbad_search_id_by_id(cursor, tab, 'HIP', son_table, 'simbad_HIP', column_key_name, lastrowid)

        # load simbad_HD
        f.simbad_search_id_by_id(cursor, tab, 'HD', son_table, 'simbad_HD', column_key_name, lastrowid)

        # load in_simbad
        f.search_id_in_simbad(tab, cursor, son_table, 'in_simbad', column_key_name, lastrowid)

        columns_names_and_indexes = [('right_ascension', 1), ('declination', 2), ('parallax', 3), ('parallax_error', 4),
                                     ('pm', 5), ('pmra', 6), ('pmdec', 7), ('ruwe', 8), ('phot_g_mean_mag', 9),
                                     ('phot_bp_mean_mag', 10), ('phot_rp_mean_mag', 11), ('teff_gspphot', 12),
                                     ('teff_gspphot_lower', 13), ('teff_gspphot_upper', 14), ('logg_gspphot', 15),
                                     ('logg_gspphot_lower', 16), ('logg_gspphot_upper', 17), ('mh_gspphot', 18),
                                     ('mh_gspphot_lower', 19), ('mh_gspphot_upper', 20), ('distance_gspphot', 21),
                                     ('distance_gspphot_lower', 22), ('distance_gspphot_upper', 23)]
        for(column_name, index) in columns_names_and_indexes:
            f.update_table(cursor, son_table, column_name, line, index, column_key_name, lastrowid)

csv_file.close()

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()