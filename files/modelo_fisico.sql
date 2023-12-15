drop database catalogo_gaia;
create database catalogo_gaia;
use catalogo_gaia;


create table Source_Gaia (
	numero_ordinal_do_registro INT not null auto_increment primary key,
	solution_id NUMERIC(65,30) not null,
	designation CHAR(100),
	source_id NUMERIC(65,30) not null,
	random_index NUMERIC(65,30) not null,
	ref_epoch NUMERIC(65,30) not null,
	ra NUMERIC(65,30) not null,
	ra_error NUMERIC(65,30) not null,
	declination NUMERIC(65,30) not null,
	dec_error NUMERIC(65,30) not null,
	parallax NUMERIC(65,30) not null,
	parallax_error NUMERIC(65,30) not null,
	parallax_over_error NUMERIC(65,30) not null,
	pm NUMERIC(65,30) not null,
	pmra NUMERIC(65,30) not null,
	pmra_error NUMERIC(65,30) not null,
	pmdec NUMERIC(65,30) not null,
	pmdec_error NUMERIC(65,30) not null,
	ra_dec_corr NUMERIC(65,30) not null,
	ra_parallax_corr NUMERIC(65,30) not null,
	ra_pmra_corr NUMERIC(65,30) not null,
	ra_pmdec_corr NUMERIC(65,30) not null,
	dec_parallax_corr NUMERIC(65,30) not null,
	dec_pmra_corr NUMERIC(65,30) not null,
	dec_pmdec_corr NUMERIC(65,30) not null,
	parallax_pmra_corr NUMERIC(65,30) not null,
	parallax_pmdec_corr NUMERIC(65,30) not null,
	pmra_pmdec_corr NUMERIC(65,30) not null,
	astrometric_n_obs_al NUMERIC(65,30) not null,
	astrometric_n_obs_ac NUMERIC(65,30) not null,
	astrometric_n_good_obs_al NUMERIC(65,30) not null,
	astrometric_n_bad_obs_al NUMERIC(65,30) not null,
	astrometric_gof_al NUMERIC(65,30) not null,
	astrometric_chi2_al NUMERIC(65,30) not null,
	astrometric_excess_noise NUMERIC(65,30) not null,
	astrometric_excess_noise_sig NUMERIC(65,30) not null,
	astrometric_params_solved NUMERIC(65,30) not null,
	astrometric_primary_flag boolean not null,
	nu_eff_used_in_astrometry NUMERIC(65,30) not null,
	pseudocolour NUMERIC(65,30) not null,
	pseudocolour_error NUMERIC(65,30) not null,
	ra_pseudocolour_corr NUMERIC(65,30) not null,
	dec_pseudocolour_corr NUMERIC(65,30) not null,
	parallax_pseudocolour_corr NUMERIC(65,30) not null,
	pmra_pseudocolour_corr NUMERIC(65,30) not null,
	pmdec_pseudocolour_corr NUMERIC(65,30) not null,
	astrometric_matched_transits NUMERIC(65,30) not null,
	visibility_periods_used NUMERIC(65,30) not null,
	astrometric_sigma5d_max NUMERIC(65,30) not null,
	matched_transits NUMERIC(65,30) not null,
	new_matched_transits NUMERIC(65,30) not null,
	matched_transits_removed NUMERIC(65,30) not null,
	ipd_gof_harmonic_amplitude NUMERIC(65,30) not null,
	ipd_gof_harmonic_phase NUMERIC(65,30) not null,
	ipd_frac_multi_peak NUMERIC(65,30) not null,
	ipd_frac_odd_win NUMERIC(65,30) not null,
	ruwe NUMERIC(65,30) not null,
	scan_direction_strength_k1 NUMERIC(65,30) not null,
	scan_direction_strength_k2 NUMERIC(65,30) not null,
	scan_direction_strength_k3 NUMERIC(65,30) not null,
	scan_direction_strength_k4 NUMERIC(65,30) not null,
	scan_direction_mean_k1 NUMERIC(65,30) not null,
	scan_direction_mean_k2 NUMERIC(65,30) not null,
	scan_direction_mean_k3 NUMERIC(65,30) not null,
	scan_direction_mean_k4 NUMERIC(65,30) not null,
	duplicated_source boolean not null,
	phot_g_n_obs NUMERIC(65,30) not null,
	phot_g_mean_flux NUMERIC(65,30) not null,
	phot_g_mean_flux_error NUMERIC(65,30) not null,
	phot_g_mean_flux_over_error NUMERIC(65,30) not null,
	phot_g_mean_mag NUMERIC(65,30) not null,
	phot_bp_n_obs NUMERIC(65,30) not null,
	phot_bp_mean_flux NUMERIC(65,30) not null,
	phot_bp_mean_flux_error NUMERIC(65,30) not null,
	phot_bp_mean_flux_over_error NUMERIC(65,30) not null,
	phot_bp_mean_mag NUMERIC(65,30) not null,
	phot_rp_n_obs NUMERIC(65,30) not null,
	phot_rp_mean_flux NUMERIC(65,30) not null,
	phot_rp_mean_flux_error NUMERIC(65,30) not null,
	phot_rp_mean_flux_over_error NUMERIC(65,30) not null,
	phot_rp_mean_mag NUMERIC(65,30) not null,
	phot_bp_rp_excess_factor NUMERIC(65,30) not null,
	phot_bp_n_contaminated_transits NUMERIC(65,30) not null,
	phot_bp_n_blended_transits NUMERIC(65,30) not null,
	phot_rp_n_contaminated_transits NUMERIC(65,30) not null,
	phot_rp_n_blended_transits NUMERIC(65,30) not null,
	phot_proc_mode NUMERIC(65,30) not null,
	bp_rp NUMERIC(65,30) not null,
	bp_g NUMERIC(65,30) not null,
	g_rp NUMERIC(65,30) not null,
	radial_velocity NUMERIC(65,30) not null,
	radial_velocity_error NUMERIC(65,30) not null, 
	rv_method_used NUMERIC(65,30) not null, 	
	rv_nb_transits NUMERIC(65,30) not null, 
	rv_nb_deblended_transits NUMERIC(65,30) not null,
	rv_visibility_periods_used NUMERIC(65,30) not null, 
	rv_expected_sig_to_noise NUMERIC(65,30) not null, 
	rv_renormalised_gof NUMERIC(65,30) not null, 
	rv_chisq_pvalue NUMERIC(65,30) not null, 
	rv_time_duration NUMERIC(65,30) not null,
	rv_amplitude_robust NUMERIC(65,30) not null,
	rv_template_teff NUMERIC(65,30) not null,
	rv_template_logg NUMERIC(65,30) not null,
	rv_template_fe_h NUMERIC(65,30) not null,
	rv_atm_param_origin NUMERIC(65,30) not null,
	vbroad NUMERIC(65,30) not null,
	vbroad_error NUMERIC(65,30) not null,
	vbroad_nb_transits NUMERIC(65,30) not null,
	grvs_mag NUMERIC(65,30) not null,
	grvs_mag_error NUMERIC(65,30) not null,
	grvs_mag_nb_transits NUMERIC(65,30) not null,
	rvs_spec_sig_to_noise NUMERIC(65,30) not null,
	phot_variable_flag CHAR(100) not null,
	galactic_longitude NUMERIC(65,30) not null,
	galactic_latitude NUMERIC(65,30) not null,
	ecl_lon NUMERIC(65,30) not null,
	ecl_lat NUMERIC(65,30) not null,
	in_qso_candidates boolean not null,
	in_galaxy_candidates boolean not null,
	non_single_star NUMERIC(65,30) not null,
	has_xp_continuous boolean not null,
	has_xp_sampled boolean not null,
	has_rvs boolean not null,
	has_epoch_photometry boolean not null,
	has_epoch_rv boolean not null,
	has_mcmc_gspphot boolean not null,
	has_mcmc_msc boolean not null,
	in_andromeda_survey boolean not null,
	classprob_dsc_combmod_quasar NUMERIC(65,30) not null,
	classprob_dsc_combmod_galaxy NUMERIC(65,30) not null,
	classprob_dsc_combmod_star NUMERIC(65,30) not null,
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
	azero_gspphot NUMERIC(65,30) not null,
	azero_gspphot_lower NUMERIC(65,30) not null,
	azero_gspphot_upper NUMERIC(65,30) not null,
	ag_gspphot NUMERIC(65,30) not null,
	ag_gspphot_lower NUMERIC(65,30) not null,
	ag_gspphot_upper NUMERIC(65,30) not null,
	ebpminrp_gspphot NUMERIC(65,30) not null,
	ebpminrp_gspphot_lower NUMERIC(65,30) not null,
	ebpminrp_gspphot_upper NUMERIC(65,30) not null,
	libname_gspphot CHAR(100) not null
);



create table Source_Hipparcos (
	numero_ordinal_do_registro INT not null auto_increment primary key,
	Catalog NUMERIC(65,30) not null, 
	HIP NUMERIC(65,30) not null, 	
	Proxy NUMERIC(65,30) not null, 
	RAhms NUMERIC(65,30) not null, 
	DEdms NUMERIC(65,30) not null, 
	Vmag NUMERIC(65,30) not null, 
	VarFlag NUMERIC(65,30) not null, 
	r_Vmag NUMERIC(65,30) not null, 
	RAdeg NUMERIC(65,30) not null, 
	DEdeg NUMERIC(65,30) not null, 
	AstroRef NUMERIC(65,30) not null, 
	Plx NUMERIC(65,30) not null, 
	pmRA NUMERIC(65,30) not null, 
	pmDE NUMERIC(65,30) not null, 
	e_RAdeg NUMERIC(65,30) not null, 
	e_DEdeg NUMERIC(65,30) not null, 
	e_Plx NUMERIC(65,30) not null, 
	e_pmRA NUMERIC(65,30) not null, 
	e_pmDE NUMERIC(65,30) not null, 
	DE_RA NUMERIC(65,30) not null, 
	Plx_RA NUMERIC(65,30) not null, 
	Plx_DE NUMERIC(65,30) not null, 
	pmRA_RA NUMERIC(65,30) not null, 
	pmRA_DE NUMERIC(65,30) not null, 
	pmRA_Plx NUMERIC(65,30) not null, 
	pmDE_RA NUMERIC(65,30) not null, 
	pmDE_DE NUMERIC(65,30) not null, 
	pmDE_Plx NUMERIC(65,30) not null, 
	pmDE_pmRA NUMERIC(65,30) not null, 
	F1 NUMERIC(65,30) not null, 
	F2 NUMERIC(65,30) not null, 
	— NUMERIC(65,30) not null, 
	BTmag NUMERIC(65,30) not null, 
	e_BTmag NUMERIC(65,30) not null, 
	VTmag NUMERIC(65,30) not null, 
	e_VTmag NUMERIC(65,30) not null, 
	m_BTmag NUMERIC(65,30) not null, 
	B_V NUMERIC(65,30) not null, 
	e_B_V NUMERIC(65,30) not null, 
	r_B_V NUMERIC(65,30) not null, 
	V_I NUMERIC(65,30) not null, 
	e_V_I NUMERIC(65,30) not null, 
	r_V_I NUMERIC(65,30) not null, 
	CombMag NUMERIC(65,30) not null, 
	Hpmag NUMERIC(65,30) not null, 
	e_Hpmag NUMERIC(65,30) not null, 
	Hpscat NUMERIC(65,30) not null, 
	o_Hpmag NUMERIC(65,30) not null, 
	m_Hpmag NUMERIC(65,30) not null, 
	Hpmax NUMERIC(65,30) not null, 
	HPmin NUMERIC(65,30) not null, 
	Period NUMERIC(65,30) not null, 
	HvarType NUMERIC(65,30) not null, 
	moreVar NUMERIC(65,30) not null, 
	morePhoto NUMERIC(65,30) not null, 
	CCDM NUMERIC(65,30) not null, 
	n_CCDM NUMERIC(65,30) not null, 
	Nsys NUMERIC(65,30) not null, 
	Ncomp NUMERIC(65,30) not null, 
	MultFlag NUMERIC(65,30) not null, 
	Source NUMERIC(65,30) not null, 
	Qual NUMERIC(65,30) not null, 
	m_HIP NUMERIC(65,30) not null, 
	theta NUMERIC(65,30) not null, 
	rho NUMERIC(65,30) not null, 
	e_rho NUMERIC(65,30) not null, 
	dHp NUMERIC(65,30) not null, 
	e_dHp NUMERIC(65,30) not null,  
	Survey NUMERIC(65,30) not null, 
	Chart NUMERIC(65,30) not null, 
	Notes NUMERIC(65,30) not null, 
	HD NUMERIC(65,30) not null, 
	BD NUMERIC(65,30) not null, 
	CoD NUMERIC(65,30) not null, 
	CPD NUMERIC(65,30) not null, 
	V_Ired NUMERIC(65,30) not null, 
	SpType NUMERIC(65,30) not null, 
	r_SpType NUMERIC(65,30) not null
);	



create table Planet_temp_table(
	numero_ordinal_do_registro INT,
	name CHAR(100),
	mass NUMERIC(65,30), 
	semi_major_axis NUMERIC(65,30),
	right_ascension NUMERIC(65,30),
	declination NUMERIC(65,30),   
	discovered INT,
	star_name CHAR(100),
	orbital_period NUMERIC(65,30)
;


create table Planet(
      numero_ordinal_do_registro INT,
      name CHAR(100),
      mass NUMERIC(65,30), 
      semi_major_axis NUMERIC(65,30),
      right_ascension NUMERIC(65,30),
      declination NUMERIC(65,30),   
      discovered INT,
      star_name CHAR(100),
      orbital_period NUMERIC(65,30),
      primary key(name),
      foreign key (numero_ordinal_do_registro) references Source_Gaia(numero_ordinal_do_registro) ON DELETE RESTRICT
);


====================================================================================

create table Produto_Gaia (
     numero_ordinal_do_registro int primary key,
     Mg double not null,
     MRp double not null,
     Bp_menos_Rp double not null,
     erro_de_mg double not null,
     erro_de_MRp double not null,
     foreign key (numero_ordinal_do_registro) references Source_Gaia(numero_ordinal_do_registro) on delete restrict 
);



create table Produto_Hipparcos(
      numero_ordinal_do_registro int primary key,
      MV double not null,
      MVt double not null,
      B_menos_V double not null,
      BT_menos_VT double not null,
      foreign key (numero_ordinal_do_registro) references Source_Hipparcos(numero_ordinal_do_registro) on delete restrict 
);




create table Diagrama_Gaia(
      codigo char(10) not null,
      diagrama blob not null,
      descricao char(100),
      primary key (codigo)
);



create table Diagrama_Hipparcos(
       codigo char(10) not null,
       diagrama blob not null,
       descricao char(100),
       primary key (codigo)
);


create table Produto_Gaia_é_plotado_em(
      parallax double not null,
      ra double not null,
      declination double not null,
      codigo char(10) not null,
      primary key (ra, declination, parallax, codigo),
      foreign key (ra, declination) references Produto_Gaia(ra, declination),
      foreign key (codigo) references Diagrama_Gaia(codigo)
);


create table Produto_Hipparcos_é_plotado_em(
      parallax double not null,
      RAdeg double not null,
      DEdeg double not null,
      codigo char(10) not null,
      primary key (RAdeg, DEdeg, parallax, codigo),
      foreign key (RAdeg, DEdeg) references Produto_Hipparcos(RAdeg, DEdeg),
      foreign key (codigo) references Diagrama_Hipparcos(codigo)
);
































