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
               "MRp decimal(65, 30) null, "
               "MRp_error decimal(65, 30) null, "
               "MBp decimal(65, 30) null, "
               "MBp_error decimal(65, 30) null, "
               "MG decimal(65, 30) null, "
               "MG_error decimal(65, 30) null, "
               "distance_gspphot_error decimal(65, 30) null, "
               "azero_gspphot_error decimal(65, 30) null, "
               "foreign key({son_key_column}) references {father_table}({father_key_column}) on delete restrict "
               ")".format(son_table=son_table,
                          son_key_column=son_key_column,
                          father_table=father_table,
                          father_key_column=father_key_column))

# carregar os dados de table_name.csv na tabela table_name
with open("../input_files/Gaia_product_algumas_estrelas_gaia-result.csv", "r") as csv_file:

    next(csv_file) # pular a linha do header do csv

    for line in csv_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        line = line.split(",")

        # load designation
        f.insert_key(cursor, son_table, son_key_column, line, 0)
        lastrowid = line[0].strip() # .strip() para retirar os espaços vazios da designation

        columns_names_and_indexes = [('MRp', 1), ('MRp_error', 2), ('MBp', 3), ('MBp_error', 4),
                                     ('MG', 5), ('MG_error', 6), ('distance_gspphot_error', 7), ('azero_gspphot_error', 8)]

        for(column_name, index) in columns_names_and_indexes:
            f.update_table(cursor, son_table, column_name, line, index, son_key_column, lastrowid)

csv_file.close()

# certificar de que os dados foram gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()