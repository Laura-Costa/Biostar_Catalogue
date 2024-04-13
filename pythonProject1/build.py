from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astroquery.simbad import Simbad
import csv
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', port='3306', user='helena', password='ic2023')
cursor = connection.cursor()

cursor.execute("drop database if exists gaia_catalogue_1")
cursor.execute("create database gaia_catalogue_1")

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

# Crir a tabela Hipparcos no BD:

cursor.execute("create table Hipparcos("
               "HIP INT primary key,"
               "HD CHAR(100) null,"
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
               "B_V NUMERIC(65,30) null)")

# Carregar os dados da tabela Hipparcos:

with open("HIP_MAIN.DAT") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) != 0:
            line = line[0].split("|")
            if len(line[11].strip()) != 0 and float(line[11].strip()) >= 0.039 * 1000.0:

                HIP_value = line[1].strip()
                if len(HIP_value) == 0:
                    cursor.execute("insert into Hipparcos(HIP) values(NULL)")
                else:
                    cursor.execute("insert into Hipparcos(HIP) values({})".format(int(HIP_value)))

                HD_value = line[71].strip()
                if len(HD_value) == 0:
                    cursor.execute("update Hipparcos set HD = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set HD = {} where HIP = {}".format(HD_value, int(HIP_value)))

                Vmag_value = line[5].strip()
                if len(Vmag_value) == 0:
                    cursor.execute("update Hipparcos set Vmag = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set Vmag = {} where HIP = {}".format(float(Vmag_value), int(HIP_value)))

                RAdeg_value = line[8].strip()
                if len(RAdeg_value) == 0:
                    cursor.execute("update Hipparcos set RAdeg = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set RAdeg = {} where HIP = {}".format(float(RAdeg_value), int(HIP_value)))

                DEdeg_value = line[9].strip()
                if len(DEdeg_value) == 0:
                    cursor.execute("update Hipparcos set DEdeg = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set DEdeg = {} where HIP = {}".format(float(DEdeg_value), int(HIP_value)))

                RAhms_value = line[3].strip()
                if len(RAhms_value) == 0:
                    cursor.execute("update Hipparcos set RAhms = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set RAhms = '{}' where HIP = {}".format(RAhms_value, int(HIP_value)))

                DEdms_value = line[4].strip()
                if len(DEdms_value) == 0:
                    cursor.execute("update Hipparcos set DEdms = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set DEdms = '{}' where HIP = {}".format(DEdms_value, int(HIP_value)))

                Plx_value = line[11].strip()
                if len(Plx_value) == 0:
                    cursor.execute("update Hipparcos set Plx = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set Plx = {} where HIP = {}".format(float(Plx_value), int(HIP_value)))

                e_Plx_value = line[16].strip()
                if len(e_Plx_value) == 0:
                    cursor.execute("update Hipparcos set e_Plx = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set e_Plx = {} where HIP = {}".format(float(e_Plx_value), int(HIP_value)))

                pmRA_value = line[12].strip()
                if len(pmRA_value) == 0:
                    cursor.execute("update Hipparcos set pmRA = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set pmRA = {} where HIP = {}".format(float(pmRA_value), int(HIP_value)))

                pmDE_value = line[13].strip()
                if len(pmDE_value) == 0:
                    cursor.execute("update Hipparcos set pmDE = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set pmDE = {} where HIP = {}".format(float(pmDE_value), int(HIP_value)))

                BTmag_value = line[32].strip()
                if len(BTmag_value) == 0:
                    cursor.execute("update Hipparcos set BTmag = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set BTmag = {} where HIP = {}".format(float(BTmag_value), int(HIP_value)))

                VTmag_value = line[34].strip()
                if len(VTmag_value) == 0:
                    cursor.execute("update Hipparcos set VTmag = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set VTmag = {} where HIP = {}".format(float(VTmag_value), int(HIP_value)))

                B_V_value = line[37].strip()
                if len(B_V_value) == 0:
                    cursor.execute("update Hipparcos set B_V = NULL where HIP = {}".format(int(HIP_value)))
                else:
                    cursor.execute("update Hipparcos set B_V = {} where HIP = {}".format(float(B_V_value), int(HIP_value)))
tsv.close()

# Criar a tabela Gaia no BD

cursor.execute("create table Gaia("
               "designation CHAR(100) primary key,"
               "HIP INT null,"
               "HD CHAR(100) null,"
               "ra NUMERIC(65,30) null,"
               "declination NUMERIC(65,30) null,"
               "parallax NUMERIC(65,30) null,"
               "parallax_error NUMERIC(65,30) null,"
               "pm NUMERIC(65,30) null,"
               "pmra NUMERIC(65,30) null,"
               "pmdec NUMERIC(65,30) null,"
               "ruwe NUMERIC(65,30) null,"
               "phot_g_mean_mag NUMERIC(65,30) null,"
               "phot_bp_mean_mag NUMERIC(65,30) null,"
               "phot_rp_mean_mag NUMERIC(65,30) null,"
               "teff_gspphot NUMERIC(65,30) null,"
               "teff_gspphot_lower NUMERIC(65,30) null,"
               "teff_gspphot_upper NUMERIC(65,30) null,"
               "logg_gspphot NUMERIC(65,30) null,"
               "logg_gspphot_lower NUMERIC(65,30) null,"
               "logg_gspphot_upper NUMERIC(65,30) null,"
               "mh_gspphot NUMERIC(65,30) null,"
               "mh_gspphot_lower NUMERIC(65,30) null,"
               "mh_gspphot_upper NUMERIC(65,30) null,"
               "distance_gspphot NUMERIC(65,30) null,"
               "distance_gspphot_lower NUMERIC(65,30) null,"
               "distance_gspphot_upper NUMERIC(65,30) null,"
               "foreign key (HIP) references Hipparcos(HIP) on delete restrict)")

# Carregar dados da tabela Gaia

cursor.execute("select HIP from Hipparcos")
HIPs_in_Hipparcos = cursor.fetchall()

with open("1712690092801O-result.csv", 'r') as csv_file:
    next(csv_file)

    with open('HIPs_novos.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file, dialect='unix', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow(["HIP", "designation", "HD"])

        for line in csv_file:
            line = line.split(",")
            line[0] = line[0].split('"')[1]

            # load designation

            designation_value = line[0].strip()
            if len(designation_value) == 0:
                cursor.execute("insert into Gaia(designation) values(NULL)")
            else:
                cursor.execute("insert into Gaia(designation) values('{}')".format(designation_value))


            # Verificar se no Simbad existe um HD correspondente a designation
            # Se houver, carregar no BD. Senao, colocar NULL.


            tab = Simbad.query_objectids(designation_value)

            if (len([id for id in tab['ID'] if id.startswith('HD')]) == 0):
                cursor.execute("update Gaia set HD = NULL where designation = '{}'".format(designation_value))
            else:
                HD_value = [id for id in tab['ID'] if id.startswith('HD')][0][2:].strip()
                cursor.execute("update Gaia set HD = '{}' where designation = '{}'".format(HD_value, designation_value))

            # Verificar se no Simbad existe um HIP correspondente a designation
            # Se houver, carregar no BD. Senao, colocar NULL.
            # OBS: o HIP correspondente só é carregado se ele já estiver na tabela Hipparcos (25,64 pc)

            if (len([id for id in tab['ID'] if id.startswith('HIP')]) == 0):
                cursor.execute("update Gaia set HIP = NULL where designation = '{}'".format(designation_value))
            else:
                HIP_value = [id for id in tab['ID'] if id.startswith('HIP')][0][3:].strip()
                cursor.execute("update Gaia set HIP = {} where designation = '{}' and HIP in"
                               "(select HIP from Hipparcos)".format(int(HIP_value), designation_value))

                # Gerar um arquivo com os HIPs novos na intersecao entre Gaia e Hipparcos
                # Ou seja, o Gaia 'correspondeu' com HIPs que não estao na selecao atual do Hipparcos

                if (int(HIP_value),) not in HIPs_in_Hipparcos:
                    csv_writer.writerow([int(HIP_value), designation_value, HD_value])

            # load ra

            ra_value = line[1].strip()
            if len(ra_value) == 0:
                cursor.execute("update Gaia set ra = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set ra = {} where designation = '{}'".format(float(ra_value), designation_value))

            # load declination

            declination_value = line[2].strip()
            if len(declination_value) == 0:
                cursor.execute("update Gaia set declination = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set declination = {} where designation = '{}'".format(float(declination_value), designation_value))

            # load parallax

            parallax_value = line[3].strip()
            if len(parallax_value) == 0:
                cursor.execute("update Gaia set parallax = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set parallax = {} where designation = '{}'".format(float(parallax_value), designation_value))

            # load parallax_error

            parallax_error_value = line[4].strip()
            if len(parallax_error_value) == 0:
                cursor.execute("update Gaia set parallax_error = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set parallax_error = {} where designation = '{}'".format(float(parallax_error_value), designation_value))

            # load pm

            pm_value = line[5].strip()
            if len(pm_value) == 0:
                cursor.execute("update Gaia set pm = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set pm = {} where designation = '{}'".format(float(pm_value), designation_value))

            # load pmra

            pmra_value = line[6].strip()
            if len(pmra_value) == 0:
                cursor.execute("update Gaia set pmra = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set pmra = {} where designation = '{}'".format(float(pmra_value), designation_value))

            # load pmdec

            pmdec_value = line[7].strip()
            if len(pmdec_value) == 0:
                cursor.execute("update Gaia set pmdec = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set pmdec = {} where designation = '{}'".format(float(pmdec_value), designation_value))

            # load ruwe

            ruwe_value = line[8].strip()
            if len(ruwe_value) == 0:
                cursor.execute("update Gaia set ruwe = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set ruwe = {} where designation = '{}'".format(float(ruwe_value), designation_value))

            # load phot_g_mean_mag

            phot_g_mean_mag_value = line[9].strip()
            if len(phot_g_mean_mag_value) == 0:
                cursor.execute("update Gaia set phot_g_mean_mag = NULL where designation = '{}'".format(float(phot_g_mean_mag_value), designation_value))
            else:
                cursor.execute("update Gaia set phot_g_mean_mag = {} where designation = '{}'".format(float(phot_g_mean_mag_value), designation_value))

            # load phot_bp_mean_mag

            phot_bp_mean_mag_value = line[10].strip()
            if len(phot_bp_mean_mag_value) == 0:
                cursor.execute("update Gaia set phot_bp_mean_mag = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set phot_bp_mean_mag = {} where designation = '{}'".format(float(phot_bp_mean_mag_value), designation_value))

            # load phot_rp_mean_mag

            phot_rp_mean_mag_value = line[11].strip()
            if len(phot_rp_mean_mag_value) == 0:
                cursor.execute("update Gaia set phot_rp_mean_mag = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set phot_rp_mean_mag = {} where designation = '{}'".format(float(phot_rp_mean_mag_value), designation_value))

            # load teff_gspphot

            teff_gspphot_value = line[12].strip()
            if len(teff_gspphot_value) == 0:
                cursor.execute("update Gaia set teff_gspphot = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set teff_gspphot = {} where designation = '{}'".format(float(teff_gspphot_value), designation_value))

            # load teff_gspphot_lower

            teff_gspphot_lower_value = line[13].strip()
            if len(teff_gspphot_lower_value) == 0:
                cursor.execute("update Gaia set teff_gspphot_lower = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set teff_gspphot_lower = {} where designation = '{}'".format(float(teff_gspphot_lower_value), designation_value))

            # load teff_gspphot_upper

            teff_gspphot_upper_value = line[14].strip()
            if len(teff_gspphot_upper_value) == 0:
                cursor.execute("update Gaia set teff_gspphot_upper = NULL where designation = '{}'".format(float(teff_gspphot_upper_value), designation_value))
            else:
                cursor.execute("update Gaia set teff_gspphot_upper = {} where designation = '{}'".format(float(teff_gspphot_upper_value), designation_value))

            # load logg_gspphot

            logg_gspphot_value = line[15].strip()
            if len(logg_gspphot_value) == 0:
                cursor.execute("update Gaia set logg_gspphot = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set logg_gspphot = {} where designation = '{}'".format(float(logg_gspphot_value), designation_value))

            # load logg_gspphot_lower

            logg_gspphot_lower_value = line[16].strip()
            if len(logg_gspphot_lower_value) == 0:
                cursor.execute("update Gaia set logg_gspphot_lower = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set logg_gspphot_lower = {} where designation = '{}'".format(float(logg_gspphot_lower_value), designation_value))

            # load logg_gspphot_upper

            logg_gspphot_upper_value = line[17].strip()
            if len(logg_gspphot_upper_value) == 0:
                cursor.execute("update Gaia set logg_gspphot_upper = NULL where deignation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set logg_gspphot_upper = {} where designation = '{}'".format(float(logg_gspphot_upper_value), designation_value))

            # load mh_gspphot

            mh_gspphot_value = line[18].strip()
            if len(mh_gspphot_value) == 0:
                cursor.execute("update Gaia set mh_gspphot = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set mh_gspphot = {} where designation = '{}'".format(float(mh_gspphot_value), designation_value))

            # load mh_gspphot_upper

            mh_gspphot_lower_value = line[19].strip()
            if len(mh_gspphot_lower_value) == 0:
                cursor.execute("update Gaia set mh_gspphot_lower = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set mh_gspphot_lower = {} where designation = '{}'".format(float(mh_gspphot_lower_value), designation_value))

            # load mh_gspphot_lower

            mh_gspphot_upper_value = line[20].strip()
            if len(mh_gspphot_upper_value) == 0:
                cursor.execute("update Gaia set mh_gspphot_upper = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set mh_gspphot_upper = {} where designation = '{}'".format(float(mh_gspphot_upper_value), designation_value))

            # load distance_gspphot

            distance_gspphot_value = line[21].strip()
            if len(distance_gspphot_value) == 0:
                cursor.execute("update Gaia set distance_gspphot = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set distance_gspphot = {} where designation = '{}'".format(float(distance_gspphot_value), designation_value))

            # load distance_gspphot_lower

            distance_gspphot_lower_value = line[22].strip()
            if len(distance_gspphot_lower_value) == 0:
                cursor.execute("update Gaia set distance_gspphot_lower = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set distance_gspphot_lower = {} where designation = '{}'".format(float(distance_gspphot_lower_value), designation_value))

            # load distance_upper

            distance_gspphot_upper_value = line[23].strip()
            if len(distance_gspphot_upper_value) == 0:
                cursor.execute("update Gaia set distance_gspphot_upper = NULL where designation = '{}'".format(designation_value))
            else:
                cursor.execute("update Gaia set distance_gspphot_upper = {} where designation = '{}'".format(float(distance_gspphot_upper_value), designation_value))

        file.close()
    csv_file.close()


# Criar a tabela Gaia_product no BD

cursor.execute("create table Gaia_product("
               "designation CHAR(100) primary key,"
               "Mg NUMERIC(65,30) null,"
               "Mg_error NUMERIC(65,30) null,"
               "MRp NUMERIC(65,30) null,"
               "MRp_error NUMERIC(65,30) null,"
               "Bp_minus_Rp NUMERIC(65,30) null,"
               "foreign key (designation) references Gaia(designation) on delete restrict)")

# Carregar dados da tabela Gaia_product

# load designation

cursor.execute("select designation from Gaia")
value = cursor.fetchall()

add_row = ("insert into Gaia_product (designation) values (%(designation)s)")

for registro in value:
    data_row = {
        'designation': registro[0]
    }
    cursor.execute(add_row, data_row)

# load Mg

cursor.execute("select designation, phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as Mg from Gaia where phot_g_mean_mag is not NULL")
value = cursor.fetchall()
for (designation_value, Mg_value) in value:
    cursor.execute("update Gaia_product set Mg = {} where designation = '{}'".format(Mg_value, designation_value))

cursor.execute("select designation from Gaia where phot_g_mean_mag is NULL")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set Mg = NULL where designation = '{}'".format(designation_value))

# load Mg_error

cursor.execute("select designation, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2 as Mg_error "
               "from Gaia "
               "where phot_g_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL")
value = cursor.fetchall()
for (designation_value, Mg_error_value) in value:
    cursor.execute("update Gaia_product set Mg_error = {} where designation = '{}'".format(Mg_error_value, designation_value))

cursor.execute("select designation "
               "from Gaia "
               "where phot_g_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set Mg_error = NULL where designation = '{}'".format(designation_value))

# load MRp

cursor.execute("select designation, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000.0) as MRp from Gaia where phot_rp_mean_mag is not NULL")
value = cursor.fetchall()
for (designation_value, MRp_value) in value:
    cursor.execute("update Gaia_product set MRp = {} where designation = '{}'".format(MRp_value, designation_value))

cursor.execute("select designation from Gaia where phot_rp_mean_mag is NULL")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set MRp = NULL where designation = '{}'".format(designation_value))

# load MRp_error

cursor.execute("select designation, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2 as MRp_error "
               "from Gaia "
               "where phot_rp_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL")
value = cursor.fetchall()
for (designation_value, MRp_error_value) in value:
    cursor.execute("update Gaia_product set MRp_error = {} where designation = '{}'".format(MRp_error_value, designation_value))

cursor.execute("select designation from Gaia "
               "where phot_rp_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set MRp_error = NULL where designation = '{}'".format(designation_value))

# load Bp_minus_Rp

cursor.execute("select designation, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from Gaia "
               "where phot_bp_mean_mag is not NULL and phot_rp_mean_mag is not NULL")
value = cursor.fetchall()
for (designation_value, Bp_minus_Rp_value) in value:
    cursor.execute("update Gaia_product set Bp_minus_Rp = {} where designation = '{}'".format(Bp_minus_Rp_value, designation_value))

cursor.execute("select designation from Gaia "
               "where phot_bp_mean_mag is NULL or phot_rp_mean_mag is NULL")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia set Bp_minus_Rp = NULL where designation = '{}'".format(designation_value))

# Criar a tabela Hipparcos_product no BD



# Make sure data is committed to the database

connection.commit()
cursor.close()
connection.close()








