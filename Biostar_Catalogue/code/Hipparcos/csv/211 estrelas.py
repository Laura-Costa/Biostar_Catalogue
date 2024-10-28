import mysql.connector
import pandas as pd
import os

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

header = ["designation", "right_ascension", "declination", "phot_g_mean_mag", "MG", "Bp_Rp", "simbad_HD", "HD", "HIP"]

cursor.execute("""select CAT1.designation, """
               """CAT1.right_ascension, """
               """CAT1.declination, """
               """CAT1.phot_g_mean_mag, """
               """CAT1_product.MG, """
               """CAT1_product.Bp_Rp, """
               """CAT1.simbad_HD, """
               """Hipparcos.HD, """
               """Hipparcos.HIP """
               """from CAT1, CAT1_product, Hipparcos """
               """where CAT1.designation = CAT1_product.designation and """
               """CAT1.HIP = Hipparcos.HIP and """  
               """Hipparcos.HD in {stringHD} """
               """into outfile '/var/lib/mysql-files/211_CAT1.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(stringHD=stringHD))

file = pd.read_csv('/var/lib/mysql-files/211_CAT1.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/csv/211_CAT1.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/211_CAT1.csv")

header = ["simbad_DR3", "GaiaDR3_parallax", "GaiaDR3_parallax_error", "HD", "HIP"]

cursor.execute("""select simbad_DR3, """
               """GaiaDR3_parallax, """
               """GaiaDR3_parallax_error, """
               """Hipparcos.HD, """
               """Hipparcos.HIP """
               """from Hipparcos """
               """where Hipparcos.HD in {stringHD} """
               """into outfile '/var/lib/mysql-files/211.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(stringHD=stringHD))

file = pd.read_csv('/var/lib/mysql-files/211.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/csv/211.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/211.csv")

header = ["designation", "right_ascension", "declination", "phot_g_mean_mag", "MG", "Bp_Rp", "simbad_HD"]

cursor.execute("""select CAT1.designation, """
               """CAT1.right_ascension, """
               """CAT1.declination, """
               """CAT1.phot_g_mean_mag, """
               """CAT1_product.MG, """
               """CAT1_product.Bp_Rp, """
               """CAT1.simbad_HD """
               """from CAT1, CAT1_product """
               """where CAT1.designation = CAT1_product.designation and """
               """CAT1.simbad_HD in {stringHD} """
               """into outfile '/var/lib/mysql-files/211_plotado.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(stringHD=stringHD))

file = pd.read_csv('/var/lib/mysql-files/211_plotado.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/csv/211_plotado.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/211_plotado.csv")

header = ["designation", "right_ascension", "declination", "phot_g_mean_mag", "MG", "Bp_Rp", "simbad_HD"]

cursor.execute("""select CAT1.designation, """
               """CAT1.right_ascension, """
               """CAT1.declination, """
               """CAT1.phot_g_mean_mag, """
               """CAT1_product.MG, """
               """CAT1_product.Bp_Rp, """
               """CAT1.simbad_HD """
               """from CAT1, CAT1_product """
               """where CAT1.designation = CAT1_product.designation and """
               """CAT1.simbad_HD in {stringHD} and """
               """CAT1.HIP is null """
               """into outfile '/var/lib/mysql-files/211_CAT1_HIP_null.csv' """ 
               """fields optionally enclosed by '"' """
               """terminated by ',' """
               """lines terminated by '\n' """.format(stringHD=stringHD))

file = pd.read_csv('/var/lib/mysql-files/211_CAT1_HIP_null.csv', header=None)
file.to_csv("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/Hipparcos/csv/211_CAT1_HIP_null.csv", header=header, index=None)
os.remove("/var/lib/mysql-files/211_CAT1_HIP_null.csv")