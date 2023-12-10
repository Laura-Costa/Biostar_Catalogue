drop database tratamento_dataset_Planet;
create database tratamento_dataset_Planet; 
use tratamento_dataset_Planet;

create table Star_Gaia (
	record_ordinal_number INT not null auto_increment primary key,
	designation CHAR(100),
	ra NUMERIC(65,30) not null,
	declination NUMERIC(65,30) not null,
	parallax NUMERIC(65,30) not null,
	parallax_error NUMERIC(65,30) not null,
	ruwe NUMERIC(65,30) not null,
	phot_g_mean_mag NUMERIC(65,30) not null,
	phot_bp_mean_mag NUMERIC(65,30) not null,
	phot_rp_mean_mag NUMERIC(65,30) not null,
	teff_gspphot NUMERIC(65,30) not null,
	teff_gspphot_lower NUMERIC(65,30) not null,
	teff_gspphot_upper NUMERIC(65,30) not null,
	logg_gspphot NUMERIC(65,30) not null,
	logg_gspphot_lower NUMERIC(65,30) not null, 
	logg_gspphot_upper NUMERIC(65,30) not null,
	mh_gspphot NUMERIC(65,30) not null,
	mh_gspphot_lower NUMERIC(65,30) not null,
	mh_gspphot_upper NUMERIC(65,30) not null,
	distance_gspphot NUMERIC(65,30) not null,
	distance_gspphot_lower NUMERIC(65,30) not null,
	distance_gspphot_upper NUMERIC(65,30) not null
);
	
create table Star_Hipparcos (
	record_ordinal_number INT not null auto_increment primary key,
	HIP LONG, 	
	Vmag NUMERIC(65,30), 
	RAdeg NUMERIC(65,30), 
	DEdeg NUMERIC(65,30), 
	Plx NUMERIC(65,30), 
	pmRA NUMERIC(65,30), 
	pmDE NUMERIC(65,30), 
	e_Plx NUMERIC(65,30), 
	BTmag NUMERIC(65,30), 
	e_BTmag NUMERIC(65,30), 
	VTmag NUMERIC(65,30), 
	e_VTmag NUMERIC(65,30), 
	B_V NUMERIC(65,30), 
	e_B_V NUMERIC(65,30)
);	

create table Planet(
	      discovered INT,
	      star_name CHAR(100),
	      name CHAR(100),
	      mass NUMERIC(65,30), 
	      semi_major_axis NUMERIC(65,30),
	      right_ascension NUMERIC(65,30),
	      declination NUMERIC(65,30),
	      orbital_period NUMERIC(65,30),
	      primary key(name)
);

