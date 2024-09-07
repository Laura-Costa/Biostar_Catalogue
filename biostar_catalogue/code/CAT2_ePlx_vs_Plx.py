import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
import pandas as pd

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

cursor.execute('''select TRIM(Hipparcos.e_Plx)+0, '''
               '''TRIM(Hipparcos.Plx)+0 '''
               '''from Hipparcos '''
               '''into outfile '/var/lib/mysql-files/Hipparcos_ePlx_Plx_sem_header.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

#header_list = ["e_Plx", "Plx"]
#file = pd.read_csv("/var/lib/mysql-files/Hipparcos_ePlx_Plx_sem_header.csv")
#file.to_csv("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/CAT2/Hipparcos_ePlx_Plx.csv", header=header_list, index=False)

cursor.close()
connection.close()

df = pd.read_table("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/Hipparcos_ePlx_Plx.csv", sep=',', header=None, names=['ePlx', 'Plx'])
print(df.describe())

# Create a Simple Scatter Plot
scatter_plot = sns.scatterplot(x=df['ePlx'], y=df['Plx'], s=3, color='black', edgecolor='black')
scatter_plot.set_xlabel('e_Plx (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('Plx (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_errors_seaborn.pdf")
plt.close()

# Logarithmic Scale
scatter_plot = sns.scatterplot(x=df['ePlx'], y=df['Plx'], s=3, color='black', edgecolor='black')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('e_Plx (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('Plx (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_errors_seaborn_logarithmic_scale.pdf")
plt.close()

# Create a Simple Scatter Plot (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['ePlx'], y=df['Plx'], s=3, color='black', edgecolor='black')
scatter_plot.set_xlabel('e_Plx (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('Plx (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_errors_seaborn_apresentation.pdf")
plt.close()

# Logarithmic Scale (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['ePlx'], y=df['Plx'], s=3, color='black', edgecolor='black')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('e_Plx (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('Plx (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Hipparcos_errors_seaborn_logarithmic_scale_apresentation.pdf")
plt.close()

