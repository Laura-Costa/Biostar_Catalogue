import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'BrightStar'
son_table = 'BrightStar_product'

query_plotadas = ("select {father_table}.HR, "
                  "{father_table}.HD, "
                  "trim({father_table}.simbad_parallax)+0, "
                  "{father_table}.simbad_parallax_source, "
                  "trim({father_table}.V)+0, "
                  "trim({son_table}.MV)+0, "
                  "trim({father_table}.B_V)+0, "
                  "{father_table}.Name, "
                  "{father_table}.simbad_SpType, "
                  "{father_table}.simbad_main_identifier "
                  "from {father_table}, {son_table} "
                  "where {father_table}.HR = {son_table}.HR and "
                  "{father_table}.ADS_Comp is null and  "
                  "{father_table}.simbad_DR3 is null and "
                  "{son_table}.MV is not null and "
                  "{son_table}.B_V is not null".format(father_table=father_table, son_table=son_table))

query_nao_plotadas = ("select {father_table}.HR, "
                      "{father_table}.HD, "
                      "trim({father_table}.simbad_parallax)+0, "
                      "{father_table}.simbad_parallax_source, "
                      "trim({father_table}.V)+0, "
                      "trim({son_table}.MV)+0, "
                      "trim({father_table}.B_V)+0, "
                      "{father_table}.Name, "
                      "{father_table}.simbad_SpType, "
                      "{father_table}.simbad_main_identifier "
                      "from {father_table}, {son_table} "
                      "where {father_table}.HR = {son_table}.HR and "
                      "{father_table}.ADS_Comp is null and  "
                      "{father_table}.simbad_DR3 is null and "
                      "({son_table}.MV is null or "
                      "{son_table}.B_V is null)".format(father_table=father_table, son_table=son_table))

header = ["HR", "HD", "simbad_parallax", "simbad_parallax_source", "V",
          "MV", "B_V", "Name", "simbad_SpType", "simbad_main_identifier"]

path = 'BrightStar/csv/BrightStar_estrelas_sem_ADS_Comp_e_sem_DR3.xlsx'
sheets = ["plotadas_no_diagrama_HR", "nao_plotadas_no_diagrama_HR"]
queries = [query_plotadas, query_nao_plotadas]
f.xlsx(cursor, queries, header, path, sheets)

connection.close()
cursor.close()