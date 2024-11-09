import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

# colocamos distinct aqui porque o Supplement têm HDs repetidos
query = ("select "
         "Supplement.HD as current_HD, "
         "( "
         "select count(distinct SupplementMultiple.simbad_main_identifier)-1 "
         "from SupplementMultiple, Supplement "
         "where Supplement.ordinal_number = SupplementMultiple.ordinal_number_Supplement and "
         "Supplement.HD = current_HD "
         ") as count "
         "from Supplement "
         "where "
         "Supplement.HD_Suffix is not null and "
         "Supplement.HD_Suffix not like '%/%' "
         "group by HD "
         "order by count asc")

header = ["HD", "count"]
path = "SupplementMultiple/csv/query_round_por_estrela.xlsx"
queries = [query]

# def xlsx(cursor, query, header, path, sheets):
f.xlsx(cursor, queries, header, path, ["query_around_por_estrela"])

cursor.close()
connection.close()