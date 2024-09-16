import mysql.connector
from astroquery.simbad import Simbad
# para tratar warnings como erros:
import warnings
warnings.filterwarnings("error")

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

# Criar a tabela BrightStar no BD:

cursor.execute("drop table if exists BrightStar")

cursor.execute("create table BrightStar( "
               "HR CHAR(100) primary key, "
               "Name CHAR(100) null, "
               "HD CHAR(100) null, "
               "HD_Suffix CHAR(100) null, "
               "V NUMERIC(6,2) null, "
               "B_V NUMERIC(7,2) null, "
               "SpType CHAR(100) null, "
               "simbad_designation_DR3 CHAR(100) null, "
               "simbad_parallax NUMERIC(65,30) null, "
               "simbad_parallax_error NUMERIC(65,30) null)")

# Carregar os dados da tabela BrightStar:

with open("BSC5_edited.DAT", 'r') as file:
    for line in file:

        # pular as linhas vazias do arquivo
        if line == '\n' or len(line) == 0: continue

        # load HR

        HR_value = line[0:4].strip()

        # aqui é adicionado o prefixo 'HR' apenas se a estrela tiver um HR
        #########
        if len(HR_value) != 0:
            HR_value = 'HR ' + HR_value
        #########

        if len(HR_value) == 0:
            cursor.execute("insert into BrightStar(HR) values(NULL)")
        else:
            cursor.execute("insert into BrightStar(HR) values('{}')".format(HR_value))

        # load Name

        Name_value = line[4:14].strip()

        if len(Name_value) == 0:
            cursor.execute("update BrightStar set Name = NULL where HR = '{}'".format(HR_value))
        else:
            cursor.execute("update BrightStar set Name = '{}' where HR = '{}'".format(Name_value, HR_value))

        # load HD

        HD_value = line[25:31].strip()

        # aqui é adicionado o prefixo 'HD' apenas se a estrela tiver um HD
        #########
        if len(HD_value) != 0:
            HD_value = 'HD ' + HD_value
        #########

        if len(HD_value) == 0:
            cursor.execute("update BrightStar set HD = NULL where HR = '{}'".format(HR_value))
        else:
            cursor.execute("update BrightStar set HD = '{}' where HR = '{}'".format(HD_value, HR_value))

        # load V

        V_value = line[102:107].strip()
        if len(V_value) == 0:
            cursor.execute("update BrightStar set V = NULL where HR = '{}'".format(HR_value))
        else:
            cursor.execute("update BrightStar set V = {} where HR = '{}'".format(float(V_value), HR_value))

        # load B-V

        B_V_value = line[109:114].strip()
        if len(B_V_value) == 0:
            cursor.execute("update BrightStar set B_V = NULL where HR = '{}'".format(HR_value))
        else:
            cursor.execute("update BrightStar set B_V = {} where HR = '{}'".format(float(B_V_value), HR_value))

        # load SpType

        SpType_value = line[127:147].strip()
        if len(SpType_value) == 0:
            cursor.execute("update BrightStar set SpType = NULL where HR = '{}'".format(HR_value))
        else:
            cursor.execute("update BrightStar set SpType = '{}' where HR = '{}'".format(SpType_value, HR_value))

        # Verificar se no Simbad existe uma designacao Gaia DR3 correspondente ao HD
        # Se houver, carregar no BD. Senao, colocar NULL.

        #########
        if len(HD_value) == 0:
            # caso a estrela nao tenha HD, buscamos ela no Simbad usando o HR
            try:
                tab = Simbad.query_objectids(HR_value[:])
            except:
                print("{} não encontrado no Simbad".format(HR_value))
                continue # ir para a próxima linha do arquivo

            if tab is None or len([id for id in tab['ID'] if id.startswith('Gaia DR3')]) == 0:
                cursor.execute("update BrightStar set simbad_designation_DR3 = NULL where HR = '{}'".format(HR_value))
            else:
                designation_DR3_value = [id for id in tab['ID'] if id.startswith('Gaia DR3')][0][:].strip()
                cursor.execute("update BrightStar set simbad_designation_DR3 = '{}' where HR = '{}'".format(designation_DR3_value, HR_value))
        else:
            tab = Simbad.query_objectids(HD_value[:])
            if tab is None or len([id for id in tab['ID'] if id.startswith('Gaia DR3')]) == 0:
                cursor.execute("update BrightStar set simbad_designation_DR3 = NULL where HR = '{}'".format(HR_value))
            else:
                designation_DR3_value = [id for id in tab['ID'] if id.startswith('Gaia DR3')][0][:].strip()
                cursor.execute("update BrightStar set simbad_designation_DR3 = '{}' where HR = '{}'".format(designation_DR3_value, HR_value))
        #########
        '''
        # puxar do Simbad o atributo parallax correspondente ao HD
        # se houver, carregar no BD. Senao, colocar NULL

        Simbad.add_votable_fields('plx')  # adicionar o campo plx aos campos default do Simbad

        # antes de pesquisar no Simbad, verificamos se o HD termina com 'A'
        # se termina com 'A', esse 'A' é removido antes da busca
        #########
        if len(HD_value) == 0:
            cursor.execute("update BrightStar set simbad_parallax = NULL where HD = '{}'".format(HD_value))
        else:
            if HD_value[-1] == 'A':
                sim = Simbad.query_object(HD_value[:-1])
            else:
                sim = Simbad.query_object(HD_value[:])

            if sim is None or len(sim['PLX_VALUE']) == 0 or str(sim['PLX_VALUE'][0]) == '--':
                cursor.execute(
                    "update BrightStar set simbad_parallax = NULL where HD = '{}'".format(HD_value))
            else:
                parallax_value = float(sim['PLX_VALUE'])
                cursor.execute(
                    "update BrightStar set simbad_parallax = {:.10f} where HD = '{}'".format(parallax_value, HD_value))
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
            cursor.execute("update BrightStar set simbad_parallax_error = NULL where HD = '{}'".format(HD_value))
        else:
            parallax_error_value = float(sim['PLX_ERROR'])
            cursor.execute("update BrightStar set simbad_parallax_error = {:.10f} where HD = '{}'".format(parallax_error_value, HD_value))
        '''
file.close()

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()