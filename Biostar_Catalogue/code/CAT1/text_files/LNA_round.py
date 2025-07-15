import mysql.connector
import pandas as pd
import os

def deg2hms(ra):
    RA, rs = '', ''
    if ra < 0:
        rs, ra = '-', abs(ra)

    raH = int(ra / 15)
    raM = int(((ra / 15) - raH) * 60)
    raS = round(((((ra / 15) - raH) * 60) - raM) * 60, 2)
    raS = f"{raS:05.2f}"

    RA = '{}{:02d}:{:02d}:{}'.format(rs, raH, raM, raS)

    return RA

def deg2dms(dec):
    DEC, ds = '', ''
    if dec < 0:
        ds, dec = '-', abs(dec)
    else:
        ds, dec = '+', abs(dec)

    decD = int(dec)
    decM = int(((dec - decD) * 3600) / 60.0)
    decS = round(((dec - decD) * 3600) % 60.0, 2)
    decS = f"{decS:05.2f}"

    DEC = '{}{:02d}:{:02d}:{}'.format(ds, decD, decM, decS)

    return DEC

father_table = 'CAT1'
son_table = 'CAT1_product'
brother_table = 'hipparcos'
nephew_table = 'Hipparcos_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

stringHD = "("

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/211_stars.txt") as file:
    cont = 0
    for line in file:
        cont += 1
        if cont != 211:
            stringHD += "'HD {}', ".format(line.rstrip())
        else:
            stringHD += "'HD {}')".format(line.rstrip())
        if(line.strip() == '146233' or line.strip() == '4628' or line.strip() == '16160' or line.strip() == '32147' or line.strip() == '191408' or line.strip() == '219134'):
            print(line.rstrip())

cursor.execute("""select {father_table}.designation, """
               """{father_table}.simbad_HD, """
               """trim({father_table}.right_ascension)+0, """
               """trim({father_table}.declination)+0, """
               """trim({father_table}.phot_g_mean_mag)+0, """
               """trim({son_table}.Bp_Rp)+0, """
               """trim({son_table}.MG)+0 """
               """from {father_table}, {son_table} """
               """where {father_table}.designation = {son_table}.designation and """ 
               """Bp_Rp <= 1.500 and """
               """MG <= 9.000 and """
               """(simbad_HD is null or """
               """(simbad_HD is not null and """
               """simbad_HD not in {stringHD})) """
               """order by Bp_Rp asc""".format(father_table=father_table,
                                                          son_table=son_table, stringHD=stringHD))

value = cursor.fetchall()
designation_list = []
simbad_HD_list = []
ra_list = []
dec_list = []
G_list = []
Bp_Rp_list = []
MG_list = []

for (designation_value, simbad_HD_value, ra_value, dec_value, G_value, Bp_Rp_value, MG_value) in value:
    designation_list.append(designation_value)
    simbad_HD_list.append(simbad_HD_value)
    ra_list.append(ra_value)
    dec_list.append(dec_value)
    G_list.append(G_value)
    Bp_Rp_list.append(Bp_Rp_value)
    MG_list.append(MG_value)

# process ra
for i in range(len(ra_list)):
    ra_list[i] = deg2hms(ra_list[i])

# process dec
for i in range(len(dec_list)):
    dec_list[i] = deg2dms(dec_list[i])

# process G
for i in range(len(G_list)):
    G_list[i] = round(G_list[i], 2)
    G_list[i] = f"{G_list[i]:05.2f}"

# process Bp_Rp
for i in range(len(Bp_Rp_list)):
    Bp_Rp_list[i] = round(Bp_Rp_list[i], 2)
    Bp_Rp_list[i] = f"{Bp_Rp_list[i]:05.2f}"

# process MG
for i in range(len(MG_list)):
    MG_list[i] = round(MG_list[i], 2)
    MG_list[i] = f"{MG_list[i]:05.2f}"


with open("/output_files/CAT1/text_files/LNA_round.txt", "w") as text_file:
    header = ["identifier", "ra", "dec", "G", "Bp_Rp", "MG", "mag", "object", "comment"]
    text_file.write("{0[0]:<30}{0[1]:<13}{0[2]:<14}{0[3]:<7}{0[4]:<7}{0[5]:<7}{0[6]:<4}{0[7]:<13}{0[8]:<10}\n".format(header))
    for (designation, simbad_HD, ra, dec, G, Bp_Rp, MG) in zip(designation_list, simbad_HD_list, ra_list, dec_list, G_list, Bp_Rp_list, MG_list):
        if simbad_HD is not None:
            lista = [simbad_HD, ra, dec, G, Bp_Rp, MG, "G", "nearby_star", "star"]
            text_file.write("{0[0]:<30}{0[1]:<13}{0[2]:<14}{0[3]:<7}{0[4]:<7}{0[5]:<7}{0[6]:<4}{0[7]:<13}{0[8]:<10}\n".format(lista))
        else:
            lista = [designation, ra, dec, G, Bp_Rp, MG, "G", "nearby_star", "star"]
            text_file.write("{0[0]:<30}{0[1]:<13}{0[2]:<14}{0[3]:<7}{0[4]:<7}{0[5]:<7}{0[6]:<4}{0[7]:<13}{0[8]:<10}\n".format(lista))