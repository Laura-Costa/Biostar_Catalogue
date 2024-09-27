import code.figures.functions as f
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Gaia30pc'
son_table = 'Gaia30pc_product'

"""
fazer um histograma da distribuição de M(G)
estrelas com parallax >=50.00 ou (parallax < 50.00 e parallax+parallax_error >= 50.00)
sem Bp-Rp mas com G
são 72 estrelas
"""
query = ("select trim({father_table}.parallax)+0, " 
         "trim({son_table}.MG)+0 " 
         "from {father_table}, {son_table} " 
         "where {father_table}.designation = {son_table}.designation and " 
         "{father_table}.parallax >= (1.0/23)*1000 and " 
         "( " 
         "{father_table}.parallax >= 50.00 or " 
         "({father_table}.parallax < 50.00 and ({father_table}.parallax + 2*{father_table}.parallax_error) >= 50.00) " 
         ") and " 
         "{son_table}.Bp_Rp is null and " 
         "{father_table}.phot_g_mean_mag is not null and " 
         "{son_table}.MG is not null").format(father_table=father_table, son_table=son_table)
f.histogram(query, cursor,'M(G)', 10, '/23pc_selection/figures/histograma1.pdf')

'''
fazer um histograma da distribuição de M(G)
estrelas com parallax >= (1/23)*1000 
estrelas sem cor Bp-Rp
estrelas com G
são 99 estrelas
'''
query = ("select trim({father_table}.parallax)+0, " 
         "trim({son_table}.MG)+0 " 
         "from {father_table}, {son_table} " 
         "where {father_table}.designation = {son_table}.designation and " 
         "{father_table}.parallax >= (1.0/23)*1000 and " 
         "{son_table}.Bp_Rp is null and " 
         "{father_table}.phot_g_mean_mag is not null and " 
         "{son_table}.MG is not null").format(father_table=father_table, son_table=son_table)
f.histogram(query, cursor,'M(G)', 15, '/23pc_selection/figures/histograma2.pdf', rot=15)


# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()
