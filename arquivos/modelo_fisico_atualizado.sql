mysql -u helena -p --local_infile
ic2023
set global local_infile='ON';
drop database gaia_catalog;
create database gaia_catalog;
use gaia_catalog;


create table Gaia (
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

create table Hipparcos (
	record_ordinal_number INT not null auto_increment primary key,
	HIP INT not null, 	
	Vmag NUMERIC(65,30) not null, 
	RAdeg NUMERIC(65,30) not null, 
	DEdeg NUMERIC(65,30) not null, 
	Plx NUMERIC(65,30) not null, 
	e_Plx NUMERIC(65,30) not null,
	pmRA NUMERIC(65,30) not null, 
	pmDE NUMERIC(65,30) not null, 
	BTmag NUMERIC(65,30) not null, 
	VTmag NUMERIC(65,30) not null, 
	B_V NUMERIC(65,30) not null
);	

create table Gaia_Diagram(
      name char(100) not null,
      diagram blob not null,
      description char(100),
      primary key (name)
);

create table Hipparcos_Diagram(
       name char(100) not null,
       diagram blob not null,
       description char(100),
       primary key (name)
);

create table Gaia_product (
     record_ordinal_number int primary key,
     Mg double not null,
     MRp double not null,
     Bp_minus_Rp double not null,
     Mg_error double not null,
     MRp_error double not null,
     foreign key (record_ordinal_number) references Gaia(record_ordinal_number) on delete restrict 
);

create table Hipparcos_product(
      record_ordinal_number int primary key,
      MV double not null,
      MVt double not null,
      B_minus_V double not null,
      BT_minus_VT double not null,
      MV_error double,
      MVt_error double,
      foreign key (record_ordinal_number) references Hipparcos(record_ordinal_number) on delete restrict 
);

create table Gaia_product_is_ploted_on(
      record_ordinal_number INT not null,
      name char(100) not null,
      primary key (record_ordinal_number, name),
      foreign key (record_ordinal_number) references Gaia_product(record_ordinal_number),
      foreign key (name) references Gaia_Diagram(name)
);

create table Hipparcos_product_is_ploted_on(
      record_ordinal_number INT not null,
      name char(100) not null,
      primary key (record_ordinal_number, name),
      foreign key (record_ordinal_number) references Hipparcos_product(record_ordinal_number),
      foreign key (name) references Hipparcos_Diagram(name)
);

create table matched(
	record_ordinal_number_gaia INT not null,
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
	distance_gspphot_upper NUMERIC(65,30) not null,
	record_ordinal_number_hipparcos INT not null,
	HIP INT not null, 	
	Vmag NUMERIC(65,30) not null, 
	RAdeg NUMERIC(65,30) not null, 
	DEdeg NUMERIC(65,30) not null, 
	Plx NUMERIC(65,30) not null, 
	e_Plx NUMERIC(65,30) not null,
	pmRA NUMERIC(65,30) not null, 
	pmDE NUMERIC(65,30) not null, 
	BTmag NUMERIC(65,30) not null, 
	VTmag NUMERIC(65,30) not null, 
	B_V NUMERIC(65,30) not null,
	primary key (record_ordinal_number_gaia, record_ordinal_number_hipparcos),
	foreign key (record_ordinal_number_gaia) references Gaia(record_ordinal_number),
	foreign key (record_ordinal_number_hipparcos) references Hipparcos(record_ordinal_number)
);


create table matched_python(
	record_ordinal_number_gaia INT not null,
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
	distance_gspphot_upper NUMERIC(65,30) not null,
	record_ordinal_number_hipparcos INT not null,
	HIP INT not null, 	
	Vmag NUMERIC(65,30) not null, 
	RAdeg NUMERIC(65,30) not null, 
	DEdeg NUMERIC(65,30) not null, 
	Plx NUMERIC(65,30) not null, 
	e_Plx NUMERIC(65,30) not null,
	pmRA NUMERIC(65,30) not null, 
	pmDE NUMERIC(65,30) not null, 
	BTmag NUMERIC(65,30) not null, 
	VTmag NUMERIC(65,30) not null, 
	B_V NUMERIC(65,30) not null,
	primary key (record_ordinal_number_gaia, record_ordinal_number_hipparcos),
	foreign key (record_ordinal_number_gaia) references Gaia(record_ordinal_number),
	foreign key (record_ordinal_number_hipparcos) references Hipparcos(record_ordinal_number)
);

==============================================================================================================

create table HIP_designation (
	HIP INT null, 	
	designation CHAR(100),
	primary key (designation)
);


