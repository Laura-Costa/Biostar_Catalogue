from astroquery.simbad import Simbad
tab = Simbad.query_objectids('Gaia DR3 4345775217221821312')
print([id for id in tab['ID'] if id.startswith('HIP')])