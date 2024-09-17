import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("create table TESTE("
               "HIP CHAR(100) primary key)")

with open("/home/lh/Desktop/CAT2_intersec_GaiaCompleto_via_simbad_ANTIGA.csv", 'r') as csv_file:
    next(csv_file)

    for line in csv_file:
        line = line.split(",")

        # load HIP

        HIP_value = line[0].strip()
        if len(HIP_value) == 0:
            cursor.execute("insert into TESTE(HIP) values(NULL)")
        else:
            cursor.execute("insert into TESTE(HIP) values('{}')".format(HIP_value))

csv_file.close()

# Make sure data is committed to the database
connection.commit()

cursor.close()
connection.close()