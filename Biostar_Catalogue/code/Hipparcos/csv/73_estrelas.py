import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

path = '/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/73_estrelas.txt'
_73_stars = "("

with open(path) as file:

    print('file opened successfully')
    cont = 0
    nrows = sum( 1 for line in file if '--' not in line and 'HIP' not in line)

    # reset to the beginning of the file
    file.seek(0)

    for line in file:

      if '--' in line or 'HIP' in line:
        continue

      cont += 1
      if cont != nrows:
          _73_stars += "{}, ".format(line.rstrip())
      else:
          _73_stars += "{})".format(line.rstrip())
    file.close()

print(_73_stars)

father_table = "public_hipparcos"
son_table = "public_hipparcos_product"

query = ("select {father_table}.hip, "
         "{father_table}.hd, "
         "{father_table}.bd, "
         "{father_table}.cod, "
         "{father_table}.cpd, "
         "trim({father_table}.vmag)+0, "
         "trim({father_table}.vtmag)+0, "
         "trim({father_table}.e_vtmag)+0, "
         "trim({father_table}.btmag)+0, "
         "trim({father_table}.e_btmag)+0, "
         "trim({father_table}.ra)+0, "
         "trim({father_table}.de)+0, "
         "{father_table}.sptype, "
         "trim({father_table}.plx)+0, "
         "trim({father_table}.e_plx)+0, "
         "trim({son_table}.mv)+0, "
         "trim({son_table}.e_mv)+0, "
         "trim({son_table}.mvt)+0, "
         "trim({son_table}.e_mvt)+0, "
         "trim({son_table}.b_v)+0, "
         "trim({father_table}.e_b_v)+0, "
         "trim({son_table}.bt_vt)+0 "
         "from {father_table}, {son_table} "                                                                                                                                                                                                                                                           
         "where {father_table}.hip = {son_table}.hip and "
         "{father_table}.hip in {_73_stars}".format(father_table=father_table, son_table=son_table, _73_stars=_73_stars))

header = ["hip", "hd", "bd", "cod", "cpd", "vmag", "vtmag", "e_vtmag", "btmag", "e_btmag", "ra", "de",
          "sptype", "plx", "e_plx", "mv", "e_mv", "mvt", "e_mvt", "b_v", "e_b_v", "bt_vt"]

path = "hipparcos/csv/73_estrelas.xlsx"
queries = [query]

f.xlsx(cursor, queries, header, path, ["73_estrelas"])

# fechar o cursor
cursor.close()

# fechar a conexão com o banco de dados
connection.close()