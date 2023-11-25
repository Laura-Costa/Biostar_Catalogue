
Aqui os tipos foram colocados tudo double:

CREATE TABLE Source (
	numero_ordinal_do_registro int not null auto_increment unique,
	designation char(100) PRIMARY KEY,
	ruwe double not null,
	parallax double not null,
	parallax_error double not null,
	phot_g_mean_mag double not null,
	phot_bp_mean_mag double not null,
	phot_rp_mean_mag double not null,
	teff_gspphot double not null,
	teff_gspphot_lower double not null,
	teff_gspphot_upper double not null,
	logg_gspphot double not null,
	logg_gspphot_lower double not null,
	logg_gspphot_upper double not null,
	mh_gspphot double not null,
	mh_gspphot_lower double not null,
	mh_gspphot_upper double not null,
	distance_gspphot double not null,
	distance_gspphot_lower double not null,
	distance_gspphot_upper double not null
);



CREATE TABLE Source_Hipparcos (
	numero_ordinal_do_registro int auto_increment PRIMARY KEY,
	Catalog double not null, 
	HIP double not null, 	
	Proxy double not null, 
	RAhms double not null, 
	DEdms double not null, 
	Vmag double not null, 
	VarFlag double not null, 
	r_Vmag double not null, 
	RAdeg double not null, 
	DEdeg double not null, 
	AstroRef double not null, 
	Plx double not null, 
	pmRA double not null, 
	pmDE double not null, 
	e_RAdeg double not null, 
	e_DEdeg double not null, 
	e_Plx double not null, 
	e_pmRA double not null, 
	e_pmDE double not null, 
	DE_RA double not null, 
	Plx_RA double not null, 
	Plx_DE double not null, 
	pmRA_RA double not null, 
	pmRA_DE double not null, 
	pmRA_Plx double not null, 
	pmDE_RA double not null, 
	pmDE_DE double not null, 
	pmDE_Plx double not null, 
	pmDE_pmRA double not null, 
	F1 double not null, 
	F2 double not null, 
	— double not null, 
	BTmag double not null, 
	e_BTmag double not null, 
	VTmag double not null, 
	e_VTmag double not null, 
	m_BTmag double not null, 
	B_V double not null, 
	e_B_V double not null, 
	r_B_V double not null, 
	V_I double not null, 
	e_V_I double not null, 
	r_V_I double not null, 
	CombMag double not null, 
	Hpmag double not null, 
	e_Hpmag double not null, 
	Hpscat double not null, 
	o_Hpmag double not null, 
	m_Hpmag double not null, 
	Hpmax double not null, 
	HPmin double not null, 
	Period double not null, 
	HvarType double not null, 
	moreVar double not null, 
	morePhoto double not null, 
	CCDM double not null, 
	n_CCDM double not null, 
	Nsys double not null, 
	Ncomp double not null, 
	MultFlag double not null, 
	Source double not null, 
	Qual double not null, 
	m_HIP double not null, 
	theta double not null, 
	rho double not null, 
	e_rho double not null, 
	dHp double not null, 
	e_dHp double not null,  
	Survey double not null, 
	Chart double not null, 
	Notes double not null, 
	HD double not null, 
	BD double not null, 
	CoD double not null, 
	CPD double not null, 
	V_Ired double not null, 
	SpType double not null, 
	r_SpType double not null
);	































