alter table Star_Hipparcos
add column RAdeg_2016 NUMERIC(65,30) after RAdeg;

alter table Star_Hipparcos
add column DEdeg_2016 NUMERIC(65,30) after DEdeg;

update Star_Hipparcos
set RAdeg_2016 = RAdeg + (    (3.07234*15/3600) + (20.0468/3600)*(sin(RAdeg*(3.141592653589793238462643383279/180)))*(tan(DEdeg*(3.141592653589793238462643383279/180)))      )*16 + ((pmRA/1000)/3600)*16;

update Star_Hipparcos
set DEdeg_2016 = DEdeg + (     (20.0468/3600)*(cos(RAdeg*(3.141592653589793238462643383279/180)))         )*16 +       ((pmDE/1000)/3600)*16;




-- consulta para achar a estrela GAIA que o planeta orbita

SELECT Star_Gaia.record_ordinal_number as record_ordinal_number, Planet_join_Hipparcos.name as name, Planet_join_Hipparcos.mass as mass, Planet_join_Hipparcos.semi_major_axis as semi_major_axis, Planet_join_Hipparcos.RAdeg_2016 as right_ascension, Planet_join_Hipparcos.DEdeg_2016 as declination, Planet_join_Hipparcos.discovered as discovered, Planet_join_Hipparcos.star_name as star_name, Planet_join_Hipparcos.orbital_period as orbital_period
FROM (SELECT Planet.name, Planet.mass, Planet.semi_major_axis, Planet.discovered, Planet.star_name, Planet.orbital_period, Star_Hipparcos.RAdeg_2016, Star_Hipparcos.DEdeg_2016 
FROM Planet LEFT OUTER JOIN Star_Hipparcos
ON Planet.right_ascension = Star_Hipparcos.RAdeg AND Planet.declination = Star_Hipparcos.DEdeg AND Star_Hipparcos.RAdeg != 0 AND Star_Hipparcos.DEdeg != 0) AS Planet_join_Hipparcos LEFT OUTER JOIN Star_Gaia 
ON ABS(RAdeg_2016 - Star_Gaia.ra)<=0.0003 AND ABS(DEdeg_2016 - Star_Gaia.declination)<=0.0003 
ORDER BY Star_Gaia.record_ordinal_number ASC
INTO OUTFILE '/var/lib/mysql/data_Planet.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
LINES TERMINATED BY '\n';

