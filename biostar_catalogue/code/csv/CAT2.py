import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

header_list = ["HIP", "HD", "designation", "Vmag", "RAdeg", "DEdeg", "RAhms", "DEdms", "Plx", "e_Plx", "distance_Plx",
               "pmRA", "pmDE", "BTmag", "VTmag", "MV", "MV_error", "MVt", "MVt_error", "B_minus_V", "BT_minus_VT"]

# Criando o arquivo CAT2_MV_versus_B_minus_V_plotted.csv

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
               '''CAT2_product.B_minus_V is not NULL '''
               '''order by CAT2.Plx ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_MV_versus_B_minus_V_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_MV_versus_B_minus_V_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_MV_versus_B_minus_V_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_MV_versus_B_minus_V_plotted.csv")

# Criando o arquivo CAT2_MVt_versus_BT_minus_VT_plotted.csv

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
               '''CAT2_product.BT_minus_VT is not NULL '''
               '''order by CAT2.Plx ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_MVt_versus_BT_minus_VT_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_plotted.csv")

# Criando o arquivo CAT2_MVt_versus_BT_minus_VT_not_plotted.csv

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
               '''CAT2_product.BT_minus_VT is NULL) '''
               '''order by CAT2.Plx ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_MVt_versus_BT_minus_VT_not_plotted.csv")

# Criar o arquivo CAT2_intersec_GaiaCompleto_DR1_DR2_DR3_via_Simbad.csv

cursor.execute('''select CAT2_DR1_DR2_DR3.HIP, '''
               '''CAT2_DR1_DR2_DR3.designation_DR3 as designation_DR3, '''
               '''CAT2_DR1_DR2_DR3.designation_DR2 as designation_DR2, '''
               '''CAT2_DR1_DR2_DR3.designation_DR1 as designation_DR1, '''
               '''CAT2.Plx, '''
               '''CAT2.e_Plx, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax)+0 as simbad_parallax, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax_error)+0 '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and '''
               '''(designation_DR3 is not null or '''
               '''designation_DR2 is not null or '''
               '''designation_DR1 is not null) '''
               '''order by simbad_parallax ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_intersec_GaiaCompleto_DR1_DR2_DR3_via_Simbad.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "designation_DR3", "designation_DR2", "designation_DR1", "hipparcos_parallax", "hipparcos_parallax_error",
               "simbad_parallax", "simbad_parallax_error"]

file = pd.read_csv("/var/lib/mysql-files/CAT2_intersec_GaiaCompleto_DR1_DR2_DR3_via_Simbad.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2/csv/CAT2_intersec_GaiaCompleto_DR1_DR2_DR3_via_Simbad.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_intersec_GaiaCompleto_DR1_DR2_DR3_via_Simbad.csv")

cursor.close()
connection.close()
