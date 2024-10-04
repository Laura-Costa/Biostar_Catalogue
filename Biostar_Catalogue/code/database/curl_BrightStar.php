<?php
    // criar um objeto client url para fazer transferências
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

    $query = mysqli_query($conn, "select HR from BrightStar");
    while($row = mysqli_fetch_array($query)) {

        // pegar HR do BD
        $HR = substr($row[0], 3); // o índice 3 aqui é para pegar apenas a componente numérica do HR

        // configurar URL
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=HR+" . $HR);

        // retornar a transferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a string única retornada pela tranferência
        $string_array = explode(" ", $output);

        // definindo variáveis para o processamento dos dados
        $identifiers_started = False;
        $identifiers_ended = False;
        $cont = 0;
        $simbad_DR1 = "";
        $simbad_DR2 = "";
        $simbad_DR3 = "";
        $simbad_HIP = "";

        // tempo inicial
        $time_start = microtime(True);

        // início do processamento da página
        foreach($string_array as $word){
            if(str_contains($word, "Identifiers")){
                $identifiers_started = True;
            }
            if($identifiers_started && str_contains($word, "Bibcodes")){
                $identifiers_ended = True;
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
            $cont++;
        }

        // carregar os dados obtidos na web para o BD, caso existam
        if(strlen($simbad_DR1) != 0){
            mysqli_query($conn, "update BrightStar set simbad_DR1 = '" . $simbad_DR1 . "' where HR = '" . $HR . "'");
        }
        if(strlen($simbad_DR2) != 0){
            mysqli_query($conn, "update BrightStar set simbad_DR2 = '" . $simbad_DR2 . "' where HR = '" . $HR . "'");
        }
        if(strlen($simbad_DR3) != 0){
            mysqli_query($conn, "update BrightStar set simbad_DR3 = '" . $simbad_DR3 . "' where HR = '" . $HR . "'");
        }
        if(strlen($simbad_HIP) != 0){
            mysqli_query($conn, "update BrightStar set simbad_HIP = '" . $simbad_HIP . "' where HR = '" . $HR . "'");
        }

        // atualizar chaves estrangeiras (HIP e designation) da tabela BrightStar
        mysqli_query($conn, "update BrightStar set BrightStar.HIP = BrightStar.simbad_HIP where BrightStar.simbad_HIP in (select Hipparcos.HIP from Hipparcos)");
        mysqli_query($conn, "update BrightStar set BrightStar.designation = BrightStar.simbad_DR3 where BrightStar.simbad_DR3 in (select Gaia30pc.designation from Gaia30pc)");

        // tempo final
        $time_end = microtime(True);

        // tempo de execução
        $execution_time = $time_end - $time_start;

        print($execution_time . "\n");
    }

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>