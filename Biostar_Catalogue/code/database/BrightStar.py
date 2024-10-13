import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

son_table = 'BrightStar'
son_column_key = 'HR'
father_table_Hipparcos = 'Hipparcos'
father_table_Hipparcos_column_key = 'HIP'
father_table_Gaia = 'Gaia30pc'
father_table_Gaia_column_key = 'designation'

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_name no BD
cursor.execute("create table {son_table}( "
               "HR char(100) primary key, "
               "HIP char(100) null, "
               "designation char(100) null, "
               "Name char(100) null, "
               "DM_Cat char(100) null, "
               "DM char(100) null, "
               "HD char(100) null, "
               "SAO char(100) null, "
               "FK5 char(100) null, "
               "Multiple char(100) null, "
               "ADS char(100) null, "
               "ADS_Comp char(100) null, "
               "Var_ID char(100) null, "
               "V numeric(65, 30) null, "
               "B_V numeric(65, 30) null, "
               "SpType char(100) null, "
               "Mult_MDiff numeric(65, 30) null, "
               "Mult_Sep numeric(65, 30) null, "
               "Mult_ID char(100) null, "
               "Mult_Cnt int null, "
               "simbad_DR1 char(100) null, "
               "simbad_DR2 char(100) null, "
               "simbad_DR3 char(100) null, "
               "simbad_HIP char(100) null, "
               "simbad_parallax numeric(65, 30) null, "
               "simbad_parallax_error numeric(65, 30) null, "
               "simbad_B numeric(65, 30) null, "
               "simbad_V numeric(65, 30) null, "
               "foreign key(HIP) references {father_table_Hipparcos}({father_table_Hipparcos_column_key}) on delete restrict, "
               "foreign key(designation) references {father_table_Gaia}({father_table_Gaia_column_key}) on delete restrict)".format(
                                                   son_table=son_table,
                                                   father_table_Hipparcos=father_table_Hipparcos,
                                                   father_table_Hipparcos_column_key=father_table_Hipparcos_column_key,
                                                   father_table_Gaia = father_table_Gaia,
                                                   father_table_Gaia_column_key=father_table_Gaia_column_key))

# carregar os dados de BSC5_edited.DAT na tabela son_table
with open("input_files/BSC5_edited.DAT", "r") as dat_file:
    for line in dat_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        # load HR
        f.insert_key(cursor, son_table, son_column_key, line, 0, True, 4)
        lastrowid = "HR " + line[0:4].strip() # .strip() para retirar os espaços vazios da segunda componente do HR

        # load Name
        f.update_table(cursor, son_table, 'Name', line, 4, son_column_key, lastrowid, False, 14)

        # load DM_Cat
        f.update_table(cursor, son_table, 'DM_Cat', line, 14, son_column_key, lastrowid, False, 16)

        # load DM
        f.update_table(cursor, son_table, 'DM', line, 16, son_column_key, lastrowid, False, 25)

        # load HD
        f.update_table(cursor, son_table, 'HD', line, 25, son_column_key, lastrowid, True, 31)

        # load SAO
        f.update_table(cursor, son_table, 'SAO', line, 31, son_column_key, lastrowid, True, 37)

        # load FK5
        f.update_table(cursor, son_table, 'FK5', line, 37, son_column_key, lastrowid, True, 41)

        # load Mutiple
        f.update_table(cursor, son_table, 'Multiple', line, 43, son_column_key, lastrowid, False, 44)

        # load ADS
        f.update_table(cursor, son_table, 'ADS', line, 44, son_column_key, lastrowid, True, 49)

        # load ADS_Comp
        f.update_table(cursor, son_table, 'ADS_Comp', line, 49, son_column_key, lastrowid, False, 51)

        # load Var_ID
        f.update_table(cursor, son_table, 'Var_ID', line, 51, son_column_key, lastrowid, False, 60)

        # load V
        f.update_table(cursor, son_table, 'V', line, 102, son_column_key, lastrowid, False, 107)

        # load B_V
        f.update_table(cursor, son_table, 'B_V', line, 109, son_column_key, lastrowid, False, 114)

        # load SpType
        f.update_table(cursor, son_table, 'SpType', line, 127, son_column_key, lastrowid, False, 147)

        # load Mult_MDiff
        f.update_table(cursor, son_table, 'Mult_MDiff', line, 180, son_column_key, lastrowid, False, 184)

        # load Mult_Sep
        f.update_table(cursor, son_table, 'Mult_Sep', line, 184, son_column_key, lastrowid, False, 190)

        # load Mult_ID

        # O HR 2343 tem o valor de Mult_ID igual a -> AA'
        # Aqui este caractere "'" é removido
        #########
        index2 = 194
        if lastrowid == 'HR 2343':
            index2 = index2 - 2
        #########
        f.update_table(cursor, son_table, 'Mult_ID', line, 190, son_column_key, lastrowid, False, index2)

        # load Mult_Cnt
        f.update_table(cursor, son_table, 'Mult_Cnt', line, 194, son_column_key, lastrowid, False, 196)

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()