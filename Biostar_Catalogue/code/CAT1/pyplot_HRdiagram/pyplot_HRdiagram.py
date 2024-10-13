import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['deepskyblue', 'red', 'magenta', 'lime', 'gold', 'chocolate']
HDs = ['HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis):
    father_table = 'Gaia30pc'
    son_table = 'Gaia30pc_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "( "
             "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
             ") and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({son_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "( "
                      "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                      ") and "
                      "{son_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

def sql_query_zoom(y_axis, x_axis):
    father_table = 'Gaia30pc'
    son_table = 'Gaia30pc_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "( "
             "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
             ") and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "{son_table}.{y_axis} <= 8.1".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({son_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "( "
                      "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                      ") and "
                      "{son_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{son_table}.{y_axis} <= 8.1 and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)
'''
"""
fazer o diagrama de M(Rp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MRp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MRp_Bp_Rp.png', 0.25, 1.0, r'$B_p-R_p$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MRp_Bp_Rp_ampliado.png', 0.25, 1.0, r'$B_p-R_p$', 'M(Rp)', 4.0, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Rp) x G-Rp
"""
(query, query_emphasis) = sql_query('MRp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MRp_G_Rp.png', 0.25, 1.0, r'$G-R_p$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MRp_G_Rp_ampliado.png', 0.25, 1.0, r'$G-R_p$', r'$M(R_p)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Rp) x Bp-G
"""
(query, query_emphasis) = sql_query('MRp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MRp_Bp_G.png', 0.25, 1.0, r'$B_p-G$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MRp_Bp_G_ampliado.png', 0.25, 1.0, r'$B_p-G$', r'$M(R_p)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MBp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MBp_Bp_Rp.png', 0.25, 1, r'$B_p-R_p$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MBp_Bp_Rp_ampliado.png', 0.25, 1, r'$B_p-R_p$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x G-Rp
"""
(query, query_emphasis) = sql_query('MBp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MBp_G_Rp.png', 0.25, 1, r'$G-R_p$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MBp_G_Rp_ampliado.png', 0.25, 1, r'$G-R_p$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x Bp-G
"""
(query, query_emphasis) = sql_query('MBp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MBp_Bp_G.png', 0.25, 1, r'$B_p-G$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MBp_Bp_G_ampliado.png', 0.25, 1, r'$B_p-G$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')
'''
"""
fazer o diagrama de M(G) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MG', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MG_Bp_Rp.pdf', 0.1, 0.5, r'$B_p-R_p$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 'CAT1', xrot=30)
(query, query_emphasis) = sql_query_zoom('MG', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MG_Bp_Rp_ampliado.pdf', 0.1, 0.5, r'$B_p-R_p$', r'$M(G)$', 4.0, 0.20, 0.20, 0.0, 'CAT1', xrot=0)
'''
"""
fazer o diagrama de M(G) x G-Rp
"""
(query, query_emphasis) = sql_query('MG', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MG_G_Rp.png', 0.25, 1, r'$G-R_p$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MG', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MG_G_Rp_ampliado.png', 0.25, 1, r'$G-R_p$', r'$M(G)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(G) x Bp-G
"""
(query, query_emphasis) = sql_query('MG', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MG_Bp_G.png', 0.25, 1, r'$B_p-G$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MG', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/MG_Bp_G_ampliado.png', 0.25, 1, r'$B_p-G$', r'$M(G)$', 4.0, 0.20, 0.20, 0.0, 'CAT1')
'''
# fechar a conexão com o BD
connection.close()