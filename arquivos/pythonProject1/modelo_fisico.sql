mysql -u helena -p --local_infile
sudo mysql --local_infile
ic2023 / e2.7182
set global local_infile='ON';








drop database gaia_catalogue_1;
create database gaia_catalogue_1;
use gaia_catalogue_1;


create table Gaia (
	record_ordinal_number INT not null auto_increment,
	designation CHAR(100) primary key,
	HIP INT,
	HD CHAR(100) null,
	ra NUMERIC(65,30) not null,
	declination NUMERIC(65,30) not null,
	parallax NUMERIC(65,30) not null,
	parallax_error NUMERIC(65,30) not null,
	pm NUMERIC(65,30) not null,
	pmra NUMERIC(65,30) not null,
	pmdec NUMERIC(65,30) not null,
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
	foreign key (HIP) references Hipparcos(HIP) on delete restrict 
);

create table Hipparcos (
	record_ordinal_number INT not null auto_increment,
	HIP INT primary key, 	
	HD CHAR(100) null,
	Vmag NUMERIC(65,30) not null, 
	RAdeg NUMERIC(65,30) not null, 
	DEdeg NUMERIC(65,30) not null,
	RAhms CHAR(100) not null,
	DEdms CHAR(100) not null,
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
     designation CHAR(100) primary key,
     Mg NUMERIC(65,30) not null,
     Mg_error NUMERIC(65,30) not null,
     MRp NUMERIC(65,30) not null,
     MRp_error NUMERIC(65,30) not null,
     Bp_minus_Rp NUMERIC(65,30) not null,   
     foreign key (designation) references Gaia(designation) on delete restrict 
);

create table Hipparcos_product(
      HIP INT primary key,
      MV NUMERIC(65,30) not null,
      MV_error NUMERIC(65,30) not null,
      MVt NUMERIC(65,30) not null,
      MVt_error NUMERIC(65,30) not null,
      B_minus_V NUMERIC(65,30) not null,
      BT_minus_VT NUMERIC(65,30) not null,
      foreign key (HIP) references Hipparcos(HIP) on delete restrict 
);

create table Gaia_product_is_ploted_on(
      designation CHAR(100) primary key,
      name char(100) not null,
      primary key (designation, name),
      foreign key (designation) references Gaia_product(designation),
      foreign key (name) references Gaia_Diagram(name)
);

create table Hipparcos_product_is_ploted_on(
      HIP INT primary key,
      name char(100) not null,
      primary key (HIP, name),
      foreign key (HIP) references Hipparcos_product(HIP),
      foreign key (name) references Hipparcos_Diagram(name)
);



















================================================================================================================
create table designation_HD_HIP (
	designation CHAR(100) primary key,
	HD CHAR(100) null,
	HIP INT null
);


create table Hipparcos_temp (
	record_ordinal_number INT not null auto_increment,
	HIP INT primary key, 	
	HD CHAR(100)not null,
	Vmag NUMERIC(65,30) not null, 
	RAdeg NUMERIC(65,30) not null, 
	DEdeg NUMERIC(65,30) not null, 
	RAhms CHAR(100) not null,
	DEdms CHAR(100) not null,
	Plx NUMERIC(65,30) not null, 
	e_Plx NUMERIC(65,30) not null,
	pmRA NUMERIC(65,30) not null, 
	pmDE NUMERIC(65,30) not null, 
	BTmag NUMERIC(65,30) not null, 
	VTmag NUMERIC(65,30) not null, 
	B_V NUMERIC(65,30) not null
);


create table Gaia_temp (
	record_ordinal_number INT not null auto_increment,
	designation CHAR(100) primary key,
	ra NUMERIC(65,30) not null,
	declination NUMERIC(65,30) not null,
	parallax NUMERIC(65,30) not null,
	parallax_error NUMERIC(65,30) not null,
	pm NUMERIC(65,30) not null,
	pmra NUMERIC(65,30) not null,
	pmdec NUMERIC(65,30) not null,
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
