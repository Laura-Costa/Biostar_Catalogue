import mysql.connector
import code.functions.xlsx as f

father_table = 'Gaia'
son_table = 'Gaia_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query_sem_G = ("select {father_table}.designation, "
              "{father_table}.simbad_HD, "
              "trim({father_table}.phot_g_mean_mag)+0, "
              "trim({father_table}.phot_bp_mean_mag)+0, "
              "trim({father_table}.phot_rp_mean_mag)+0, "
              "trim({son_table}.MG)+0, "
              "trim({son_table}.MG_error)+0, "
              "trim({son_table}.MBp)+0, "
              "trim({son_table}.MBp_error)+0, "
              "trim({son_table}.MRp)+0, "
              "trim({son_table}.MRp_error)+0, "
              "trim({father_table}.bp_rp)+0, "
              "trim({father_table}.g_rp)+0, "
              "trim({father_table}.bp_g)+0 "
              "from {father_table}, {son_table} " 
              "where phot_g_mean_mag is null and "
              "{father_table}.designation = {son_table}.designation".format(father_table=father_table, son_table=son_table))

query_sem_bp_rp = ("select {father_table}.designation, "
                   "{father_table}.simbad_HD, "
                   "trim({father_table}.phot_g_mean_mag)+0, "
                   "trim({father_table}.phot_bp_mean_mag)+0, "
                   "trim({father_table}.phot_rp_mean_mag)+0, "
                   "trim({son_table}.MG)+0, "
                   "trim({son_table}.MG_error)+0, "
                   "trim({son_table}.MBp)+0, "
                   "trim({son_table}.MBp_error)+0, "
                   "trim({son_table}.MRp)+0, "
                   "trim({son_table}.MRp_error)+0, "
                   "trim({father_table}.bp_rp)+0, "
                   "trim({father_table}.g_rp)+0, "
                   "trim({father_table}.bp_g)+0 "
                   "from {father_table}, {son_table} " 
                   "where {father_table}.bp_rp is null and "
                   "{father_table}.designation = {son_table}.designation".format(father_table=father_table, son_table=son_table))

headers = ['designation', 'simbad_HD',
           'phot_g_mean_mag', 'phot_bp_mean_mag', 'phot_rp_mean_mag',
           'MG', 'MG_error',
           'MBp', 'MBp_error',
           'MRp', 'MRp_error',
           'bp_rp', 'g_rp', 'bp_g']
path = 'CAT1/csv/CAT1_estrelas_sem_G_e_estrelas_sem_Bp_Rp.xlsx'
sheets = ['sem_G', 'sem_Bp_Rp']
queries = [query_sem_G, query_sem_bp_rp]
f.xlsx(cursor, queries, headers, path, sheets)

connection.close()
cursor.close()