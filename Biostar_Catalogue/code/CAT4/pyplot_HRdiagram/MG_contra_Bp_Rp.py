import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['tomato']
HDs = ['HD 131156B']

def sql_query(y_axis, x_axis):
    father_table = 'CAT1'
    son_table = 'CAT1_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "{father_table}.HIP is null".format(father_table=father_table,
                                       son_table=son_table,
                                       x_axis=x_axis,
                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({son_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "{son_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{father_table}.HIP is null and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)
"""
fazer o diagrama de M(G) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MG', 'Bp_Rp')
for ext in ['jpg']:
    f.diagram(cursor, query, query_emphasis, colors, HDs, 'CAT4/pyplot_HRdiagram/' + ext + '/MG_Bp_Rp.' + ext, 0.25, 1.0, r'$B_p-R_p$', r'$M(G)$', 5, 0.20, 0.20, 0.25, 0.25, 'CAT4: CAT1 - hipparcos', xrot=0, redx=8, redy=7)

# fechar a conexão com o BD
connection.close()