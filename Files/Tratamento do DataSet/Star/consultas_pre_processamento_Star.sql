alter table Star_Hipparcos
add column RAdeg_2016 NUMERIC(65,30) after RAdeg;

alter table Star_Hipparcos
add column DEdeg_2016 NUMERIC(65,30) after DEdeg;


update Star_Hipparcos
set RAdeg_2016 = RAdeg + (3.07234*15/3600 + (20.0468/3600)*(sin(RAdeg))*(tan(DEdeg)))*16 + ((pmRA/1000)/3600)*16;

update Star_Hipparcos
set DEdeg_2016 = DEdeg + ((20.0468/3600)*(cos(RAdeg)))*16 + ((pmDE/1000)/3600)*16;

select HIP, designation, RAdeg, DEdeg, RAdeg_2016, DEdeg_2016, ra, declination
from Star_Hipparcos, Star_Gaia
where (ra between (RAdeg_2016 + 0.0003) and (RAdeg_2016 - 0.0003)) and (declination between (DEdeg_2016 + 0.0003) and (DEdeg_2016 - 0.0003));



select HIP, designation, RAdeg, ra, declination
from Star_Hipparcos, Star_Gaia
where (ra between (RAdeg_2016 + 0.0003) and (RAdeg_2016 - 0.0003)) and (declination between (DEdeg_2016 + 0.0003) and (DEdeg_2016 - 0.0003));



select RAdeg_2016, DEdeg_2016 from Star_Hipparcos where HIP=79672;


select (declination - DEdeg_2016)*3600/15 from Star_Gaia, Star_Hipparcos where designation='Gaia DR3 4345775217221821312' and HIP=79672;


select (ra - RAdeg_2016)*3600/15 from Star_Gaia, Star_Hipparcos where designation='Gaia DR3 4345775217221821312' and HIP=79672;


==========================================================================================================================


alter table Star_Hipparcos
add column RAdeg_2016 NUMERIC(65,30) after RAdeg;

alter table Star_Hipparcos
add column DEdeg_2016 NUMERIC(65,30) after DEdeg;


update Star_Hipparcos
set RAdeg_2016 = RAdeg + (3.07234*15/3600 + (20.0468/3600)*(sin(RAdeg*PI/180))*(tan(DEdeg*PI/180)))*16 + ((pmRA/1000)/3600)*16;

update Star_Hipparcos
set DEdeg_2016 = DEdeg + ((20.0468/3600)*(cos(RAdeg*PI/180)))*16 + ((pmDE/1000)/3600)*16;

select HIP, designation, ra, declination
from Star_Hipparcos, Star_Gaia
where ABS(ra-RAdeg_2016) <= 0.0003 and ABS(declination-DEdeg_2016) <= 0.0003;



select HIP, designation, RAdeg, ra, declination
from Star_Hipparcos, Star_Gaia
where (ra between (RAdeg_2016 + 0.0003) and (RAdeg_2016 - 0.0003)) and (declination between (DEdeg_2016 + 0.0003) and (DEdeg_2016 - 0.0003));



select RAdeg_2016, DEdeg_2016 from Star_Hipparcos where HIP=79672;
=====================================================================
select abs(declination - DEdeg_2016) from Star_Gaia, Star_Hipparcos where designation='Gaia DR3 4345775217221821312' and HIP=79672;


select abs(ra - RAdeg_2016) from Star_Gaia, Star_Hipparcos where designation='Gaia DR3 4345775217221821312' and HIP=79672;

=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================

alter table Star_Hipparcos
add column RAdeg_2016 NUMERIC(65,30) after RAdeg;

alter table Star_Hipparcos
add column DEdeg_2016 NUMERIC(65,30) after DEdeg;



update Star_Hipparcos
set RAdeg_2016 = RAdeg + ((3.07234*15/3600) + (20.0468/3600)*(sin(RAdeg*(3.141592653589793238462643383279)/180))*(tan(DEdeg*(3.141592653589793238462643383279)/180)))*16 + ((pmRA/1000)/3600)*16;

update Star_Hipparcos
set DEdeg_2016 = DEdeg + ((20.0468/3600)*(cos(RAdeg*(3.141592653589793238462643383279)/180)))*16 + ((pmDE/1000)/3600)*16;



select HIP, designation, ra, declination
from Star_Hipparcos, Star_Gaia
where ABS(ra-RAdeg_2016) <= 0.0003 and ABS(declination-DEdeg_2016) <= 0.0003;

select ra, declination from Star_Gaia where designation='Gaia DR3 4345775217221821312';
select RAdeg_2016, DEdeg_2016 from Star_Hipparcos where HIP=79672;


=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================
=========================================================================================

alter table Star_Hipparcos
add column RAdeg_2016 NUMERIC(65,30) after RAdeg;

alter table Star_Hipparcos
add column DEdeg_2016 NUMERIC(65,30) after DEdeg;



update Star_Hipparcos
set RAdeg_2016 = RAdeg + (    (3.07234*15/3600) + (20.0468/3600)*(sin(RAdeg*(3.141592653589793238462643383279/180)))*(tan(DEdeg*(3.141592653589793238462643383279/180)))      )*16 + ((pmRA/1000)/3600)*16;

update Star_Hipparcos
set DEdeg_2016 = DEdeg + (     (20.0468/3600)*(cos(RAdeg*(3.141592653589793238462643383279/180)))         )*16 +       ((pmDE/1000)/3600)*16;


	
select HIP, designation, ra, declination
from Star_Hipparcos, Star_Gaia
where ABS(ra-RAdeg_2016) <= 0.0003 and ABS(declination-DEdeg_2016) <= 0.0003;

select ra, declination from Star_Gaia where designation='Gaia DR3 4345775217221821312';
select RAdeg_2016, DEdeg_2016 from Star_Hipparcos where HIP=79672;
============================================================================================================================
============================================================================================================================
============================================================================================================================
============================================================================================================================

alter table Star_Hipparcos
add column RAdeg_2016 NUMERIC(65,30) after RAdeg;

alter table Star_Hipparcos
add column DEdeg_2016 NUMERIC(65,30) after DEdeg;



update Star_Hipparcos
set RAdeg_2016 = RAdeg + (    (3.07234*15/3600) + (20.0468/3600)*(sin(RAdeg*(3.141592653589793238462643383279/180)))*(tan(DEdeg*(3.141592653589793238462643383279/180)))      )*16 + ((pmRA/1000)/3600)*16;

update Star_Hipparcos
set DEdeg_2016 = DEdeg + (     (20.0468/3600)*(cos(RAdeg*(3.141592653589793238462643383279/180)))         )*16 +       ((pmDE/1000)/3600)*16;



select Star_Gaia.record_ordinal_number as record_ordinal_number, designation, ra, declination, parallax,
parallax_error, ruwe, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, teff_gspphot, teff_gspphot_lower, teff_gspphot_upper, logg_gspphot, logg_gspphot_lower, logg_gspphot_upper, mh_gspphot, mh_gspphot_lower, mh_gspphot_upper, distance_gspphot, distance_gspphot_lower, distance_gspphot_upper, HIP, Vmag, RAdeg, DEdeg, RAdeg_2016, DEdeg_2016, Plx, pmRA, pmDE, e_Plx, BTmag, e_BTmag, VTmag, e_VTmag, B_V, e_B_V
from Star_Gaia left outer join Star_Hipparcos
ON  ABS(ra-RAdeg_2016) <= 0.0003 AND ABS(declination-DEdeg_2016) <= 0.0003
INTO OUTFILE '/var/lib/mysql/data_Star.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
LINES TERMINATED BY '\n';


cd /var/log/mysql
sudo mv data_Star.csv /home/h/'Área de trabalho'/Catalogo_GAIA/Files
vim arq.csv



