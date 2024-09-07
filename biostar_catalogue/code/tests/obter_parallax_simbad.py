import math
from math import nan

from astropy.coordinates import SkyCoord
from astroquery.simbad import Simbad

# Cmpos disponiveis
#print(Simbad.list_votable_fields())

# Add to the default field returned by Simbad:
Simbad.add_votable_fields('plx', 'distance', 'plx_error', 'parallax')

sim = Simbad.query_object('HIP 63882')
#print(sim.colnames)
#print('{:.10f}'.format(float(sim['PLX_VALUE'])))
print(sim['PLX_ERROR'])
print("sim['PLX_ERROR'][0]: ", sim['PLX_ERROR'][0])

print(type(sim['PLX_VALUE']))
print(len(sim['PLX_VALUE']))
print(type(sim['PLX_VALUE']))
#print(float(sim['PLX_VALUE']))
print(str(sim['PLX_VALUE'].mask[0]) == '--')
print(str(sim['PLX_VALUE'].mask) == '--')
print(str(sim['PLX_VALUE'].mask) == '[--]')
print(sim['PLX_VALUE'].mask[0])
print(str(sim['PLX_VALUE'][0]) == '--')
#print("sim['PLX_VALUE']: ", sim['PLX_VALUE'])
#print(sim['Distance_distance'])
#print(sim['PLX_ERROR'])
#print(sim['PLX_VALUE_2'])










