import code.functions.pyplot_histogram as f
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Gaia30pc'

"""
Histograma de pi
para as estrelas do núcleo mais borda
paralaxe >= 50 ou (paralaxe < 50 e paralax + 3*erro >= 50) 
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.parallax >= 50.00 "
         "or "
         "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00) "
         ")".format(father_table=father_table))

f.histogram(query, cursor, 'paralaxe', 4, '/CAT1/pyplot_histogram/CAT1_parallax.svg', yfontsize=5, xfontsize=0.5,  log=True)

"""
Histograma de sigma(pi)
para as estrelas da borda
paralaxe < 50 e (paralaxe + 3*erro) >= 50
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax_error)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.parallax >= 50.00 "
         "or "
         "({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00) "
         ")".format(father_table=father_table))

f.histogram(query, cursor, r"$σ_π$(CAT1)", np.arange(0.0, 4.57095, 0.15), '/CAT1/pyplot_histogram/CAT1_parallax_error_log.svg', yfontsize=5, xfontsize=5,  rot=30, log=True, yticks_equally_spaced=True)
f.histogram(query, cursor, r"$σ_π$(CAT1)", np.arange(0.0, 4.57095, 0.15), '/CAT1/pyplot_histogram/CAT1_parallax_error_lin.svg', yfontsize=5, xfontsize=5, rot=30, yticks_equally_spaced=True, xticks_not_edges=False)


"""
Histograma de sigma(pi)
para estrelas da borda
parallax < 50.00 e (parallax + 3*parallax_error) >= 50.00
130 estrelas
"""
query = ("select trim({father_table}.parallax_error)+0 "
         "from {father_table} "
         "where "
         "( "
         "{father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00"
         ")".format(father_table=father_table))

cursor.execute(query)
value = cursor.fetchall()

parallax_error = []
for my_tuple in value:
    parallax_error.append(my_tuple[0])

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

fig.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
for i, bins in enumerate([10, 80]):
    ax[i].hist(parallax_error, bins=bins, histtype='stepfilled', alpha=0.2, density=True)
    ax[i].set_xlabel('parallax_error')
    ax[i].set_ylabel('frequency')
    ax[i].set_title(f'plt.hist(parallax_error, bins={bins})', fontdict=dict(family='monospace'))

plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/pyplot_histogram/sigma_pi_borda.svg')
plt.close()


