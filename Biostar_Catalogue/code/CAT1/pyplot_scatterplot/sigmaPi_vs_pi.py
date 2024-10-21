import mysql.connector
import code.functions.pyplot_scatterplot as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = "CAT1"

# Criar o diagrama CAT1_errors.svg
query = ("select trim({father_table}.parallax_error)+0, "
               "trim({father_table}.parallax)+0 "
               "from {father_table} "
               "where {father_table}.parallax >= 50.00 or "
               "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))".format(father_table=father_table))
f.scatterplot(cursor, query, 0.05, 0.05, 8.0, 8.0, "paralaxe em milissegundos de arco", "erro da paralaxe em milissegundos de arco", '/jpg/erro_da_paralaxe_contra_paralaxe.jpg', "CAT1: σ(π) x π")

# Criar o diagrama CAT1_parallax_error_versus_parallax_log_scale.svg
query = ("select trim({father_table}.parallax_error)+0, "
               "trim({father_table}.parallax)+0 "
               "from {father_table} "
               "where {father_table}.parallax >= 50.00 or "
               "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))".format(father_table=father_table))
f.scatterplot(cursor, query, 0.001, 0.5, 0.001, 15.0, 'paralaxe em milissegundos de arco (escala logarítmica)',
              'erro da paralaxe em milissegundos de arco (escala logarítmica)', '/jpg/erro_da_paralaxe_contra_paralaxe_log.jpg', "CAT1: σ(π) x π", 30, True, True)

cursor.close()
connection.close()
