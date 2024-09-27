from astroquery.simbad import Simbad
import mysql.connector
import code.database.functions as f
import time

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

table_name = 'Hipparcos'
column_key_name = 'HIP'

# apagar a tabela Hipparcos caso ela já exista
cursor.execute("drop table if exists {}".format(table_name))

# criar tabela Hipparcos no BD
cursor.execute("create table {}( "
               "HIP char(100) primary key, "
               "HD char(100) null, "
               "BD char(100) null, "
               "CoD char(100) null, "
               "CPD char(100) null, "
               "in_simbad bool, "
               "simbad_DR1 char(100) null, "
               "simbad_DR2 char(100) null, "
               "simbad_DR3 char(100) null, "
               "Vmag numeric(65, 30) null, "
               "RAdeg numeric(65, 30) null, "
               "DEdeg numeric(65, 30) null, "
               "RAhms char(100) null, "
               "DEdms char(100) null, "
               "Plx numeric(65, 30) null, "
               "e_Plx numeric(65, 30) null, "
               "pmRA numeric(65, 30) null, "
               "pmDE numeric(65, 30) null, "
               "BTmag numeric(65, 30) null, "
               "e_BTmag numeric(65, 30) null, "
               "VTmag numeric(65, 30) null, "
               "e_VTmag numeric(65, 30) null, "
               "B_V numeric(65, 30) null, "
               "e_B_V numeric(65, 30) null "
               ")".format(table_name))

# carregar os dados de HIP_MAIN.DAT na tabela Hipparcos
with open("input_files/HIP_MAIN.DAT", "r") as dat_file:
    for line in dat_file:

        if len(line) == 0 or line == '\n' or line == '\r':
            continue # pular as linhas vazias do arquivo

        line = line.split("|")

        if len(line[11].strip()) == 0: # or float(line[11].strip()) < 29.00:
            continue # pular os registros que não têm paralaxe

        # load HIP
        f.insert_key(cursor, table_name, column_key_name, line, 1, True)
        lastrowid = "HIP " + line[1].strip()

        # load in_simbad
        tab = Simbad.query_objectids(lastrowid)
        f.search_id_in_simbad(tab, cursor, table_name, 'in_simbad', column_key_name, lastrowid)

        # load simbad_DRX
        for data_release in ['1', '2', '3']:
            time.sleep(0.000000001)
            f.simbad_search_id_by_id(cursor, tab, 'Gaia DR'+data_release, table_name, 'simbad_DR'+data_release, column_key_name, lastrowid)

        # load HD
        f.update_table(cursor, table_name, 'HD', line, 71, column_key_name, lastrowid, True)

        columns_names_and_indexes = [('BD', 72), ('CoD', 73), ('CPD', 74), ('Vmag', 5), ('RAdeg', 8), ('DEdeg', 9),
                                     ('RAhms', 3), ('DEdms', 4), ('Plx', 11), ('e_Plx', 16), ('pmRA', 12), ('pmDE', 13),
                                     ('BTmag', 32), ('e_BTmag', 33), ('VTmag', 34), ('e_VTmag', 35), ('B_V', 37), ('e_B_V', 38)]

        for (column_name, index) in columns_names_and_indexes:
            f.update_table(cursor, table_name, column_name, line, index, column_key_name, lastrowid)

dat_file.close()

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()