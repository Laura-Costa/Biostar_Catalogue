import pandas as pd

header_list = ["e_Plx", "Plx"]
file = pd.read_csv("/var/lib/mysql-files/Hipparcos_ePlx_Plx_sem_header.csv")
file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/CAT2/CSVs/Hipparcos_ePlx_Plx.csv", header=header_list, index=False)
