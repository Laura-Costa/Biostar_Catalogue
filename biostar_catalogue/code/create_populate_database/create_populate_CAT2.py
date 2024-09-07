import csv
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar a tabela CAT2 no BD:

cursor.execute("create table CAT2("
               "HIP CHAR(100) primary key,"
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
               "SpType CHAR(100) null)")

# Carregar os dados da tabela CAT2:

with open("HIP_MAIN.DAT") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) != 0:
            line = line[0].split("|")
            if len(line[11].strip()) != 0 and float(line[11].strip()) >= 0.039 * 1000.0:

                HIP_value = "HIP " + line[1].strip()
                if len(HIP_value) == 0:
                    cursor.execute("insert into CAT2(HIP) values(NULL)")
                else:
                    cursor.execute("insert into CAT2(HIP) values('{}')".format(HIP_value))

                HD_value = line[71].strip()
                if len(HD_value) == 0:
                    cursor.execute("update CAT2 set HD = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set HD = {} where HIP = '{}'".format(HD_value, HIP_value))

                BD_value = line[72].strip()
                if len(BD_value) == 0:
                    cursor.execute("update CAT2 set BD = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set BD = '{}' where HIP = '{}'".format(BD_value, HIP_value))

                CoD_value = line[73].strip()
                if len(CoD_value) == 0:
                    cursor.execute("update CAT2 set CoD = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set CoD = '{}' where HIP = '{}'".format(CoD_value, HIP_value))

                CPD_value = line[74].strip()
                if len(CPD_value) == 0:
                    cursor.execute("update CAT2 set CPD = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set CPD = '{}' where HIP = '{}'".format(CPD_value, HIP_value))

                Vmag_value = line[5].strip()
                if len(Vmag_value) == 0:
                    cursor.execute("update CAT2 set Vmag = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set Vmag = {} where HIP = '{}'".format(float(Vmag_value), HIP_value))

                RAdeg_value = line[8].strip()
                if len(RAdeg_value) == 0:
                    cursor.execute("update CAT2 set RAdeg = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set RAdeg = {} where HIP = '{}'".format(float(RAdeg_value), HIP_value))

                DEdeg_value = line[9].strip()
                if len(DEdeg_value) == 0:
                    cursor.execute("update CAT2 set DEdeg = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set DEdeg = {} where HIP = '{}'".format(float(DEdeg_value), HIP_value))

                RAhms_value = line[3].strip()
                if len(RAhms_value) == 0:
                    cursor.execute("update CAT2 set RAhms = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set RAhms = '{}' where HIP = '{}'".format(RAhms_value, HIP_value))

                DEdms_value = line[4].strip()
                if len(DEdms_value) == 0:
                    cursor.execute("update CAT2 set DEdms = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set DEdms = '{}' where HIP = '{}'".format(DEdms_value, HIP_value))

                Plx_value = line[11].strip()
                if len(Plx_value) == 0:
                    cursor.execute("update CAT2 set Plx = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set Plx = {} where HIP = '{}'".format(float(Plx_value), HIP_value))

                e_Plx_value = line[16].strip()
                if len(e_Plx_value) == 0:
                    cursor.execute("update CAT2 set e_Plx = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set e_Plx = {} where HIP = '{}'".format(float(e_Plx_value), HIP_value))

                pmRA_value = line[12].strip()
                if len(pmRA_value) == 0:
                    cursor.execute("update CAT2 set pmRA = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set pmRA = {} where HIP = '{}'".format(float(pmRA_value), HIP_value))

                pmDE_value = line[13].strip()
                if len(pmDE_value) == 0:
                    cursor.execute("update CAT2 set pmDE = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set pmDE = {} where HIP = '{}'".format(float(pmDE_value), HIP_value))

                BTmag_value = line[32].strip()
                if len(BTmag_value) == 0:
                    cursor.execute("update CAT2 set BTmag = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set BTmag = {} where HIP = '{}'".format(float(BTmag_value), HIP_value))

                VTmag_value = line[34].strip()
                if len(VTmag_value) == 0:
                    cursor.execute("update CAT2 set VTmag = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set VTmag = {} where HIP = '{}'".format(float(VTmag_value), HIP_value))

                B_V_value = line[37].strip()
                if len(B_V_value) == 0:
                    cursor.execute("update CAT2 set B_V = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set B_V = {} where HIP = '{}'".format(float(B_V_value), HIP_value))

                SpType_value = line[76].strip()
                if len(SpType_value) == 0:
                    cursor.execute("update CAT2 set SpType = NULL where HIP = '{}'".format(HIP_value))
                else:
                    cursor.execute("update CAT2 set SpType = '{}' where HIP = '{}'".format(SpType_value, HIP_value))
tsv.close()

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()