import mysql.connector
import pandas as pd
import os

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar o arquivo CAT1_intersec_HIP_not_in_CAT2.csv

cursor.execute('''select CAT1_intersec_HIP_not_in_CAT2.HIP, '''
               '''CAT1.HD, '''
               '''CAT1.designation, '''
               '''TRIM(CAT1.parallax)+0, '''
               '''TRIM(CAT1.parallax_error)+0, '''
               '''TRIM(CAT1.distance_gspphot)+0, '''
               '''TRIM(CAT1.phot_g_mean_mag)+0, '''
               '''TRIM(CAT1_product.Mg)+0, '''
               '''TRIM(Hipparcos_completo.Plx)+0, '''
               '''TRIM(Hipparcos_completo.e_Plx)+0, '''
               '''TRIM(1 / (Hipparcos_completo.Plx / 1000.0))+0 as distance_Plx, '''
               '''TRIM(Hipparcos_completo.Vmag)+0, '''               
               '''TRIM(Hipparcos_completo.Vmag + 5.0 + 5.0 * log(10, Hipparcos_completo.Plx / 1000.0))+0, '''
               '''TRIM(Hipparcos_completo.B_V)+0 '''
               '''from CAT1_intersec_HIP_not_in_CAT2, CAT1, CAT1_product, Hipparcos_completo '''               
               '''where CAT1_intersec_HIP_not_in_CAT2.designation = CAT1.designation and '''
               '''CAT1.designation = CAT1_product.designation and '''
               '''CAT1_intersec_HIP_not_in_CAT2.HIP = Hipparcos_completo.HIP '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/CAT1_intersec_HIP_not_in_CAT2.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "HD", "designation", "parallax", "parallax_error", "distance_gspphot", "phot_g_mean_mag",
               "Mg", "Plx", "e_Plx", "distance_Plx", "Vmag", "MV", "B_minus_V"]

file = pd.read_csv("/var/lib/mysql-files/CAT1_intersec_HIP_not_in_CAT2.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT1_intersec_HIP_not_in_CAT2.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT1_intersec_HIP_not_in_CAT2.csv")

# Criar o arquivo Hipparcos_completo.csv

cursor.execute('''select Hipparcos_completo.HIP, ''' 
               '''TRIM(Hipparcos_completo.e_Plx)+0, '''
               '''TRIM(Hipparcos_completo.Plx)+0 '''
               '''from Hipparcos_completo '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_completo.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "e_Plx", "Plx"]

file = pd.read_csv("/var/lib/mysql-files/Hipparcos_completo.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/Hipparcos_completo",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/Hipparcos_completo.csv")

# Criar o arquivo CAT2_intersec_GaiaCompleto_via_Simbad.csv

cursor.execute('''select CAT2_DR1_DR2_DR3.HIP, '''
               '''CAT2_DR1_DR2_DR3.designation_DR3 as designation_DR3, '''
               '''CAT2_DR1_DR2_DR3.designation_DR2 as designation_DR2, '''
               '''CAT2_DR1_DR2_DR3.designation_DR1 as designation_DR1, '''
               '''CAT2.Plx, '''
               '''CAT2.e_Plx, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax)+0 as simbad_parallax, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax_error)+0, '''
               '''TRIM(1/(CAT2_DR1_DR2_DR3.simbad_parallax/1000.0))+0 as simbad_distance_parallax '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and '''
               '''(designation_DR3 is not null or '''
               '''designation_DR2 is not null or '''
               '''designation_DR1 is not null) '''
               '''order by simbad_parallax ASC '''
               '''into outfile '/var/lib/mysql-files/CAT2_intersec_GaiaCompleto_via_Simbad.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

header_list = ["HIP", "designation_DR3", "designation_DR2", "designation_DR1", "Plx", "e_Plx", "simbad_parallax",
               "simbad_parallax_error", "simbad_distance_parallax"]

file = pd.read_csv("/var/lib/mysql-files/CAT2_intersec_GaiaCompleto_via_Simbad.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/CAT2_intersec_GaiaCompleto_via_Simbad.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/CAT2_intersec_GaiaCompleto_via_Simbad.csv")

# Criar o arquivo das as estrelas que estão no CAT5, possuem dados Gaia DR1, DR2 ou DR3 e não estão no CAT1

cursor.execute('''select CAT2_DR1_DR2_DR3.HIP, '''
               '''CAT2_DR1_DR2_DR3.designation_DR3 as designation_DR3,'''
               '''CAT2_DR1_DR2_DR3.designation_DR2 as designation_DR2, '''
               '''CAT2_DR1_DR2_DR3.designation_DR1 as designation_DR1, '''
               '''TRIM(CAT2.Plx)+0, '''
               '''TRIM(CAT2.e_Plx)+0, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax)+0 as simbad_parallax, '''
               '''TRIM(CAT2_DR1_DR2_DR3.simbad_parallax_error)+0, '''
               '''TRIM(1/(CAT2_DR1_DR2_DR3.simbad_parallax/1000.0))+0 as simbad_distance_parallax '''
               '''from CAT2_DR1_DR2_DR3, CAT2 '''
               '''where CAT2_DR1_DR2_DR3.HIP = CAT2.HIP and ''' 
               '''(designation_DR3 is not null or '''
               '''designation_DR2 is not null or '''
               '''designation_DR1 is not null) and''' 
               '''(CAT2_DR1_DR2_DR3.HIP not in( '''
               '''select CAT1.HIP from CAT1 where CAT1.HIP is not NULL)) '''
               '''order by simbad_parallax ASC '''
               '''into outfile '/var/lib/mysql-files/estrelas_que_estao_no_CAT5_possuem_dados_Gaia_e_nao_estao_no_CAT1.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

file = pd.read_csv("/var/lib/mysql-files/estrelas_que_estao_no_CAT5_possuem_dados_Gaia_e_nao_estao_no_CAT1.csv", header=None)
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/files/estrelas_que_estao_no_CAT5_possuem_dados_Gaia_e_nao_estao_no_CAT1.csv",
            header=header_list, index=False)
os.remove("/var/lib/mysql-files/estrelas_que_estao_no_CAT5_possuem_dados_Gaia_e_nao_estao_no_CAT1.csv")

cursor.close()
connection.close()