import mysql.connector
import code.functions.xlsx as f

father_table = 'gaia'
son_table = 'Gaia_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query_tres_estrelas_da_borda = ("select {father_table}.designation, "
                                "{father_table}.simbad_HD, "
                                "{father_table}.simbad_HIP, "
                                "trim({father_table}.parallax)+0, "
                                "trim({father_table}.parallax_error)+0, "
                                "trim({father_table}.phot_g_mean_mag)+0 as G, "
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
                                "where {father_table}.designation = {son_table}.designation and "
                                "{father_table}.parallax < 50.00 and "
                                "{father_table}.parallax + 3*{father_table}.parallax_error >= 50.00 and "
                                "{son_table}.MG <= 7.57 and "
                                "{father_table}.phot_g_mean_mag <= 9.08 "
                                "order by G asc".format(father_table=father_table, son_table=son_table))

headers = ['designation', 'simbad_HD', 'simbad_HIP',
           'parallax', 'parallax_error',
           'phot_g_mean_mag', 'phot_bp_mean_mag', 'phot_rp_mean_mag',
           'MG', 'MG_error',
           'MBp', 'MBp_error',
           'MRp', 'MRp_error',
           'bp_rp', 'g_rp', 'bp_g']
path = 'CAT1/text_files/tres_estrelas_da_borda.xlsx'
sheets = ['tres_estrelas_da_borda']
queries = [query_tres_estrelas_da_borda]
f.xlsx(cursor, queries, headers, path, sheets)

connection.close()
cursor.close()