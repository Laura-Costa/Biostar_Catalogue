<?php
    // criar um objeto client url
    $ch = curl_init();

    // definindo as variáveis para a conexão com o banco de dados
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    // criar conexão com o banco de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // checar conexão
    if ($conn->connect_error) {
        die("connection failed: " . $conn->connect_error);
    } else {
        echo "succes";
    }

    $query = mysqli_query($conn, "select designation from Gaia");
    while($row = mysqli_fetch_array($query)){

        // inicializando variáveis
        $designation = null;

        // pegar a designation do bd
        $designation = $row[0];

        // colocar o + nos espaços
        $designation_plus = explode(" ", $designation);
        $temp = null;
        foreach($designation_plus as $piece) {
            if(is_null($temp)) {
                $temp = trim($piece);
            }
            else {
                $temp = $temp . "+" . trim($piece);
            }
        }
        $designation_plus = $temp;

        // configurar a url
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=" . $designation_plus);

        // retornar a tranferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a string única retornada pela tranferência
        $string_array = explode(" ", $output);

        // definindo variáveis para o processamento dos dados
        $identifiers_started = False;
        $identifiers_ended = False;
        $simbad_DR3 = null;
        $simbad_HIP = null;
        $simbad_HD = null;
        $cont = 0;


        // inicio do processamento da página
        foreach($string_array as $word){

            if(str_contains($word, "Identifiers")){
                $identifiers_started = True;
            }
            if($identifiers_started && str_contains($word, "Bibcodes")){
                $identifiers_ended = True;
            }

            // buscar pelos identificadores (simbad_DR3, simbad_DR1, simbad_DR2, simbad_DR3 e simbad_HIP)
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "Gaia") && str_contains($string_array[$cont+1], "DR3")){
                $simbad_DR3 = $word . " " . $string_array[$cont+1] . " " . $string_array[$cont+2];
            }
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "HD") && str_contains($word[-1], "D")){
                $simbad_HD = $word . " " . $string_array[$cont+1];
            }
            if(!$identifiers_ended && $identifiers_started && str_contains($word, "HIP")){
                $simbad_HIP = $word . " " . $string_array[$cont+1];
            }
            $cont++;
        }
        /*
        printf("\n\ndesignation: " . $designation);
        printf("\nsimbad_HD: " . $simbad_HD);
        printf("\nsimbad_HIP: " . $simbad_HIP);
        */
        // carregar os dados obtidos na web para o BD, caso existam
        if(!is_null($simbad_DR3)){
            mysqli_query($conn, "update Gaia set in_simbad = 1 where designation = '" . $designation  . "'");
        } else{
            mysqli_query($conn, "update Gaia set in_simbad = 0 where designation = '" . $designation  . "'");
        }
        if(!is_null($simbad_HIP)){
            mysqli_query($conn, "update Gaia set simbad_HIP = '" . $simbad_HIP . "' where designation = '" . $designation  . "'");
        }
        if(!is_null($simbad_HD)){
            mysqli_query($conn, "update Gaia set simbad_HD = '" . $simbad_HD . "' where designation = '" . $designation . "'");
        }
    }

    // atualizar chaves estrangeiras (HIP) da tabela Gaia
    mysqli_query($conn, "update Gaia set Gaia.HIP = Gaia.simbad_HIP where Gaia.simbad_HIP in (select Hipparcos.HIP from Hipparcos)");

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>