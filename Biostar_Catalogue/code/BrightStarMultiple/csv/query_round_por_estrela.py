import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

query = ("select "
         "(case "
         "when HD is not null then HD "
         "else BrightStarMultiple.HR "
         "end) as id, "
         "count(*) as count from BrightStarMultiple, BrightStar "
         "where BrightStar.HR = BrightStarMultiple.HR "
         "group by id")

header = ["HD", "count"]
path = "BrightStarMultiple/csv/query_round_por_estrela.xlsx"

# def xlsx(cursor, query, headers, path, sheet_name):
f.xlsx(cursor, query, header, path, "query_around_por_estrela")

cursor.close()
connection.close()