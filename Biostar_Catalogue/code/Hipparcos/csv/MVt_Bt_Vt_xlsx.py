import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'hipparcos'
son_table = 'Hipparcos_product'

query_plotadas = ("select {father_table}.HIP as HIP_order, "
                  "{father_table}.HD, "
                  "trim({father_table}.Vmag)+0, "
                  "trim({father_table}.VTmag)+0, "
                  "trim({son_table}.B_V)+0, "
                  "trim({son_table}.Bt_Vt)+0, "
                  "trim({father_table}.Plx)+0, "
                  "trim({father_table}.e_Plx)+0, "
                  "trim({son_table}.MVt)+0, "
                  "trim({son_table}.MV)+0, "
                  "{father_table}.SpType "
                  "from {father_table}, {son_table} "
                  "where {father_table}.HIP = {son_table}.HIP and "
                  "{father_table}.simbad_DR3 is null and "
                  "{father_table}.Plx is not null and "
                  "{father_table}.Plx > 0.00000 and "
                  "{father_table}.BTmag is not null and "
                  "{father_table}.VTmag is not null "
                  "order by cast(substring(HIP_order,4) as unsigned) asc".format(father_table=father_table, son_table=son_table))

query_nao_plotadas = ("select {father_table}.HIP as HIP_order, "
                  "{father_table}.HD, "
                  "trim({father_table}.Vmag)+0, "
                  "trim({father_table}.VTmag)+0, "
                  "trim({son_table}.B_V)+0, "
                  "trim({son_table}.Bt_Vt)+0, "
                  "trim({father_table}.Plx)+0, "
                  "trim({father_table}.e_Plx)+0, "
                  "trim({son_table}.MVt)+0, "
                  "trim({son_table}.MV)+0, "
                  "{father_table}.SpType "
                  "from {father_table}, {son_table} "
                  "where {father_table}.HIP = {son_table}.HIP and "
                  "{father_table}.simbad_DR3 is null and "
                  "( "
                  "{father_table}.Plx is null or "
                  "{father_table}.Plx <= 0.00000 or "
                  "{father_table}.BTmag is null or "
                  "{father_table}.VTmag is null "
                  ") "
                  "order by cast(substring(HIP_order,4) as unsigned) asc".format(father_table=father_table, son_table=son_table))

header = ["HIP", "HD", "Vmag", "VTmag", "B_V", "BT_VT", "Plx", "e_Plx", "MVt", "MV", "SpType"]
path = "hipparcos/csv/MVt_Bt_Vt.xlsx"
queries = [query_plotadas, query_nao_plotadas]

f.xlsx(cursor, queries, header, path, ["plotadas", "nao_plotadas"])

# fechar o cursor
cursor.close()

# fechar a conexão com o banco de dados
connection.close()