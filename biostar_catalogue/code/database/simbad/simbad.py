import time
import mysql.connector
import web_crawler as f1
import database as f2

# abrir conexão com o BD
connection = mysql.connector.connect(host='localhost', 
                                     port='3306', 
                                     database='biostar_catalogue', 
                                     user='lh', 
                                     password='ic2023')

# inicializar o cursor
cursor = connection.cursor()

table = 'simbad'
# apagar a tabela table_name caso ela já exista
cursor.execute("drop table if exists {table}".format(table=table))

# criar a tabela table_name
cursor.execute("create table {table}( "
               "source_id bigint primary key, "
               "radial_velocity decimal(65, 30) null, "
               "radial_velocity_error decimal(65, 30) null, "
               "foreign key(source_id) references gaia(source_id) on delete restrict)".format(table=table))

# load radial velocities and radial velocities errors from simbad (searched by gaia stars)
cursor.execute("select designation from gaia")
value = cursor.fetchall()

designation_list = []
for (designation,) in value:
    designation_list.append(designation)
    source_id = designation[9:]
    f2.insert_key(cursor, table, 'source_id', (source_id,), 0)

n = len(designation_list) # n is the total number of stars to be searched for in simbad
step = 13 # number of simultaneous requests; must be divisor of n
label = "Radial velocity"
divisor = 689 # n/divisor corresponds to the number of percentiles shown
sleep = 1378 # if number_of_hips_already_searched % sleep == 0, the program waits for sleep_minutes
sleep_minutes = 2

# function call
start_time = time.time()
star_dict = f1.crawler(designation_list, n, step, label, divisor, sleep, sleep_minutes)
(hours, minutes, seconds) = f1.calculate_time(start_time)
print("time of execution: {hours}h {minutes}m {seconds}s".format(hours=hours, minutes=minutes, seconds=seconds))
print('LEN(DICT)', len(star_dict))

for designation in star_dict.keys():
    source_id = designation[9:]
    if star_dict[designation] is None:
        continue
    f2.update_table(cursor, table, 'radial_velocity', star_dict[designation], 0, 'source_id', source_id)
    f2.update_table(cursor, table, 'radial_velocity_error', star_dict[designation], 1, 'source_id', source_id)

# certificar-se de que os dados estão gravados no BD
connection.commit()

# fechar o cursor
cursor.close()

# fechar conexão com o BD
connection.close()