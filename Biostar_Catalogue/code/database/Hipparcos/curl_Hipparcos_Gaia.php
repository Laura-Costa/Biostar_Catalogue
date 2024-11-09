<?php
    // criar um objeto curl para fazer as tranferências
    $ch = curl_init();

    //definindo as variáveis para a conexão com o banco de dados
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

    $query = mysqli_query($conn, "select HIP, simbad_DR3 from Hipparcos where simbad_DR3 is not null");
    while($row = mysqli_fetch_array($query)){

        // pegar HIP e simbad_DR3 do BD
        $HIP = substr($row[0], 4); // o índice 4 aqui é para pegar apenas a componente numérica do HIP
        $simbad_DR3 = $row[1];
        $GaiaDR3_array = explode(" ", $simbad_DR3);
        $GaiaDR3 = $GaiaDR3_array[0] . "+" . $GaiaDR3_array[1] . "+" . $GaiaDR3_array[2];

        // if($simbad_DR3 == "Gaia DR3 217328235692110080") {print("\n" . $GaiaDR3);} essa estrela tinha dado erro

        // configurar url
        curl_setopt($ch, CURLOPT_URL, "https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT+parallax,parallax_error+FROM+gaiadr3.gaia_source+WHERE+designation='" . $GaiaDR3 . "'");

        // retornar a tranferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);
        $basic_data_array = array(0=>null, 1=>null);
        $basic_data_array = explode("\n", $output);
        $GaiaDR3_parallax = null;
        $GaiaDR3_parallax_error = null;

        // header
        if(!str_contains($basic_data_array[0], ",")) {
            print("\n0 - simbad_DR3: --" . $simbad_DR3 . "--\n");
            print("\n1 - basic_data_array[0]: --" . $basic_data_array[0] . "--\n");
        }
        // dados
        if(!str_contains($basic_data_array[1], ",")) {
            print("\n2 - simbad_DR3: --" . $simbad_DR3 . "--\n");
            print("\n3 - basic_data_array[1]: --" . $basic_data_array[1] . "--\n");
        }

        //if(strlen($basic_data_array[1]) != 0) {$basic_data_array = explode(",", $basic_data_array[1]);}
        $parallax_parallax_error_array = array(0=>null, 1=>null);
        $parallax_parallax_error_array = explode(",", $basic_data_array[1]);

        if(!is_null($parallax_parallax_error_array[0]) && strlen($parallax_parallax_error_array[0]) != 0) {
            $GaiaDR3_parallax = $parallax_parallax_error_array[0];
        }
        if(!is_null($parallax_parallax_error_array[1]) and strlen($parallax_parallax_error_array[1]) != 0) {
            $GaiaDR3_parallax_error = $parallax_parallax_error_array[1];
        }

        /*
        print("\nsimbad_DR3: " . $simbad_DR3);
        print("\nGaiaDR3_parallax: " . $GaiaDR3_parallax);
        print("\nGaiaDR3_parallax_error: " . $GaiaDR3_parallax_error);
        */

        // carregar os dados obtidos no Gaia Archive para o BD, caso existam
        if(strlen($GaiaDR3_parallax) != 0 && !is_null($GaiaDR3_parallax)){
            mysqli_query($conn, "update Hipparcos set GaiaDR3_parallax = " . $GaiaDR3_parallax . " where HIP = 'HIP " . $HIP . "'");
        }
        if(strlen($GaiaDR3_parallax_error) != 0 && !is_null($GaiaDR3_parallax)){
            mysqli_query($conn, "update Hipparcos set GaiaDR3_parallax_error = " . $GaiaDR3_parallax_error . " where HIP = 'HIP " . $HIP . "'");
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
    trim(e_B_V)+0,
    SpType
    from Hipparcos
    into outfile '/var/lib/mysql-files/backup_Hipparcos.csv'
    fields optionally enclosed by '"'
    terminated by ','
    lines terminated by '\n'
    EOD;

    mysqli_query($conn, $backup_query);
    // shell_exec("sudo chmod a+r+w /var/lib/mysql-files/*");  nao eh mais necessario pois usuário lh foi adicionado ao grupo mysql
    shell_exec("mv -v /var/lib/mysql-files/backup_Hipparcos.csv /home/lh/Desktop/Biostar_Catalogue/Biostar_Catalogue/code/database/backup_files/backup_Hipparcos.csv");

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);

?>