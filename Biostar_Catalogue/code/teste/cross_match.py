import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/txt_cross_match.txt") as file:
    cont = 0
    stringHIP = "("
    for line in file:
        cont += 1
        if cont != 100010:
            stringHIP += "'HIP {}', ".format(line.rstrip())
        else:
            stringHIP += "'HIP {}')".format(line.rstrip())

print(stringHIP)

cursor.execute("""select Hipparcos.HIP """
               """from Hipparcos """
               """where Hipparcos.simbad_DR3 is null and """
               """Hipparcos.HIP not in {stringHIP}""".format(stringHIP=stringHIP))

value = cursor.fetchall()
HIP_list = []

for (HIP_value) in value:
    HIP_list.append(HIP_value)

print("QTDE: ", len(HIP_list))
print()
print(HIP_list)

def sql_query(y_axis, x_axis):
    father_table = 'Hipparcos'
    son_table = 'Hipparcos_product'

    query = ("select {father_table}.HD, "
             "trim({father_table}.Plx)+0, "
             "trim({son_table}.{x_axis})+0, "
             "trim({son_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.HIP = {son_table}.HIP and "
             "{father_table}.simbad_DR3 is null and "
             "Hipparcos.HIP not in {stringHIP} and "
             "{son_table}.{x_axis} is not null and "
             "{son_table}.{y_axis} is not null".format(father_table=father_table,
                                                       son_table=son_table,
                                                       x_axis=x_axis,
                                                       y_axis=y_axis,
                                                       stringHIP=stringHIP))

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
f.diagram(cursor, query, query_emphasis, colors, HDs, 'Hipparcos/pyplot_HRdiagram/#/CROSS_MATCH_MV_B_V.#',
          0.5, 4.0,
          r'$B-V$', r'$M(V)$', 9,
          0.20, 0.20, 0.60, 0.60,
          'Hipparcos sem DR3', xrot=0, minortickwidth=1, majortickwidth=1.3,
          axeslabelsize=10, lgnd_loc='lower left',
          y_minor_gap=10)

# fechar o cursor
cursor.close()

# fechar a conexão com o BD
connection.close()