import concurrent.futures
import mysql.connector
from bs4 import BeautifulSoup
import requests
import time
import math

def get_html(url):
    """
    :param url: url da pagina
    :return: html da pagina
    """
    #return requests.get(url).text
    session = requests.Session()
    response = session.get(url).text
    return response

def get_data(html):
    table = get_table(html)
    return get_simbad_dr3(table)

def get_table(html):
    soup = BeautifulSoup(html, 'html.parser')

    # pegar a tabela que contém os identificadores
    table_list = soup.findAll('table')
    n_table = len(table_list)
    i = 0
    while i < n_table:
      if table_list[i].find('tr') is not None:
        tr = table_list[i].find('tr')
        if tr.find('td') is not None:
          text = tr.find('td').text

          if "Identifiers" in str(text):
            #print(text)
            return table_list[i+1]
      i += 1

    #table_row = table.find('tr').find_next('tr')
    #table = table_row.find('table')

def get_simbad_dr3(table):

    #print(table)

    tr_list = table.findAll('tr')
    n_tr = len(tr_list)
    i = 0

    while i < n_tr:
      tr = tr_list[i] # tr da vez
      td_list = tr.findAll('td')
      n_td = len(td_list)
      j = 0

      while j < n_td: # enquanto houver tds
        #print('estou no j = ', j)
        # verificar se o td é vazio. Se for, vai para próximo td
        #print(td_list[j].find_next('b').find('tt'))
        current_td = td_list[j]
        data = current_td.find_next('b').find('tt')
        if data is None:
          #print('CONTINUE estou no j = ', j)
          j += 1
          continue

        text = data.find('a').text

        #print("ID: ", text)

        if "Gaia" in text:
            text_list = data.text.split(" ")

            text_list = [word.replace("\n", "").strip() for word in text_list]
            text = text + " " + text_list[1] + " " + text_list[2]

            #print(text)

            if "Gaia DR3" in text:
              return text

        j += 1
      i += 1


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


# pegar os identificadores da tabela Hipparcos

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

father_table = "Hipparcos"

cursor.execute("select HIP from {father_table}".format(father_table=father_table))

identifier_list = []
cursor.execute("select HIP from {father_table}".format(father_table=father_table))
value = cursor.fetchall()
for (HIP,) in value: # my_tuple is like ('HIP 79672',)
    identifier_list.append(HIP)

# main

# começo
start_time = time.time()

my_dict = {}
n = len(identifier_list)

quant_hips_searched = 0
for idx in range(0, n-16, 17):

    #print("AQUI", identifier_list[idx])
    urls = []
    url = 'https://simbad.cds.unistra.fr/simbad/sim-id?Ident='
    for i in range(17):
      urls.append(url + 'HIP' + '+' + str(identifier_list[idx+i]))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(get_html, urls)
        #print(results)

    idxs = [idx+i for i in range(17)]

    # [idx, idx+1, idx+2, idx+3, idx+4, idx+5, idx+6, idx+7, idx+8, idx+9, idx+10, idx+11, idx+12, idx+13, idx+14, idx+15, idx+16]

    for (html, ind) in zip(results, idxs):
      gaiaDR3 = get_data(html)

      if gaiaDR3 is not None:
        my_dict[str(identifier_list[ind])] = gaiaDR3

    # print("HIP", identifier_list[ind], "result:", gaiaDR3)
    quant_hips_searched += 17
    if quant_hips_searched % 19703 == 0:
        percent = round((quant_hips_searched*100)/118218.0, 1)
        print(f"quant_hips_searched = {quant_hips_searched} ({percent}%)")
        if quant_hips_searched == 59109:
          time.sleep(60*5.0)


#print(my_dict)

key_list = list(my_dict.keys())
#print(key_list)

with open("/content/Hip_stars_with_Dr3_at_Simbad.txt", "w") as text_file:
    for HIP in key_list:
      text_file.write("{0[0]}\n".format([HIP]))

# fim
end_time = time.time()
segundos_totais = (end_time-start_time)
horas = math.floor(segundos_totais//3600)
minutos = math.floor((segundos_totais%3600)//60)
segundos = math.floor((segundos_totais%3600)%60)
print("time of execution: {horas}h {minutos}m {segundos}s\n".format(horas=horas, minutos=minutos, segundos=segundos))