import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = "Supplement"
father_table_key_column = "ordinal_number"
son_table = "Supplement_product"
son_table_key_column = "ordinal_number"
x_axis = "B_V"
y_axis = "MV"

query_plotadas = ("select {father_table}.HD, "
                  "{father_table}.DM_Cat, "
                  "{father_table}.DM, "
                  "trim({father_table}.simbad_parallax)+0, "
                  "{father_table}.simbad_parallax_source, "
                  "trim({father_table}.V)+0, "
                  "trim({son_table}.MV)+0, "
                  "trim({son_table}.B_V)+0, "
                  "{father_table}.simbad_SpType, "
                  "{father_table}.simbad_main_identifier "
                  "from {father_table}, {son_table} "
                  "where {father_table}.{father_table_key_column} = {son_table}.{son_table_key_column} and "
                  "{son_table}.{x_axis} is not null and "
                  "{son_table}.{y_axis} is not null and "
                  "{father_table}.simbad_DR3 is null and "
                  "{father_table}.HD_Suffix is null".format(x_axis=x_axis,
                                                       y_axis=y_axis,
                                                       father_table=father_table,
                                                       father_table_key_column=father_table_key_column,
                                                       son_table=son_table,
                                                       son_table_key_column=son_table_key_column))

query_nao_plotadas = ("select {father_table}.HD, "
                      "{father_table}.DM_Cat, "
                      "{father_table}.DM, "
                      "trim({father_table}.simbad_parallax)+0, "
                      "{father_table}.simbad_parallax_source, "
                      "trim({father_table}.V)+0, "
                      "trim({son_table}.MV)+0, "
                      "trim({son_table}.B_V)+0, "
                      "{father_table}.simbad_SpType, "
                      "{father_table}.simbad_main_identifier "
                      "from {father_table}, {son_table} "
                      "where {father_table}.{father_table_key_column} = {son_table}.{son_table_key_column} and "
                      "( "
                      "{son_table}.{x_axis} is null or "
                      "{son_table}.{y_axis} is null "
                      ") and "
                      "{father_table}.simbad_DR3 is null and "
                      "{father_table}.HD_Suffix is null".format(x_axis=x_axis,
                                                           y_axis=y_axis,
                                                           father_table=father_table,
                                                           father_table_key_column=father_table_key_column,
                                                           son_table=son_table,
                                                           son_table_key_column=son_table_key_column))

header = ["HD", "DM_Cat", "DM", "simbad_parallax", "simbad_parallax_source", "V",
          "MV", "B_V", "simbad_SpType", "simbad_main_identifier"]

path = 'Supplement/csv/Supplement_estrelas_sem_HD_Suffix_e_sem_DR3.xlsx'
sheets = ["plotadas_no_diagrama_HR", "nao_plotadas_no_diagrama_HR"]
queries = [query_plotadas, query_nao_plotadas]
f.xlsx(cursor, queries, header, path, sheets)

connection.close()
cursor.close()