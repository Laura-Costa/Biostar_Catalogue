import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'view_CAT1'
son_table = 'gaia_product'

query = ("select {father_table}.designation as designation_order, "
         "trim({father_table}.parallax)+0, "
         "trim({father_table}.parallax_error)+0, "
         "trim({father_table}.phot_g_mean_mag)+0, "
         "trim({father_table}.phot_bp_mean_mag)+0, "
         "trim({father_table}.phot_rp_mean_mag)+0, "
         "trim({father_table}.bp_rp)+0, "
         "trim({father_table}.bp_g)+0, "
         "trim({father_table}.g_rp)+0,"
         "trim({son_table}.u)+0, "
         "trim({son_table}.v)+0, "
         "trim({son_table}.w)+0, "
         "trim({son_table}.vt_alpha)+0, "
         "trim({son_table}.vt_delta)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.source_id = {son_table}.source_id "
         "order by cast(substring(designation_order, 9) as unsigned) asc".format(father_table=father_table,
                                                                                 son_table=son_table))

header = ["designation",
          "parallax",
          "parallax_error",
          "phot_g_mean_mag", "phot_bp_mean_mag", "phot_rp_mean_mag",
          "bp_rp", "bp_g", "g_rp",
          "u", "v", "w",
          "vt_alpha", "vt_delta"]
path = "CAT1/csv/CAT1.xlsx"
queries = [query]

f.xlsx(cursor, queries, header, path, ["CAT1"])

# fechar o cursor
cursor.close()

# fechar a conexão com o banco de dados
connection.close()