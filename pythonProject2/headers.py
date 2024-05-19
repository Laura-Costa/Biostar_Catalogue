import csv

import pandas as pd

file = pd.read_csv("Gaia_without_header.csv", delimiter=',')

print(file)

# list header
headerList = ['designation', 'HIP', 'HD', 'ra', 'declination', 'parallax', 'parallax_error', 'pm', 'pmra', 'pmdec',
              'ruwe', 'phot_g_mean_mag', 'phot_bp_mean_mag', 'phot_rp_mean_mag', 'teff_gspphot', 'teff_gspphot_lower',
              'teff_gspphot_upper', 'logg_gspphot', 'logg_gspphot_lower', 'logg_gspphot_upper', 'mh_gspphot',
              'mh_gspphot_lower', 'mh_gspphot_upper', 'distance_gspphot', 'distance_gspphot_lower', 'distance_gspphot_upper',
              'Mg', 'Mg_error', 'MRp', 'MRp_error', 'Bp_minus_Rp']

file.to_csv("Gaia.csv", header=headerList, index=False, quoting=csv.QUOTE_NONNUMERIC)
