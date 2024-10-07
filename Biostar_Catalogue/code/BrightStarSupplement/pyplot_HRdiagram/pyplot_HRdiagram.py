import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(x_axis, y_axis):

    father_table = 'BrightStarSupplement'
    father_key_column = 'id'
    son_table = 'BrightStarSupplement_product'
    son_key_column = 'id'

    query = ("select {father_table}.HD, "
             "trim({father_table}.simbad_parallax)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.{father_key_column} = {son_table}.{son_key_column} and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "{father_table}.simbad_DR3 is null and "
             "( "
             "length(trim({father_table}.HD_Suffix)) <=1 or "
             "{father_table}.HD_Suffix is null "
             ")".format(father_table=father_table,
                        father_key_column=father_key_column,
                        son_table=son_table,
                        son_key_column=son_key_column,
                        x_axis=x_axis,
                        y_axis=y_axis))

    father_table = 'BrightStar'
    father_key_column = 'HR'
    son_table = 'BrightStar_product'
    son_key_column = 'HR'

    query_emphasis = ("select {father_table}.HD, "
                      "trim({son_table}.{x_axis})+0, "
                      "trim({son_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.{father_key_column} = {son_table}.{son_key_column} and "
                      "{son_table}.{x_axis} is not null and "
                      "{son_table}.{y_axis} is not null and "
                      "{father_table}.HD = ".format(father_table=father_table,
                                                    father_key_column=father_key_column,
                                                    son_table=son_table,
                                                    son_key_column=son_key_column,
                                                    x_axis=x_axis,
                                                    y_axis=y_axis))
    return (query, query_emphasis)

"""
Fazer o diagrama MV x B_V
"""
colors = ['deepskyblue', 'red', 'magenta', 'lime', 'gold', 'chocolate']
HDs = ['HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134']

(query, query_emphasis) = sql_query('B_V', 'MV')
f.diagram(cursor, query, query_emphasis, colors, HDs, '/BrightStarSupplement/pyplot_HRdiagram/MV_B_V.svg', 0.0625, 1.0, r'B-V', r'M(V)', 6.0, 0.20, 2.0, 2.0, r'Objetos do Bright Star Supplement sem designação Gaia DR3 no Simbad')

"""
Fazer o diagrama simbad_MV x simbad_B_V 
"""
colors = ['deepskyblue', 'red', 'lime', 'gold', 'chocolate']
HDs = ['HD 146233', 'HD 4628', 'HD 32147', 'HD 191408', 'HD 219134']

(query, query_emphasis) = sql_query('simbad_B_V', 'simbad_MV')
f.diagram(cursor, query, query_emphasis, colors, HDs, '/BrightStarSupplement/pyplot_HRdiagram/simbad_MV_simbad_B_V.svg', 0.125, 1.0, r'B-V (simbad)', r'M(V) (simbad)' , 6.0, 0.20, 2.0, 2.0, 'Objetos do Bright Star Supplement sem designação Gaia DR3 no Simbad')

# fechar conexão com o BD
connection.close()