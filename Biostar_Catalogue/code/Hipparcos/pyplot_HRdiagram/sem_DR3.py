import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(y_axis, x_axis):
    father_table = 'hipparcos'
    son_table = 'Hipparcos_product'

    query = ("select {father_table}.HD, "
             "trim({father_table}.Plx)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.HIP = {son_table}.HIP and "
             "{father_table}.simbad_DR3 is null and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null".format(father_table=father_table,
                                                       son_table=son_table,
                                                       x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.HD, "
                      "trim({son_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.HIP = {son_table}.HIP and "
                      "{son_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{father_table}.HD = ".format(father_table=father_table,
                                                    son_table=son_table,
                                                    x_axis=x_axis,
                                                    y_axis=y_axis))

    return(query, query_emphasis)

"""
fazer o diagrama de M(V) x B-V
"""
colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

(query, query_emphasis) = sql_query('MV', 'B_V')
f.diagram(cursor, query, query_emphasis, colors, HDs, 'hipparcos/pyplot_HRdiagram/#/MV_B_V.#',
          0.5, 4.0,
          r'$B-V$', r'$M(V)$', 9,
          0.20, 0.20, 0.60, 0.60,
          'hipparcos sem DR3', xrot=0, minortickwidth=1, majortickwidth=1.3, dp=1,
          axeslabelsize=10)

"""
fazer o diagrama de M(Vt) x Bt-Vt
"""
colors = ['red', 'lime', 'deepskyblue']
HDs = ['HD 4628', 'HD 32147', 'HD 146233']

(query, query_emphasis) = sql_query('MVt', 'Bt_Vt')
f.diagram(cursor, query, query_emphasis, colors, HDs, 'hipparcos/pyplot_HRdiagram/#/MVt_Bt_Vt.#',
          0.5, 4.0,
          r'$B_t-V_t$', r'$M(V_t)$', 9,
          0.20, 0.20, 0.60, 0.60,
          'hipparcos sem DR3', xrot=0, minortickwidth=1, majortickwidth=1.3, dp=1,
          axeslabelsize=10)

# fechar o cursor
cursor.close()

# fechar a conexão
connection.close()