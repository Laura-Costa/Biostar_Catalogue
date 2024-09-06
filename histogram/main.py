import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

#Now I will read the file creating a Pandas DataFrame:
filename = 'Hipparcos_minus_Gaia_MV_versus_B_minus_V_red_dwarfs.csv'
df = pd.read_table(filename, skiprows=1, sep=',', header=None, index_col=0,
                   names = ['HIP', 'HD', 'BD', 'CoD', 'CPD', 'B-V', 'BT-VT', 'MV', 'MVt', 'SpType'],
                   skipfooter=0, engine='python')

print('***shape of the dataframe***')
print(df.shape)

print('')
print('***head of the dataframe***')
print(df.head())

print('')
print('***tail of the dataframe***')
print(df.tail())

# Rows that do not meet the condition alpha + num are eliminated
f = lambda s: (len(s) >= 1)  and (s[0].isalpha()) # and (s[1].isdigit())
i  = df['SpType'].apply(f)
df = df[i]

f = lambda s: s[0]
df['SpType2'] = df['SpType'].map(f)

print('***count number each class in df_clean***')
print(df['SpType2'].value_counts())
print('----------------')


print('***shape of the dataframe***')
print(df.shape)

print('')
print('***head of the dataframe***')
print(df.head())

print('')
print('***tail of the dataframe***')
print(df.tail())

f, ax = plt.subplots()
ax.hist(df['SpType2'], bins = 4)
plt.savefig('/home/lh/Downloads/histogram/teste.pdf')