from astroquery.simbad import Simbad
import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

son_table = 'Gaia'
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
               "foreign key(HIP) references {father_table}(HIP) on delete restrict)".format(son_table=son_table,
                                                                                            father_table=father_table))

# carregar os dados de table_name.csv na tabela table_name
with open("../input_files/Gaia-result.csv", "r") as csv_file:

    next(csv_file) # pular a linha do header do csv

    for line in csv_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        line = line.split(",")

        """ vamos verificar no resultado final se alguma estrela não tem paralaxe
        if len(line[3].strip()) == 0: # or float(line[3].strip()) < (1.0/30)*1000:
            continue # pular os registros que não têm paralaxe ou têm paralaxe menor do que (1/30)*1000
        """

        # load designation
        f.insert_key(cursor, son_table, column_key_name, line, 0)
        lastrowid = line[0].strip() # .strip() para retirar os espaços vazios da designation

        columns_names_and_indexes = [('right_ascension', 1), ('declination', 2), ('parallax', 3), ('parallax_error', 4),
                                     ('pm', 5), ('pmra', 6), ('pmdec', 7), ('ruwe', 8), ('phot_variable_flag', 9),
                                     ('non_single_star', 10), ('phot_g_mean_mag', 11), ('phot_bp_mean_mag', 12),
                                     ('phot_rp_mean_mag', 13), ('bp_rp', 14), ('bp_g', 15), ('g_rp', 16), ('teff_gspphot', 17),
                                     ('teff_gspphot_lower', 18), ('teff_gspphot_upper', 19), ('logg_gspphot', 20),
                                     ('logg_gspphot_lower', 21), ('logg_gspphot_upper', 22), ('mh_gspphot', 23),
                                     ('mh_gspphot_lower', 24), ('mh_gspphot_upper', 25), ('distance_gspphot', 26),
                                     ('distance_gspphot_lower', 27), ('distance_gspphot_upper', 28), ('azero_gspphot', 29),
                                     ('azero_gspphot_lower', 30), ('azero_gspphot_upper', 31)]
        for(column_name, index) in columns_names_and_indexes:
            f.update_table(cursor, son_table, column_name, line, index, column_key_name, lastrowid)

csv_file.close()

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()