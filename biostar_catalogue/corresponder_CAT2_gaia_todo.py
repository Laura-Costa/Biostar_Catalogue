from astroquery.simbad import Simbad
import mysql.connector
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

cursor.execute("drop table if exists Gaia_DR3")

cursor.execute("select Hipparcos.HIP "
               "from Hipparcos ")
value = cursor.fetchall()

HIP_list = []

for (HIP_value,) in value:
    HIP_list.append(HIP_value)

hips_com_designacao_DR3 = ()

for i in range(len(HIP_list)):
    tab = Simbad.query_objectids("HIP " + str(HIP_list[i]))

    ids = [id for id in tab['ID'] if id.startswith('Gaia DR3')]
    if len(ids) != 0:
        # se esse if é True, entao a estrela com identificador HIP_list[i] tem designation no Gaia DR3
        hips_com_designacao_DR3 += (str(HIP_list[i]),)

print(len(hips_com_designacao_DR3))

# Criar a tabela Gaia_DR3 no BD:

cursor.execute("create table Gaia_DR3("
               "designation CHAR(100) primary key,"
               "Plx NUMERIC(65,30) null,"
               "e_Plx NUMERIC(65,30) null,"
               "distance_gspphot NUMERIC(65,30) null, "
               "HIP INT null)")

# Carregar os dados da tabela Gaia_DR3:

with open("asu.tsv") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):

        if len(line) != 0:
            line = line[0].split("|")

            designation_value = line[0].strip()
            if len(designation_value) == 0:
                cursor.execute("insert into Gaia_DR3(designation) values(NULL)")
            else:
                cursor.execute("insert into Gaia_DR3(designation) values('{}')".format(designation_value))

            Plx_value = line[1].strip()
            if len(Plx_value) == 0:
                cursor.execute("update Gaia_DR3 set Plx = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia_DR3 set Plx = {} where designation = '{}'".format(float(Plx_value), designation_value))

            e_Plx_value = line[2].strip()
            if len(e_Plx_value) == 0:
                cursor.execute("update Gaia_DR3 set e_Plx = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia_DR3 set e_Plx = {} where designation = '{}'".format(float(e_Plx_value), designation_value))

            distance_gspphot_value = line[3].strip()
            if len(distance_gspphot_value) == 0:
                cursor.execute("update Gaia_DR3 set distance_gspphot = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia_DR3 set distance_gspphot = {} where designation = '{}'".format(float(distance_gspphot_value), designation_value))

            HIP_value = line[4].strip()
            if len(HIP_value) == 0:
                cursor.execute("update Gaia_DR3 set HIP = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia_DR3 set HIP = {} where designation = '{}'".format(int(HIP_value), designation_value))
tsv.close()

# cursor.execute("drop table Gaia_DR3")

# Make sure data is committed to the database
connection.commit()

# Criar o arquivo CAT2_intersecao_Gaia.csv
hips_com_designacao_DR3 = ",".join(hips_com_designacao_DR3)
cursor.execute('''select Hipparcos.HIP, '''
               '''Gaia_DR3.designation, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(Gaia_DR3.Plx)+0 as Plx_Gaia, '''
               '''TRIM(Gaia_DR3.e_Plx)+0, '''
               '''TRIM(Gaia_DR3.distance_gspphot)+0 '''
               '''from Hipparcos, Gaia_DR3 '''
               '''where Hipparcos.HIP IN (%s) and ''' 
               '''Hipparcos.HIP = Gaia_DR3.HIP '''
               '''order by Plx_Gaia DESC '''
               '''into outfile '/var/lib/mysql-files/CAT2_intersecao_Gaia.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''' % hips_com_designacao_DR3)

cursor.close()
connection.close()