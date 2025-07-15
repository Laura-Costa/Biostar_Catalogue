import xlsxwriter

def xlsx(cursor, queries, header, path, sheets):
    """
    :param queries: lista com as consultas SQL que retornam os dados para cada sheet do workbook
    :param header: lista contendo as strings dos nomes dos atributos retornados pela query (na mesma ordem do retorno da query).
                   Importante: a mesma lista de títulos será usada para todas as sheets passadas.
    :param path: caminho relativo (a partir do /outputfiles) onde se deseja salvar o arquivo xlsx no PC
    :param sheets: lista com as strings dos nomes das sheets
    :return:
    """

    workbook = xlsxwriter.Workbook('/home/lh/Documents/Biostar_Catalogue/Biostar_Catalogue/output_files/' + path)

    for (sheet, query) in zip(sheets, queries):

        cursor.execute(query)
        value = cursor.fetchall()
        sheet = workbook.add_worksheet(sheet)
        # escrever na sheet
        for i in range(len(value[0])):
            temp_list = []
            for j in range(len(value)):
                temp_list.append(value[j][i])
            temp_list.insert(0, header[i])
            # escrever a coluna no workbook
            sheet.write_column(0, i, temp_list)
    workbook.close()