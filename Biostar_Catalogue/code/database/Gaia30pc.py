from astroquery.simbad import Simbad
import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

table_name = 'Gaia30pc'
column_key_name = 'designation'

# apagar a tabela table_name caso ela já exista
cursor.execute("drop table if exists {}".format(table_name))

# criar a tabela table_name
cursor.execute("create table {table_name}( "
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
               "foreign key(HIP) references Hipparcos(HIP) on delete restrict)".format(table_name=table_name))

# carregar os dados de table_name.csv na tabela table_name
with open("input_files/Gaia30pc.csv", "r") as csv_file:

    next(csv_file) # pular a linha do header do csv

    for line in csv_file:

        if len(line) == 0 or line == '\n' or line == '\r':
            continue # pular as linhas vazias do arquivo

        line = line.split(",")

        if len(line[3].strip()) == 0 or float(line[3].strip()) < (1.0/30)*1000:
            continue # pular os registros que não têm paralaxe ou têm paralaxe menor do que (1/30)*1000

        # load designation
        f.insert_key(cursor, table_name, column_key_name, line, 0)
        lastrowid = line[0].strip()

        # load HIP
        cursor.execute("update {table_name} set {table_name}.HIP = {table_name}.simbad_HIP "
                       "where {table_name}.simbad_HIP in (select Hipparcos.HIP from Hipparcos)".format(table_name=table_name))

        # load simbad_HIP
        tab = Simbad.query_objectids(lastrowid)
        f.simbad_search_id_by_id(cursor, tab, 'HIP', table_name, 'simbad_HIP', column_key_name, lastrowid)

        # load simbad_HD
        f.simbad_search_id_by_id(cursor, tab, 'HD', table_name, 'simbad_HD', column_key_name, lastrowid)

        # load in_simbad
        f.search_id_in_simbad(tab, cursor, table_name, 'in_simbad', column_key_name, lastrowid)

        columns_names_and_indexes = [('right_ascension', 1), ('declination', 2), ('parallax', 3), ('parallax_error', 4),
                                     ('pm', 5), ('pmra', 6), ('pmdec', 7), ('ruwe', 8), ('phot_g_mean_mag', 9),
                                     ('phot_bp_mean_mag', 10), ('phot_rp_mean_mag', 11), ('teff_gspphot', 12),
                                     ('teff_gspphot_lower', 13), ('teff_gspphot_upper', 14), ('logg_gspphot', 15),
                                     ('logg_gspphot_lower', 16), ('logg_gspphot_upper', 17), ('mh_gspphot', 18),
                                     ('mh_gspphot_lower', 19), ('mh_gspphot_upper', 20), ('distance_gspphot', 21),
                                     ('distance_gspphot_lower', 22), ('distance_gspphot_upper', 23)]
        for(column_name, index) in columns_names_and_indexes:
            f.update_table(cursor, table_name, column_name, line, index, column_key_name, lastrowid)

csv_file.close()

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()