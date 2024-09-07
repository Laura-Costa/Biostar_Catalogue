from astroquery.simbad import Simbad
import mysql.connector
import csv

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("drop table if exists CAT2_DR1_DR2_DR3")

# Criar a tabela CAT2_DR1_DR2_DR3 no BD:

cursor.execute("create table CAT2_DR1_DR2_DR3("
               "HIP CHAR(100) primary key,"
               "designation_DR3 CHAR(100) null,"
               "designation_DR2 CHAR(100) null,"
               "designation_DR1 CHAR(100) null,"
               "simbad_parallax NUMERIC(65,30) null,"
               "simbad_parallax_error NUMERIC(65,30) null)")

# Carregar os dados da tabela CAT2_DR1_DR2_DR3:

with open("HIP_MAIN.DAT") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        if len(line) != 0:
            line = line[0].split("|")
            if len(line[11].strip()) != 0 and float(line[11].strip()) >= 0.039 * 1000.0:

                HIP_value = "HIP " + line[1].strip()
                if len(HIP_value) == 0:
                    cursor.execute("insert into CAT2_DR1_DR2_DR3(HIP) values(NULL)")
                else:
                    cursor.execute("insert into CAT2_DR1_DR2_DR3(HIP) values('{}')".format(HIP_value))

                # Verificar se no Simbad existe um Gaia DR3 correspondente ao HIP
                # Se houver, carregar no BD. Senao, colocar NULL.

                tab = Simbad.query_objectids(HIP_value)

                if len([id for id in tab['ID'] if id.startswith('Gaia DR3')]) == 0:
                    cursor.execute("update CAT2_DR1_DR2_DR3 set designation_DR3 = NULL where HIP = '{}'".format(HIP_value))
                else:
                    designation_DR3_value = [id for id in tab['ID'] if id.startswith('Gaia DR3')][0][:].strip()
                    cursor.execute(
                        "update CAT2_DR1_DR2_DR3 set designation_DR3 = '{}' where HIP = '{}'".format(designation_DR3_value, HIP_value))

                # Verificar se no Simbad existe um Gaia DR2 correspondente ao HIP
                # Se houver, carregar no BD. Senao, colocar NULL.

                if len([id for id in tab['ID'] if id.startswith('Gaia DR2')]) == 0:
                    cursor.execute("update CAT2_DR1_DR2_DR3 set designation_DR2 = NULL where HIP = '{}'".format(HIP_value))
                else:
                    designation_DR2_value = [id for id in tab['ID'] if id.startswith('Gaia DR2')][0][:].strip()
                    cursor.execute(
                        "update CAT2_DR1_DR2_DR3 set designation_DR2 = '{}' where HIP = '{}'".format(designation_DR2_value, HIP_value))

                # Verificar se no Simbad existe um Gaia DR1 correspondente ao HIP
                # Se houver, carregar no BD. Senao, colocar NULL.

                if len([id for id in tab['ID'] if id.startswith('Gaia DR1')]) == 0:
                    cursor.execute("update CAT2_DR1_DR2_DR3 set designation_DR1 = NULL where HIP = '{}'".format(HIP_value))
                else:
                    designation_DR1_value = [id for id in tab['ID'] if id.startswith('Gaia DR1')][0][:].strip()
                    cursor.execute(
                        "update CAT2_DR1_DR2_DR3 set designation_DR1 = '{}' where HIP = '{}'".format(designation_DR1_value, HIP_value))

                # Puxar do Simbad o atributo parallax correspondente ao HIP
                # Se houver, carregar no BD. Senao, colocar NULL.

                Simbad.add_votable_fields('plx') # adicionar o campo plx aos campos default do Simbad
                sim = Simbad.query_object(HIP_value)

                if len(sim['PLX_VALUE']) == 0 or str(sim['PLX_VALUE'][0]) == '--':
                    cursor.execute("update CAT2_DR1_DR2_DR3 set simbad_parallax = NULL where HIP = '{}'".format(HIP_value))
                else:
                    parallax_value = float(sim['PLX_VALUE'])
                    cursor.execute(
                        "update CAT2_DR1_DR2_DR3 set simbad_parallax = {:.10f} where HIP = '{}'".format(parallax_value, HIP_value))

                # Puxar do Simbad o atributo parallax_error correspondente ao HIP
                # Se houver, carregar no BD. Senao, colocar NULL.

                Simbad.add_votable_fields('plx_error') # adicionar o campo plx_error aos campos default do Simbad
                sim = Simbad.query_object(HIP_value)

                if len(sim['PLX_ERROR']) == 0 or str(sim['PLX_ERROR'][0]) == '--':
                    cursor.execute("update CAT2_DR1_DR2_DR3 set simbad_parallax_error = NULL where HIP = '{}'".format(HIP_value))
                else:
                    parallax_error_value = float(sim['PLX_ERROR'])
                    cursor.execute(
                        "update CAT2_DR1_DR2_DR3 set simbad_parallax_error = {:.10f} where HIP = '{}'".format(parallax_error_value, HIP_value))
tsv.close()

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()