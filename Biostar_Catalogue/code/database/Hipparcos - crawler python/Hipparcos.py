import mysql.connector
from bs4 import BeautifulSoup
import requests

def get_html(url):
    """
    :param url: url da pagina
    :return: html da pagina
    """
    return requests.get(url).text

def remove_spaces(str):
    list = str.split(" ")
    result = ""
    for piece in list:
        if piece == '' or piece == '\n':
            continue
        if result == "":
            result = piece.strip()
        else:
            result = result + " " + piece.strip()
    return result

def get_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table').find_next('table').find_next('table')
    table_row = table.find('tr').find_next('tr')
    table = table_row.find('table')
    return table

def get_simbad_main_identifier_and_comment(table):
    tr = table.find('tr')
    td = tr.find('td')
    font = td.find('font')
    simbad_main_identifier = remove_spaces(font.text.split("--")[0])
    simbad_comment = remove_spaces(font.text.split("--")[1])
    return simbad_main_identifier, simbad_comment

def get_simbad_parallax_parallax_error_parallax_source(table):
    tr = table.find('tr')
    text = tr.find('td').text

    while "Parallaxes" not in text and tr.find_next('tr') is not None: # enquanto não chegar na Paralaxe E enquanto houver tr's
        tr = tr.find_next('tr')
        text = tr.find('td').text

    if "Parallaxes" in tr.find('td').text:
        td = tr.find('td').find_next('td')
        b = td.find('b')
        tt = b.find('tt')
        tt = tt.text.split("[")

        # coletar a paralaxe e o erro da paralaxe
        simbad_parallax = remove_spaces(tt[0])
        simbad_parallax_error = remove_spaces(tt[1].split("]")[0])

        # coletar a fonte da paralaxe
        b = td.find('b').find_next('b')
        tt = b.find('tt')
        span = tt.find('span')
        print(span.get('title'))

        simbad_parallax_source = remove_spaces(span.text)

        if "~" in simbad_parallax:
            simbad_parallax = ""
        if "~" in simbad_parallax_error:
            simbad_parallax_error = ""

        return simbad_parallax, simbad_parallax_error, simbad_parallax_source
    else:
        return "", ""

def get_data(html):
    table = get_table(html)
    simbad_main_identifier, simbad_comment = get_simbad_main_identifier_and_comment(table)
    simbad_parallax, simbad_parallax_error, simbad_parallax_source = get_simbad_parallax_parallax_error_parallax_source(table)
    return simbad_main_identifier, simbad_comment, simbad_parallax, simbad_parallax_error, simbad_parallax_source

# abrir conexao com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

# pegar os identificadores da tabela Hipparcos
cursor.execute("select HIP from Hipparcos where HIP is not null")
value = cursor.fetchall()

identifier_list = []
for (identifier_value,) in value:
    identifier_list.append(identifier_value)

for identifier in identifier_list:
    print(identifier)
    url = "https://simbad.cds.unistra.fr/simbad/sim-id?Ident="
    url = url + identifier[0:3] + "+" + identifier[4:]
    html = get_html(url)
    results = get_data(html)
    print(results)