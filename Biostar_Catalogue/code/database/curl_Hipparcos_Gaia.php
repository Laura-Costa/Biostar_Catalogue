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
        if($simbad_DR3 == "Gaia DR3 217328235692110080") {print("\n" . substr($GaiaDR3, 1, -1));}
        /*
        // configurar url
        curl_setopt($ch, CURLOPT_URL, "https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT+parallax,parallax_error+FROM+gaiadr3.gaia_source+WHERE+designation='" . $GaiaDR3 . "'");

        // retornar a tranferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);
        $basic_data_array = explode("\n", $output);
        $GaiaDR3_parallax = null;
        $GaiaDR3_parallax_error = null;

        if(!isset($basic_data_array[0])) {print("\n0: " . $simbad_DR3);} // header
        if(!isset($basic_data_array[1])) {print("\n1: " . $simbad_DR3);} // dados

        if(strlen($basic_data_array[1]) != 0) {$basic_data_array = explode(",", $basic_data_array[1]);}

        if(!isset($basic_data_array[0])) {print("\n2: " . $simbad_DR3);} // parallax
        if(!isset($basic_data_array[1])) {print("\n3: " . $simbad_DR3);} // parallax_error

        if(strlen($basic_data_array[0]) != 0) {$GaiaDR3_parallax = $basic_data_array[0];}
        if(strlen($basic_data_array[1]) != 0) {$GaiaDR3_parallax_error = $basic_data_array[1];}

        print("\nsimbad_DR3: " . $simbad_DR3);
        print("\nGaiaDR3_parallax: " . $GaiaDR3_parallax);
        print("\nGaiaDR3_parallax_error: " . $GaiaDR3_parallax_error)

        // carregar os dados obtidos no Gaia Archive para o BD, caso existam
        if(!(strlen($GaiaDR3_parallax) == 0) && !is_null($GaiaDR3_parallax)){
            mysqli_query($conn, "update Hipparcos set GaiaDR3_parallax = " . $GaiaDR3_parallax . " where HIP = 'HIP " . $HIP . "'");
        }
        if(!(strlen($GaiaDR3_parallax_error) == 0) && !is_null($GaiaDR3_parallax)){
            mysqli_query($conn, "update Hipparcos set GaiaDR3_parallax_error = " . $GaiaDR3_parallax_error . " where HIP = 'HIP " . $HIP . "'");
        }
        */
    }

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);

?>