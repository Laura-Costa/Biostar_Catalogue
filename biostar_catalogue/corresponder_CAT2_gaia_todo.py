from xxsubtype import bench
from astroquery.simbad import Simbad
import mysql.connector
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import decimal
import numpy as np
from matplotlib.ticker import FormatStrFormatter

from edited_diagram import hips_com_designacao

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

# Criar o diagrama Hipparcos_minus_Gaia.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos.HIP "
               "from Hipparcos ")
value = cursor.fetchall()

HIP_list = []

for (HIP_value,) in value:
    HIP_list.append(HIP_value)

print(HIP_list)
# Separar os dados das estrelas que têm designação mas não estão no catálogo 1

hips_com_designacao = ()
for i in range(len(HIP_list)):
    tab = Simbad.query_objectids("HIP " + str(HIP_list[i]))
    ids = [id for id in tab['ID'] if id.startswith('Gaia')]
    if len(ids) != 0:
        # se esse if é True, entao a estrela com identificador HIP_list[i] tem designation, ela está no Gaia com distancia maior do que 23pc
        hips_com_designacao += (str(HIP_list[i]),)


cursor.close()
connection.close()