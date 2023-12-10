load data local infile '/var/lib/mysql/data_Star.csv'
    into table Star
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    (@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9, @col10, @col11, @col12, @col13, @col14, @col15, @col16, @col17, @col18, @col19, @col20, @col21, @col22, @col23, @col24, @col25, @col26, @col27, @col28, @col29, @col30, @col31, @col32, @col33, @col34, @col35, @col36, @col37, @col38) 
	set 
	record_ordinal_number=@col1, 
	designation=@col2, 
	ra=@col3, 
	declination=@col4, 
	parallax=@col5,
	parallax_error=@col6, 
	ruwe=@col7, 
	phot_g_mean_mag=@col8, 
	phot_bp_mean_mag=@col9, 
	phot_rp_mean_mag=@col10, 
	teff_gspphot=@col11, 
	teff_gspphot_lower=@col12, 
	teff_gspphot_upper=@col13, 
	logg_gspphot=@col14, 
	logg_gspphot_lower=@col15, 
	logg_gspphot_upper=@col16, 
	mh_gspphot=@col17, 
	mh_gspphot_lower=@col18, 
	mh_gspphot_upper=@col19, 
	distance_gspphot=@col20, 
	distance_gspphot_lower=@col21, 
	distance_gspphot_upper=@col22, 
	HIP=@col23, 
	Vmag=@col24, 
	RAdeg=@col25, 
	DEdeg=@col26, 
	RAdeg_2016=@col27, 
	DEdeg_2016=@col28, 
	Plx=@col29, 
	pmRA=@col30, 
	pmDE=@col31, 
	e_Plx=@col32, 
	BTmag=@col33, 
	e_BTmag=@col34, 
	VTmag=@col35, 
	e_VTmag=@col36, 
	B_V=@col37, 
	e_B_V=@col38
;

