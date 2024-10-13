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

    $query = mysqli_query($conn, "select ordinal_number, identifier from BrightStarMultiple");
    while($row = mysqli_fetch_array($query)) {

        // pegar o ordinal_number e o identifier do BD
        $last_ordinal_number = $row[0];
        $identifier = "";

        foreach (explode(" ", $row[1]) as $piece){
            $identifier .= $piece;
        }


        // configurar URL
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=" . $identifier);

        // retornar a transferência como uma string
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
        $simbad_B = null;
        $simbad_V = null;

        // início do processamento da página
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

            // buscar pelos identificadores (simbad_DR1, simbad_DR2, simbad_DR3 e simbad_HIP)
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

            // buscar pelos dados numericos (simbad_parallax e simbad_parallax_error)
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Parallax:")){
                $simbad_parallax = $string_array[$cont+1];
                $simbad_parallax_error = substr($string_array[$cont+2], 1, -1);
            }
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Flux") && str_contains($string_array[$cont+1], "B")){
                $simbad_B = $string_array[$cont+3]; // somamos 3 no índice porque o fluxo B é dado desta forma na web page-> 'Flux B : 3.89'
            }
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Flux") && str_contains($string_array[$cont+1], "V")){
                $simbad_V = $string_array[$cont+3]; // somamos 3 no índice porque o fluxo V é dado desta forma na web page-> 'Flux V : 8.99'
            }
            $cont++;
        }

        printf("\nidentifier: " . $identifier);
        printf("\nsimbad_parallax: " . $simbad_parallax);
        printf("\nsimbad_parallax_error: " . $simbad_parallax_error);
        printf("\nsimbad_B: " . $simbad_B);
        printf("\nsimbad_V: " . $simbad_V);

        // carregar os dados obtidos na web para o BD, caso existam
        if(!is_null($simbad_DR1)){
            mysqli_query($conn, "update BrightStarMultiple set simbad_DR1 = '" . $simbad_DR1 . "' where ordinal_number = " . $last_ordinal_number);
        }
        if(!is_null($simbad_DR2)){
            mysqli_query($conn, "update BrightStarMultiple set simbad_DR2 = '" . $simbad_DR2 . "' where ordinal_number = " . $last_ordinal_number);
        }
        if(!is_null($simbad_DR3)){
            mysqli_query($conn, "update BrightStarMultiple set simbad_DR3 = '" . $simbad_DR3 . "' where ordinal_number = " . $last_ordinal_number);
        }
        if(!is_null($simbad_HIP)){
            mysqli_query($conn, "update BrightStarMultiple set simbad_HIP = '" . $simbad_HIP . "' where ordinal_number = " . $last_ordinal_number);
        }
        if(!is_null($simbad_parallax) && !str_contains($simbad_parallax, "~")){
            $parallax_query = ("update BrightStarMultiple set simbad_parallax = " . $simbad_parallax . " where ordinal_number = " . $last_ordinal_number);
            mysqli_query($conn, $parallax_query);
        }
        if(!is_null($simbad_parallax_error) && !str_contains($simbad_parallax_error, "~")){
            $parallax_error_query = ("update BrightStarMultiple set simbad_parallax_error = " . $simbad_parallax_error . " where ordinal_number = " . $last_ordinal_number);
            mysqli_query($conn, $parallax_error_query);
        }
        if(!is_null($simbad_B) && !str_contains($simbad_B, "~")){
            $simbad_B_query = ("update BrightStarMultiple set simbad_B = " . $simbad_B . " where ordinal_number = " . $last_ordinal_number);
            mysqli_query($conn, $simbad_B_query);
        }
        if(!is_null($simbad_V) && !str_contains($simbad_V, "~")){
            $simbad_V_query = ("update BrightStarMultiple set simbad_V = " . $simbad_V . " where ordinal_number = " . $last_ordinal_number);
            mysqli_query($conn, $simbad_V_query);
        }

        // atualizar chaves estrangeiras (HIP e designation) da tabela BrightStar
        mysqli_query($conn, "update BrightStarMultiple set BrightStarMultiple.HIP = BrightStarMultiple.simbad_HIP where BrightStarMultiple.simbad_HIP in (select Hipparcos.HIP from Hipparcos)");
        mysqli_query($conn, "update BrightStarMultiple set BrightStarMultiple.designation = BrightStarMultiple.simbad_DR3 where BrightStarMultiple.simbad_DR3 in (select Gaia30pc.designation from Gaia30pc)");
    }

    // fechar instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>
