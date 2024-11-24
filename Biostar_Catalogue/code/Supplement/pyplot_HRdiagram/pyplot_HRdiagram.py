import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

def sql_query(x_axis, y_axis):

    father_table = "Supplement"
    father_table_key_column = "ordinal_number"
    son_table = "Supplement_product"
    son_table_key_column = "ordinal_number"

    Supplement = ("select {father_table}.HD, "
             "trim({father_table}.simbad_parallax)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.{father_table_key_column} = {son_table}.{son_table_key_column} and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null and "
             "{father_table}.simbad_DR3 is null and "
             "( "
             "{father_table}.HD_Suffix is null or "  # estrelas com '/' no HD_Suffix são incluidas aqui porque elas não vão para SupplementMultiple
                                                     # porem, nenhuma delas eh plotada aqui, porque nao tem os dados necessarios
                                                     # a condicao poderia ser somente "HD_Suffix is null"
             "{father_table}.HD_Suffix like '%/%' "
             ") ".format(x_axis=x_axis,
                         y_axis=y_axis,
                         father_table=father_table,
                         father_table_key_column=father_table_key_column,
                         son_table=son_table,
                         son_table_key_column=son_table_key_column))

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
    return (Supplement, query_emphasis)

"""
Fazer o diagrama MV x B_V
"""
colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
hds = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

(Supplement, query_emphasis) = sql_query('B_V', 'MV')

f.diagram(cursor, Supplement, query_emphasis, colors, hds, 'Supplement/pyplot_HRdiagram/#/MV_B_V.#',
          0.50, 5.0,
          r'$B-V$', r'$M(V)$', 13,
          0.10, 0.10, 0.50, 0.50,
          'Supplement', xrot=0, minortickwidth=1.0, majortickwidth=1.3, dp=1,
          axeslabelsize=10,
          x_minor_gap=5, y_minor_gap=10)

# fechar conexão com o BD
connection.close()