create table Source_Gaia (
	numero_ordinal_do_registro int not null auto_increment primary key,
	solution_id long not null,
	designation char(100),
	source_id long not null,
	random_index long not null,
	ref_epoch double not null,
	ra double not null,
	ra_error float not null,
	declination double not null,
	dec_error float not null,
	parallax double not null,
	parallax_error float not null,
	parallax_over_error float not null,
	pm float not null,
	pmra double not null,
	pmra_error float not null,
	pmdec double not null,
	pmdec_error float not null,
	ra_dec_corr float not null,
	ra_parallax_corr float not null,
	ra_pmra_corr float not null,
	ra_pmdec_corr float not null,
	dec_parallax_corr float not null,
	dec_pmra_corr float not null,
	dec_pmdec_corr float not null,
	parallax_pmra_corr float not null,
	parallax_pmdec_corr float not null,
	pmra_pmdec_corr float not null,
	astrometric_n_obs_al int not null,
	astrometric_n_obs_ac int not null,
	astrometric_n_good_obs_al int not null,
	astrometric_n_bad_obs_al int not null,
	astrometric_gof_al float not null,
	astrometric_chi2_al float not null,
	astrometric_excess_noise float not null,
	astrometric_excess_noise_sig float not null,
	astrometric_params_solved int not null,
	astrometric_primary_flag boolean not null,
	nu_eff_used_in_astrometry float not null,
	pseudocolour float not null,
	pseudocolour_error float not null,
	ra_pseudocolour_corr float not null,
	dec_pseudocolour_corr float not null,
	parallax_pseudocolour_corr float not null,
	pmra_pseudocolour_corr float not null,
	pmdec_pseudocolour_corr float not null,
	astrometric_matched_transits int not null,
	visibility_periods_used int not null,
	astrometric_sigma5d_max float not null,
	matched_transits int not null,
	new_matched_transits int not null,
	matched_transits_removed int not null,
	ipd_gof_harmonic_amplitude float not null,
	ipd_gof_harmonic_phase float not null,
	ipd_frac_multi_peak int not null,
	ipd_frac_odd_win int not null,
	ruwe float not null,
	scan_direction_strength_k1 float not null,
	scan_direction_strength_k2 float not null,
	scan_direction_strength_k3 float not null,
	scan_direction_strength_k4 float not null,
	scan_direction_mean_k1 float not null,
	scan_direction_mean_k2 float not null,
	scan_direction_mean_k3 float not null,
	scan_direction_mean_k4 float not null,
	duplicated_source boolean not null,
	phot_g_n_obs int not null,
	phot_g_mean_flux double not null,
	phot_g_mean_flux_error float not null,
	phot_g_mean_flux_over_error float not null,
	phot_g_mean_mag float not null,
	phot_bp_n_obs int not null,
	phot_bp_mean_flux double not null,
	phot_bp_mean_flux_error float not null,
	phot_bp_mean_flux_over_error float not null,
	phot_bp_mean_mag float not null,
	phot_rp_n_obs int not null,
	phot_rp_mean_flux double not null,
	phot_rp_mean_flux_error float not null,
	phot_rp_mean_flux_over_error float not null,
	phot_rp_mean_mag float not null,
	phot_bp_rp_excess_factor float not null,
	phot_bp_n_contaminated_transits int not null,
	phot_bp_n_blended_transits int not null,
	phot_rp_n_contaminated_transits int not null,
	phot_rp_n_blended_transits int not null,
	phot_proc_mode int not null,
	bp_rp float not null,
	bp_g float not null,
	g_rp float not null,
	radial_velocity float not null,
	radial_velocity_error float not null, 
	rv_method_used int not null, 	
	rv_nb_transits int not null, 
	rv_nb_deblended_transits int not null,
	rv_visibility_periods_used int not null, 
	rv_expected_sig_to_noise float not null, 
	rv_renormalised_gof float not null, 
	rv_chisq_pvalue float not null, 
	rv_time_duration float not null,
	rv_amplitude_robust float not null,
	rv_template_teff float not null,
	rv_template_logg float not null,
	rv_template_fe_h float not null,
	rv_atm_param_origin int not null,
	vbroad float not null,
	vbroad_error float not null,
	vbroad_nb_transits int not null,
	grvs_mag float not null,
	grvs_mag_error float not null,
	grvs_mag_nb_transits int not null,
	rvs_spec_sig_to_noise float not null,
	phot_variable_flag char(100) not null,
	galactic_longitude double not null,
	galactic_latitude double not null,
	ecl_lon double not null,
	ecl_lat double not null,
	in_qso_candidates boolean not null,
	in_galaxy_candidates boolean not null,
	non_single_star int not null,
	has_xp_continuous boolean not null,
	has_xp_sampled boolean not null,
	has_rvs boolean not null,
	has_epoch_photometry boolean not null,
	has_epoch_rv boolean not null,
	has_mcmc_gspphot boolean not null,
	has_mcmc_msc boolean not null,
	in_andromeda_survey boolean not null,
	classprob_dsc_combmod_quasar float not null,
	classprob_dsc_combmod_galaxy float not null,
	classprob_dsc_combmod_star float not null,
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
	azero_gspphot float not null,
	azero_gspphot_lower float not null,
	azero_gspphot_upper float not null,
	ag_gspphot float not null,
	ag_gspphot_lower float not null,
	ag_gspphot_upper float not null,
	ebpminrp_gspphot float not null,
	ebpminrp_gspphot_lower float not null,
	ebpminrp_gspphot_upper float not null,
	libname_gspphot char(100) not null
);



create table Source_Hipparcos (
	numero_ordinal_do_registro int not null auto_increment primary key,
	Catalog double not null, 
	HIP long not null, 	
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


====================================================================================

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
































