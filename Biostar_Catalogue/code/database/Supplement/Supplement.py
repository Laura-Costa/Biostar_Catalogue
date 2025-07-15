import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

son_table = 'Supplement'
son_key_column = 'ordinal_number'
father_table_Hipparcos = 'hipparcos'
father_table_Gaia = 'gaia'

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table no BD
cursor.execute("create table {son_table}( "
               "{son_key_column} int not null auto_increment primary key, "
               "HIP char(100) null, "
               "designation char(100) null, "
               "DM_Cat char(100) null, " # not
               "DM char(100) null, " # not
               "HD char(100) null, "
               "HD_Suffix char(100) null, "
               "SAO char(100) null, "
               "Comp char(100) null, "
               "Comp_Cnt int null, "
               "V numeric(65, 30) null, "
               "B_V numeric(65, 30) null, "
               "SpType char(100) null, "
               "Parallax numeric(65, 30) null, "
               "Mult_MDiff numeric(65, 30) null, "
               "Mult_Flag char(100) null, "
               "Mult_Sep numeric(65, 30) null, "
               "Sep_Code char(100) null, "
               "Mult_ID char(100) null, "
               "simbad_main_identifier char(100) null, "
               "simbad_DR1 char(100) null, "
               "simbad_DR2 char(100) null, "
               "simbad_DR3 char(100) null, "
               "simbad_HIP char(100) null, "
               "simbad_parallax numeric(65, 30) null, "
               "simbad_parallax_error numeric(65, 30) null, "
               "simbad_parallax_source char(100) null, "
               "simbad_B numeric(65, 30) null, "
               "simbad_V numeric(65, 30) null, "
               "simbad_SpType char(100) null, "
               #"primary key(DM_Cat, DM), "
               "foreign key(HIP) references {father_table_Hipparcos}(HIP) on delete restrict, "
               "foreign key(designation) references {father_table_Gaia}(designation) on delete restrict)".format(son_table=son_table,
                                                                                                                 son_key_column=son_key_column,
                                                                                                                 father_table_Hipparcos=father_table_Hipparcos,
                                                                                                                 father_table_Gaia=father_table_Gaia))

# carregar os dados de BSC4S.DAT na tabela son_table
cont = 0
with open("../input_files/BSC4S.DAT", "r") as dat_file:
    for line in dat_file:

        if len(line) == 0 or line == '\n' or line == '\r' or line == '\r\n':
            continue # pular as linhas vazias do arquivo

        cont += 1
        """
        DM_Cat = line[8:10]
        DM = line[10:19]
        cursor.execute("insert into {son_table}(DM_Cat, DM) values('{DM_Cat}', '{DM}')".format(son_table=son_table, DM_Cat=DM_Cat, DM=DM))
        """
        # load DM_Cat
        f.insert_key(cursor, son_table, 'DM_Cat', line, 8, False, 10)

        # load DM
        f.update_table(cursor, son_table, 'DM', line, 10, son_key_column, cont, False, 19)

        # load HD
        f.update_table(cursor, son_table, 'HD', line, 0, son_key_column, cont, True, 6)

        # load HD_Suffix
        f.update_table(cursor, son_table, 'HD_Suffix', line, 6, son_key_column, cont, False, 8)

        # load SAO
        f.update_table(cursor, son_table, 'SAO', line, 19, son_key_column, cont, True, 26)

        # load Comp
        f.update_table(cursor, son_table, 'Comp', line, 204, son_key_column, cont, False, 209)

        # load Comp_Cnt
        f.update_table(cursor, son_table, 'Comp_Cnt', line, 209, son_key_column, cont, False, 211)

        # load V

        # A HD 84005 tem o valor de V igual a -> 6.77:
        # Aqui, este caractere ":" é removido
        #########
        HD = 'HD ' + line[0:6].strip()
        index2 = 109
        if HD == 'HD 84005':
            index2 = index2 - 1
        #########
        f.update_table(cursor, son_table, 'V', line, 104, son_key_column, cont, False, index2)

        # load B_V
        f.update_table(cursor, son_table, 'B_V', line, 109, son_key_column, cont, False, 115)

        # load SpType
        f.update_table(cursor, son_table, 'SpType', line, 127, son_key_column, cont, False, 148)

        # load Parallax
        f.update_table(cursor, son_table, 'Parallax', line, 162, son_key_column, cont, False, 168)

        # load Mult_MDiff
        f.update_table(cursor, son_table, 'Mult_MDiff', line, 184, son_key_column, cont, False, 188)

        # load Mult_Flag
        f.update_table(cursor, son_table, 'Mult_Flag', line, 188, son_key_column, cont, False, 190)

        # load Mult_Sep
        f.update_table(cursor, son_table, 'Mult_Sep', line, 190, son_key_column, cont, False, 195)

        # load Sep_Code
        f.update_table(cursor, son_table, 'Sep_Code', line, 195, son_key_column, cont, False, 196)

        # load Mult_ID
        f.update_table(cursor, son_table, 'Mult_ID', line, 27, son_key_column, cont, False, 36)

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()