import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query = ("select hipparcos.HIP, "
         "HD, "
         "trim(Vmag)+0, "
         "trim(VTmag)+0, "
         "trim(Hipparcos_product.B_V)+0, "
         "trim(Bt_Vt)+0, "
         "trim(Plx)+0, "
         "trim(e_Plx)+0, "
         "trim(MVt)+0, "
         "trim(MV)+0, "
         "SpType "
         "from hipparcos, Hipparcos_product "
         "where hipparcos.HIP = Hipparcos_product.HIP and "
         "simbad_DR3 is null")

header = ["HIP", "HD", "Vmag", "VTmag", "B_V", "BT_VT", "Plx", "e_Plx", "MVt", "MV", "SpType"]
path = "hipparcos/csv/estrelas_sem_DR3.xlsx"
queries = [query]

f.xlsx(cursor, queries, header, path, ["estrelas_sem_DR3"])

# fechar o cursor
cursor.close()

# fechar a conexão com o banco de dados
connection.close()