import mysql.connector
import code.functions.database as f

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

son_table = "BrightStarMultiple"
son_column_key = "ordinal_number"
father_table_Hipparcos = "Hipparcos"
father_table_Hipparcos_column_key = "HIP"
father_table_Gaia = "Gaia30pc"
father_table_Gaia_column_key = "designation"
father_table_Bright = 'BrightStar'
father_table_Bright_column_key = 'HR'

# apagar a tabela son_table caso ela já exista
cursor.execute("drop table if exists {son_table}".format(son_table=son_table))

# criar a tabela son_table no BD
cursor.execute("create table {son_table}( "
               "{son_column_key} int not null auto_increment primary key, "
               "HR char(100) null, "
               "HIP char(100) null, "
               "designation char(100) null, "
               "identifier char(100) null, "
               "simbad_DR1 char(100) null, "
               "simbad_DR2 char(100) null, "
               "simbad_DR3 char(100) null, "
               "simbad_HIP char(100) null, "
               "simbad_parallax numeric(65, 30) null, "
               "simbad_parallax_error numeric(65, 30) null, "
               "simbad_B numeric(65, 30) null, "
               "simbad_V numeric(65, 30) null, "
               "foreign key(HIP) references {father_table_Hipparcos}({father_table_Hipparcos_column_key}) on delete restrict, "
               "foreign key(designation) references {father_table_Gaia}({father_table_Gaia_column_key}) on delete restrict, "
               "foreign key(HR) references {father_table_Bright}({father_table_Bright_column_key}) on delete restrict"
               ")".format(son_table=son_table,
                          son_column_key=son_column_key,
                          father_table_Hipparcos=father_table_Hipparcos,
                          father_table_Hipparcos_column_key=father_table_Hipparcos_column_key,
                          father_table_Gaia=father_table_Gaia,
                          father_table_Gaia_column_key=father_table_Gaia_column_key,
                          father_table_Bright=father_table_Bright,
                          father_table_Bright_column_key=father_table_Bright_column_key))

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()