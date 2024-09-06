import matplotlib.pyplot as plt
import numpy as np

x = {'M':243, 'K':54, 'A':1, 'G':1}

keys = x.keys()
vals = x.values()

plt.bar(keys, vals)

plt.ylim(0,245)
plt.ylabel ('quantidade de estrelas')
plt.xlabel ('tipo espectral')
plt.yticks()
plt.xticks(list(keys))

plt.savefig('/home/lh/Downloads/histogram/teste2.pdf')