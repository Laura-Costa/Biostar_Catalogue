from astroquery.simbad import Simbad
import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

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

with open("Gaia_archive_CAT1.csv", 'r') as csv_file:
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

cursor.close()
connection.close()