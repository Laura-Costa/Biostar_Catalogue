import mysql.connector

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

cursor.execute("create view view_CAT1 as "
               "select * "
               "from CAT1, CAT1_product "
               "where "
               "CAT1.designation = CAT1_product.designation and "
               "( "
               "(parallax >= 50.00 and phot_g_mean_mag is not null) or "
               "(parallax >= 50.00 and phot_g_mean_mag is null and MRp < 8.0) or " # condição para incluir a estrela 'Gaia DR3 5443030200460964480'
               "(parallax < 50.00 and MG <= 9.08) " # condição que seleciona as 3 estrelas da "borda" de 3*sigmas 
               ")")

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o banco de dados
connection.close()