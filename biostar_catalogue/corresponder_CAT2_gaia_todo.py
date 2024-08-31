from astroquery.simbad import Simbad
import mysql.connector
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")







#######################################################################################
# consulta para saber quantos HIP têm Gaia DR3

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
#######################################################################################



cursor.execute("drop table if exists Gaia_DR3")

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

#cursor.execute("drop table Gaia_DR3")

cursor.execute("drop table if exists Hipparcos_DR3")

# Criar a tabela Hipparcos_DR3 no BD:

cursor.execute("create table Hipparcos_DR3("
               "HIP INT primary key,"
               "HD CHAR(100) null,"
               "BD CHAR(100) null,"
               "CoD CHAR(100) null,"
               "CPD CHAR(100) null,"
               "Vmag NUMERIC(65,30) null,"
               "RAdeg NUMERIC(65,30) null,"
               "DEdeg NUMERIC(65,30) null,"
               "RAhms CHAR(100) null,"
               "DEdms CHAR(100) null,"
               "Plx NUMERIC(65,30) null,"
               "e_Plx NUMERIC(65,30) null,"
               "pmRA NUMERIC(65,30) null,"
               "pmDE NUMERIC(65,30) null,"
               "BTmag NUMERIC(65,30) null,"
               "VTmag NUMERIC(65,30) null,"
               "B_V NUMERIC(65,30) null,"
               "SpType CHAR(100) null,"
               "designation_DR3 CHAR(100) null)")

# Carregar os dados da tabela Hipparcos:

with open("HIP_MAIN.DAT") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) != 0:
            line = line[0].split("|")
            if len(line[11].strip()) != 0 and float(line[11].strip()) >= 0.039 * 1000.0:

                HIP_value = line[1].strip()
                if len(HIP_value) == 0:
                    cursor.execute("insert into Hipparcos_DR3(HIP) values(NULL)")
                else:
                    cursor.execute("insert into Hipparcos_DR3(HIP) values({})".format(int(HIP_value)))

                HD_value = line[71].strip()
                if len(HD_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set HD = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set HD = {} where HIP = {}".format(HD_value, int(HIP_value)))

                BD_value = line[72].strip()
                if len(BD_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set BD = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set BD = '{}' where HIP = {}".format(BD_value, int(HIP_value)))

                CoD_value = line[73].strip()
                if len(CoD_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set CoD = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set CoD = '{}' where HIP = {}".format(CoD_value, int(HIP_value)))

                CPD_value = line[74].strip()
                if len(CPD_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set CPD = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set CPD = '{}' where HIP = {}".format(CPD_value, int(HIP_value)))

                Vmag_value = line[5].strip()
                if len(Vmag_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set Vmag = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set Vmag = {} where HIP = {}".format(float(Vmag_value), int(HIP_value)))

                RAdeg_value = line[8].strip()
                if len(RAdeg_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set RAdeg = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set RAdeg = {} where HIP = {}".format(float(RAdeg_value), int(HIP_value)))

                DEdeg_value = line[9].strip()
                if len(DEdeg_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set DEdeg = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set DEdeg = {} where HIP = {}".format(float(DEdeg_value), int(HIP_value)))

                RAhms_value = line[3].strip()
                if len(RAhms_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set RAhms = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set RAhms = '{}' where HIP = {}".format(RAhms_value, int(HIP_value)))

                DEdms_value = line[4].strip()
                if len(DEdms_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set DEdms = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set DEdms = '{}' where HIP = {}".format(DEdms_value, int(HIP_value)))

                Plx_value = line[11].strip()
                if len(Plx_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set Plx = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set Plx = {} where HIP = {}".format(float(Plx_value), int(HIP_value)))

                e_Plx_value = line[16].strip()
                if len(e_Plx_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set e_Plx = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set e_Plx = {} where HIP = {}".format(float(e_Plx_value), int(HIP_value)))

                pmRA_value = line[12].strip()
                if len(pmRA_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set pmRA = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set pmRA = {} where HIP = {}".format(float(pmRA_value), int(HIP_value)))

                pmDE_value = line[13].strip()
                if len(pmDE_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set pmDE = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set pmDE = {} where HIP = {}".format(float(pmDE_value), int(HIP_value)))

                BTmag_value = line[32].strip()
                if len(BTmag_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set BTmag = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set BTmag = {} where HIP = {}".format(float(BTmag_value), int(HIP_value)))

                VTmag_value = line[34].strip()
                if len(VTmag_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set VTmag = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set VTmag = {} where HIP = {}".format(float(VTmag_value), int(HIP_value)))

                B_V_value = line[37].strip()
                if len(B_V_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set B_V = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set B_V = {} where HIP = {}".format(float(B_V_value), int(HIP_value)))

                SpType_value = line[76].strip()
                if len(SpType_value) == 0:
                    cursor.execute("update Hipparcos_DR3 set SpType = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos_DR3 set SpType = '{}' where HIP = {}".format(SpType_value, int(HIP_value)))

                # Verificar se no Simbad existe um Gaia DR3 correspondente ao HIP
                # Se houver, carregar no BD. Senao, colocar NULL.

                tab = Simbad.query_objectids("HIP " + str(HIP_value))

                if len([id for id in tab['ID'] if id.startswith('Gaia DR3')]) == 0:
                    cursor.execute("update Hipparcos_DR3 set designation_DR3 = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    designation_DR3_value = [id for id in tab['ID'] if id.startswith('Gaia DR3')][0][0:].strip()
                    cursor.execute(
                        "update Hipparcos_DR3 set designation_DR3 = '{}' where HIP = {}".format(designation_DR3_value, int(HIP_value)))
tsv.close()

#cursor.execute("drop table Hipparcos_DR3")

# Make sure data is committed to the database
connection.commit()

# Criar o arquivo CAT2_intersecao_Gaia.csv

'''hips_com_designacao_DR3 = ",".join(hips_com_designacao_DR3)'''

cursor.execute('''select Hipparcos_DR3.HIP, '''
               '''Gaia_DR3.designation, '''
               '''TRIM(Hipparcos_DR3.Plx)+0, '''
               '''TRIM(Hipparcos_DR3.e_Plx)+0, '''
               '''TRIM(Gaia_DR3.Plx)+0 as Plx_Gaia, '''
               '''TRIM(Gaia_DR3.e_Plx)+0, '''
               '''TRIM(Gaia_DR3.distance_gspphot)+0 '''
               '''from Hipparcos_DR3, Gaia_DR3 '''
               '''where Hipparcos_DR3.designation_DR3 = Gaia_DR3.designation and '''
               '''Hipparcos_DR3.designation_DR3 is not NULL '''
               '''order by Plx_Gaia DESC '''
               '''into outfile '/var/lib/mysql-files/CAT2_intersecao_Gaia.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

cursor.close()
connection.close()