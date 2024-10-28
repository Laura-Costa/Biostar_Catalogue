import mysql.connector
import code.functions.pyplot_HRdiagram as f

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

colors = ['red', 'magenta', 'lime', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 146233', 'HD 191408', 'HD 219134']

def sql_query(y_axis, x_axis, y_error, x_error):
    table = 'Hipparcos'

    query_Hipparcos = ("select {table}.HD, "
             "trim({table}.{x_axis})+0, "
             "trim({table}.{x_axis})+0, "
             "trim({table}.{y_axis})+0, "
             "trim({table}.{x_error})+0, "
             "trim({table}.{y_error})+0 "
             "from {table} "
             "where {table}.{x_axis} is not null and "
             "{table}.{y_axis} is not null and "
             "{table}.{x_error} is not null and "
             "{table}.{y_error} is not null".format(table=table, y_axis=y_axis, x_axis=x_axis, y_error=y_error, x_error=x_error))

    query_Hipparcos39mas = ("select {table}.HD, "
             "trim({table}.{x_axis})+0, "
             "trim({table}.{x_axis})+0, "
             "trim({table}.{y_axis})+0, "
             "trim({table}.{x_error})+0, "
             "trim({table}.{y_error})+0 "
             "from {table} "
             "where {table}.{x_axis} is not null and "
             "{table}.{y_axis} is not null and "
             "{table}.{x_error} is not null and "
             "{table}.{y_error} is not null and "
             "{table}.{y_axis} >= 39.000 and ( "
             "simbad_DR1 is not null or "
             "simbad_DR2 is not null or "
             "simbad_DR3 is not null "
             ")".format(table=table, y_axis=y_axis, x_axis=x_axis, y_error=y_error, x_error=x_error))

    query_emphasis = ("select {table}.HD, "
                      "trim({table}.{x_axis})+0, "
                      "trim({table}.{y_axis})+0, "
                      "trim({table}.{x_error})+0, "
                      "trim({table}.{y_error})+0 "
                      "from {table} "
                      "where {table}.{x_axis} is not null and "
                      "{table}.{y_axis} is not null and "
                      "{table}.{x_error} is not null and "
                      "{table}.{y_error} is not null and "
                      "{table}.HD = ".format(table=table, y_axis=y_axis, x_axis=x_axis, y_error=y_error, x_error=x_error))
    return (query_Hipparcos, query_Hipparcos39mas, query_emphasis)

"""
fazer o diagrama de Plx x GaiaDR3_parallax
"""
(query_Hipparcos, query_Hiparcos39mas, query_emphasis) = sql_query('Plx', 'GaiaDR3_parallax', 'e_Plx', 'GaiaDR3_parallax_error')
f.diagram(cursor, query_Hipparcos, query_emphasis, colors, HDs,'Hipparcos/pyplot_scatterplot/error_bars_emphasis.jpg', 40.00, 40.0, 'paralaxe Gaia DR3', 'paralaxe Hipparcos', 0.5, 15.00, 15.00, 70.00, 70.00, 'Estrelas do Hipparcos com paralaxe no Gaia DR3', xrot=0, error_bars=True)

"""
fazer o diagrama de Plx x simbad_parallax
"""
(query_Hipparcos, query_Hipparcos39mas, query_emphasis) = sql_query('Plx', 'simbad_parallax', 'e_Plx', 'simbad_parallax_error')
f.diagram(cursor, query_Hipparcos, query_emphasis, colors, HDs,'Hipparcos/pyplot_scatterplot/simbad_error_bars_emphasis.jpg', 40.00, 40.0, 'paralaxe Simbad', 'paralaxe Hipparcos', 0.5, 40.00, 15.00, 70.00, 70.00, 'Estrelas do Hipparcos com paralaxe no Simbad', xrot=0, error_bars=True)

colors = ['red', 'magenta', 'lime', '#95a5a6', 'deepskyblue', 'gold', 'chocolate']
HDs = ['HD 4628', 'HD 16160', 'HD 32147', 'HD 131976', 'HD 146233', 'HD 191408', 'HD 219134']

f.diagram(cursor, query_Hipparcos39mas, query_emphasis, colors, HDs,'Hipparcos/pyplot_scatterplot/simbad_error_bars_emphasis_39mas.jpg', 40.00, 40.0, 'paralaxe Simbad', 'paralaxe Hipparcos', 0.5, 15.00, 15.00, 70.00, 120.00, 'Estrelas do CAT2 (Plx ≥ 39.00 mas) com designação Gaia DR1, DR2 ou DR3 no Simbad', xrot=0, error_bars=True)

# fechar a conexão com o BD
connection.close()