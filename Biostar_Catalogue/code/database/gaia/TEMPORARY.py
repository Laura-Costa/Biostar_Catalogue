import mysql.connector
import code.functions.database as f2

# abrir a conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()


table = 'simbad'

# apagar a tabela table_name caso ela já exista
cursor.execute("drop table if exists {table}".format(table=table))

# criar a tabela table_name
cursor.execute("create table {table}( "
               "source_id bigint primary key, "
               "radial_velocity decimal(65, 30) null, "
               "radial_velocity_error decimal(65, 30) null, "
               "foreign key(source_id) references gaia(source_id) on delete restrict)".format(table=table))


table = 'simbad'
father_key_column = 'source_id'

# ler o arquivo
with open("/home/lh/Downloads/CAT1(1).txt") as file:
    for line in file:
        lista = line.split(" ")
        lista = [x for x in lista if x != '']
        lista.remove('\n')
        print(lista)
        source_id = lista[2]
        f2.insert_key(cursor, table, 'source_id', (source_id,), 0)
        if len(lista) != 5:
            continue
        vr = lista[3]
        e_vr = lista[4]

        f2.update_table(cursor, table, 'radial_velocity', [vr], 0, 'source_id', source_id)
        f2.update_table(cursor, table, 'radial_velocity_error', [e_vr], 0, 'source_id', source_id)

        print(lista)

# certificar de que os dados foram gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()