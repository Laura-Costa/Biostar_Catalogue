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

    // configurar url
    curl_setopt($ch, CURLOPT_URL, "https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=SELECT+TOP+2+designation,parallax+FROM+gaiadr3.gaia_source+WHERE+parallax>50.00");

    // retornar a tranferência como uma string
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

    // executar a requisição
    $output = curl_exec($ch);

    print("\noutput: " . $output . "\n");
    print("\ngettype(output): " . gettype($output) . "\n");
    $stars = explode("\n", $output);


    foreach($stars as $star){

    }

    // fechar a instância do client curl
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>