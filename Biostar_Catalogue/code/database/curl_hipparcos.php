<?php
    $ch = curl_init();
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    //criar conexao com o banco de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    //checar conexao
    if ($conn->connect_error){
        die("connection failed: " . $conn->connect_error);
    } else{
        echo "sucess";
    }

    $query = mysqli_query($conn, "select HIP from Hipparcos");
    while($row = mysqli_fetch_array($query)){

        //pegar o HIP do BD
        $id = substr($row[0], 4);

        //configurar url
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=HIP+" . $id);

        //retornar a tranferencia como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        //executar a requisicao
        $output = curl_exec($ch);

        $string_array = explode(" ", $output);
        $started = False;
        $ended = False;
        $cont = 0;
        $simbad_DR1 = "";
        $simbad_DR2 = "";
        $simbad_DR3 = "";
        $simbad_HIP = "";

        //inicio do processamento da pagina
        foreach($string_array as $word){
            if(str_contains($word, "Identifiers")){
                $started = True;
            }
            if($started && str_contains($word, "Bibcodes")){
                $ended = True;
            }
            if(!$ended && $started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR1")){
                $simbad_DR1 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$ended && $started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR2")){
                $simbad_DR2 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$ended && $started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR3")){
                $simbad_DR3 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$ended && $started && str_contains($word, "HIP")){
                $simbad_HIP = $word . " " . $string_array[$cont+1];
            }
            $cont++;
        }

        // colocar os dados no BD
        if(strlen($simbad_DR1) != 0){
            mysqli_query($conn, "update Hipparcos set simbad_DR1 = '" . $simbad_DR1 . "' where HIP = 'HIP " . $id . "'");
        }
        if(strlen($simbad_DR2) != 0){
            mysqli_query($conn, "update Hipparcos set simbad_DR2 = '" . $simbad_DR2 . "' where HIP = 'HIP " . $id . "'");
        }
        if(strlen($simbad_DR3) != 0){
            mysqli_query($conn, "update Hipparcos set simbad_DR3 = '" . $simbad_DR3 . "' where HIP = 'HIP " . $id . "'");
        }
        if(strlen($simbad_HIP) != 0){
            mysqli_query($conn, "update Hipparcos set in_simbad = 1 where HIP = 'HIP " . $id . "'");
        }
    }

    // fazer backup dos dados

    $backup_query = <<<'EOD'
    select HIP,
    HD,
    BD,
    CoD,
    CPD,
    in_simbad,
    simbad_DR1,
    simbad_DR2,
    simbad_DR3,
    trim(Vmag)+0,
    trim(RAdeg)+0,
    trim(DEdeg)+0,
    RAhms,
    DEdms,
    trim(Plx)+0,
    trim(e_Plx)+0,
    trim(pmRA)+0,
    trim(pmDE)+0,
    trim(BTmag)+0,
    trim(e_BTmag)+0,
    trim(VTmag)+0,
    trim(e_VTmag)+0,
    trim(B_V)+0,
    trim(e_B_V)+0
    from Hipparcos
    into outfile '/var/lib/mysql-files/backup_Hipparcos.csv'
    fields optionally enclosed by '"'
    terminated by ','
    lines terminated by '\n'
    EOD;

    mysqli_query($conn, $backup_query);
    shell_exec("sudo chmod a+r+w /var/lib/mysql-files/*");
    shell_exec("mv -v /var/lib/mysql-files/backup_Hipparcos.csv /home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/backup_files/backup_Hipparcos.csv");

    curl_close($ch);
    mysqli_close($conn);
?>