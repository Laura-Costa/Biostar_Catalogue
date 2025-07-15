import mysql.connector

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'hipparcos'
son_table = 'Hipparcos_product'

cursor.execute("select {father_table}.HIP as HIP_order, "
         "{father_table}.HD, "
         "trim({father_table}.Vmag)+0, "
         "trim({father_table}.VTmag)+0, "
         "trim({son_table}.B_V)+0, "
         "trim({son_table}.Bt_Vt)+0, "
         "trim({father_table}.Plx)+0, "
         "trim({father_table}.e_Plx)+0, "
         "trim({son_table}.MVt)+0, "
         "trim({son_table}.MV)+0, "
         "{father_table}.SpType "
         "from {father_table}, {son_table} "
         "where {father_table}.HIP = {son_table}.HIP and "
         "{father_table}.simbad_DR3 is null "
         "order by cast(substring(HIP_order,4) as unsigned) asc".format(father_table=father_table, son_table=son_table))

value = cursor.fetchall()
HIP_list = []
HD_list = []
Vmag_list = []
VTmag_list = []
B_V_list = []
Bt_Vt_list = []
Plx_list = []
e_Plx_list = []
MVt_list = []
MV_list = []
SpType_list = []

for (HIP_value, HD_value, Vmag_value, VTmag_value, B_V_value, Bt_Vt_value, Plx_value, e_Plx_value, MVt_value, MV_value, SpType_value) in value:
    HIP_list.append(HIP_value)
    HD_list.append(HD_value)
    Vmag_list.append(Vmag_value)
    VTmag_list.append(VTmag_value)
    B_V_list.append(B_V_value)
    Bt_Vt_list.append(Bt_Vt_value)
    Plx_list.append(Plx_value)
    e_Plx_list.append(e_Plx_value)
    MVt_list.append(MVt_value)
    MV_list.append(MV_value)
    SpType_list.append(SpType_value)

# process Vmag
for i in range(len(Vmag_list)):
    if Vmag_list[i] is not None:
        sinal = None
        if Vmag_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        Vmag_list[i] = abs(Vmag_list[i])
        Vmag_list[i] = round(Vmag_list[i], 2)
        Vmag_list[i] = f"{Vmag_list[i]:05.2f}"
        Vmag_list[i] = sinal + Vmag_list[i]

# process VTmag
for i in range(len(VTmag_list)):
    if VTmag_list[i] is not None:
        sinal = None
        if VTmag_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        VTmag_list[i] = abs(VTmag_list[i])
        VTmag_list[i] = round(VTmag_list[i], 2)
        VTmag_list[i] = f"{VTmag_list[i]:05.2f}"
        VTmag_list[i] = sinal + VTmag_list[i]

# process B_V
for i in range(len(B_V_list)):
    if B_V_list[i] is not None:
        sinal = None
        if B_V_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        B_V_list[i] = abs(B_V_list[i])
        B_V_list[i] = round(B_V_list[i], 2)
        B_V_list[i] = f"{B_V_list[i]:04.2f}"
        B_V_list[i] = sinal + B_V_list[i]

# process Bt_Vt
for i in range(len(Bt_Vt_list)):
    if Bt_Vt_list[i] is not None:
        sinal = None
        if Bt_Vt_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        Bt_Vt_list[i] = abs(Bt_Vt_list[i])
        Bt_Vt_list[i] = round(Bt_Vt_list[i], 2)
        Bt_Vt_list[i] = f"{Bt_Vt_list[i]:04.2f}"
        Bt_Vt_list[i] = sinal + Bt_Vt_list[i]

# process Plx
for i in range(len(Plx_list)):
    if Plx_list[i] is not None:
        sinal = None
        if Plx_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        Plx_list[i] = abs(Plx_list[i])
        Plx_list[i] = round(Plx_list[i], 2)
        Plx_list[i] = f"{Plx_list[i]:06.2f}"
        Plx_list[i] = sinal + Plx_list[i]

# process e_Plx
for i in range(len(e_Plx_list)):
    if e_Plx_list[i] is not None:
        e_Plx_list[i] = round(e_Plx_list[i], 2)
        e_Plx_list[i] = f"{e_Plx_list[i]:06.2f}"

# process MVt
for i in range(len(MVt_list)):
    if MVt_list[i] is not None:
        sinal = None
        if MVt_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        MVt_list[i] = abs(MVt_list[i])
        MVt_list[i] = round(MVt_list[i], 2)
        MVt_list[i] = f"{MVt_list[i]:05.2f}"
        MVt_list[i] = sinal + MVt_list[i]

# process MV
for i in range(len(MV_list)):
    if MV_list[i] is not None:
        sinal = None
        if MV_list[i] < 0:
            sinal = "-"
        else:
            sinal = "+"
        MV_list[i] = abs(MV_list[i])
        MV_list[i] = round(MV_list[i], 2)
        MV_list[i] = f"{MV_list[i]:05.2f}"
        MV_list[i] = sinal + MV_list[i]

cont = 0
with open("/home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/output_files/hipparcos/csv/estrelas_sem_dr3.txt", "w") as text_file:
    header = ["HIP", "HD", "Vmag", "VTmag", "B_V", "Bt_Vt", "Plx", "MVt", "MV", "SpType"]
    text_file.write("{0[0]:<7}" # HIP
                    "{0[1]:<7}" # HD
                    "{0[2]:<7}" # Vmag
                    "{0[3]:<7}" # VTmag
                    "{0[4]:<6}" # B_V
                    "{0[5]:<6}" # Bt_Vt
                    "{0[6]:<17}" # Plx
                    "{0[7]:<7}" # MVt
                    "{0[8]:<7}" # MV
                    "{0[9]:<0}" # SpType
                    "\n".format(header))
    for (HIP, HD, Vmag, VTmag, B_V, Bt_Vt, Plx, e_Plx, MVt, MV, SpType) in zip(HIP_list, HD_list, Vmag_list, VTmag_list, B_V_list, Bt_Vt_list, Plx_list, e_Plx_list, MVt_list, MV_list, SpType_list):
        if HIP is None:
            HIP = ""
        if HD is None:
            HD = ""
        if Vmag is None:
            Vmag = ""
        if VTmag is None:
            VTmag = ""
        if B_V is None:
            B_V = ""
        if Bt_Vt is None:
            Bt_Vt = ""
        if Plx is None:
            Plx = ""
        if e_Plx is None:
            e_Plx = ""
        if MVt is None:
            MVt = ""
        if MV is None:
            MV = ""
        if SpType is None:
            SpType = ""

        mais_ou_menos = ""
        if e_Plx != "":
            mais_ou_menos = "±"

        lista = [HIP[4:], HD[3:], Vmag, VTmag, B_V, Bt_Vt, Plx, e_Plx, MVt, MV, SpType, mais_ou_menos]
        text_file.write("{0[0]:<7}" # HIP
                        "{0[1]:<7}" # HD
                        "{0[2]:<7}" # Vmag
                        "{0[3]:<7}" # VTmag
                        "{0[4]:<6}" # B_V
                        "{0[5]:<6}" # Bt_Vt
                        "{0[6]:<8}" # Plx
                        "{0[11]:<2}" # +/-
                        "{0[7]:<7}" # e_Plx
                        "{0[8]:<7}" # MVt
                        "{0[9]:<7}" # MV
                        "{0[10]:<0}" # SpType
                        "\n".format(lista))
        cont += 1

print("Quantidade de estrelas no arquivo: ", cont)

cursor.close()
connection.close()