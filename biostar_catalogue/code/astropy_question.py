from astroquery.simbad import Simbad

tab = Simbad.query_objectids("HIP " + str(79672))

print([id for id in tab['ID'] if id.startswith('Gaia DR3')][0])
