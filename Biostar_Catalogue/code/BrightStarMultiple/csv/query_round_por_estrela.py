import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query = ("select "
         "(case "
         "when BrightStar.HD is not null then BrightStar.HD "
         "else BrightStar.HR "
         "end) as id, "
         "count(*) as count from BrightStarMultiple, BrightStar "
         "where BrightStar.HR = BrightStarMultiple.HR "
         "group by id "
         "order by count asc")

headers = ["HD", "count"]
path = "BrightStarMultiple/csv/query_around_por_estrela.xlsx"
queries = [query]

# def xlsx(cursor, queries, headers, path, sheets):
f.xlsx(cursor, queries, headers, path, ["query_around_por_estrela"])

cursor.close()
connection.close()