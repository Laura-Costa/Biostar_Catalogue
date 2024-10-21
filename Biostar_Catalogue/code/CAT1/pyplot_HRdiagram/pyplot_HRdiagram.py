import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis):
    father_table = 'CAT1'
    son_table = 'CAT1_product'

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
    father_table = 'CAT1'
    son_table = 'CAT1_product'

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
             "{son_table}.{y_axis} <= 9.5".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
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
                      "{son_table}.{y_axis} <= 9.5 and "
                      "{father_table}.simbad_HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return (query, query_emphasis)

"""
fazer o diagrama de M(Rp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MRp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_Rp.jpg', 0.25, 1.0, r'$B_p-R_p$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_Rp_ampliado.jpg', 0.25, 1.0, r'$B_p-R_p$', 'M(Rp)', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Rp) x G-Rp
"""
(query, query_emphasis) = sql_query('MRp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_G_Rp.jpg', 0.25, 1.0, r'$G-R_p$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_G_Rp_ampliado.jpg', 0.25, 1.0, r'$G-R_p$', r'$M(R_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Rp) x Bp-G
"""
(query, query_emphasis) = sql_query('MRp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_G.jpg', 0.25, 1.0, r'$B_p-G$', r'$M(R_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MRp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MRp_Bp_G_ampliado.jpg', 0.25, 1.0, r'$B_p-G$', r'$M(R_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MBp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_Rp.jpg', 0.25, 1, r'$B_p-R_p$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'Bp_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_Rp_ampliado.jpg', 0.25, 1, r'$B_p-R_p$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x G-Rp
"""
(query, query_emphasis) = sql_query('MBp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_G_Rp.jpg', 0.25, 1, r'$G-R_p$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_G_Rp_ampliado.jpg', 0.25, 1, r'$G-R_p$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(Bp) x Bp-G
"""
(query, query_emphasis) = sql_query('MBp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_G.jpg', 0.25, 1.0, r'$B_p-G$', r'$M(B_p)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MBp', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MBp_Bp_G_ampliado.jpg', 0.25, 1, r'$B_p-G$', r'$M(B_p)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(G) x Bp-Rp
"""
(query, query_emphasis) = sql_query('MG', 'Bp_Rp')
for ext in ['jpg']:
    f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/' + ext + '/MG_Bp_Rp.' + ext, 0.25, 1.0, r'$B_p-R_p$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1', xrot=0, redx=9, redy=8)
    f.diagram(cursor, query, query_emphasis, colors, HDs, 'CAT1/pyplot_HRdiagram/' + ext + '/LNA_MG_Bp_Rp.' + ext, 0.25, 1.0, r'$B_p-R_p$', r'$M(G)$', 0.8, 0.20, 0.20, 0.20, 0.20, 'CAT1', xrot=0, redx=9, redy=8)

(query, query_emphasis) = sql_query_zoom('MG', 'Bp_Rp')
for ext in ['pdf', 'svg', 'jpeg', 'png', 'jpg']:
    f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/' + ext + '/MG_Bp_Rp_ampliado.' + ext, 0.25, 1.0, r'$B_p-R_p$', r'$M(G)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1', xrot=0, redx=6, redy=8)

"""
fazer o diagrama de M(G) x G-Rp
"""
(query, query_emphasis) = sql_query('MG', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_G_Rp.jpg', 0.25, 1, r'$G-R_p$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MG', 'G_Rp')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_G_Rp_ampliado.jpg', 0.25, 1, r'$G-R_p$', r'$M(G)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

"""
fazer o diagrama de M(G) x Bp-G
"""
(query, query_emphasis) = sql_query('MG', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_Bp_G.jpg', 0.25, 1, r'$B_p-G$', r'$M(G)$', 0.5, 0.20, 0.20, 0.20, 0.20, 'CAT1')
(query, query_emphasis) = sql_query_zoom('MG', 'Bp_G')
f.diagram(cursor, query, query_emphasis, colors, HDs,'CAT1/pyplot_HRdiagram/jpg/MG_Bp_G_ampliado.jpg', 0.25, 1, r'$B_p-G$', r'$M(G)$', 4.0, 0.20, 0.20, 0.20, 0.0, 'CAT1')

# fechar a conexão com o BD
connection.close()