import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("""select BrightStar.HD as HD, """
               """count(*) as count from BrightStarMultiple, BrightStar """
               """where BrightStar.HR = BrightStarMultiple.HR """
               """group by HD """
               """order by cast(substring(HD,3) as unsigned) asc""")

value = cursor.fetchall()
HD_list = []
count_list = []

for (HD_value, count_value) in value:
    HD_list.append(HD_value)
    count_list.append(count_value)

cont = 0
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/BrightStarMultiple/csv/query_around_por_estrela.txt", "w") as text_file:
    header = ["HD", "count"]
    text_file.write("{0[0]:<7}{0[1]:<0}\n".format(header))
    for (HD, count) in zip(HD_list, count_list):
        lista = [HD[3:], count]
        text_file.write("{0[0]:<7}{0[1]:<0}\n".format(lista))
        cont += 1

print("Qtde de estrelas no arquivo:", cont)

cursor.close()
connection.close()