import code.figures.functions as f
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Gaia50pc'

"""
Histograma de sigma-pi
para as estrelas da borda
paralaxe >= 50 ou (paralaxe < 50 e paralaxe+erro >= 50)
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.parallax >= 50.00 "
         "or "
         "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ")".format(father_table=father_table))
f.histogram(query, cursor, 'paralaxe', 4, '/CAT1/histogramas/hist.pdf', log=True)