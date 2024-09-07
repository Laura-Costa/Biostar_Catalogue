from astroquery.simbad import Simbad
import csv
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', user='lh', password='ic2023')
cursor = connection.cursor()

cursor.execute("drop database if exists biostar_catalogue")
cursor.execute("create database biostar_catalogue")

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

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

with open("create_populate_database/HIP_MAIN.DAT") as tsv:
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

# Criar a tabela Hipparcos_completo no BD:

cursor.execute("create table Hipparcos_completo("
               "HIP CHAR(100) primary key,"
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

# Carregar os dados da tabela Hipparcos_completo:

with open("create_populate_database/HIP_MAIN.DAT") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) != 0:
            line = line[0].split("|")

            HIP_value = "HIP " + line[1].strip()
            if len(HIP_value) == 0:
                cursor.execute("insert into Hipparcos_completo(HIP) values(NULL)")
            else:
                cursor.execute("insert into Hipparcos_completo(HIP) values('{}')".format(HIP_value))

            HD_value = line[71].strip()
            if len(HD_value) == 0:
                cursor.execute("update Hipparcos_completo set HD = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set HD = {} where HIP = '{}'".format(HD_value, HIP_value))

            Vmag_value = line[5].strip()
            if len(Vmag_value) == 0:
                cursor.execute("update Hipparcos_completo set Vmag = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set Vmag = {} where HIP = '{}'".format(float(Vmag_value), HIP_value))

            RAdeg_value = line[8].strip()
            if len(RAdeg_value) == 0:
                cursor.execute("update Hipparcos_completo set RAdeg = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set RAdeg = {} where HIP = '{}'".format(float(RAdeg_value), HIP_value))

            DEdeg_value = line[9].strip()
            if len(DEdeg_value) == 0:
                cursor.execute("update Hipparcos_completo set DEdeg = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set DEdeg = {} where HIP = '{}'".format(float(DEdeg_value), HIP_value))

            RAhms_value = line[3].strip()
            if len(RAhms_value) == 0:
                cursor.execute("update Hipparcos_completo set RAhms = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set RAhms = '{}' where HIP = '{}'".format(RAhms_value, HIP_value))

            DEdms_value = line[4].strip()
            if len(DEdms_value) == 0:
                cursor.execute("update Hipparcos_completo set DEdms = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set DEdms = '{}' where HIP = '{}'".format(DEdms_value, HIP_value))

            Plx_value = line[11].strip()
            if len(Plx_value) == 0:
                cursor.execute("update Hipparcos_completo set Plx = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set Plx = {} where HIP = '{}'".format(float(Plx_value), HIP_value))

            e_Plx_value = line[16].strip()
            if len(e_Plx_value) == 0:
                cursor.execute("update Hipparcos_completo set e_Plx = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set e_Plx = {} where HIP = '{}'".format(float(e_Plx_value), HIP_value))

            pmRA_value = line[12].strip()
            if len(pmRA_value) == 0:
                cursor.execute("update Hipparcos_completo set pmRA = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set pmRA = {} where HIP = '{}'".format(float(pmRA_value), HIP_value))

            pmDE_value = line[13].strip()
            if len(pmDE_value) == 0:
                cursor.execute("update Hipparcos_completo set pmDE = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set pmDE = {} where HIP = '{}'".format(float(pmDE_value), HIP_value))

            BTmag_value = line[32].strip()
            if len(BTmag_value) == 0:
                cursor.execute("update Hipparcos_completo set BTmag = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set BTmag = {} where HIP = '{}'".format(float(BTmag_value), HIP_value))

            VTmag_value = line[34].strip()
            if len(VTmag_value) == 0:
                cursor.execute("update Hipparcos_completo set VTmag = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set VTmag = {} where HIP = '{}'".format(float(VTmag_value), HIP_value))

            B_V_value = line[37].strip()
            if len(B_V_value) == 0:
                cursor.execute("update Hipparcos_completo set B_V = NULL where HIP = '{}'".format(HIP_value))
            else:
                cursor.execute("update Hipparcos_completo set B_V = {} where HIP = '{}'".format(float(B_V_value), HIP_value))
tsv.close()

# Make sure data is committed to the database
connection.commit()

# Criar a tabela CAT1 no BD

cursor.execute("create table CAT1("
               "designation CHAR(100) primary key,"
               "HIP CHAR(100) null,"
               "HD CHAR(100) null,"
               "ra float null,"
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
               "foreign key (HIP) references CAT2(HIP) on delete restrict)")

# Criar tabela CAT1_intersec_HIP_not_in_CAT2 no BD
# Esta tabela armazena as estrelas ADICIONAIS resultantes da
# intersecao do CAT1 com o Hipparcos completo

cursor.execute("create table CAT1_intersec_HIP_not_in_CAT2("
               "designation CHAR(100) primary key, "
               "HIP CHAR(100) null, "
               "HD CHAR(100) null )")

# Criar tabela CAT1_not_in_Simbad no BD
# Esta tabela armazena as estrelas que estão no CAT1
# mas nao estao no Simbad

cursor.execute("create table CAT1_not_in_Simbad("
               "designation CHAR(100) primary key)")

# Carregar dados da tabela CAT1

cursor.execute("select HIP from CAT2")
HIPs_in_CAT2 = cursor.fetchall()

with open("create_populate_database/Gaia_archive_CAT1.csv", 'r') as csv_file:
    next(csv_file)

    for line in csv_file:
        line = line.split(",")

        # load designation

        designation_value = line[0].strip()
        if len(designation_value) == 0:
            cursor.execute("insert into CAT1(designation) values(NULL)")
        else:
            cursor.execute("insert into CAT1(designation) values('{}')".format(designation_value))

        # Verificar se no Simbad existe um HD correspondente a designation
        # Se houver, carregar no BD. Senao, colocar NULL.

        tab = Simbad.query_objectids(designation_value)

        # Algumas estrelas do Gaia_archive_CAT1.csv não possuem nenhum ID no Simbad
        # Estas sao armazenadas na tabela CAT1_not_in_Simbad
        if tab is None:
            cursor.execute("insert into CAT1_not_in_Simbad(designation) values('{}')".format(designation_value))

        if tab is None or len([id for id in tab['ID'] if id.startswith('HD')]) == 0:
            cursor.execute("update CAT1 set HD = NULL where designation = '{}'".format(designation_value))
        else:
            HD_value = [id for id in tab['ID'] if id.startswith('HD')][0][2:].strip()
            cursor.execute("update CAT1 set HD = '{}' where designation = '{}'".format(HD_value, designation_value))

        # Verificar se no Simbad existe um HIP correspondente a designation
        # Se houver, carregar no BD. Senao, colocar NULL.
        # OBS: o HIP correspondente só é carregado se ele já estiver na tabela CAT2 (25.64 pc, 39.0 mas)

        if tab is None or len([id for id in tab['ID'] if id.startswith('HIP')]) == 0:
            cursor.execute("update CAT1 set HIP = NULL where designation = '{}'".format(designation_value))
        else:
            HIP_value = [id for id in tab['ID'] if id.startswith('HIP')][0][:].strip()
            cursor.execute("update CAT1 set HIP = '{}' where designation = '{}' AND '{}' in"
                           "(select HIP from CAT2)".format(HIP_value, designation_value, HIP_value))

            # Gerar um arquivo com os HIPs que não estão na interseção entre CAT1 e CAT2, mas
            # estao na intersecao entre o CAT1 e o hipparcos completo
            # Ou seja, o CAT1 'correspondeu' com HIPs que não estao no CAT2

            if (HIP_value,) not in HIPs_in_CAT2:
                cursor.execute("insert into CAT1_intersec_HIP_not_in_CAT2(designation) values('{}')".format(designation_value))
                cursor.execute("update CAT1_intersec_HIP_not_in_CAT2 set HIP = '{}' where designation = '{}'".format(HIP_value, designation_value))
                cursor.execute("update CAT1_intersec_HIP_not_in_CAT2 set HD = '{}' where designation = '{}'".format(HD_value, designation_value))

        # load ra

        ra_value = line[1].strip()
        if len(ra_value) == 0:
            cursor.execute("update CAT1 set ra = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set ra = {} where designation = '{}'".format(float(ra_value), designation_value))

        # load declination

        declination_value = line[2].strip()
        if len(declination_value) == 0:
            cursor.execute("update CAT1 set declination = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set declination = {} where designation = '{}'".format(float(declination_value), designation_value))

        # load parallax

        parallax_value = line[3].strip()
        if len(parallax_value) == 0:
            cursor.execute("update CAT1 set parallax = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set parallax = {} where designation = '{}'".format(float(parallax_value), designation_value))

        # load parallax_error

        parallax_error_value = line[4].strip()
        if len(parallax_error_value) == 0:
            cursor.execute("update CAT1 set parallax_error = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set parallax_error = {} where designation = '{}'".format(float(parallax_error_value), designation_value))

        # load pm

        pm_value = line[5].strip()
        if len(pm_value) == 0:
            cursor.execute("update CAT1 set pm = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set pm = {} where designation = '{}'".format(float(pm_value), designation_value))

        # load pmra

        pmra_value = line[6].strip()
        if len(pmra_value) == 0:
            cursor.execute("update CAT1 set pmra = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set pmra = {} where designation = '{}'".format(float(pmra_value), designation_value))

        # load pmdec

        pmdec_value = line[7].strip()
        if len(pmdec_value) == 0:
            cursor.execute("update CAT1 set pmdec = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set pmdec = {} where designation = '{}'".format(float(pmdec_value), designation_value))

        # load ruwe

        ruwe_value = line[8].strip()
        if len(ruwe_value) == 0:
            cursor.execute("update CAT1 set ruwe = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set ruwe = {} where designation = '{}'".format(float(ruwe_value), designation_value))

        # load phot_g_mean_mag

        phot_g_mean_mag_value = line[9].strip()
        if len(phot_g_mean_mag_value) == 0:
            cursor.execute("update CAT1 set phot_g_mean_mag = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set phot_g_mean_mag = {} where designation = '{}'".format(float(phot_g_mean_mag_value), designation_value))

        # load phot_bp_mean_mag

        phot_bp_mean_mag_value = line[10].strip()
        if len(phot_bp_mean_mag_value) == 0:
            cursor.execute("update CAT1 set phot_bp_mean_mag = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set phot_bp_mean_mag = {} where designation = '{}'".format(float(phot_bp_mean_mag_value), designation_value))

        # load phot_rp_mean_mag

        phot_rp_mean_mag_value = line[11].strip()
        if len(phot_rp_mean_mag_value) == 0:
            cursor.execute("update CAT1 set phot_rp_mean_mag = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set phot_rp_mean_mag = {} where designation = '{}'".format(float(phot_rp_mean_mag_value), designation_value))

        # load teff_gspphot

        teff_gspphot_value = line[12].strip()
        if len(teff_gspphot_value) == 0:
            cursor.execute("update CAT1 set teff_gspphot = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set teff_gspphot = {} where designation = '{}'".format(float(teff_gspphot_value), designation_value))

        # load teff_gspphot_lower

        teff_gspphot_lower_value = line[13].strip()
        if len(teff_gspphot_lower_value) == 0:
            cursor.execute("update CAT1 set teff_gspphot_lower = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set teff_gspphot_lower = {} where designation = '{}'".format(float(teff_gspphot_lower_value), designation_value))

        # load teff_gspphot_upper

        teff_gspphot_upper_value = line[14].strip()
        if len(teff_gspphot_upper_value) == 0:
            cursor.execute("update CAT1 set teff_gspphot_upper = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set teff_gspphot_upper = {} where designation = '{}'".format(float(teff_gspphot_upper_value), designation_value))

        # load logg_gspphot

        logg_gspphot_value = line[15].strip()
        if len(logg_gspphot_value) == 0:
            cursor.execute("update CAT1 set logg_gspphot = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set logg_gspphot = {} where designation = '{}'".format(float(logg_gspphot_value), designation_value))

        # load logg_gspphot_lower

        logg_gspphot_lower_value = line[16].strip()
        if len(logg_gspphot_lower_value) == 0:
            cursor.execute("update CAT1 set logg_gspphot_lower = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set logg_gspphot_lower = {} where designation = '{}'".format(float(logg_gspphot_lower_value), designation_value))

        # load logg_gspphot_upper

        logg_gspphot_upper_value = line[17].strip()
        if len(logg_gspphot_upper_value) == 0:
            cursor.execute("update CAT1 set logg_gspphot_upper = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set logg_gspphot_upper = {} where designation = '{}'".format(float(logg_gspphot_upper_value), designation_value))

        # load mh_gspphot

        mh_gspphot_value = line[18].strip()
        if len(mh_gspphot_value) == 0:
            cursor.execute("update CAT1 set mh_gspphot = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set mh_gspphot = {} where designation = '{}'".format(float(mh_gspphot_value), designation_value))

        # load mh_gspphot_upper

        mh_gspphot_lower_value = line[19].strip()
        if len(mh_gspphot_lower_value) == 0:
            cursor.execute("update CAT1 set mh_gspphot_lower = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set mh_gspphot_lower = {} where designation = '{}'".format(float(mh_gspphot_lower_value), designation_value))

        # load mh_gspphot_lower

        mh_gspphot_upper_value = line[20].strip()
        if len(mh_gspphot_upper_value) == 0:
            cursor.execute("update CAT1 set mh_gspphot_upper = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set mh_gspphot_upper = {} where designation = '{}'".format(float(mh_gspphot_upper_value), designation_value))

        # load distance_gspphot

        distance_gspphot_value = line[21].strip()
        if len(distance_gspphot_value) == 0:
            cursor.execute("update CAT1 set distance_gspphot = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set distance_gspphot = {} where designation = '{}'".format(float(distance_gspphot_value), designation_value))

        # load distance_gspphot_lower

        distance_gspphot_lower_value = line[22].strip()
        if len(distance_gspphot_lower_value) == 0:
            cursor.execute("update CAT1 set distance_gspphot_lower = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set distance_gspphot_lower = {} where designation = '{}'".format(float(distance_gspphot_lower_value), designation_value))

        # load distance_upper

        distance_gspphot_upper_value = line[23].strip()
        if len(distance_gspphot_upper_value) == 0:
            cursor.execute("update CAT1 set distance_gspphot_upper = NULL where designation = '{}'".format(designation_value))
        else:
            cursor.execute("update CAT1 set distance_gspphot_upper = {} where designation = '{}'".format(float(distance_gspphot_upper_value), designation_value))

csv_file.close()

# Make sure data is committed to the database
connection.commit()

# Criar a tabela CAT1_product no BD

cursor.execute("create table CAT1_product("
               "designation CHAR(100) primary key,"
               "Mg NUMERIC(65,30) null,"
               "Mg_error NUMERIC(65,30) null,"
               "MRp NUMERIC(65,30) null,"
               "MRp_error NUMERIC(65,30) null,"
               "Bp_minus_Rp NUMERIC(65,30) null,"
               "foreign key (designation) references CAT1(designation) on delete restrict)")

# Carregar dados da tabela CAT1_product

# load designation

cursor.execute("select designation from CAT1")
value = cursor.fetchall()

for (designation_value,) in value:
    cursor.execute("insert into CAT1_product(designation) values('{}')".format(designation_value))

# load Mg

cursor.execute("select designation, phot_g_mean_mag + 5 + 5*log(10, parallax/1000.0) as Mg "
               "from CAT1 "
               "where phot_g_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax > 0")
value = cursor.fetchall()
for (designation_value, Mg_value) in value:
    cursor.execute("update CAT1_product set Mg = {} where designation = '{}'".format(Mg_value, designation_value))

cursor.execute("select designation from CAT1 "
               "where phot_g_mean_mag is NULL or "
               "parallax is NULL and "
               "parallax <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set Mg = NULL where designation = '{}'".format(designation_value))

# load Mg_error

cursor.execute("select designation, "
               "( "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_g_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_g_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2.0 as Mg_error "
               "from CAT1 "
               "where phot_g_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL and "
               "parallax > 0 and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0")
value = cursor.fetchall()
for (designation_value, Mg_error_value) in value:
    cursor.execute("update CAT1_product set Mg_error = {} where designation = '{}'".format(Mg_error_value, designation_value))

cursor.execute("select designation "
               "from CAT1 "
               "where phot_g_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL or "
               "parallax <= 0 or "
               "parallax + parallax_error <= 0 or "
               "parallax - parallax_error <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set Mg_error = NULL where designation = '{}'".format(designation_value))

# load MRp

cursor.execute("select designation, phot_rp_mean_mag + 5 + 5*log(10, parallax/1000.0) as MRp "
               "from CAT1 "
               "where phot_rp_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax > 0")
value = cursor.fetchall()
for (designation_value, MRp_value) in value:
    cursor.execute("update CAT1_product set MRp = {} where designation = '{}'".format(MRp_value, designation_value))

cursor.execute("select designation "
               "from CAT1 "
               "where phot_rp_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set MRp = NULL where designation = '{}'".format(designation_value))

# load MRp_error

cursor.execute("select designation, "
               "( "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax + parallax_error) / 1000.0))) "
               "+ "
               "abs((phot_rp_mean_mag + 5 + 5 * log(10, parallax / 1000.0)) - (phot_rp_mean_mag + 5 + 5 * log(10, (parallax - parallax_error) / 1000.0))) "
               ") / 2.0 as MRp_error "
               "from CAT1 "
               "where phot_rp_mean_mag is not NULL and "
               "parallax is not NULL and "
               "parallax_error is not NULL and "
               "parallax > 0 and "
               "parallax + parallax_error > 0 and "
               "parallax - parallax_error > 0")
value = cursor.fetchall()
for (designation_value, MRp_error_value) in value:
    cursor.execute("update CAT1_product set MRp_error = {} where designation = '{}'".format(MRp_error_value, designation_value))

cursor.execute("select designation from CAT1 "
               "where phot_rp_mean_mag is NULL or "
               "parallax is NULL or "
               "parallax_error is NULL or "
               "parallax <= 0 or "
               "parallax + parallax_error <= 0 or "
               "parallax - parallax_error <= 0")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set MRp_error = NULL where designation = '{}'".format(designation_value))

# load Bp_minus_Rp

cursor.execute("select designation, phot_bp_mean_mag - phot_rp_mean_mag as Bp_minus_Rp from CAT1 "
               "where phot_bp_mean_mag is not NULL and phot_rp_mean_mag is not NULL")
value = cursor.fetchall()
for (designation_value, Bp_minus_Rp_value) in value:
    cursor.execute("update CAT1_product set Bp_minus_Rp = {} where designation = '{}'".format(Bp_minus_Rp_value, designation_value))

cursor.execute("select designation "
               "from CAT1 "
               "where phot_bp_mean_mag is NULL or "
               "phot_rp_mean_mag is NULL")
value = cursor.fetchall()
for (designation_value,) in value:
    cursor.execute("update CAT1_product set Bp_minus_Rp = NULL where designation = '{}'".format(designation_value))

# Make sure data is committed to the database
connection.commit()

# Criar a tabela CAT2_product no BD

cursor.execute("create table CAT2_product( "
               "HIP CHAR(100) primary key, "
               "MV NUMERIC(65,30) null, "
               "MV_error NUMERIC(65,30) null, "
               "MVt NUMERIC(65,30) null, "
               "MVt_error NUMERIC(65,30) null, "
               "B_minus_V NUMERIC(65,30) null, "
               "BT_minus_VT NUMERIC(65,30) null, "
               "foreign key (HIP) references CAT2(HIP) on delete restrict)")

# Carregar dados da tabela CAT2_product

# load HIP

cursor.execute("select HIP from CAT2")
value = cursor.fetchall()

#add_row = ("insert into Hipparcos_product (HIP) values (%(HIP)s)")

for (HIP_value,) in value:
    #data_row = {
    #    'HIP': registro[0]
    #}
    #cursor.execute(add_row, data_row)
    cursor.execute("insert into CAT2_product(HIP) values ('{}')".format(HIP_value))

# load MV

cursor.execute("select HIP, Vmag + 5 + 5 * log(10, Plx/1000.0) as MV "
               "from CAT2 "
               "where Vmag is not NULL and "
               "Plx is not NULL and "
               "Plx > 0")
value = cursor.fetchall()
for (HIP_value, MV_value) in value:
    cursor.execute("update CAT2_product set MV = {} where HIP = '{}'".format(MV_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where Vmag is NULL or "
               "Plx is NULL or "
               "Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MV = NULL where HIP = '{}'".format(HIP_value))

# load MV_error

cursor.execute("select HIP, "
               "("
               "abs((Vmag + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx + e_Plx) / 1000.0))) "
               "+ "
               "abs((Vmag  + 5 + 5 * log(10, Plx/1000.0)) - (Vmag + 5 + 5 * log(10, (Plx - e_Plx) / 1000.0))) "
               ") / 2.0 as MV_error "
               "from CAT2 "
               "where Vmag is not NULL and "
               "Plx is not NULL and "
               "e_Plx is not NULL and "
               "Plx > 0 and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0")
value = cursor.fetchall()
for (HIP_value, MV_error_value) in value:
    cursor.execute("update CAT2_product set MV_error = {} where HIP = '{}'".format(MV_error_value, HIP_value))

cursor.execute("select HIP from CAT2 "
               "where Vmag is NULL or "
               "Plx is NULL or "
               "e_Plx is NULL or "
               "Plx <= 0 or "
               "Plx + e_Plx <= 0 or "
               "Plx - e_Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MV_error = NULL where HIP = '{}'".format(HIP_value))

# load MVt

cursor.execute("select HIP, "
               "VTmag + 5 + 5 * log(10, Plx / 1000.0) as MVt "
               "from CAT2 "
               "where VTmag is not NULL and "
               "Plx is not NULL and "
               "Plx > 0")
value = cursor.fetchall()
for (HIP_value, MVt_value) in value:
    cursor.execute("update CAT2_product set MVt = {} where HIP = '{}'".format(MVt_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where VTmag is NULL or "
               "Plx is NULL or "
               "Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MVt = NULL where HIP = '{}'".format(HIP_value))

# load MVt_error

cursor.execute("select HIP, "
               "( "
               "abs(( VTmag + 5 + 5 * log(10, Plx / 1000.0)) - (VTmag + 5 + 5 * log(10, (Plx + e_Plx) / 1000.0))) "
               "+ "
               "abs(( VTmag + 5 + 5 * log(10, Plx / 1000.0)) - (VTmag + 5 + 5 * log(10, (Plx - e_Plx) / 1000.0))) "
               ") / 2.0 as MVt_error "
               "from CAT2 "
               "where VTmag is not NULL and "
               "Plx is not NULL and "
               "e_Plx is not NULL and "
               "Plx > 0 and "
               "Plx + e_Plx > 0 and "
               "Plx - e_Plx > 0")
value = cursor.fetchall()
for (HIP_value, MVt_error_value) in value:
    cursor.execute("update CAT2_product set MVt_error = {} where HIP = '{}'".format(MVt_error_value, HIP_value))

cursor.execute("select HIP from CAT2 "
               "where VTmag is NULL or "
               "Plx is NULL or "
               "e_Plx is NULL or "
               "Plx <= 0 or "
               "Plx + e_Plx <= 0 or "
               "Plx - e_Plx <= 0")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set MVt_error = NULL where HIP = '{}'".format(HIP_value))

# load B_minus_V

cursor.execute("select HIP, "
               "B_V as B_minus_V "
               "from CAT2 "
               "where B_V is not NULL")
value = cursor.fetchall()
for (HIP_value, B_minus_V_value) in value:
    cursor.execute("update CAT2_product set B_minus_V = {} where HIP = '{}'".format(B_minus_V_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where B_V is NULL")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set B_minus_V = NULL where HIP = '{}'".format(HIP_value))

# load BT_minus_VT

cursor.execute("select HIP, "
               "BTmag - VTmag  as BT_minus_VT "
               "from CAT2 "
               "where BTmag is not NULL and "
               "VTmag is not NULL")
value = cursor.fetchall()
for (HIP_value, BT_minus_VT_value) in value:
    cursor.execute("update CAT2_product set BT_minus_VT = {} where HIP = '{}'".format(BT_minus_VT_value, HIP_value))

cursor.execute("select HIP "
               "from CAT2 "
               "where BTmag is NULL or "
               "VTmag is NULL")
value = cursor.fetchall()
for (HIP_value,) in value:
    cursor.execute("update CAT2_product set BT_minus_VT = NULL where HIP = '{}'".format(HIP_value))

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()