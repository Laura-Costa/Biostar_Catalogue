# from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astroquery.simbad import Simbad
import csv
import mysql.connector
import matplotlib.pyplot as plt
import decimal

connection = mysql.connector.connect(host='localhost', port='3306', user='helena', password='ic2023IC*')
cursor = connection.cursor()

cursor.execute("drop database if exists gaia_catalogue_1")
cursor.execute("create database gaia_catalogue_1")

connection = mysql.connector.connect(host='localhost', port='3306', database='gaia_catalogue_1', user='helena', password='ic2023IC*', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

# Criar a tabela Hipparcos no BD:

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

# Criar a tabela Hipparcos_completo no BD:

cursor.execute("create table Hipparcos_completo("
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

# Criar tabela onze_estrelas no BD

cursor.execute("create table onze_estrelas("
               "HIP INT primary key, "
               "designation CHAR(100) null )")

# Carregar os dados da tabela Hipparcos_completo:

with open("HIP_MAIN.DAT") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) != 0:
            line = line[0].split("|")
            #if len(line[11].strip()) != 0:
            HIP_value = line[1].strip()
            if len(HIP_value) == 0:
                cursor.execute("insert into Hipparcos_completo(HIP) values(NULL)")
            else:
                cursor.execute("insert into Hipparcos_completo(HIP) values({})".format(int(HIP_value)))

            HD_value = line[71].strip()
            if len(HD_value) == 0:
                cursor.execute("update Hipparcos_completo set HD = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set HD = {} where HIP = {}".format(HD_value, int(HIP_value)))

            Vmag_value = line[5].strip()
            if len(Vmag_value) == 0:
                cursor.execute("update Hipparcos_completo set Vmag = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set Vmag = {} where HIP = {}".format(float(Vmag_value), int(HIP_value)))

            RAdeg_value = line[8].strip()
            if len(RAdeg_value) == 0:
                cursor.execute("update Hipparcos_completo set RAdeg = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set RAdeg = {} where HIP = {}".format(float(RAdeg_value), int(HIP_value)))

            DEdeg_value = line[9].strip()
            if len(DEdeg_value) == 0:
                cursor.execute("update Hipparcos_completo set DEdeg = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set DEdeg = {} where HIP = {}".format(float(DEdeg_value), int(HIP_value)))

            RAhms_value = line[3].strip()
            if len(RAhms_value) == 0:
                cursor.execute("update Hipparcos_completo set RAhms = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set RAhms = '{}' where HIP = {}".format(RAhms_value, int(HIP_value)))

            DEdms_value = line[4].strip()
            if len(DEdms_value) == 0:
                cursor.execute("update Hipparcos_completo set DEdms = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set DEdms = '{}' where HIP = {}".format(DEdms_value, int(HIP_value)))

            Plx_value = line[11].strip()
            if len(Plx_value) == 0:
                cursor.execute("update Hipparcos_completo set Plx = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set Plx = {} where HIP = {}".format(float(Plx_value), int(HIP_value)))

            e_Plx_value = line[16].strip()
            if len(e_Plx_value) == 0:
                cursor.execute("update Hipparcos_completo set e_Plx = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set e_Plx = {} where HIP = {}".format(float(e_Plx_value), int(HIP_value)))

            pmRA_value = line[12].strip()
            if len(pmRA_value) == 0:
                cursor.execute("update Hipparcos_completo set pmRA = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set pmRA = {} where HIP = {}".format(float(pmRA_value), int(HIP_value)))

            pmDE_value = line[13].strip()
            if len(pmDE_value) == 0:
                cursor.execute("update Hipparcos_completo set pmDE = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set pmDE = {} where HIP = {}".format(float(pmDE_value), int(HIP_value)))

            BTmag_value = line[32].strip()
            if len(BTmag_value) == 0:
                cursor.execute("update Hipparcos_completo set BTmag = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set BTmag = {} where HIP = {}".format(float(BTmag_value), int(HIP_value)))

            VTmag_value = line[34].strip()
            if len(VTmag_value) == 0:
                cursor.execute("update Hipparcos_completo set VTmag = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set VTmag = {} where HIP = {}".format(float(VTmag_value), int(HIP_value)))

            B_V_value = line[37].strip()
            if len(B_V_value) == 0:
                cursor.execute("update Hipparcos_completo set B_V = NULL where HIP = {}".format(int(HIP_value)))
            else:
                cursor.execute("update Hipparcos_completo set B_V = {} where HIP = {}".format(float(B_V_value), int(HIP_value)))
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
                cursor.execute("update Gaia set HIP = {} where designation = '{}' and {} in"
                               "(select HIP from Hipparcos)".format(int(HIP_value), designation_value, int(HIP_value)))

                # Gerar um arquivo com os HIPs novos na intersecao entre Gaia e Hipparcos
                # Ou seja, o Gaia 'correspondeu' com HIPs que não estao na selecao atual do Hipparcos

                if (int(HIP_value),) not in HIPs_in_Hipparcos:
                    csv_writer.writerow([int(HIP_value), designation_value, HD_value])
                    cursor.execute("insert into onze_estrelas(HIP) values({})".format(int(HIP_value)))
                    cursor.execute("update onze_estrelas set designation = '{}' where HIP = {}".format(designation_value, int(HIP_value)))

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

cursor.execute("select designation, phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as Mg "
               "from Gaia "
               "where phot_g_mean_mag is not NULL and "
               "parallax > 0")
value = cursor.fetchall()
for (designation_value, Mg_value) in value:
    cursor.execute("update Gaia_product set Mg = {} where designation = '{}'".format(Mg_value, designation_value))

cursor.execute("select designation from Gaia "
               "where phot_g_mean_mag is NULL or "
               "parallax <= 0")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set Mg = NULL where designation = '{}'".format(designation_value))

# load Mg_error

cursor.execute("select designation, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2.0 as Mg_error "
               "from Gaia "
               "where phot_g_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL and "
               "parallax > 0 and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0")
value = cursor.fetchall()
for (designation_value, Mg_error_value) in value:
    cursor.execute("update Gaia_product set Mg_error = {} where designation = '{}'".format(Mg_error_value, designation_value))

cursor.execute("select designation "
               "from Gaia "
               "where phot_g_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL or "
               "parallax <= 0 or "
               "parallax + parallax_error <= 0 or "
               "parallax - parallax_error <= 0")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set Mg_error = NULL where designation = '{}'".format(designation_value))

# load MRp

cursor.execute("select designation, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000.0) as MRp "
               "from Gaia "
               "where phot_rp_mean_mag is not NULL and "
               "parallax > 0")
value = cursor.fetchall()
for (designation_value, MRp_value) in value:
    cursor.execute("update Gaia_product set MRp = {} where designation = '{}'".format(MRp_value, designation_value))

cursor.execute("select designation "
               "from Gaia "
               "where phot_rp_mean_mag is NULL or "
               "parallax <= 0")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set MRp = NULL where designation = '{}'".format(designation_value))

# load MRp_error

cursor.execute("select designation, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2.0 as MRp_error "
               "from Gaia "
               "where phot_rp_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL and "
               "parallax > 0 and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0")
value = cursor.fetchall()
for (designation_value, MRp_error_value) in value:
    cursor.execute("update Gaia_product set MRp_error = {} where designation = '{}'".format(MRp_error_value, designation_value))

cursor.execute("select designation from Gaia "
               "where phot_rp_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL or "
               "parallax <= 0 or "
               "parallax + parallax_error <= 0 or "
               "parallax - parallax_error <= 0")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia_product set MRp_error = NULL where designation = '{}'".format(designation_value))

# load Bp_minus_Rp

cursor.execute("select designation, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from Gaia "
               "where phot_bp_mean_mag is not NULL and phot_rp_mean_mag is not NULL")
value = cursor.fetchall()
for (designation_value, Bp_minus_Rp_value) in value:
    cursor.execute("update Gaia_product set Bp_minus_Rp = {} where designation = '{}'".format(Bp_minus_Rp_value, designation_value))

cursor.execute("select designation "
               "from Gaia "
               "where phot_bp_mean_mag is NULL or "
               "phot_rp_mean_mag is NULL")
value = cursor.fetchall()
for (designation_value) in value:
    cursor.execute("update Gaia set Bp_minus_Rp = NULL where designation = '{}'".format(designation_value))

# Criar a tabela Hipparcos_product no BD

cursor.execute("create table Hipparcos_product( "
               "HIP INT primary key, "
               "MV NUMERIC(65,30) null, "
               "MV_error NUMERIC(65,30) null, "
               "MVt NUMERIC(65,30) null, "
               "MVt_error NUMERIC(65,30) null, "
               "B_minus_V NUMERIC(65,30) null, "
               "BT_minus_VT NUMERIC(65,30) null, "
               "foreign key (HIP) references Hipparcos(HIP) on delete restrict)")

# Carregar dados da tabela Hipparcos_product

# load HIP

cursor.execute("select HIP from Hipparcos")
value = cursor.fetchall()

add_row = ("insert into Hipparcos_product (HIP) values (%(HIP)s)")

for registro in value:
    data_row = {
        'HIP': registro[0]
    }
    cursor.execute(add_row, data_row)

# load MV

cursor.execute("select HIP, Vmag + 5 + 5 * log(10, Plx/1000.0) as MV "
               "from Hipparcos "
               "where Vmag is not NULL and "
               "Plx is not NULL and "
               "Plx > 0")
value = cursor.fetchall()
for (HIP_value, MV_value) in value:
    cursor.execute("update Hipparcos_product set MV = {} where HIP = {}".format(MV_value, HIP_value))

cursor.execute("select HIP "
               "from Hipparcos "
               "where Vmag is NULL or "
               "Plx is NULL or "
               "Plx <= 0")
value = cursor.fetchall()
for (HIP_value) in value:
    cursor.execute("update Hipparcos_product set MV = NULL where HIP = {}".format(HIP_value))

# load MV_error

cursor.execute("select HIP, "
               "("
               "abs((Vmag + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx + e_Plx) / 1000.0))) "
               "+ "
               "abs((Vmag  + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx - e_Plx) / 1000.0))) "
               ") / 2.0 as MV_error "
               "from Hipparcos "
               "where Vmag is not NULL and "
               "Plx is not NULL and "
               "e_Plx is not NULL and "
               "Plx > 0 and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0")
value = cursor.fetchall()
for (HIP_value, MV_error_value) in value:
    cursor.execute("update Hipparcos_product set MV_error = {} where HIP = {}".format(MV_error_value, HIP_value))

cursor.execute("select HIP from Hipparcos "
               "where Vmag is NULL or "
               "Plx is NULL or "
               "e_Plx is NULL or "
               "Plx <= 0 or "
               "Plx + e_Plx <= 0 or "
               "Plx - e_Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update Hipparcos_product set MV_error = NULL where HIP = {}".format(HIP_value))

# load MVt

cursor.execute("select HIP, "
               "VTmag + 5 + 5 * log(10, Plx / 1000.0) as MVt "
               "from Hipparcos "
               "where VTmag is not NULL and "
               "Plx > 0")
value = cursor.fetchall()
for (HIP_value, MVt_value) in value:
    cursor.execute("update Hipparcos_product set MVt = {} where HIP = {}".format(MVt_value, HIP_value))

cursor.execute("select HIP "
               "from Hipparcos "
               "where VTmag is NULL or "
               "Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update Hipparcos_product set MVt = NULL where HIP = {}".format(HIP_value))

# load MVt_error

cursor.execute("select HIP, "
               "( "
               "abs(( VTmag + 5 + 5 * log(10, Plx / 1000.0)) - (VTmag + 5 + 5 * log(10, (Plx + e_Plx) / 1000.0))) "
               "+ "
               "abs(( VTmag + 5 + 5 * log(10, Plx / 1000.0)) - (VTmag + 5 + 5 * log(10, (Plx - e_Plx) / 1000.0))) "
               ") / 2.0 as MVt_error "
               "from Hipparcos "
               "where VTmag is not NULL and "
               "Plx is not NULL and "
               "e_Plx is not NULL and "
               "Plx > 0 and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0")
value = cursor.fetchall()
for (HIP_value, MVt_error_value) in value:
    cursor.execute("update Hipparcos_product set MVt_error = {} where HIP = {}".format(MVt_error_value, HIP_value))

cursor.execute("select HIP from Hipparcos "
               "where VTmag is NULL or "
               "Plx is NULL or "
               "e_Plx is NULL or "
               "Plx <= 0 or "
               "Plx + e_Plx <= 0 or "
               "Plx - e_Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update Hipparcos_product set MVt_error = NULL where HIP = {}".format(HIP_value))

# load B_minus_V

cursor.execute("select HIP, "
               "B_V as B_minus_V "
               "from Hipparcos "
               "where B_V is not NULL")
value = cursor.fetchall()
for (HIP_value, B_minus_V_value) in value:
    cursor.execute("update Hipparcos_product set B_minus_V = {} where HIP = {}".format(B_minus_V_value, HIP_value))

cursor.execute("select HIP "
               "from Hipparcos "
               "where B_V is NULL")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update Hipparcos_product set B_minus_V = NULL where HIP = {}".format(HIP_value))

# load BT_minus_VT

cursor.execute("select HIP, "
               "BTmag - VTmag  as BT_minus_VT "
               "from Hipparcos "
               "where BTmag is not NULL and "
               "VTmag is not NULL")
value = cursor.fetchall()
for (HIP_value, BT_minus_VT_value) in value:
    cursor.execute("update Hipparcos_product set BT_minus_VT = {} where HIP = {}".format(BT_minus_VT_value, HIP_value))

cursor.execute("select HIP "
               "from Hipparcos "
               "where BTmag is NULL or "
               "VTmag is NULL")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update Hipparcos_product set BT_minus_VT = NULL where HIP = {}".format(HIP_value))

# Criar a tabela Gaia_diagram no BD

cursor.execute("create table Gaia_diagram( "
               "name char(100) primary key, "
               "image blob null, "
               "description char(100))")

# Criar a tabela Gaia_product_is_plotted_on no BD

cursor.execute("create table Gaia_product_is_plotted_on( "
               "designation CHAR(100) not null, "
               "name char(100) not null, "
               "primary key (designation, name), "
               "foreign key (designation) references Gaia_product(designation), "
               "foreign key (name) references Gaia_diagram(name))")

# Criar o diagrama Gaia_Mg_versus_Bp_minus_Rp.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Gaia_product.Mg "
               "from Gaia_product, Gaia "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia_product.Mg is not NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp_value, Mg_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia: {} estrelas em um raio de {:.5f}pc (π ≥ {:.5f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.ylabel("M(G)")
plt.xlabel("Bp-Rp")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_Mg_versus_Bp_minus_Rp.png')
# plt.savefig('/var/lib/mysql/Gaia_Mg_versus_Bp_minus_Rp')


# cursor.execute("insert into Gaia_diagram(name, image, description) values ('Gaia_Mg_versus_Bp_minus_Rp', "
#                "load_file('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_Mg_versus_Bp_minus_Rp.png'), "
#                "'Diagrama HR (M(G) vs Bp-Rp) das estrelas Gaia (seleção de 23 parsecs)')")


# Plotar, em deepskyblue, a estrela HD146233

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Gaia_product.Mg "
               "from Gaia_product, Gaia "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia_product.Mg is not NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, Mg_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_Mg_versus_Bp_minus_Rp.png')

# close matplotlib.pyplot object
plt.clf()

######################################################################################################
# DIAGRAMA M(G) vs M(V)

cursor.execute("select Gaia_product.Mg, Gaia.parallax, Hipparcos_product.MV "
               "from Hipparcos_product, Gaia, Gaia_product "
               "where Hipparcos_product.HIP = Gaia.HIP and "
               "Gaia.designation = Gaia_product.designation and "
               "Gaia_product.Mg is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (Mg_value, parallax_value, MV_value) in value:
    parallax_list.append(parallax_value)
    y_axis.append(MV_value)
    x_axis.append(Mg_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(min(y_axis) - decimal.Decimal(0.5), max(y_axis) + decimal.Decimal(0.5))
plt.title("Gaia: {} estrelas em um raio de {:.5f}pc (π ≥ {:.5f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.ylabel("M(G)")
plt.xlabel("M(V)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_Mg_versus_MV.png')

# close matplotlib.pyplot object
plt.clf()

######################################################################################################
# DIAGRAMA phot_g_mean_mag vs Vmag

cursor.execute("select Gaia.phot_g_mean_mag, Gaia.parallax, Hipparcos.Vmag "
               "from Hipparcos, Gaia "
               "where Hipparcos.HIP = Gaia.HIP and "
               "Hipparcos.Vmag is not NULL")
value = cursor.fetchall()

parallax_list = []
x_axis = []
y_axis = []

for (phot_g_mean_mag_value, parallax_value, Vmag_value) in value:
    parallax_list.append(parallax_value)
    y_axis.append(Vmag_value)
    x_axis.append(phot_g_mean_mag_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(min(y_axis) - decimal.Decimal(0.5), max(y_axis) + decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("phot_g_mean_mag")
plt.ylabel("Vmag")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_phot_g_mean_mag_versus_Vmag.png')

# Plotar, em deepskyblue, a estrela HD146233

cursor.execute("select Gaia.phot_g_mean_mag, Hipparcos.Vmag "
               "from Hipparcos, Gaia "
               "where Hipparcos.HIP = Gaia.HIP and "
               "Hipparcos.Vmag is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (phot_g_mean_mag_value, Vmag_value) in value:
    x_axis.append(phot_g_mean_mag_value)
    y_axis.append(Vmag_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='lower right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_phot_g_mean_mag_versus_Vmag.png')

# close matplotlib.pyplot object
plt.clf()
######################################################################################################

# Criar o diagrama Gaia_MRp_versus_Bp_minus_Rp.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Gaia_product.MRp "
               "from Gaia, Gaia_product "
               "where Gaia.designation = Gaia_product.designation and "
               "Gaia_product.MRp is not NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp_value, MRp_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia: {} stars within {:.5f}pc (π ≥ {:.5f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.ylabel("M(Rp)")
plt.xlabel("Bp-Rp")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_MRp_versus_Bp_minus_Rp.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Gaia_product.MRp "
               "from Gaia, Gaia_product "
               "where Gaia.designation = Gaia_product.designation and "
               "Gaia_product.MRp is not NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, MRp_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_MRp_versus_Bp_minus_Rp.png')

# close matplotlib.pyplot object
plt.clf()

# Criar o diagrama Gaia_intersection_Hipparcos_Mg_versus_Bp_minus_Rp.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Gaia_product.Mg "
               "from Gaia_product, Gaia, Hipparcos "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos.HIP and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.Mg is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp_value, Mg_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(G)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_Mg_versus_Bp_minus_Rp.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Gaia_product.Mg "
               "from Gaia_product, Gaia, Hipparcos "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos.HIP and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.Mg is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, Mg_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_Mg_versus_Bp_minus_Rp.png')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama Gaia_intersection_Hipparcos_MRp_versus_Bp_minus_Rp.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Gaia_product.MRp "
               "from Gaia_product, Gaia, Hipparcos "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos.HIP and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.Mg is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp_value, MRp_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(Rp)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MRp_versus_Bp_minus_Rp.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Gaia_product.MRp "
               "from Gaia_product, Gaia, Hipparcos "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos.HIP and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.Mg is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, MRp_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MRp_versus_Bp_minus_Rp.png')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama Gaia_intersection_Hipparcos_MRp_versus_MVt.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.MRp, "
               "Hipparcos_product.MVt "
               "from Gaia_product, Gaia, Hipparcos_product "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos_product.HIP and "
               "Gaia_product.MRp is not NULL and "
               "Hipparcos_product.MVt is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, MRp_value, MVt_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(MRp_value)
    y_axis.append(MVt_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("M(Rp)")
plt.ylabel("M(Vt)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MRp_versus_MVt.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Gaia_product.MRp, "
               "Hipparcos_product.MVt "
               "from Gaia_product, Gaia, Hipparcos_product "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos_product.HIP and "
               "Gaia_product.MRp is not NULL and "
               "Hipparcos_product.MVt is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (MRp_value, MVt_value) in value:
    x_axis.append(MRp_value)
    y_axis.append(MVt_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MRp_versus_MVt.png')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama Gaia_intersection_Hipparcos_Bp_minus_Rp_versus_BT_minus_VT.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Hipparcos_product.BT_minus_VT "
               "from Gaia_product, Gaia, Hipparcos_product "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos_product.HIP and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Hipparcos_product.BT_minus_VT is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp, BT_minus_VT) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp)
    y_axis.append(BT_minus_VT)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp-Rp")
plt.ylabel("Bt-Vt")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_Bp_minus_Rp_versus_BT_minus_VT.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Hipparcos_product.BT_minus_VT "
               "from Gaia_product, Gaia, Hipparcos_product "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP = Hipparcos_product.HIP and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Hipparcos_product.BT_minus_VT is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp, BT_minus_VT) in value:
    x_axis.append(Bp_minus_Rp)
    y_axis.append(BT_minus_VT)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_Bp_minus_Rp_versus_BT_minus_VT.png')

# close matplotlib.pyplot object
plt.close()

# Criar o diagrama Gaia_minus_Hipparcos_Mg_versus_Bp_minus_Rp.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Gaia_product.Mg "
               "from Gaia_product, Gaia "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP is NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.Mg is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp_value, Mg_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5

plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia - Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("M(G)")
plt.ylabel("Bp - Rp")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_minus_Hipparcos_Mg_versus_Bp_minus_Rp.png')

# Plotar, em tomato, a estrela 131156B

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Gaia_product.Mg "
               "from Gaia_product, Gaia "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP is NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.Mg is not NULL and "
               "Gaia.HD = '131156B'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, Mg_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(Mg_value)

tomato = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'tomato', alpha = transparency)

plt.legend((tomato,),
           ('HD 131156B',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_minus_Hipparcos_Mg_versus_Bp_minus_Rp.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Gaia_minus_Hipparcos_MRp_versus_Bp_minus_Rp.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Gaia_product.designation, "
               "Gaia.parallax, "
               "Gaia_product.Bp_minus_Rp, "
               "Gaia_product.MRp "
               "from Gaia_product, Gaia "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP is NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.MRp is not NULL")
value = cursor.fetchall()

designation_list = []
parallax_list = []
x_axis = []
y_axis = []

for (designation_value, parallax_value, Bp_minus_Rp_value, MRp_value) in value:
    designation_list.append(designation_value)
    parallax_list.append(parallax_value)
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia - Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("Bp - Rp")
plt.ylabel("M(Rp)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_minus_Hipparcos_MRp_versus_Bp_minus_Rp.png')

# Plotar, em tomato, a estrela 131156B

cursor.execute("select Gaia_product.Bp_minus_Rp, "
               "Gaia_product.MRp "
               "from Gaia_product, Gaia "
               "where Gaia_product.designation = Gaia.designation and "
               "Gaia.HIP is NULL and "
               "Gaia_product.Bp_minus_Rp is not NULL and "
               "Gaia_product.MRp is not NULL and "
               "Gaia.HD = '131156B'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (Bp_minus_Rp_value, MRp_value) in value:
    x_axis.append(Bp_minus_Rp_value)
    y_axis.append(MRp_value)

tomato = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'tomato', alpha = transparency)

plt.legend((tomato,),
           ('HD 131156B',),
           scatterpoints=1,
           loc='lower left',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_minus_Hipparcos_MRp_versus_Bp_minus_Rp.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_MV_versus_B_minus_V.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Hipparcos_MV_versus_B_minus_V.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL and "
               "Hipparcos.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (B_minus_V_value, MV_value) in value:
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Hipparcos_MV_versus_B_minus_V.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_MVt_versus_BT_minus_VT.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.BT_minus_VT, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.BT_minus_VT is not NULL and "
               "Hipparcos_product.MVt is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, BT_minus_VT_value, MVt_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha =  transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("BT - VT")
plt.ylabel("M(Vt)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Hipparcos_MVt_versus_BT_minus_VT.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Hipparcos_product.BT_minus_VT, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.BT_minus_VT is not NULL and "
               "Hipparcos_product.MVt is not NULL and "
               "Hipparcos.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (BT_minus_VT_value, MVt_value) in value:
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha =  transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Hipparcos_MVt_versus_BT_minus_VT.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Gaia_intersection_Hipparcos_MV_versus_B_minus_V.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Gaia.parallax, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Gaia "
               "where Hipparcos_product.HIP = Gaia.HIP and "
               "Hipparcos_product.MV is not NULL and "
               "Hipparcos_product.B_minus_V is not NULL")
value = cursor.fetchall()

HIP_list = []
parallax_list = []
x_axis = []
y_axis = []

for (HIP_value, parallax_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    parallax_list.append(parallax_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MV_versus_B_minus_V.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Gaia "
               "where Hipparcos_product.HIP = Gaia.HIP and "
               "Hipparcos_product.MV is not NULL and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (B_minus_V_value, MV_value) in value:
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MV_versus_B_minus_V.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Gaia.parallax, "
               "Hipparcos_product.BT_minus_VT, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Gaia "
               "where Hipparcos_product.HIP = Gaia.HIP and "
               "Hipparcos_product.BT_minus_VT is not NULL and "
               "Hipparcos_product.MVt is not NULL")
value = cursor.fetchall()

HIP_list = []
parallax_list = []
x_axis = []
y_axis = []

for (HIP_value, parallax_value, BT_minus_VT_value, MVt_value) in value:
    HIP_list.append(HIP_value)
    parallax_list.append(parallax_value)
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

min_parallax = min(parallax_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Gaia ∩ Hipparcos: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_parallax / decimal.Decimal(1000.0)), min_parallax / decimal.Decimal(1000.0)))
plt.xlabel("BT - VT")
plt.ylabel("M(Vt)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT.png')

# Plotar, em deepskyblue, a estrela HD 146233

cursor.execute("select Hipparcos_product.BT_minus_VT, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Gaia "
               "where Hipparcos_product.HIP = Gaia.HIP and "
               "Hipparcos_product.BT_minus_VT is not NULL and "
               "Hipparcos_product.MVt is not NULL and "
               "Gaia.HD = '146233'")
value = cursor.fetchall()

x_axis = []
y_axis = []

for (BT_minus_VT_value, MVt_value) in value:
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

deepskyblue = plt.scatter(x_axis, y_axis, s = size, marker = "s", edgecolors = 'deepskyblue', alpha = transparency)

plt.legend((deepskyblue,),
           ('HD 146233',),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)

plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_minus_Gaia_MV_versus_B_minus_V_edited.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.B_minus_V, "
               "Hipparcos_product.MV "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.B_minus_V is not NULL and "
               "Hipparcos_product.MV is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, B_minus_V_value, MV_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(B_minus_V_value)
    y_axis.append(MV_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("B - V")
plt.ylabel("M(V)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject2/static/img/Hipparcos_minus_Gaia_MV_versus_B_minus_V_edited.png')

# close matplotlib.pyplot as plt object
plt.close()

# Criar o diagrama Hipparcos_minus_Gaia_MVt_versus_BT_minus_VT.png numa pasta do computador (NÃO conseguiu ainda salvar no BD)

cursor.execute("select Hipparcos_product.HIP, "
               "Hipparcos.Plx, "
               "Hipparcos_product.BT_minus_VT, "
               "Hipparcos_product.MVt "
               "from Hipparcos_product, Hipparcos "
               "where Hipparcos_product.HIP = Hipparcos.HIP and "
               "Hipparcos_product.HIP not in ( "
               "select Gaia.HIP from Gaia where Gaia.HIP is not NULL) and "
               "Hipparcos_product.BT_minus_VT is not NULL and "
               "Hipparcos_product.MVt is not NULL")
value = cursor.fetchall()

HIP_list = []
Plx_list = []
x_axis = []
y_axis = []

for (HIP_value, Plx_value, BT_minus_VT_value, MVt_value) in value:
    HIP_list.append(HIP_value)
    Plx_list.append(Plx_value)
    x_axis.append(BT_minus_VT_value)
    y_axis.append(MVt_value)

min_Plx = min(Plx_list)

transparency = 1
size = 1.5
plt.scatter(x_axis, y_axis, s = size, marker = ".", edgecolors = 'black', alpha = transparency)
plt.xlim(min(x_axis) - decimal.Decimal(0.2), max(x_axis) + decimal.Decimal(0.2))
plt.ylim(max(y_axis) + decimal.Decimal(0.5), min(y_axis) - decimal.Decimal(0.5))
plt.title("Hipparcos - Gaia: {} estrelas em um raio de {:.4f}pc (π ≥ {:.4f}'')".format(len(value), decimal.Decimal(1.0) / (min_Plx / decimal.Decimal(1000.0)), min_Plx / decimal.Decimal(1000.0)))
plt.xlabel("BT - VT")
plt.ylabel("M(Vt)")
plt.savefig('/home/h/Área de trabalho/Catalogo_GAIA/pythonProject1/static/img/Hipparcos_minus_Gaia_MVt_versus_BT_minus_VT.png')

# close matplotlib.pyplot as plt object
plt.close()

# Make sure data is committed to the database
connection.commit()

'''
 Criando um arquivo do tipo CSV para cada tabela da aplicação web
'''

# Criando o arquivo Gaia.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HIP, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0 '''
               '''from Gaia, Gaia_product '''
               '''where Gaia.designation = Gaia_product.designation '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Hipparcos_MV_versus_B_minus_V_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL '''
               '''order by Hipparcos.HIP '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_MV_versus_B_minus_V_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Hipparcos_MV_versus_B_minus_V_not_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''(Hipparcos_product.MV is NULL or '''
               '''Hipparcos_product.B_minus_V is NULL) '''
               '''order by Hipparcos.HIP '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_MV_versus_B_minus_V_not_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Hipparcos_MVt_versus_BT_minus_VT_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MVt is not NULL and '''
               '''Hipparcos_product.BT_minus_VT is not NULL '''
               '''order by Hipparcos.HIP '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_MVt_versus_BT_minus_VT_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Hipparcos_MVt_versus_BT_minus_VT_not_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''(Hipparcos_product.MVt is NULL or '''
               '''Hipparcos_product.BT_minus_VT is NULL) '''
               '''order by Hipparcos.HIP '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_MVt_versus_BT_minus_VT_not_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Gaia_intersection_Hipparcos_Mg_or_MRp_versus_Bp_minus_Rp.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HIP, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Gaia, Gaia_product, Hipparcos, Hipparcos_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP = Hipparcos.HIP and Hipparcos.HIP = Hipparcos_product.HIP '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_intersection_Hipparcos_Mg_or_MRp_versus_Bp_minus_Rp_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HIP, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Gaia, Gaia_product, Hipparcos, Hipparcos_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP = Hipparcos.HIP and Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_intersection_Hipparcos_MV_versus_B_minus_V_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Gaia_intersection_Hipparcos_MV_versus_B_minus_V_not_plotted.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HIP, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Gaia, Gaia_product, Hipparcos, Hipparcos_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP = Hipparcos.HIP and Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''(Hipparcos_product.MV is NULL or '''
               '''Hipparcos_product.B_minus_V is NULL) '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_intersection_Hipparcos_MV_versus_B_minus_V_not_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT_plotted.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HIP, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Gaia, Gaia_product, Hipparcos, Hipparcos_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP = Hipparcos.HIP and Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MVt is not NULL and '''
               '''Hipparcos_product.BT_minus_VT is not NULL '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT_not_plotted.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HIP, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Gaia, Gaia_product, Hipparcos, Hipparcos_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP = Hipparcos.HIP and Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''(Hipparcos_product.MVt is NULL or '''
               '''Hipparcos_product.BT_minus_VT is NULL) '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_intersection_Hipparcos_MVt_versus_BT_minus_VT_not_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Gaia_minus_Hipparcos_Mg_or_MRp_versus_Bp_minus_Rp.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HD, '''
               '''Gaia.HIP, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0 '''
               '''from Gaia, Gaia_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP is NULL '''
               '''order by Gaia.designation '''
               '''into outfile '/var/lib/mysql-files/Gaia_minus_Hipparcos_Mg_or_MRp_versus_Bp_minus_Rp_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo Gaia_minus_Hipparcos_Bp_minus_Rp_less_than_or_iqual_to_1.6.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HD, '''
               '''Gaia.HIP, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0 '''
               '''from Gaia, Gaia_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP is NULL and '''
               '''Gaia_product.Bp_minus_Rp <= 1.6 '''
               '''order by Gaia_product.Bp_minus_Rp desc '''
               '''into outfile '/var/lib/mysql-files/Gaia_minus_Hipparcos_Bp_minus_Rp_less_than_or_equal_to_1.6_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo Gaia_minus_Hipparcos_Bp_minus_Rp_less_than_or_iqual_to_1.6_redux.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HD, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0 '''
               '''from Gaia, Gaia_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP is NULL and '''
               '''Gaia_product.Bp_minus_Rp <= 1.6 '''
               '''order by Gaia_product.Bp_minus_Rp desc '''
               '''into outfile '/var/lib/mysql-files/Gaia_minus_Hipparcos_Bp_minus_Rp_less_than_or_equal_to_1.6_redux_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criando o arquivo Gaia_minus_Hipparcos_Bp_minus_Rp_greater_than_1.6.csv

cursor.execute('''select Gaia.designation, '''
               '''Gaia.HD, '''
               '''Gaia.HIP, '''
               '''TRIM(Gaia.ra)+0, '''
               '''TRIM(Gaia.declination)+0, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.pm)+0, '''
               '''TRIM(Gaia.pmra)+0, '''
               '''TRIM(Gaia.pmdec)+0, '''
               '''TRIM(Gaia.ruwe)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia.phot_bp_mean_mag)+0, '''
               '''TRIM(Gaia.phot_rp_mean_mag)+0, '''
               '''TRIM(Gaia.teff_gspphot)+0, '''
               '''TRIM(Gaia.teff_gspphot_lower)+0, '''
               '''TRIM(Gaia.teff_gspphot_upper)+0, '''
               '''TRIM(Gaia.logg_gspphot)+0, '''
               '''TRIM(Gaia.logg_gspphot_lower)+0, '''
               '''TRIM(Gaia.logg_gspphot_upper)+0, '''
               '''TRIM(Gaia.mh_gspphot)+0, '''
               '''TRIM(Gaia.mh_gspphot_lower)+0, '''
               '''TRIM(Gaia.mh_gspphot_upper)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.distance_gspphot_lower)+0, '''
               '''TRIM(Gaia.distance_gspphot_upper)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Gaia_product.Mg_error)+0, '''
               '''TRIM(Gaia_product.MRp)+0, '''
               '''TRIM(Gaia_product.MRp_error)+0, '''
               '''TRIM(Gaia_product.Bp_minus_Rp)+0 '''
               '''from Gaia, Gaia_product '''
               '''where Gaia.designation = Gaia_product.designation and '''
               '''Gaia.HIP is NULL and '''
               '''Gaia_product.Bp_minus_Rp > 1.6 '''
               '''order by Gaia_product.Bp_minus_Rp '''
               '''into outfile '/var/lib/mysql-files/Gaia_minus_Hipparcos_Bp_minus_Rp_greater_than_1.6_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MV is not NULL and '''
               '''Hipparcos_product.B_minus_V is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo Hipparcos_minus_Gaia_MV_versus_B_minus_V_not_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''(Hipparcos_product.MV is NULL or '''
               '''Hipparcos_product.B_minus_V is NULL) and '''
               '''Hipparcos.HIP not in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MV_versus_B_minus_V_not_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o diagrama Hipparcos_minus_Gaia_MVt_versus_BT_minus_VT_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos_product.MVt is not NULL and '''
               '''Hipparcos_product.BT_minus_VT is not NULL and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MVt_versus_BT_minus_VT_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo Hipparcos_minus_Gaia_MVt_versus_BT_minus_VT_not_plotted.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''IF (Hipparcos.HIP in ( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL), '''
               '''(select Gaia.designation from Gaia where Gaia.HIP = Hipparcos.HIP), NULL) AS designation, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.pmRA)+0, '''
               '''TRIM(Hipparcos.pmDE)+0, '''
               '''TRIM(Hipparcos.BTmag)+0, '''
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''(Hipparcos_product.MVt is NULL or '''
               '''Hipparcos_product.BT_minus_VT is NULL) and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_minus_Gaia_MVt_versus_BT_minus_VT_not_plotted_temp.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo catalogo5.csv

cursor.execute('''select Hipparcos.HIP, '''
               '''Hipparcos.HD, '''
               '''TRIM(Hipparcos.RAdeg)+0, '''
               '''TRIM(Hipparcos.DEdeg)+0, '''
               '''Hipparcos.RAhms, '''
               '''Hipparcos.DEdms, '''
               '''TRIM(Hipparcos.Plx)+0, '''
               '''TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(1/(Hipparcos.Plx/1000.0))+0 AS distance_Plx, '''
               '''TRIM(Hipparcos.Vmag)+0, '''
               '''TRIM(Hipparcos_product.MV)+0, '''
               '''TRIM(Hipparcos_product.MV_error)+0, '''               
               '''TRIM(Hipparcos.VTmag)+0, '''
               '''TRIM(Hipparcos_product.MVt)+0, '''
               '''TRIM(Hipparcos_product.MVt_error)+0, '''               
               '''TRIM(Hipparcos_product.B_minus_V)+0, '''
               '''TRIM(Hipparcos_product.BT_minus_VT)+0 '''
               '''from Hipparcos, Hipparcos_product '''
               '''where Hipparcos.HIP = Hipparcos_product.HIP and '''
               '''Hipparcos.HIP not in( '''
               '''select Gaia.HIP from Gaia where Gaia.HIP is not NULL) '''
               '''order by distance_Plx DESC '''
               '''into outfile '/var/lib/mysql-files/catalogo5.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

# Criar o arquivo onze_estrelas.csv

cursor.execute('''select onze_estrelas.HIP, '''
               '''Gaia.HD, '''
               '''Gaia.designation, '''
               '''TRIM(Gaia.parallax)+0, '''
               '''TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.distance_gspphot)+0, '''
               '''TRIM(Gaia.phot_g_mean_mag)+0, '''
               '''TRIM(Gaia_product.Mg)+0, '''
               '''TRIM(Hipparcos_completo.Plx)+0, '''
               '''TRIM(Hipparcos_completo.e_Plx)+0, '''
               '''TRIM(1 / (Hipparcos_completo.Plx / 1000.0))+0, '''
               '''TRIM(Hipparcos_completo.Vmag)+0, '''               
               '''TRIM(Hipparcos_completo.Vmag + 5.0 + 5.0 * log(10, Hipparcos_completo.Plx / 1000.0))+0, '''
               '''TRIM(Hipparcos_completo.B_V)+0 '''
               '''from onze_estrelas, Gaia, Gaia_product, Hipparcos_completo '''               
               '''where onze_estrelas.designation = Gaia.designation and '''
               '''Gaia.designation = Gaia_product.designation and '''
               '''onze_estrelas.HIP = Hipparcos_completo.HIP '''
               '''into outfile '/var/lib/mysql-files/onze_estrelas.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

cursor.execute("drop table onze_estrelas")
cursor.execute("drop table Hipparcos_completo")

cursor.close()
connection.close()