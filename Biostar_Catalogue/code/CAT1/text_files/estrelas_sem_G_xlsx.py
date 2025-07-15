import mysql.connector
import code.functions.xlsx as f

father_table = 'gaia'
son_table = 'Gaia_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query_sem_G = ("select {father_table}.designation as designation_order, "
              "trim({father_table}.parallax)+0, "
              "trim({father_table}.parallax_error)+0, "
              "trim({father_table}.phot_bp_mean_mag)+0, "
              "trim({father_table}.phot_rp_mean_mag)+0, "
              "trim({son_table}.MBp)+0, "
              "trim({son_table}.MBp_error)+0, "
              "trim({son_table}.MRp)+0, "
              "trim({son_table}.MRp_error)+0, "
              "trim({father_table}.bp_rp)+0 "
              "from {father_table}, {son_table} " 
              "where {father_table}.phot_g_mean_mag is null and "
              "{father_table}.designation = {son_table}.designation and "
              "{father_table}.parallax + 3*{father_table}.parallax_error >= 50.00 "
              "order by cast(substring(designation_order, 9) as unsigned) asc ".format(father_table=father_table, son_table=son_table))

headers = ['designation',
           'parallax', 'parallax_error',
           'phot_bp_mean_mag', 'phot_rp_mean_mag',
           'MBp', 'MBp_error',
           'MRp', 'MRp_error',
           'bp_rp']
path = 'CAT1/text_files/estrelas_sem_G.xlsx'
sheets = ['sem_G']
queries = [query_sem_G]
f.xlsx(cursor, queries, headers, path, sheets)

connection.close()
cursor.close()