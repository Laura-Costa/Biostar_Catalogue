<?php
    // criar um objeto client url para fazer transferências
    $ch = curl_init();

    // definindo as variáveis para a conexão com o banco de dados
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    // criar conexao com o banco de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // checar conexao
    if ($conn->connect_error){
        die("connection failed: " . $conn->connect_error);
    } else {
        echo "sucess";
    }

    $query = mysqli_query($conn, "select HIP from Hipparcos");
    while($row = mysqli_fetch_array($query)){

        // pegar o HIP do BD
        $id = substr($row[0], 4); // o índice 4 aqui é para pegar apenas a componente numérica do HIP

        // configurar url
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=HIP+" . $id);

        // retornar a tranferencia como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a string única retornada pela tranferência
        $string_array = explode(" ", $output);

        // definindo variáveis para o processamento dos dados
        $identifiers_started = False;
        $basic_data_started = False;
        $identifiers_ended = False;
        $basic_data_ended = False;

        $cont = 0;
        $simbad_DR1 = null;
        $simbad_DR2 = null;
        $simbad_DR3 = null;
        $simbad_HIP = null;
        $simbad_parallax = null;
        $simbad_parallax_error = null;

        // início do processamento da pagina
        foreach($string_array as $word){
            if(str_contains($word, "Identifiers")){
                $identifiers_started = True;
            }
            if(str_contains($word, "Object")){
                $basic_data_started = True;
            }
            if($identifiers_started && str_contains($word, "Bibcodes")){
                $identifiers_ended = True;
            }
            if($basic_data_started && str_contains($word, "Identifiers")){
                $basic_data_ended = True;
            }
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR1")){
                $simbad_DR1 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR2")){
                $simbad_DR2 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR3")){
                $simbad_DR3 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "HIP")){
                $simbad_HIP = $word . " " . $string_array[$cont+1];
            }
            // ler dados numéricos do Simbad
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Parallax:")){
                $simbad_parallax = $string_array[$cont + 1];
                $simbad_parallax_error = substr($string_array[$cont + 2], 1, -1);
            }
            $cont++;
        }
        /*
        printf("\nsimbad_DR1: " . $simbad_DR1);
        printf("\nsimbad_DR2: " . $simbad_DR2);
        printf("\nsimbad_DR3: " . $simbad_DR3);
        printf("\nsimbad_HIP: " . $simbad_HIP);
        printf("\nsimbad_parallax: " . $simbad_parallax);
        printf("\nsimbad_parallax_error: " . $simbad_parallax_error);*/

        // carregar os dados obtidos na web para o BD, caso existam
        if(!is_null($simbad_DR1)){
            mysqli_query($conn, "update Hipparcos set simbad_DR1 = '" . $simbad_DR1 . "' where HIP = 'HIP " . $id . "'");
        }
        if(!is_null($simbad_DR2)){
            mysqli_query($conn, "update Hipparcos set simbad_DR2 = '" . $simbad_DR2 . "' where HIP = 'HIP " . $id . "'");
        }
        if(!is_null($simbad_DR3)){
            mysqli_query($conn, "update Hipparcos set simbad_DR3 = '" . $simbad_DR3 . "' where HIP = 'HIP " . $id . "'");
        }
        if(!is_null($simbad_HIP)){
            mysqli_query($conn, "update Hipparcos set in_simbad = 1 where HIP = 'HIP " . $id . "'");
        }
        if(!is_null($simbad_parallax) && !str_contains($simbad_parallax, "~")){
            mysqli_query($conn, "update Hipparcos set simbad_parallax = " . $simbad_parallax . "where HIP = 'HIP " . $id . "'");
        }
        if(!is_null($simbad_parallax_error) && !str_contains($simbad_parallax_error, "~")){
            mysqli_query($conn, "update Hipparcos set simbad_parallax_error = " . $simbad_parallax_error . "where HIP = 'HIP " . $id . "'");
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
    trim(simbad_parallax)+0,
    trim(simbad_parallax_error)+0,
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

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>