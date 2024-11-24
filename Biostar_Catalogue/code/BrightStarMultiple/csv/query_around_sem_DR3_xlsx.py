import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query_plotadas = ("select distinct BrightStarMultiple.simbad_main_identifier, "
                  "trim(BrightStarMultiple.simbad_parallax)+0, "
                  "BrightStarMultiple.simbad_parallax_source, "
                  "trim(BrightStarMultiple.simbad_V)+0, "
                  "trim(BrightStarMultiple_product.simbad_MV)+0, "
                  "trim(BrightStarMultiple_product.simbad_B_V)+0, "
                  "BrightStarMultiple.simbad_SpType "
                  "from BrightStarMultiple, BrightStarMultiple_product "
                  "where BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
                  "BrightStarMultiple.simbad_DR3 is null and "
                  "BrightStarMultiple_product.simbad_MV is not null and "
                  "BrightStarMultiple_product.simbad_B_V is not null")

query_nao_plotadas = ("select distinct BrightStarMultiple.simbad_main_identifier, "
                      "trim(BrightStarMultiple.simbad_parallax)+0, "
                      "BrightStarMultiple.simbad_parallax_source, "
                      "trim(BrightStarMultiple.simbad_V)+0, "
                      "trim(BrightStarMultiple_product.simbad_MV)+0, "
                      "trim(BrightStarMultiple_product.simbad_B_V)+0, "
                      "BrightStarMultiple.simbad_SpType "
                      "from BrightStarMultiple, BrightStarMultiple_product "
                      "where BrightStarMultiple.ordinal_number = BrightStarMultiple_product.ordinal_number and "
                      "BrightStarMultiple.simbad_DR3 is null and "
                      "(BrightStarMultiple_product.simbad_MV is null or "
                      "BrightStarMultiple_product.simbad_B_V is null)")

header = ["simbad_main_identifier", "simbad_parallax", "simbad_parallax_source",
           "simbad_V", "simbad_MV", "simbad_B_V", "simbad_SpType"]

path = 'BrightStarMultiple/csv/BrightStar_estrelas_do_query_around_sem_DR3.xlsx'
sheets = ["plotadas_no_diagrama_HR", "nao_plotadas_no_diagrama_HR"]
queries = [query_plotadas, query_nao_plotadas]
f.xlsx(cursor, queries, header, path, sheets)

connection.close()
cursor.close()