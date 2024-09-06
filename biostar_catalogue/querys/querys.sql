-- esta consulta seleciona as estrelas que estão no CAT5, possuem dados Gaia e não estão no CAT1

select Hipparcos_DR1_DR2_DR3.HIP, 
	Hipparcos_DR1_DR2_DR3.designation_DR3 as designation_DR3, 
	Hipparcos_DR1_DR2_DR3.designation_DR2 as designation_DR2, 
	Hipparcos_DR1_DR2_DR3.designation_DR1 as designation_DR1,
	TRIM(Hipparcos_DR1_DR2_DR3.Plx)+0,
	TRIM(Hipparcos_DR1_DR2_DR3.e_Plx)+0, 
	TRIM(Hipparcos_DR1_DR2_DR3.parallax)+0 as parallax, 
	TRIM(Hipparcos_DR1_DR2_DR3.parallax_error)+0, 
	TRIM(1/(Hipparcos_DR1_DR2_DR3.parallax/1000.0))+0 as distance_parallax 
from Hipparcos_DR1_DR2_DR3 
where   (designation_DR3 is not null or 
	designation_DR2 is not null or 
	designation_DR1 is not null) and
	(Hipparcos_DR1_DR2_DR3.HIP not in(
        select Gaia.HIP from Gaia where Gaia.HIP is not NULL))
order by parallax ASC;

-----------------------------------------------------------------------------------------------------------

-- esta consulta verifica se alguma estrela com DR3 retornada na consulta anterior está no CAT1

select Gaia.designation
from Gaia
where Gaia.designation in(
select Hipparcos_DR1_DR2_DR3.designation_DR3 as designation_DR3
from Hipparcos_DR1_DR2_DR3 
where   Hipparcos_DR1_DR2_DR3.designation_DR3 is not null and
	(Hipparcos_DR1_DR2_DR3.HIP not in(
	select Gaia.HIP from Gaia where Gaia.HIP is not NULL)));


