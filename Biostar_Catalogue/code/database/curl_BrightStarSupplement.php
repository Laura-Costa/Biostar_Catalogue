<?php
    // criar um objeto client url para fazer tranferências
    $ch = curl_init();

    // definindo as variáveis para a conexão com o bando de dados
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    // criar conexão com o bando de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // checar conexão
    if ($conn -> connect_error){
        die("connection failed: " . $conn->connect_error);
    } else {
        echo "sucess";
    }

    $query = mysqli_query($conn, "select ordinal_number, HD, DM_Cat, DM from BrightStarSupplement");
    while($row = mysqli_fetch_array($query)) {

        // inicializando variáveis
        $ordinal_number = null;
        $identifier = null;
        $HD = null;
        $DM_Cat = null;
        $DM = null;
        $column_key_name = null;

        // pegar o ordinal_number do banco de dados
        $ordinal_number = trim($row[0]);
        // pegar HD do banco de dados
        $HD = trim($row[1]);
        // pegar DM_Cat do banco de dados
        $DM_Cat = trim($row[2]);
        // pegar DM do banco de dados
        $DM = trim($row[3]);

        if (!str_contains($HD, "HD ")){
            print("\nHD FALTANTE====================== " . $HD);
            $identifier = $DM_Cat . " " . $DM;
        } else {
            $identifier = $HD;
        }

        // configurar a url
        if (str_contains($identifier, "HD ")){
            curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=" . substr($identifier, 0, 2) . "+" . substr($identifier, 3));
        }
        if (str_contains($identifier, "CP -60  980")){
            curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=CP+-60++980");
        }
        if (str_contains($identifier, "BD +20 3283")){
            curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=+BD+%2B20+3283");
        }
        if (str_contains($identifier, "CP -61 3926")){
            curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=CP+-61+3926");
        }

        // retornar a tranferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a strings única retornada pela tranferência
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

        // inicio do processamento da página
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
            mysqli_query($conn, "update BrightStarSupplement set simbad_DR1 = '" . $simbad_DR1 . "' where ordinal_number = " . $ordinal_number);
        }
        if(!is_null($simbad_DR2)){
            mysqli_query($conn, "update BrightStarSupplement set simbad_DR2 = '" . $simbad_DR2 . "' where ordinal_number = " . $ordinal_number);
        }
        if(!is_null($simbad_DR3)){
            mysqli_query($conn, "update BrightStarSupplement set simbad_DR3 = '" . $simbad_DR3 . "' where ordinal_number = " . $ordinal_number);
        }
        if(!is_null($simbad_HIP)){
            mysqli_query($conn, "update BrightStarSupplement set simbad_HIP = '" . $simbad_HIP . "' where ordinal_number = " . $ordinal_number);
        }
        if(!is_null($simbad_parallax) && !str_contains($simbad_parallax, "~")){
            $parallax_query = ("update BrightStarSupplement set simbad_parallax = " . $simbad_parallax . " where ordinal_number = " . $ordinal_number);
            mysqli_query($conn, $parallax_query);
        }
        if(!is_null($simbad_parallax_error) && !str_contains($simbad_parallax_error, "~")){
            $parallax_error_query = ("update BrightStarSupplement set simbad_parallax_error = " . $simbad_parallax_error . " where ordinal_number = " . $ordinal_number);
            mysqli_query($conn, $parallax_error_query);
        }
        if(!is_null($simbad_B) && !str_contains($simbad_B, "~")){
            $simbad_B_query = ("update BrightStarSupplement set simbad_B = " . $simbad_B . " where ordinal_number = " . $ordinal_number);
            mysqli_query($conn, $simbad_B_query);
        }
        if(!is_null($simbad_V) && !str_contains($simbad_V, "~")){
            $simbad_V_query = ("update BrightStarSupplement set simbad_V = " . $simbad_V . " where ordinal_number = " . $ordinal_number);
            mysqli_query($conn, $simbad_V_query);
        }

        // atualizar chaves estrangeiras (HIP e designation) da tabela BrightStar
        mysqli_query($conn, "update BrightStarSupplement set BrightStarSupplement.HIP = BrightStarSupplement.simbad_HIP where BrightStarSupplement.simbad_HIP in (select Hipparcos.HIP from Hipparcos)");
        mysqli_query($conn, "update BrightStarSupplement set BrightStarSupplement.designation = BrightStarSupplement.simbad_DR3 where BrightStarSupplement.simbad_DR3 in (select CAT1.designation from CAT1)");

    }

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>