import mysql.connector
import code.functions.pyplot_scatterplot as f1
import code.functions.pyplot_HRdiagram as f2

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = "view_CAT1"

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

# Criar o diagrama erro_da_paralaxe_contra_paralaxe2.jpg com escala de números pequenos nos eixos x e y usando a função scatterplot
query = ("select {father_table}.simbad_HD, "
         "trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax_error)+0 "
         "from {father_table} "
         "where {father_table}.parallax >= 50.00 or "
         "("
         "{father_table}.parallax < 50.00 "
         "and "
         "({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00)"
         ")".format(father_table=father_table))

query_emphasis = ("select {father_table}.simbad_HD, "
                  "trim({father_table}.parallax)+0, "
                  "trim({father_table}.parallax_error)+0 "
                  "from {father_table} "
                  "where {father_table}.parallax is not null and "
                  "{father_table}.parallax_error is not null and "
                  "{father_table}.simbad_HD = ".format(father_table=father_table))

f1.scatterplot(cursor, query, query_emphasis, colors, HDs,
               0.05, 0.05, 8.0, 8.0,
               "paralaxe em milissegundos de arco", "erro da paralaxe em milissegundos de arco",
               50, 60,
               '/jpg/erro_da_paralaxe_contra_paralaxe1.jpg', "CAT1: σ(π) x π")

f2.diagram(cursor, query, query_emphasis, colors, HDs,
        'CAT1/pyplot_scatterplot/#/erro_da_paralaxe_contra_paralaxe2.#',
        100.0, 0.5,
        'paralaxe em milissegundos de arco', 'erro da paralaxe em milissegundos de arco', 8.0,
        25.0, 25.0, 0.20, 0.10,
        'CAT1', xrot=0, minortickwidth=1.0, majortickwidth=1.3, dp=1,
        axeslabelsize=10,
        x_minor_gap=10, y_minor_gap=5)


# fazer o diagrama erro_da_paralaxe_contra_paralaxe_log1.jpg com escala de números pequenos nos eixos x e y
# usando a função scatterplot
f1.scatterplot(cursor, query, query_emphasis, colors, HDs,
               0.001, 0.5, 0.001, 15.0,
               'paralaxe em milissegundos de arco (escala logarítmica)',
               'erro da paralaxe em milissegundos de arco (escala logarítmica)',
               50, 60,
               '/jpg/erro_da_paralaxe_contra_paralaxe_log1.jpg', "CAT1: σ(π) x π",
               xrot=30, xlog=True, ylog=True)

# fazer o diagrama erro_da_paralaxe_contra_paralaxe_log1.jpg com escala de números grandes nos eixos x e y
# usando a função scatterplot
f1.scatterplot(cursor, query, query_emphasis, colors, HDs,
               0.001, 0.5, 0.001, 15.0,
               'paralaxe em milissegundos de arco (escala logarítmica)',
               'erro da paralaxe em milissegundos de arco (escala logarítmica)',
               6, 6,
               '/jpg/erro_da_paralaxe_contra_paralaxe_log2.jpg', "CAT1: σ(π) x π",
               0, True, True,
               labelsize=10,
               y_dp=2,
               x_dp=1,
               fontsize=8)



cursor.close()
connection.close()
