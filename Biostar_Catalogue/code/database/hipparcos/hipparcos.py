import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

table_name = 'hipparcos'
column_key_name = 'hip'

# apagar a tabela table_name caso ela já exista
cursor.execute("drop table if exists {}".format(table_name))

# criar tabela table_name no BD
cursor.execute("create table {table_name}( "
               "hip int primary key, "
               "hd int null, "
               "bd char(100) null, "
               "cod char(100) null, "
               "cpd char(100) null, "
               "vmag numeric(65, 30) null, "    
               "ra numeric(65, 30) null, "
               "de numeric(65, 30) null, "
               "rahms char(100) null, "
               "dedms char(100) null, "
               "plx numeric(65, 30) null, "
               "e_plx numeric(65, 30) null, "
               "pmra numeric(65, 30) null, "
               "pmde numeric(65, 30) null, "
               "btmag numeric(65, 30) null, "
               "e_btmag numeric(65, 30) null, "
               "vtmag numeric(65, 30) null, "
               "e_vtmag numeric(65, 30) null, "
               "b_v numeric(65, 30) null, "
               "e_b_v numeric(65, 30) null, "
               "sptype char(100) null, "
               "r_sptype char(100) null "
               ")".format(table_name=table_name))

# carregar os dados de public.hipparcos na tabela table_name
with open("../input_files/hipparcos.csv", "r") as csv_file:

    next(csv_file) # pular a linha do header do csv

    for line in csv_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        line = line.split(",")

        # load hip
        f.insert_key(cursor, table_name, column_key_name, line, 0)
        lastrowid = line[0].strip() # .strip() para retirar os espaços vazios da chave

        columns_names_and_indexes = [('hd', 1), ('bd', 2), ('cod', 3), ('cpd', 4), ('vmag', 5), ('ra', 6), ('de', 7),
                                     ('rahms', 8), ('dedms', 9), ('plx', 10), ('e_plx', 11), ('pmra', 12), ('pmde', 13),
                                     ('btmag', 14), ('e_btmag', 15), ('vtmag', 16), ('e_vtmag', 17), ('b_v', 18),
                                     ('e_b_v', 19), ('sptype', 20), ('r_sptype', 21)]

        for(column_name, index) in columns_names_and_indexes:
            f.update_table(cursor, table_name, column_name, line, index, column_key_name, lastrowid)

csv_file.close()

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()