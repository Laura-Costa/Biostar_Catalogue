import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

x_axis = "B_V"
y_axis = "MV"

query_plotadas = ("select SupplementMultiple.simbad_main_identifier, "
                  "trim(SupplementMultiple.simbad_parallax)+0, "
                  "SupplementMultiple.simbad_parallax_source, "
                  "trim(SupplementMultiple.simbad_V)+0, "
                  "trim(SupplementMultiple_product.simbad_{x_axis})+0, "
                  "trim(SupplementMultiple_product.simbad_{y_axis})+0, "
                  "SupplementMultiple.simbad_SpType "
                  "from Supplement, SupplementMultiple, SupplementMultiple_product "
                  "where Supplement.ordinal_number = SupplementMultiple.ordinal_number_Supplement and "
                  "SupplementMultiple.ordinal_number = SupplementMultiple_product.ordinal_number and "
                  "SupplementMultiple_product.simbad_{x_axis} is not null and "
                  "SupplementMultiple_product.simbad_{y_axis} is not null and "
                  "SupplementMultiple.simbad_DR3 is null and "
                  "Supplement.HD_Suffix not like '%/%'".format(x_axis=x_axis, y_axis=y_axis))
                  # nenhuma estrela proveniente de uma estrela com / no HD_Suffix do Supplement
                  # tem os requisitos necessarios para ser plotada
                  # de modo que a restricao que exige que o HD_Suffix nao tenha /
                  # (ou seja, so tenha letras) poderia ser retirada

query_nao_plotadas = ("select SupplementMultiple.simbad_main_identifier, "
                      "trim(SupplementMultiple.simbad_parallax)+0, "
                      "SupplementMultiple.simbad_parallax_source, "
                      "trim(SupplementMultiple.simbad_V)+0, "
                      "trim(SupplementMultiple_product.simbad_{x_axis})+0, "
                      "trim(SupplementMultiple_product.simbad_{y_axis})+0, "
                      "SupplementMultiple.simbad_SpType "
                      "from Supplement, SupplementMultiple, SupplementMultiple_product "
                      "where Supplement.ordinal_number = SupplementMultiple.ordinal_number_Supplement and "
                      "SupplementMultiple.ordinal_number = SupplementMultiple_product.ordinal_number and "
                      "( "
                      "SupplementMultiple_product.simbad_{x_axis} is null or "
                      "SupplementMultiple_product.simbad_{y_axis} is null "
                      ") and "
                      "SupplementMultiple.simbad_DR3 is null and "
                      "Supplement.HD_Suffix not like '%/%'".format(x_axis=x_axis, y_axis=y_axis))

header = ["simbad_main_identifier", "simbad_parallax", "simbad_parallax_source",
          "simbad_V", "simbad_B_V", "simbad_MV", "simbad_SpType"]

path = 'SupplementMultiple/csv/Supplement_estrelas_do_query_around_sem_DR3.xlsx'
sheets = ["plotadas_no_diagrama_HR", "nao_plotadas_no_diagrama_HR"]
queries = [query_plotadas, query_nao_plotadas]
f.xlsx(cursor, queries, header, path, sheets)

connection.close()
cursor.close()