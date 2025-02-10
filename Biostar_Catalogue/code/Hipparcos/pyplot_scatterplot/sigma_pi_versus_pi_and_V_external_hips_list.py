import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

stringHIP = "("

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/stars_in_hip_main_dat_with_Dr3_at_Simbad.txt") as file:
    cont = 0
    for line in file:
        cont += 1
        if cont != 114072:
            stringHIP += "'HIP {}', ".format(line.rstrip())
        else:
            stringHIP += "'HIP {}')".format(line.rstrip())

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis):
    father_table = 'Hipparcos'
    son_table = 'Hipparcos_product'

    query = ("select {father_table}.HD, "
             "trim({father_table}.Plx)+0, "
             "trim({father_table}.{x_axis})+0, "
             "trim({father_table}.{y_axis})+0 "
             "from {father_table}, {son_table} "
             "where {father_table}.Plx > 0 and "
             "{father_table}.HIP not in {stringHIP} and "
             "{father_table}.HIP = {son_table}.HIP and "
             "{father_table}.{x_axis} is not null and "
             "{father_table}.{y_axis} is not null".format(father_table=father_table, son_table=son_table, x_axis=x_axis,
                                                       y_axis=y_axis, stringHIP=stringHIP))

    query_emphasis = ("select {father_table}.HD, "
                      "trim({father_table}.{x_axis})+0, "
                      "trim({father_table}.{y_axis})+0 "
                      "from {father_table}, {son_table} "
                      "where {father_table}.Plx > 0 and "
                      "{father_table}.HIP = {son_table}.HIP and "
                      "{father_table}.{x_axis} is not null and "
                      "{father_table}.{y_axis} is not null and "
                      "{father_table}.HD = ".format(father_table=father_table, son_table=son_table,
                                                           x_axis=x_axis, y_axis=y_axis))
    return query, query_emphasis

"""
fazer o diagrama de sigma pi x pi
"""
(query, query_emphasis) = sql_query('e_Plx', 'Plx')
f.diagram(cursor, query, query_emphasis, colors, HDs, 'Hipparcos/pyplot_scatterplot/#/sigma_pi_versus_pi_2.#',
          100.0, 10.0,
          r'$\pi \; [mas]$', r'$\sigma_{\pi} \; [mas]$',
          8.0,
          10.0, 10.0,
          2.0, 2.0,
          'Estrelas HIP sem número DR3 no Simbad',
          xrot=0, minortickwidth=0.5, majortickwidth=1.0,
          axeslabelsize=10,
          x_minor_gap=10, y_minor_gap=10)

"""
fazer o diagrama de sigma pi x V
"""
(query, query_emphasis) = sql_query('e_Plx', 'Vmag')
f.diagram(cursor, query, query_emphasis, colors, HDs, 'Hipparcos/pyplot_scatterplot/#/sigma_pi_versus_V_2.#',
          1.0, 10.0,
          r'$V \; [mag]$', r'$\sigma_{\pi} \; [mas]$',
          8.0,
          0.5, 0.5,
          2.0, 2.0,
          'Estrelas HIP sem número DR3 no Simbad',
          xrot=0, minortickwidth=0.5, majortickwidth=1.0,
          axeslabelsize=10,
          x_minor_gap=10, y_minor_gap=10,
          lgnd_loc="upper left")

# fechar a conexão com o BD
connection.close()