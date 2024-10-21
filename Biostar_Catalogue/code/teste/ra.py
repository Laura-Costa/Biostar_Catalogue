import math


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

print(deg2hms(243.90633606005997))
print(deg2dms(-8.371641161548801))