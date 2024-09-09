import mysql.connector
import pandas as pd
from code.diagram import CAT5
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

header_list = ["HIP", "HD", "designation", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx", "pmRA", "pmDE",
               "BTmag", "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

# Criar o arquivo CAT2_minus_CAT1_MV_versus_B_minus_V_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/CAT2_minus_CAT1_MV_versus_B_minus_V_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_minus_CAT1_MV_versus_B_minus_V_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT2_minus_CAT1_MV_versus_B_minus_V_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_minus_CAT1_MV_versus_B_minus_V_plotted.csv")

# Criar o arquivo CAT2_minus_CAT1_MV_versus_B_minus_V_not_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''(CAT2_product.MV is NULL or '''
               '''CAT2_product.B_minus_V is NULL) and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/CAT2_minus_CAT1_MV_versus_B_minus_V_not_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_minus_CAT1_MV_versus_B_minus_V_not_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT2_minus_CAT1_MV_versus_B_minus_V_not_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_minus_CAT1_MV_versus_B_minus_V_not_plotted.csv")

# Criar o arquivo CAT2_minus_CAT1_MVt_versus_BT_minus_VT_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MVt is not NULL and '''
               '''CAT2_product.BT_minus_VT is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_plotted.csv")

# Criar o arquivo CAT2_minus_CAT1_MVt_versus_BT_minus_VT_not_plotted.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''IF (CAT2.HIP in ( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL), '''
               '''(select CAT1.designation from CAT1 where CAT1.HIP = CAT2.HIP), NULL) AS designation, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.pmRA)+0, '''
               '''TRIM(CAT2.pmDE)+0, '''
               '''TRIM(CAT2.BTmag)+0, '''
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''(CAT2_product.MVt is NULL or '''
               '''CAT2_product.BT_minus_VT is NULL) and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_not_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_not_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_not_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_minus_CAT1_MVt_versus_BT_minus_VT_not_plotted.csv")

# Criar o arquivo CAT5.csv

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''TRIM(CAT2.RAdeg)+0, '''
               '''TRIM(CAT2.DEdeg)+0, '''
               '''CAT2.RAhms, '''
               '''CAT2.DEdms, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(1/(CAT2.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(CAT2.Vmag)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MV_error)+0, '''               
               '''TRIM(CAT2.VTmag)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''TRIM(CAT2_product.MVt_error)+0, '''               
               '''TRIM(CAT2_product.B_minus_V)+0, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0 '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/CAT5.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "HD", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx", "Vmag", "MV",
               "MV_error", "VTmag",  "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

file = pd.read_csv("/var/lib/mysql-files/CAT5.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT5.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT5.csv")

# Header List para os 5 arquivos a seguir
header_list = ["HIP", "HD", "BD", "CoD", "CPD", "B_minus_V", "BT_minus_VT", "MV", "MVt", "SpType"]

# Criar o arquivo CAT5_MV_versus_B_minus_V_white_dwarfs.csv
anas_brancas = CAT5.anas_brancas()[0]
anas_brancas = ['"' + HIP + '"' for HIP in anas_brancas]
anas_brancas = ", ".join(anas_brancas)

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''CAT2.BD, '''
               '''CAT2.CoD, '''
               '''CAT2.CPD, '''
               '''TRIM(CAT2_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''CAT2.SpType '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP IN (%s) and ''' 
               '''CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_white_dwarfs.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % anas_brancas)

file = pd.read_csv("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_white_dwarfs.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT5_MV_versus_B_minus_V_white_dwarfs.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_white_dwarfs.csv")

# Criar o arquivo CAT5_MV_versus_B_minus_V_unknown.csv
sem_classificacao = CAT5.sem_classificacao()[0]
sem_classificacao = ['"' + HIP + '"' for HIP in sem_classificacao]
sem_classificacao = ", ".join(sem_classificacao)

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''CAT2.BD, '''
               '''CAT2.CoD, '''
               '''CAT2.CPD, '''
               '''TRIM(CAT2_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''CAT2.SpType '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP IN (%s) and ''' 
               '''CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_unclassified.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % sem_classificacao)

file = pd.read_csv("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_unclassified.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT5_MV_versus_B_minus_V_unclassified.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_unclassified.csv")

# Criar o arquivo CAT5_MV_versus_B_minus_V_AFG.csv
AFG = CAT5.AFG()[0]
AFG = ['"' + HIP + '"' for HIP in AFG]
AFG = ", ".join(AFG)

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''CAT2.BD, '''
               '''CAT2.CoD, '''
               '''CAT2.CPD, '''
               '''TRIM(CAT2_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''CAT2.SpType '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP IN (%s) and ''' 
               '''CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_AFG.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % AFG)

file = pd.read_csv("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_AFG.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT5_MV_versus_B_minus_V_AFG.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_AFG.csv")

# Criar o arquivo CAT5_MV_versus_B_minus_V_GK.csv
GK = CAT5.GK()[0]
GK = ['"' + HIP + '"' for HIP in GK]
GK = ", ".join(GK)

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''CAT2.BD, '''
               '''CAT2.CoD, '''
               '''CAT2.CPD, '''
               '''TRIM(CAT2_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''CAT2.SpType '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP IN (%s) and ''' 
               '''CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_GK.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % GK)

file = pd.read_csv("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_GK.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT5_MV_versus_B_minus_V_GK.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_GK.csv")

# Criar o arquivo CAT5_MV_versus_B_minus_V_red_dwarfs.csv
anas_vermelhas = CAT5.anas_vermelhas()[0]
anas_vermelhas = ['"' + HIP + '"' for HIP in anas_vermelhas]
anas_vermelhas = ", ".join(anas_vermelhas)

cursor.execute('''select CAT2.HIP, '''
               '''CAT2.HD, '''
               '''CAT2.BD, '''
               '''CAT2.CoD, '''
               '''CAT2.CPD, '''
               '''TRIM(CAT2_product.B_minus_V)+0 AS B_minus_V, '''
               '''TRIM(CAT2_product.BT_minus_VT)+0, '''
               '''TRIM(CAT2_product.MV)+0, '''
               '''TRIM(CAT2_product.MVt)+0, '''
               '''CAT2.SpType '''
               '''from CAT2, CAT2_product '''
               '''where CAT2.HIP IN (%s) and ''' 
               '''CAT2.HIP = CAT2_product.HIP and '''
               '''CAT2_product.MV is not NULL and '''
               '''CAT2_product.B_minus_V is not NULL and '''
               '''CAT2.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL ) '''
               '''order by B_minus_V ASC '''
               '''into outfile '/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_red_dwarfs.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % anas_vermelhas)

file = pd.read_csv("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_red_dwarfs.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT5/csv/CAT5_MV_versus_B_minus_V_red_dwarfs.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT5_MV_versus_B_minus_V_red_dwarfs.csv")

cursor.close()
connection.close()