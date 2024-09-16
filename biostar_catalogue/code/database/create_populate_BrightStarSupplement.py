import mysql.connector
from astroquery.simbad import Simbad

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar a tabela BrightStarSupplement no BD:

cursor.execute("drop table if exists BrightStarSupplement")

cursor.execute("create table BrightStarSupplement( "
               "id INT not null auto_increment primary key, "
               "HD CHAR(100) null, "
               "HD_Suffix CHAR(100) null, "
               "V NUMERIC(6,2) null, "
               "B_V NUMERIC(7,2) null, "
               "SpType CHAR(100) null, "
               "simbad_designation_DR3 CHAR(100) null, "
               "simbad_parallax NUMERIC(65,30) null, "
               "simbad_parallax_error NUMERIC(65,30) null)")

# Carregar os dados da tabela BrightStarSupplement:

with open("BSC4S.DAT", 'r') as file:
    for line in file:
        if len(line) == 0: continue
        # load HD

        HD_value = line[0:6].strip()

        # aqui é adicionado o prefixo 'HD' apenas se a estrela tiver um HD
        #########
        if len(HD_value) != 0:
            HD_value = 'HD ' + HD_value
        #########

        if len(HD_value) == 0:
            cursor.execute("insert into BrightStarSupplement(HD) values(NULL)")
        else:
            cursor.execute("insert into BrightStarSupplement(HD) values('{}')".format(HD_value))

        # Pegar a chave do ultimo registro. O HD não pode ser chave porque existem HDs null (faltantes)
        #########
        cursor.execute("select id from BrightStarSupplement order by id DESC limit 1")
        value = cursor.fetchall()
        id = value[0][0]
        #########

        # load HD_Suffix

        HD_Suffix = line[6:9].strip()
        if len(HD_Suffix) == 0:
            cursor.execute("update BrightStarSupplement set HD_Suffix = NULL where id = {}".format(id))
        else:
            cursor.execute("update BrightStarSupplement set HD_Suffix = '{}' where id = {}".format(HD_Suffix, id))

        # load V

        V_value = line[104:109].strip()
        # o HD 84005 tem um caractere ':' depois do valor de V.
        # Aqui este caractere ':' é removido
        #########
        if HD_value == 'HD 84005':
            V_value = V_value[:-1]
        #########
        if len(V_value) == 0:
            cursor.execute("update BrightStarSupplement set V = NULL where id = {}".format(id))
        else:
            cursor.execute("update BrightStarSupplement set V = {} where id = {}".format(float(V_value), id))

        # load B-V

        B_V_value = line[109:115].strip()
        if len(B_V_value) == 0:
            cursor.execute("update BrightStarSupplement set B_V = NULL where id = {}".format(id))
        else:
            cursor.execute("update BrightStarSupplement set B_V = {} where id = {}".format(float(B_V_value), id))

        # load SpType

        SpType_value = line[127:148].strip()
        if len(SpType_value) == 0:
            cursor.execute("update BrightStarSupplement set SpType = NULL where id = {}".format(id))
        else:
            cursor.execute("update BrightStarSupplement set SpType = '{}' where id = {}".format(SpType_value, id))

        # Verificar se no Simbad existe uma designacao Gaia DR3 correspondente ao HD
        # Se houver, carregar no BD. Senao, colocar NULL.

        # antes de pesquisar no Simbad, verificamos se o HD é null
        # se é null, o HD nao é buscado no simbad
        #########
        if len(HD_value) == 0:
            cursor.execute("update BrightStarSupplement set simbad_designation_DR3 = NULL where id = {}".format(id))
        else:
            tab = Simbad.query_objectids(HD_value[:])

            if tab is None or len([id for id in tab['ID'] if id.startswith('Gaia DR3')]) == 0:
                cursor.execute("update BrightStarSupplement set simbad_designation_DR3 = NULL where id = {}".format(id))
            else:
                designation_DR3_value = [id for id in tab['ID'] if id.startswith('Gaia DR3')][0][:].strip()
                cursor.execute("update BrightStarSupplement set simbad_designation_DR3 = '{}' where id = {}".format(designation_DR3_value, id))
        #########
        '''
        # puxar do Simbad o atributo parallax correspondente ao HD
        # se houver, carregar no BD. Senao, colocar NULL

        Simbad.add_votable_fields('plx')  # adicionar o campo plx aos campos default do Simbad

        # antes de pesquisar no Simbad, verificamos se o HD termina com 'A'
        # se termina com 'A', esse 'A' é removido antes da busca
        #########
        if len(HD_value) == 0:
            cursor.execute("update BrightStarSupplement set simbad_parallax = NULL where HD = '{}'".format(HD_value))
        else:
            if HD_value[-1] == 'A':
                sim = Simbad.query_object(HD_value[:-1])
            else:
                sim = Simbad.query_object(HD_value[:])

            if sim is None or len(sim['PLX_VALUE']) == 0 or str(sim['PLX_VALUE'][0]) == '--':
                cursor.execute(
                    "update BrightStarSupplement set simbad_parallax = NULL where HD = '{}'".format(HD_value))
            else:
                parallax_value = float(sim['PLX_VALUE'])
                cursor.execute(
                    "update BrightStarSupplement set simbad_parallax = {:.10f} where HD = '{}'".format(parallax_value, HD_value))
        #########

        # Puxar do Simbad o atributo parallax_error correspondente ao HD
        # Se houver, carregar no BD. Senao, colocar NULL.

        Simbad.add_votable_fields('plx_error')  # adicionar o campo plx_error aos campos default do Simbad

        # antes de pesquisar no Simbad, verificamos se o HD termina com 'A'
        # se termina com 'A', esse 'A' é removido antes da busca
        #########
        if HD_value[-1] == 'A':
            sim = Simbad.query_object(HD_value[:-1])
        else:
            sim = Simbad.query_object(HD_value[:])
        #########

        if sim is None or len(sim['PLX_ERROR']) == 0 or str(sim['PLX_ERROR'][0]) == '--':
            cursor.execute("update BrightStarSupplement set simbad_parallax_error = NULL where HD = '{}'".format(HD_value))
        else:
            parallax_error_value = float(sim['PLX_ERROR'])
            cursor.execute("update BrightStarSupplement set simbad_parallax_error = {:.10f} where HD = '{}'".format(parallax_error_value, HD_value))
        '''
file.close()

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()