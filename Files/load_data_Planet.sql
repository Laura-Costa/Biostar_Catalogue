load data local infile '/var/lib/mysql/data_Planet.csv'
    into table Planet
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    (@col1, @col2, @col3, @col4, @col5, @col6, @col7, @col8, @col9) 
	set 
	record_ordinal_number=@col1,
	name=@col2,
	mass=@col3, 
	semi_major_axis=@col4,
	right_ascension=@col5,
	declination=@col6,   
	discovered=@col7,
	star_name=@col8,
	orbital_period=@col9
;
