import xlsxwriter

def xlsx(cursor, query, header, path, sheet_name):
    """
    :param query: a consulta SQL que retorna os atributos que se quer gravar no arquivo xlsx
    :param header: lista contendo as strings dos nomes dos atributos retornados pela query (na mesma ordem do retorno da query)
    :param path: caminho relativo (a partir do /outputfiles) onde se deseja salvar o arquivo xlsx no PC
    :param sheet_name: lista com as strings dos nomes das sheets
    :return:
    """
    cursor.execute(query)
    value = cursor.fetchall()

    workbook = xlsxwriter.Workbook('/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path)
    sheet = workbook.add_worksheet(sheet_name)

    for i in range(len(value[0])):
        temp_list = []
        for j in range(len(value)):
            temp_list.append(value[j][i])
        temp_list.insert(0, header[i])
        # escrever a coluna no workbook
        sheet.write_column(0, i, temp_list)

    workbook.close()