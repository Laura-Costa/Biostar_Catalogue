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

    $query = mysqli_query($conn, "select HR, HD from BrightStar");
    while($row = mysqli_fetch_array($query)) {

        // inicializando variáveis
        $HR = null;
        $HD = null;
        $id = null;

        // pegar HR do BD
        $HR = trim($row[0]);
        // pegar HD do BD
        $HD = trim($row[1]);

        if(!str_contains($HD, "HD ")){
            $id = $HR;
        } else {
            $id = $HD;
        }

        // configurar URL
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=" . substr($id, 0, 2) . "+" . substr($id, 3));

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
        $simbad_main_identifier = null;
        $simbad_DR1 = null;
        $simbad_DR2 = null;
        $simbad_DR3 = null;
        $simbad_HIP = null;
        $simbad_parallax = null;
        $simbad_parallax_error = null;
        $simbad_parallax_source = null;
        $simbad_B = null;
        $simbad_V = null;
        $simbad_SpType = null;

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

            // ler simbad_main_identifier do basic data
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Object")){
                $simbad_main_identifier = $string_array[$cont + 1];
                $cont_main_identifier = $cont + 2;
                while(!str_contains($string_array[$cont_main_identifier], "---")){
                    $simbad_main_identifier = $simbad_main_identifier . " " . trim($string_array[$cont_main_identifier]);
                    $cont_main_identifier += 1;
                }
            }
            // ler parallax, parallax_error e parallax_source do basic data
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Parallax:")){
                $simbad_parallax = $string_array[$cont+1];
                $simbad_parallax_error = substr($string_array[$cont+2], 1, -1); // o slice [1:-1] é para tirar os colchetes
                $simbad_parallax_source = explode("\n", $string_array[$cont+4])[0];
            }
            // ler magnitude B do basic data
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Flux") && str_contains($string_array[$cont+1], "B")){
                $simbad_B = $string_array[$cont+3]; // somamos 3 no índice porque o fluxo B é dado desta forma na web page-> 'Flux B : 3.89'
            }
            // ler magnitude V do basic data
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Flux") && str_contains($string_array[$cont+1], "V")){
                $simbad_V = $string_array[$cont+3]; // somamos 3 no índice porque o fluxo V é dado desta forma na web page-> 'Flux V : 8.99'
            }
            // ler SpType do basic data
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "Spectral") && str_contains($string_array[$cont+1], "type:")){
                $simbad_SpType = trim($string_array[$cont+2]);
            }
            $cont++;
        }

        /*
        printf("\nsimbad_main_identifier: " . $simbad_main_identifier);
        printf("\nHR: " . $HR);
        printf("\nsimbad_parallax: " . $simbad_parallax);
        printf("\nsimbad_parallax_error: " . $simbad_parallax_error);
        printf("\nsimbad_parallax_source: " . $simbad_parallax_source);
        printf("\nsimbad_B: " . $simbad_B);
        printf("\nsimbad_V: " . $simbad_V);
        printf("\nsimbad_SpType: " . $simbad_SpType);
        */

        // carregar os dados obtidos na web para o BD, caso existam
        if(!is_null($simbad_DR1)){
            mysqli_query($conn, "update BrightStar set simbad_DR1 = '" . $simbad_DR1 . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
        }
        if(!is_null($simbad_DR2)){
            mysqli_query($conn, "update BrightStar set simbad_DR2 = '" . $simbad_DR2 . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
        }
        if(!is_null($simbad_DR3)){
            mysqli_query($conn, "update BrightStar set simbad_DR3 = '" . $simbad_DR3 . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
        }
        if(!is_null($simbad_HIP)){
            mysqli_query($conn, "update BrightStar set simbad_HIP = '" . $simbad_HIP . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
        }
        if(!is_null($simbad_main_identifier)){
            mysqli_query($conn, "update BrightStar set simbad_main_identifier = '" . $simbad_main_identifier . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
        }
        if(!is_null($simbad_parallax) && !str_contains($simbad_parallax, "~")){
            $simbad_parallax_query = ("update BrightStar set simbad_parallax = " . $simbad_parallax . " where " . substr($id, 0, 2) . " = '" . $id . "'");
            mysqli_query($conn, $simbad_parallax_query);
        }
        if(!is_null($simbad_parallax_error) && !str_contains($simbad_parallax_error, "~")){
            $simbad_parallax_error_query = ("update BrightStar set simbad_parallax_error = " . $simbad_parallax_error . " where " . substr($id, 0, 2) . " = '" . $id . "'");
            mysqli_query($conn, $simbad_parallax_error_query);
        }
        if(!is_null($simbad_parallax_source) && !str_contains($simbad_parallax_source, "~")){
            $simbad_parallax_source_query = ("update BrightStar set simbad_parallax_source = '" . $simbad_parallax_source . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
            mysqli_query($conn, $simbad_parallax_source_query);
        }
        if(!is_null($simbad_B) && !str_contains($simbad_B, "~")){
            $simbad_B_query = ("update BrightStar set simbad_B = " . $simbad_B . " where " . substr($id, 0, 2) . " = '" . $id . "'");
            mysqli_query($conn, $simbad_B_query);
        }
        if(!is_null($simbad_V) && !str_contains($simbad_V, "~")){
            $simbad_V_query = ("update BrightStar set simbad_V = " . $simbad_V . " where " . substr($id, 0, 2) . " = '" . $id . "'");
            mysqli_query($conn, $simbad_V_query);
        }
        if(!is_null($simbad_SpType) && !str_contains($simbad_SpType, "~")){
            $simbad_SpType_query = ("update BrightStar set simbad_SpType = '" . $simbad_SpType . "' where " . substr($id, 0, 2) . " = '" . $id . "'");
            mysqli_query($conn, $simbad_SpType_query);
        }

        // atualizar chaves estrangeiras (HIP e designation) da tabela BrightStar
        mysqli_query($conn, "update BrightStar set BrightStar.HIP = BrightStar.simbad_HIP where BrightStar.simbad_HIP in (select Hipparcos.HIP from Hipparcos)");
        mysqli_query($conn, "update BrightStar set BrightStar.designation = BrightStar.simbad_DR3 where BrightStar.simbad_DR3 in (select Gaia.designation from Gaia)");

    }

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexão com o banco de dados
    mysqli_close($conn);
?>