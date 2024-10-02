import mysql.connector
import code.functions.pyplot_scatterplot as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = "Gaia30pc"

# Criar o diagrama CAT1_errors.svg
query = ("select trim({father_table}.parallax_error)+0, "
               "trim({father_table}.parallax)+0 "
               "from {father_table} "
               "where {father_table}.parallax >= 50.00 or "
               "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))".format(father_table=father_table))
f.scatterplot(cursor, query, 0.05, 0.05, 8.0, 8.0, "parallax (mas)", "parallax error (mas)", 'CAT1_parallax_error_versus_parallax.svg', "CAT1: σ(π) versus π em escala linear")

# Criar o diagrama CAT1_parallax_error_versus_parallax_log_scale.svg
query = ("select trim({father_table}.parallax_error)+0, "
               "trim({father_table}.parallax)+0 "
               "from {father_table} "
               "where {father_table}.parallax >= 50.00 or "
               "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))".format(father_table=father_table))
f.scatterplot(cursor, query, 0.001, 0.5, 0.001, 15.0, 'parallax (mas)',
              'parallax error (mas)', 'CAT1_parallax_error_versus_parallax_log_scale.svg', "CAT1: σ(π) versus π em escala logarítmica", 30, True, True)

cursor.close()
connection.close()