import mysql.connector
import pandas as pd
import os

def deg2hms(ra):
    RA, rs = '', ''
    if ra < 0:
        rs, ra = '-', abs(ra)

    raH = int(ra / 15)
    raM = int(((ra / 15) - raH) * 60)
    raS = ((((ra / 15) - raH) * 60) - raM) * 60

    RA = '{}{:02d}:{:02d}:{:02d}.{}'.format(rs, raH, raM, int(raS), str(raS)[str(raS).index(".") + 1:])  # [-2:]

    return RA

def deg2dms(dec):
    DEC, ds = '', ''
    if dec < 0:
        ds, dec = '-', abs(dec)
    else:
        ds, dec = '+', abs(dec)

    decD = int(dec)
    decM = int(((dec - decD) * 3600) / 60.0)
    decS = ((dec - decD) * 3600) % 60.0

    DEC = '{}{:02d}:{:02d}:{:02d}.{}'.format(ds, decD, decM, int(decS), str(decS)[str(decS).index(".") + 1:])

    return DEC

father_table = 'CAT1'
son_table = 'CAT1_product'
brother_table = 'Hipparcos'
nephew_table = 'Hipparcos_product'

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh',
                                     password='ic2023')
cursor = connection.cursor()

header = ["designation", "simbad_HD", "ra", "dec", "phot_g_mean_mag", "Bp_Rp", "MG"]
stringHD = "("

with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/input_files/211_stars.txt") as file:
    cont = 0
    for line in file:
        cont += 1
        if cont != 211:
            stringHD += "'HD {}', ".format(line.rstrip())
        else:
            stringHD += "'HD {}')".format(line.rstrip())

cursor.execute("""select CAT1.designation, """
               """CAT1.simbad_HD, """
               """trim(CAT1.right_ascension)+0, """
               """trim(CAT1.declination)+0, """
               """trim(CAT1.phot_g_mean_mag)+0, """
               """trim(CAT1_product.Bp_Rp)+0, """
               """trim(CAT1_product.MG)+0 """
               """from Hipparcos, CAT1, CAT1_product """
               """where CAT1.designation = CAT1_product.designation and """
               """CAT1.HIP = Hipparcos.HIP and """
               """Hipparcos.HD in {stringHD} and """
               """CAT1.simbad_HD not in {stringHD}""".format(stringHD=stringHD))

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
    n = len(str(G_list[i])[str(G_list[i]).index(".") + 1:])
    G_list[i] = f"{G_list[i]:0{n + 3}.{n}f}"

# process Bp_Rp
for i in range(len(Bp_Rp_list)):
    n = len(str(Bp_Rp_list[i])[str(Bp_Rp_list[i]).index(".") + 1:])
    Bp_Rp_list[i] = f"{Bp_Rp_list[i]:0{n + 3}.{n}f}"

# process MG
for i in range(len(MG_list)):
    n = len(str(MG_list[i])[str(MG_list[i]).index(".") + 1:])
    MG_list[i] = f"{MG_list[i]:0{n + 3}.{n}f}"

cont = 0
with open("/output_files/CAT1/text_files/LNA_simbadHD_nao_esta_entre_as_211_e_HipMainDatHD_esta_entre_as_211.txt", "w") as text_file:
    header = ["identifier", "ra", "dec", "G", "Bp_Rp", "MG", "mag", "object", "comment"]
    text_file.write(
        "{0[0]:<12}{0[1]:<27}{0[2]:<27}{0[3]:<12}{0[4]:<12}{0[5]:<20}{0[6]:<4}{0[7]:<13}{0[8]:<10}\n".format(header))
    for (designation, simbad_HD, ra, dec, G, Bp_Rp, MG) in zip(designation_list, simbad_HD_list, ra_list, dec_list,
                                                               G_list, Bp_Rp_list, MG_list):
        if simbad_HD is not None:
            cont += 1
            lista = [simbad_HD, ra, dec, G, Bp_Rp, MG, "G", "nearby_star", "star"]
            text_file.write(
                "{0[0]:<12}{0[1]:<27}{0[2]:<27}{0[3]:<12}{0[4]:<12}{0[5]:<20}{0[6]:<4}{0[7]:<13}{0[8]:<10}\n".format(
                    lista))
        else:
            cont += 1
            lista = [designation, ra, dec, G, Bp_Rp, MG, "G", "nearby_star", "star"]
            text_file.write(
                "{0[0]:<12}{0[1]:<27}{0[2]:<27}{0[3]:<12}{0[4]:<12}{0[5]:<20}{0[6]:<4}{0[7]:<13}{0[8]:<10}\n".format(
                    lista))

print(cont)