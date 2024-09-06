import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
import pandas as pd

connection = mysql.connector.connect(host='localhost', port='3306', database='biostar_catalogue', user='lh_mysql', password='ic2023', allow_local_infile=True)
cursor = connection.cursor()

cursor.execute("set global local_infile='ON'")

cursor.execute('''select TRIM(Gaia.parallax_error)+0, '''
               '''TRIM(Gaia.parallax)+0 '''
               '''from Gaia '''
               '''into outfile '/var/lib/mysql-files/Gaia_parallaxerror_parallax.csv' '''
               '''fields optionally enclosed by '"' terminated by ',' LINES TERMINATED BY '\n' ''')

cursor.close()
connection.close()

df = pd.read_table("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/Gaia_parallaxerror_parallax.csv", sep=',', header=None, names=['parallax_error', 'parallax'])
print(df.describe())

# Create a Simple Scatter Plot
scatter_plot = sns.scatterplot(x=df['parallax_error'], y=df['parallax'], s=3, color='black', edgecolor='black')
scatter_plot.set_xlabel('parallax_error (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('parallax (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Gaia_errors_seaborn.pdf")
plt.close()

# Logarithmic Scale
scatter_plot = sns.scatterplot(x=df['parallax_error'], y=df['parallax'], s=3, color='black', edgecolor='black')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('parallax_error (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('parallax (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Gaia_errors_seaborn_logarithmic_scale.pdf")
plt.close()

# Create a Simple Scatter Plot (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['parallax_error'], y=df['parallax'], s=3, color='black', edgecolor='black')
scatter_plot.set_xlabel('parallax_error (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('parallax (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Gaia_errors_seaborn_apresentation.pdf")
plt.close()

# Create a Simple Scatter Plot (apresentation)
sns.set(rc={'figure.figsize':(15, 8)})
sns.set_style('whitegrid')
scatter_plot = sns.scatterplot(x=df['parallax_error'], y=df['parallax'], s=3, color='black', edgecolor='black')
scatter_plot.set(xscale='log', yscale='log')
scatter_plot.set_xlabel('parallax_error (mas)', fontsize=12, fontweight='bold')
scatter_plot.set_ylabel('parallax (mas)', fontsize=12, fontweight='bold')
fig = scatter_plot.get_figure()
fig.savefig("/home/lh/Desktop/Catalogo_GAIA/biostar_catalogue/static/img/Gaia_errors_seaborn_logarithmic_scale_apresentation.pdf")
plt.close()