import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis):
    father_table = 'view_CAT1'
    son_table = 'Gaia_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "{father_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "Bp_Rp <= 1.500 and "
             "MG <= 9.000".format(father_table=father_table,
                                                    son_table=son_table,
                                                    x_axis=x_axis,
                                                    y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "{father_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "Bp_Rp <= 1.500 and "
                      "MG <= 9.00 and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)
"""
fazer o diagrama de M(G) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MG', 'bp_rp')

f.diagram(cursor, query, query_emphasis, colors, HDs, 'CAT1/pyplot_HRdiagram/#/LNA2_MG_Bp_Rp.#',
          0.25, 1.0,
          r'$B_p-R_p$', r'$M(G)$', 8,
          0.03, 0.01, 0.20, 0.87,
          'CAT1', xrot=0, redx=5, redy=7, minortickwidth=1.0, majortickwidth=1.3, dp=2,
          axeslabelsize=10, lgnd_loc='lower left')

# fechar a conexão com o BD
connection.close()