import concurrent.futures
import time
from bs4 import BeautifulSoup
import requests
import math

def calculate_time(start_time):

  end_time = time.time()
  total_time = (end_time-start_time)
  hours = math.floor(total_time//3600)
  minutes = math.floor((total_time%3600)//60)
  seconds = math.floor((total_time%3600)%60)

  return (hours, minutes, seconds)

def get_html(url):
    session = requests.Session()
    response = session.get(url).text
    return response

def get_data(html, label):
    table = get_basic_data_table(html)

    if table is not None:
      return get_radial_velocity(table, label)

def get_basic_data_table(html):
    soup = BeautifulSoup(html, 'html.parser')

    table_list = soup.find_all('table')
    n_table = len(table_list)
    i = 0
    while i < n_table:
      if table_list[i].find('tr') is not None:
        tr = table_list[i].find('tr')
        if tr.find('td') is not None:
          text = tr.find('td').text

          if "Basic data :" in str(text):
            return table_list[i] # table with basic data is table with the 'Basic data :' text
      i += 1

def get_radial_velocity(table, label):

    tr_list = table.find_all('tr')
    n_tr = len(tr_list)

    tr = tr_list[1]
    td = tr.find('td')
    tr_list = td.find_all('tr')

    n_tr = len(tr_list)
    i = 0

    while i < n_tr:
      current_tr = tr_list[i]
      td_list = current_tr.find_all('td')
      n_td = len(td_list)

      j = 0
      while j < n_td:
        current_td = td_list[j]
        text = current_td.text

        if label in text:
          data_list = td_list[j+1].text.split(' ')
          radial_velocity = data_list[1]
          e_radial_velocity = data_list[2][1:-1]
          return (radial_velocity, e_radial_velocity)
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

def crawler(identifier_list, n, step, label, file_name, divisor, sleep):

  number_of_stars_already_searched = 0
  star_dict = {} # dictionary that maps the star to the associated data searched
  threads = step # step is the number of threads (step must be a divisor of n)
  end = n-(step-1) # end is n-(step-1)

  for idx in range(0, end, threads):

      urls = []
      url = 'https://simbad.cds.unistra.fr/simbad/sim-id?Ident='
      for i in range(threads): # many urls are requested at once
        urls.append(url + str(identifier_list[idx+i]))
        print(identifier_list[idx+i])
      print()

      with concurrent.futures.ThreadPoolExecutor() as executor:
          results = executor.map(get_html, urls) # makes requests to the website

      idxs = [idx+i for i in range(threads)] # identifiers_list indexes of the searched stars

      for (html, ind) in zip(results, idxs):
        data = get_data(html, label)

        # register the star and associated data
        star_dict[str(identifier_list[ind])] = data
        #print(f"star: {str(identifier_list[ind])} data: {data}") # to be commented

      # show percentage of search completed
      number_of_stars_already_searched += threads
      if number_of_stars_already_searched % divisor == 0:
          percent = round((number_of_stars_already_searched*100)/float(n), 1)
          print(f"number_of_stars_already_searched = {number_of_stars_already_searched} ({percent}%)")
          if number_of_stars_already_searched == sleep:
            time.sleep(60*5.0)

  return star_dict