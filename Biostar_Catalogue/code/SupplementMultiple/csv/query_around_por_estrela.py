import mysql.connector
import code.functions.xlsx as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

# colocamos distinct aqui porque o Supplement têm HDs repetidos
# Exemplo: HD 46136 parace duas vezes no Supplement.
# +----------+-----------+------------------------+
# | HD       | HD_Suffix | simbad_main_identifier |
# +----------+-----------+------------------------+
# | HD 46136 | A         | * 20 Gem               |
# | HD 46136 | A         | * 20 Gem B             |
# | HD 46136 | A         | UCAC2 38045744         |
# | HD 46136 | A         | ATO J098.1100+17.7925  |
# | HD 46136 | B         | * 20 Gem               |
# | HD 46136 | B         | * 20 Gem B             |
# | HD 46136 | B         | UCAC2 38045744         |
# | HD 46136 | B         | ATO J098.1100+17.7925  |
# +----------+-----------+------------------------+
# Nessa situação, a consulta retorna corretamente que a estrela HD 46136
# têm 4 registros resultantes do query around. Sem a subconsulta com distinct,
# o valor retornado seria 8.
query = ("select "
         "Supplement.HD as current_HD, "
         "( "
         "select count(distinct SupplementMultiple.simbad_main_identifier) "
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
path = "SupplementMultiple/csv/query_around_por_estrela.xlsx"
queries = [query]

# def xlsx(cursor, query, header, path, sheets):
f.xlsx(cursor, queries, header, path, ["query_around_por_estrela"])

cursor.close()
connection.close()