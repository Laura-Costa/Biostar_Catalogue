import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis):
    father_table = 'Gaia'
    son_table = 'Gaia_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "( "
             "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
             ") and "
             "{father_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "( "
                      "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                      ") and "
                      "{father_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

def sql_query_zoom(y_axis, x_axis):
    father_table = 'Gaia'
    son_table = 'Gaia_product'

    query = ("select {father_table}.simbad_HD, "
             "trim({father_table}.parallax)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.designation = {son_table}.designation and "
             "( "
             "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
             ") and "
             "{father_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "{son_table}.{y_axis} <= 9.5".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
                                                       y_axis=y_axis))

    query_emphasis = ("select {father_table}.simbad_HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.designation = {son_table}.designation and "
                      "( "
                      "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                      ") and "
                      "{father_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{son_table}.{y_axis} <= 9.5 and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return query, query_emphasis
'''
"""
fazer o diagrama de M(Rp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MRp', 'bp_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_Rp.jpg', 0.25, 1.0, r'$B_p-R_p$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'bp_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_Rp_ampliado.jpg', 0.25, 1.0, r'$B_p-R_p$', 'M(Rp)', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Rp) x G-Rp
"""
(query, query_emphasis) = sql_query('MRp', 'g_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_G_Rp.jpg', 0.25, 1.0, r'$G-R_p$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'g_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_G_Rp_ampliado.jpg', 0.25, 1.0, r'$G-R_p$', r'$M(R_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Rp) x Bp-G
"""
(query, query_emphasis) = sql_query('MRp', 'bp_g')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_G.jpg', 0.25, 1.0, r'$B_p-G$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'bp_g')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_G_ampliado.jpg', 0.25, 1.0, r'$B_p-G$', r'$M(R_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MBp', 'bp_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_Rp.jpg', 0.25, 1, r'$B_p-R_p$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'bp_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_Rp_ampliado.jpg', 0.25, 1, r'$B_p-R_p$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x G-Rp
"""
(query, query_emphasis) = sql_query('MBp', 'g_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_G_Rp.jpg', 0.25, 1, r'$G-R_p$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'g_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_G_Rp_ampliado.jpg', 0.25, 1, r'$G-R_p$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x Bp-G
"""
(query, query_emphasis) = sql_query('MBp', 'bp_g')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_G.jpg', 0.25, 1.0, r'$B_p-G$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'bp_g')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_G_ampliado.jpg', 0.25, 1, r'$B_p-G$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')
'''
"""
fazer o diagrama de M(G) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MG', 'bp_rp')
for ext in ['jpg']:
    f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/' + ext + '/MG_Bp_Rp.' + ext, 1.0, 3.0, r'$B_p-R_p$', r'$M(G)$', 10.0, 0.20, 0.20, 0.20, 0.20, 'CAT1', xrot=0, minortickwidth=1.0, majortickwidth=1.3, axeslabelsize=10)
    #f.diagram(cursor, query, query_emphasis, colors, HDs, 'CAT1/pyplot_HRdiagram/' + ext + '/LNA_MG_Bp_Rp.' + ext, 0.25, 1.0, r'$B_p-R_p$', r'$M(G)$', 0.8, 0.20, 0.20, 0.20, 0.20, 'CAT1', xrot=0, redx=9, redy=8)
'''
(query, query_emphasis) = sql_query_zoom('MG', 'bp_rp')
for ext in ['pdf', 'svg', 'jpeg', 'png', 'jpg']:
    f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/' + ext + '/MG_Bp_Rp_ampliado.' + ext, 0.25, 1.0, r'$B_p-R_p$', r'$M(G)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1', xrot=0, redx=6, redy=8)

"""
fazer o diagrama de M(G) x G-Rp
"""
(query, query_emphasis) = sql_query('MG', 'g_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_G_Rp.jpg', 0.25, 1, r'$G-R_p$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MG', 'g_rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_G_Rp_ampliado.jpg', 0.25, 1, r'$G-R_p$', r'$M(G)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(G) x Bp-G
"""
(query, query_emphasis) = sql_query('MG', 'bp_g')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_Bp_G.jpg', 0.25, 1, r'$B_p-G$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MG', 'bp_g')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_Bp_G_ampliado.jpg', 0.25, 1, r'$B_p-G$', r'$M(G)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')
'''
# fechar a conexão com o BD
connection.close()