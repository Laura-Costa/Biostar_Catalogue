
create database Catalogo_Gaia;
use Catalogo_Gaia;

create table Star (
	record_ordinal_number int not null auto_increment primary key,
	designation char(100),
	ra double not null,
	declination double not null,
	parallax double not null,
	parallax_error float not null,
	pmra double not null,
	pmdec double not null,
	ruwe float not null,
	phot_g_mean_mag float not null,
	phot_bp_mean_mag float not null,
	phot_rp_mean_mag float not null,
	teff_gspphot float not null,
	teff_gspphot_lower float not null,
	teff_gspphot_upper float not null,
	logg_gspphot float not null,
	logg_gspphot_lower float not null, 
	logg_gspphot_upper float not null,
	mh_gspphot float not null,
	mh_gspphot_lower float not null,
	mh_gspphot_upper float not null,
	distance_gspphot float not null,
	distance_gspphot_lower float not null,
	distance_gspphot_upper float not null,
	HIP long not null, 	
	Vmag double, 
	RAdeg double, 
	DEdeg double, 
	Plx double, 
	BTmag double, 
	VTmag double, 
	B_V double
);	


create table Property (
     record_ordinal_number int not null auto_increment primary key,
     Mg double not null,
     MRp double not null,
     Bp_minus_Rp double not null,
     MVt double not null,
     MV double not null,
     B_minusV double not null,
     BT_minus_VT double not null,
     Mg_error double not null,
     MRp_error double not null,
     MVt_error double not null,
     MV_error double not null,
     foreign key (record_ordinal_number) references Star(record_ordinal_number) on delete cascade 
);


create table Diagram(
      diagram blob not null,
      axis char(10),
      parallax double,
      primary key (axis, parallax)
);

create table Generate(
      record_ordinal_number int not null auto_increment,
      parallax double not null,
      axis char(10) not null,

      foreign key (record_ordinal_number) references Star(record_ordinal_number) on delete cascade,
      foreign key (axis, parallax) references Diagram(axis, parallax) on delete cascade,
      primary key (record_ordinal_number, parallax, axis)
);

create table Planet(
      name char(30),
      record_ordinal_number int null,
      mass double, 
      semi_major_axis double,
      RAdeg double,
      DEdeg double,
      foreign key (record_ordinal_number) references Star(record_ordinal_number),
      primary key(name)
);


























