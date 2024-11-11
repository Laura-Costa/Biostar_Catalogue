<?php
    // criar um objeto curl para fazer as tranferências
    $ch = curl_init();

    // definindo as variáveis para a conexão com o banco de dados
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    // criar conexão com o banco de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // checar conexão
    if ($conn->connect_error){
        die("connection failed: " . $conn->connect_error);
    } else {
        echo "sucess";
    }


    $url = <<<"EOD"
    https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=
    SELECT TOP 2756%20
    designation,
    ra,
    dec,
    parallax,
    parallax_error,
    pm,
    pmra,
    pmdec,
    ruwe,
    phot_variable_flag,
    non_single_star,
    phot_g_mean_mag,
    phot_bp_mean_mag,
    phot_rp_mean_mag,
    bp_rp,
    bp_g,
    g_rp,
    teff_gspphot,
    teff_gspphot_lower,
    teff_gspphot_upper,
    logg_gspphot,
    logg_gspphot_lower,
    logg_gspphot_upper,
    mh_gspphot,
    mh_gspphot_lower,
    mh_gspphot_upper,
    distance_gspphot,
    distance_gspphot_lower,
    distance_gspphot_upper,
    azero_gspphot,
    azero_gspphot_lower,
    azero_gspphot_upper%20
    FROM gaiadr3.gaia_source%20
    WHERE%20
    (
    parallax >= 50.0000 or (parallax < 50.0000 and parallax %2B 3 * parallax_error >= 50.0000)
    )%20
    or%20
    (
    distance_gspphot <= 20.0000 or (distance_gspphot > 20.0000 and distance_gspphot - (1.0 / 2.0) * (distance_gspphot_upper - distance_gspphot_lower) <= 20.0000)
    )%20
    or%20
    (
    designation = 'Gaia DR3 6192187979961725952' or%20
    designation = 'Gaia DR3 1166216253750406144' or%20
    designation = 'Gaia DR3 4345775217221821312' or%20
    designation = 'Gaia DR3 5943191236735787520' or%20
    designation = 'Gaia DR3 4584639307993378432'
    )
    EOD;
    /*
    $url = str_replace("(","%28",$url);
    $url = str_replace(")","%29",$url);
    $url = str_replace(".","%2E",$url);
    $url = str_replace("=","%3D",$url);
     */
    //$url = str_replace("-","%2D",$url);
    //$url = str_replace("/","%2F",$url);
    //$url = str_replace("*","%2A",$url);
    //$url = str_replace(">=","%3E%3D",$url);
    //$url = str_replace("<=","%3C%3D",$url);
    //$url = str_replace(">","%3E",$url);
    //$url = str_replace("<","%3C",$url);
    $url = str_replace(" ","%20",$url);
    $url = str_replace("\n","",$url);

    // configurar url
    curl_setopt($ch, CURLOPT_URL, $url);

    // esperar indefinidamente
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 0);
    curl_setopt($ch, CURLOPT_TIMEOUT, 1000);
    set_time_limit(0);

    // retornar a tranferência como uma string
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

    // executar a requisição
    $output = curl_exec($ch);

    // separar os registros de cada estrela
    $registers = explode("\n", $output);

    // array de headers
    $headers = array(0=>"designation", 1=>"right_ascension", 2=>"declination", 3=>"parallax", 4=>"parallax_error", 5=>"pm", 6=>"pmra", 7=>"pmdec", 8=>"ruwe", 9=>"phot_variable_flag", 10=>"non_single_star", 11=>"phot_g_mean_mag", 12=>"phot_bp_mean_mag", 13=>"phot_rp_mean_mag", 14=>"bp_rp", 15=>"bp_g", 16=>"g_rp", 17=>"teff_gspphot", 18=>"teff_gspphot_lower", 19=>"teff_gspphot_upper", 20=>"logg_gspphot", 21=>"logg_gspphot_lower", 22=>"logg_gspphot_upper", 23=>"mh_gspphot", 24=>"mh_gspphot_lower", 25=>"mh_gspphot_upper", 26=>"distance_gspphot", 27=>"distance_gspphot_lower", 28=>"distance_gspphot_upper", 29=>"azero_gspphot", 30=>"azero_gspphot_lower", 31=>"azero_gspphot_upper");

    $header = True;

    foreach($registers as $str_register){
        if($header == True){
            $header = False;
            continue;
        }
        $arr_register = explode(",", $str_register);
        $cont = 0;
        foreach($arr_register as $data){
            if($cont == 0 && strlen($data) != 0 && !is_null($data)){
                mysqli_query($conn, "insert into Gaia(" . $headers[$cont] . ") values('" . substr($data, 1, -1) . "')");
                print("\n" . $headers[$cont] . " data: " . substr($data, 1, -1));
            }
            if($cont != 0 && strlen($data) != 0 && !is_null($data)){
                if($cont == 9){
                    $data = substr($data, 1, -1);
                }
                mysqli_query($conn, "update Gaia set Gaia." . $headers[$cont] . " = '" . $data . "' where Gaia.designation = '" . substr($arr_register[0], 1, -1) . "'");
                print("\n" . $headers[$cont] . " data: " . $data);
            }
            $cont++;
        }
    }

    // fechar a instância do client curl
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>