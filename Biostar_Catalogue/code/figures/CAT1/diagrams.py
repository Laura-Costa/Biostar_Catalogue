import mysql.connector
import code.figures.functions as f
from code.figures.functions import diagram

connection = mysql.connector.connect(host='localhost', port='3306', database='Biostar_Catalogue', user='lh', password='ic2023')
cursor = connection.cursor()

father_table = 'Gaia50pc'
son_table = 'Gaia50pc_product'

"""
fazer um diagrama de M(Rp) x Bp-Rp
estrelas com parallax>=50.00 ou (parallax < 50.00 e parallax+3parallax_error>=50.00)
com Bp-Rp
são 2666 estrelas
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({son_table}.Bp_Rp)+0, "
         "trim({son_table}.MRp)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{son_table}.Bp_Rp is not null and "
         "{son_table}.MRp is not null".format(father_table=father_table, son_table=son_table))

query_emphasis = ("select {father_table}.designation, "
                  "trim({son_table}.Bp_Rp)+0, "
                  "trim({son_table}.MRp)+0 "
                  "from {father_table}, {son_table} "
                  "where {father_table}.designation = {son_table}.designation and "
                  "{father_table}.parallax is not null and "
                  "( "
                  "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                  ") and "
                  "{son_table}.Bp_Rp is not null and "
                  "{son_table}.MRp is not null and "
                  "{father_table}.phot_g_mean_mag is null "
                  "union all "
                  "select {father_table}.simbad_HD, "
                  "trim({son_table}.Bp_Rp)+0, "
                  "trim({son_table}.MRp)+0 "
                  "from {father_table}, {son_table} "
                  "where {father_table}.designation = {son_table}.designation and "
                  "{father_table}.parallax is not null and "
                  "( "
                  "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                  ") and "
                  "{son_table}.Bp_Rp is not null and "
                  "{son_table}.MRp is not null and "
                  "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 1 - MRp_Bp_Rp.pdf', 0.25, 1, 'Bp-Rp', 'M(Rp)', 1.5, 0.20, 0.20)

"""
fazer um diagrama de M(Rp) x G-Bp
estrelas com parallax>=50.00 ou (parallax < 50.00 e parallax+3parallax_error>=50.00)
com G, Bp e Rp
são 2665 estrelas
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0 as G_Bp, "
         "trim({son_table}.MRp)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{son_table}.MRp is not null".format(father_table=father_table, son_table=son_table))

query_emphasis = ("select {father_table}.simbad_HD, "
                  "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0 as G_Bp, "
                  "trim({son_table}.MRp)+0 "
                  "from {father_table}, {son_table} "
                  "where {father_table}.designation = {son_table}.designation and "
                  "{father_table}.parallax is not null and "
                  "( "
                  "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                  ") and "
                  "{father_table}.phot_g_mean_mag is not null and "
                  "{father_table}.phot_bp_mean_mag is not null and "
                  "{son_table}.MRp is not null and "
                  "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 3 - MRp_G_Bp.pdf', 0.25, 1, 'G-Bp', 'M(Rp)', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(Rp) x G - Rp
estrelas com parallax>=50.00 ou (parallax<50.00 e parallax+parallax_error>=50.00)
sem Bp
com G-Rp
são 3 estrelas
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0 as G_Rp, "
         "trim({son_table}.MRp)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.MRp is not null".format(father_table=father_table, son_table=son_table))

query_emphasis = ("select {father_table}.designation, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0 as G_Rp, "
         "trim({son_table}.MRp)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_bp_mean_mag is null and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.MRp is not null "
         "union all "
         "select {father_table}.simbad_HD, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0 as G_Rp, "
         "trim({son_table}.MRp)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "{father_table}.parallax > 0 and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 2 - MRp_G_Rp.pdf', 0.25, 1, 'G-Rp', 'M(Rp)', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(Bp) x G-Bp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
sem Rp
com Bp-G
é uma estrela
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.phot_bp_mean_mag)+0 - {father_table}.phot_g_mean_mag as Bp_G, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
         "from {father_table} "
         "where {father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null".format(father_table=father_table))

query_emphasis = ("select {father_table}.designation, "
         "trim({father_table}.phot_bp_mean_mag-{father_table}.phot_g_mean_mag)+0 as Bp_G, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
         "from {father_table} "
         "where {father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))"
         ") and "
         "{father_table}.phot_rp_mean_mag is null and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null "
         "union all "
         "select {father_table}.simbad_HD, "
         "trim({father_table}.phot_bp_mean_mag - {father_table}.phot_g_mean_mag)+0, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
         "from {father_table} "
         "where {father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table))

f.diagram(cursor, query, query_emphasis, 'diagram 6.1 - MBp_Bp_G.pdf', 0.25, 1, 'Bp-G', 'M(Bp)', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(Bp) x G-Bp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
sem Rp
com G-Bp
é uma estrela
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0 as G_Bp, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
         "from {father_table} "
         "where {father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null".format(father_table=father_table))

query_emphasis = ("select {father_table}.designation, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0 as G_Bp, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
         "from {father_table} "
         "where {father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error >= 50.00))"
         ") and "
         "{father_table}.phot_rp_mean_mag is null and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null "
         "union all "
         "select {father_table}.simbad_HD, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0 as G_Bp, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
         "from {father_table} "
         "where {father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 6 - MBp_G_Bp.pdf', 0.25, 1, 'G-Bp', 'M(Bp)', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(Bp) x G-Rp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
com G, Rp, Bp
2665 estrelas
"""

query =         ("select trim({father_table}.parallax)+0, "
                 "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0 as G_Rp, "
                 "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
                 "from {father_table} "
                 "where {father_table}.parallax is not null and "
                 "{father_table}.parallax > 0 and "
                 "( "
                 "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                 ") and "
                 "{father_table}.phot_g_mean_mag is not null and "
                 "{father_table}.phot_rp_mean_mag is not null and "
                 "{father_table}.phot_bp_mean_mag is not null".format(father_table=father_table))

query_emphasis = ("select {father_table}.simbad_HD, "
                  "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0 as G_Rp, "
                  "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 as MBp "
                  "from {father_table} "
                  "where {father_table}.parallax is not null and "
                  "{father_table}.parallax > 0 and "
                  "( "
                  "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
                  ") and "
                  "{father_table}.phot_g_mean_mag is not null and "
                  "{father_table}.phot_rp_mean_mag is not null and "
                  "{father_table}.phot_bp_mean_mag is not null and "
                  "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 5 - MBp_G_Rp.pdf', 0.25, 1, 'G-Rp', 'MBp', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(Bp) x Bp-Rp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
com Rp, Bp
2666 estrelas
1 estrela sem G
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({son_table}.Bp_Rp)+0, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "{father_table}.parallax > 0 and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.Bp_Rp is not null".format(son_table=son_table, father_table=father_table))

query_emphasis = ("select {father_table}.designation, "
         "trim({son_table}.Bp_Rp)+0, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "{father_table}.parallax > 0 and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.Bp_Rp is not null and "
         "{father_table}.phot_g_mean_mag is null "
         "union all "
         "select {father_table}.simbad_HD, "
         "trim({son_table}.Bp_Rp)+0, "
         "trim({father_table}.phot_bp_mean_mag + 5 + 5 * log(10, {father_table}.parallax / 1000.0))+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "{father_table}.parallax > 0 and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.Bp_Rp is not null and "
         "{father_table}.phot_g_mean_mag is null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 4 - MBp_Bp_Rp.pdf', 0.25, 1, 'Bp-Rp', 'MBp', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(G) x Bp-Rp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
com G, Rp, Bp
2665 estrelas
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({son_table}.Bp_Rp)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{son_table}.Bp_Rp is not null and "
         "{son_table}.MG is not null".format(father_table=father_table, son_table=son_table))

query_emphasis = ("select {father_table}.simbad_HD, "
         "trim({son_table}.Bp_Rp)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{son_table}.Bp_Rp is not null and "
         "{son_table}.MG is not null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 7 - MG_Bp_Rp.pdf', 0.25, 1, 'Bp-Rp', 'M(G)', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(G) x G-Rp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
com G, Rp
2668 estrelas
3 sem Bp
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.MG is not null".format(father_table=father_table, son_table=son_table))

query_emphasis = ("select {father_table}.designation, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.MG is not null and "
         "{father_table}.phot_bp_mean_mag is null "
         "union all "
         "select {father_table}.simbad_HD, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_rp_mean_mag)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_rp_mean_mag is not null and "
         "{son_table}.MG is not null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

diagram(cursor, query, query_emphasis, 'diagrama 8 - MG_G_Rp.pdf', 0.25, 1, 'G-Rp', 'M(G)', 1.5, 0.20, 0.20)

"""
Fazer um diagrama M(G) x G-Bp
estrelas com parallax>=50.00 ou (parallax<50.00 and parallax+parallax_error>=50.00)
com G, Bp
2666 estrelas
1 sem Rp
"""

query = ("select trim({father_table}.parallax)+0, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{son_table}.MG is not null".format(father_table=father_table, son_table=son_table))

query_emphasis = ("select {father_table}.designation, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{son_table}.MG is not null and "
         "{father_table}.phot_rp_mean_mag is null "
         "union all "
         "select {father_table}.simbad_HD, "
         "trim({father_table}.phot_g_mean_mag - {father_table}.phot_bp_mean_mag)+0, "
         "trim({son_table}.MG)+0 "
         "from {father_table}, {son_table} "
         "where {father_table}.designation = {son_table}.designation and "
         "{father_table}.parallax is not null and "
         "( "
         "{father_table}.parallax >= 50.00 or ({father_table}.parallax < 50.00 and ({father_table}.parallax + 3*{father_table}.parallax_error) >= 50.00)"
         ") and "
         "{father_table}.phot_g_mean_mag is not null and "
         "{father_table}.phot_bp_mean_mag is not null and "
         "{son_table}.MG is not null and "
         "{father_table}.simbad_HD in ('HD 146233', 'HD 4628', 'HD 16160', 'HD 32147', 'HD 191408', 'HD 219134')".format(father_table=father_table, son_table=son_table))

f.diagram(cursor, query, query_emphasis, 'diagrama 9 - MG_G_Bp.pdf', 0.25, 1, 'G-Bp', 'M(G)', 1.5, 0.20, 0.20)

# fechar a conexão com o BD
connection.close()
