import mysql.connector
import code.functions.pyplot_HRdiagram as f1

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = "view_CAT1"
father_key_column = "source_id"
son_table = 'gaia_product'
son_key_column = "source_id"

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

# Criar o diagrama u_v_w.jpg
query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax)+0, "
         "trim({son_table}.u)+0, "
         "trim({son_table}.v)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.{father_key_column} = {son_table}.{son_key_column} and "
         "{son_table}.u is not null and "
         "{son_table}.v is not null and "
         "abs({son_table}.u) < 300 and "
         "abs({son_table}.v) < 300".format(father_table=father_table,
                                            father_key_column=father_key_column,
                                            son_table=son_table,
                                            son_key_column=son_key_column))

f1.diagram(cursor, query, "", colors, [],
        'CAT1/pyplot_scatterplot/#/u_v.#',
        50.0, 50.0,
        r'$U \; \left[\frac{km}{s}\right]$', r'$V \; \left[\frac{km}{s}\right]$', 10.0,
        25.0, 25.0, 25.0, 25.0,
        'CAT1', xrot=0, minortickwidth=1.0, majortickwidth=1.3,
        axeslabelsize=10,
        x_minor_gap=10, y_minor_gap=5, color='black')

cursor.close()
connection.close()