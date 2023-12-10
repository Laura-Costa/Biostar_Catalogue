	drop database Catalogo_Gaia;
	create database Catalogo_Gaia;
	use Catalogo_Gaia;

	create table Star (
		record_ordinal_number INT not null auto_increment primary key, 
		designation CHAR(100) not null, 
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
		HIP INT not null, 
		Vmag NUMERIC(65,30), 
		RAdeg NUMERIC(65,30), 
		DEdeg NUMERIC(65,30), 
		RAdeg_2016 NUMERIC(65,30), 
		DEdeg_2016 NUMERIC(65,30), 
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


	create table Property (
	     record_ordinal_number INT not null auto_increment primary key,
	     Mg NUMERIC(65,30) not null,
	     MRp NUMERIC(65,30) not null,
	     Bp_minus_Rp NUMERIC(65,30) not null,
	     MVt NUMERIC(65,30) not null,
	     MV NUMERIC(65,30) not null,
	     B_minusV NUMERIC(65,30) not null,
	     BT_minus_VT NUMERIC(65,30) not null,
	     Mg_error NUMERIC(65,30) not null,
	     MRp_error NUMERIC(65,30) not null,
	     MVt_error NUMERIC(65,30) not null,
	     MV_error NUMERIC(65,30) not null,
	     foreign key (record_ordinal_number) references Star(record_ordinal_number) on delete cascade 
	);


	create table Diagram(
	      diagram BLOB not null,
	      axis CHAR(10),
	      parallax NUMERIC(65,30),
	      primary key (axis, parallax)
	);

	create table Generate(
	      record_ordinal_number INT not null auto_increment,
	      parallax NUMERIC(65,30) not null,
	      axis CHAR(10) not null,

	      foreign key (record_ordinal_number) references Star(record_ordinal_number) on delete cascade,
	      foreign key (axis, parallax) references Diagram(axis, parallax) on delete cascade,
	      primary key (record_ordinal_number, parallax, axis)
	);

	create table Planet(
	      record_ordinal_number INT,
	      name CHAR(100),
	      mass NUMERIC(65,30), 
	      semi_major_axis NUMERIC(65,30),
	      right_ascension NUMERIC(65,30),
	      declination NUMERIC(65,30),   
	      discovered INT,
	      star_name CHAR(100),
	      orbital_period NUMERIC(65,30),
	      primary key(name)
	      foreign key (record_ordinal_number) references Star(record_ordinal_number),
	);

