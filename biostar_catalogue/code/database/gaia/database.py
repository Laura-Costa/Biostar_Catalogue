import decimal
import math

def update_table(cursor, table_name, column_name, line, index, column_key_name, key_value, preffix = False, index2=-1):
    """
    @param cursor: variável que permite ao Python executar comandos SQL
    @param table_name: nome da tabela cujo registro será atualizado
    @param column_name: nome da coluna da tabela a ser atualizada
    @param line: estrutura de dados (linha do arquivo, tupla) onde está o dado a ser inserido
    @param index: índice da linha do arquivo de entrada que contém o dado
    @param column_key_name: nome da coluna que é chave primária na tabela table_name
    @param key_value: valor da chave primária do registro a ser atualizado
    @param preffix: True se o campo tem prefixo; False caso contrário
    @return: none
    """
    if(index2 != -1):
        data_value = line[index:index2].strip()
    else:
        data_value = line[index].strip()

    if len(data_value) == 0 or data_value == '~' or data_value == '\n' or data_value == '\r\n' or data_value == '\r\r':
        cursor.execute("update {table_name} set {column_name} = null where {column_key_name} = '{key_value}'".format(table_name=table_name,
                                                                                                                     column_name=column_name,
                                                                                                                     column_key_name=column_key_name,
                                                                                                                     key_value=key_value))
        return

    if preffix: data_value = column_name + " " + data_value
    cursor.execute("update {table_name} set {column_name} = '{data_value}' where {column_key_name} = '{key_value}'".format(
                                                                                        table_name=table_name,
                                                                                        column_name=column_name,
                                                                                        data_value=data_value,
                                                                                        column_key_name=column_key_name,
                                                                                        key_value=key_value))

def update_product(cursor, son_table, son_column, son_key_column, my_tuple):
    """
    @param cursor: variável que permite ao Python executar comandos SQL
    @param son_table: nome da tabela a ser atualizada
    @param son_column: nome da coluna a ser atualizada
    @param son_key_column: nome da coluna que é chave primária na tabela a ser atualizada
    @param my_tuple: (chave, produto): tupla que contém, no índice 0, a chave do registro a ser atualizado e, no índice 1, o produto a ser inserido
    @return: none
    """
    key_value = my_tuple[0]
    product_value = my_tuple[1]
    cursor.execute("update {son_table_name} set {son_column_name} = {product_value} "
                   "where {son_column_key_name} = '{key_value}'".format(son_table_name=son_table,
                                                                        son_column_name=son_column,
                                                                        product_value=product_value,
                                                                        son_column_key_name=son_key_column,
                                                                        key_value=key_value))

def simbad_search_id_by_id(cursor, tab, catalogue, table_name, column_name, column_key_name, id):
    """

    @param cursor: permite ao Python executar comandos SQL
    @param tab: tabela de identificadores retornada pela astroquery
    @param data_release: lançamento gaia onde se deseja procurar a designação (1, 2 ou 3)
    @param table_name: nome da tabela cujo registro será atualizado
    @param column_key_name: nome da coluna chave da tabela
    @param key_value: valor da chave do registro
    @return: none
    """
    if tab is None or len([id for id in tab['ID'] if id.startswith(catalogue)]) == 0:
        cursor.execute("update {} set {} = null where {} = '{}'".format(table_name, column_name, column_key_name, id))
    else:
        simbad_id_value = [id for id in tab['ID'] if id.startswith(catalogue)][0].strip()
        if catalogue == 'HD' or catalogue == 'HIP':
            simbad_id_value = simbad_id_value.split(" ")
            preffix = simbad_id_value[0].strip() # pegando o prefixo do identificador, ex: 'HD', 'HIP'.
            number = simbad_id_value[-1].strip() # restante do id, tirando o seu prefixo.
            simbad_id_value = preffix + ' ' + number
        cursor.execute(
            "update {} set {} = '{}' where {} = '{}'".format(table_name, column_name, simbad_id_value,
                                                                      column_key_name, id))

def insert_key(cursor, table_name, column_key_name, data_structure, index, preffix=False, index2=-1):
    """
    :param cursor: permite executar comandos SQL no Python
    :param table_name: nome da tabela na qual será inserida a chave primária
    :param column_key_name: nome da coluna que é chave primária em table_name
    :param data_structure: estrutura de dados (tuple, array, string) que contém a chave primária a ser inserida
    :param index: índice do qual a data_structure será indexada para se obter a chave primária a ser inserida
    :param preffix: booleano que indica se a chave tem prefixo. Caso tenha, o prefixo será a column_key_name.
                    Caso index2 != -1, ele será o segundo índice do slice que removerá o label da chave primária.
    :param index2: segundo número do slice
    :return:
    """

    if index2 != -1 and type(data_structure[index]) != int: # para os dados do BrightStar e Supplement é preciso fazer um slice
        data_value = data_structure[index:index2].strip()
    elif type(data_structure[index]) != int:
        data_value = data_structure[index].strip()
    else:
        data_value = data_structure[index]

    if preffix: data_value = column_key_name + " " + data_value

    cursor.execute("insert into {table_name}({column_key_name}) values('{data_value}')".format(table_name=table_name,
                                                                                               column_key_name=column_key_name,
                                                                                               data_value=data_value))

def search_id_in_simbad(tab, cursor, table_name, column_name, column_key_name, key_value):
    if tab is None:
        in_simbad = 0
    else:
        in_simbad = 1
    cursor.execute("update {} set {} = {} where {} = '{}'".format(table_name, column_name, in_simbad, column_key_name, key_value))

def strassen(ra, dec, vr, vt_alpha, vt_delta):

    v = [
        [vr],
        [vt_alpha],
        [vt_delta]
        ]
    T = [
        [decimal.Decimal(-0.05487554), decimal.Decimal(-0.8734371), decimal.Decimal(-0.4838350)],
        [decimal.Decimal(0.49410945), decimal.Decimal(-0.4448296), decimal.Decimal(0.7469822)],
        [decimal.Decimal(-0.86766614), decimal.Decimal(-0.1980764), decimal.Decimal(0.4559838)]
        ]
    cos_alpha = decimal.Decimal(math.cos(ra))
    cos_delta = decimal.Decimal(math.cos(dec))
    sen_alpha = decimal.Decimal(math.sin(ra))
    sen_delta = decimal.Decimal(math.sin(dec))
    A = [
        [cos_alpha*cos_delta, -sen_alpha, -cos_alpha*sen_delta],
        [sen_alpha*cos_delta, cos_alpha, -sen_alpha*sen_delta],
        [sen_delta, 0, cos_delta]
        ]
    A_v = [
          [A[0][0]*v[0][0] + A[0][1]*v[1][0] + A[0][2]*v[2][0]],
          [A[1][0]*v[0][0] + A[1][1]*v[1][0] + A[1][2]*v[2][0]],
          [A[2][0]*v[0][0] + A[2][1]*v[1][0] + A[2][2]*v[2][0]]
          ]
    T_A_v = [
            [T[0][0]*A_v[0][0] + T[0][1]*A_v[1][0] + T[0][2]*A_v[2][0]],
            [T[1][0]*A_v[0][0] + T[1][1]*A_v[1][0] + T[1][2]*A_v[2][0]],
            [T[2][0]*A_v[0][0] + T[2][1]*A_v[1][0] + T[2][2]*A_v[2][0]]
            ]
    u = T_A_v[0][0]
    v = T_A_v[1][0]
    w = T_A_v[2][0]

    return (u, v, w)