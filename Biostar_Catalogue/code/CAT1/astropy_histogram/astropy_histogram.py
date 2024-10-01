from astropy.visualization import hist
import matplotlib.pyplot as plt
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Gaia30pc'

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

fig, ax = plt.subplots(2, 2, figsize=(10, 10))
fig.subplots_adjust(left=0.1, right=0.95, bottom=0.15)

rules = ['scott', 'freedman', 'knuth', 'blocks']
cont = 0
for row in [0, 1]:
    for col in [0, 1]:
        hist(parallax_error, bins=rules[cont], ax=ax[row][col], histtype='stepfilled', alpha=0.2, density=True)
        ax[row][col].set_xlabel('parallax_error')
        ax[row][col].set_ylabel('frequency')
        ax[row][col].set_title(f'hist(t, bins="{rules[cont]}")', fontdict=dict(family='monospace'))
        cont += 1

plt.savefig('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/CAT1/astropy_histogram/sigma_pi_borda.svg')
plt.close()