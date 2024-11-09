<?php
    // criar um objeto client url para fazer transferências
    $ch = curl_init();

    //definindo as variáveis para a conexao com o banco de dados
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    // criar conexão com o banco de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // checar conexao
    if ($conn->connect_error){
        die("connection failed: " . $conn->connect_error);
    } else {
        echo "sucess";
    }

    // o last_ordinal_number nunca mais será reinicializado em todo o script
    $last_ordinal_number = 0;

    // todos os registros com "/" no HD_Suffix têm HD
    $query = mysqli_query($conn, "select ordinal_number, HD from Supplement where HD_Suffix like '%/%'");
    while($row = mysqli_fetch_array($query)) {

        $ordinal_number_Supplement = $row[0];

        // somar uma unidade no número HD
        $HD = "HD " . (substr($row[1], 3))+1;

        // configurar url
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=" . substr($HD, 0, 2) . "+" . substr($HD, 3));

        // retornar a transferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a string única retornada pela tranferência
        $string_array = explode(" ", $output);

        // definindo variáveis para o processamento dos dados
        $basic_data_started = False;
        $basic_data_ended = False;
        $cont = 0;
        $simbad_main_identifier = null;

        // inicio do processamento da página
        foreach($string_array as $word){

            if(str_contains($word, "Object")){
                $basic_data_started = True;
            }
            if($basic_data_started && str_contains($word, "Identifiers")){
                $basic_data_ended = True;
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
            $cont++;
        }

        printf("\n\nsimbad_main_identifier: " . $simbad_main_identifier);
        printf("\nordinal_number_Supplement: " . $ordinal_number_Supplement);

        // carregar os dados obtidos na web para o BD, caso existam
        if(!is_null($simbad_main_identifier)){
            mysqli_query($conn, "insert into SupplementMultiple(simbad_main_identifier) values ('" . $simbad_main_identifier . "')");
        }
        $last_ordinal_number++;

        // carregar a chave estrangeira do SupplementMultiple
        mysqli_query($conn, "update SupplementMultiple set SupplementMultiple.ordinal_number_Supplement = " . $ordinal_number_Supplement . " where SupplementMultiple.ordinal_number = " . $last_ordinal_number);
    }

    // fechar a instância do client url
    curl_close($ch);

    // fechar a conexao com o banco de dados
    mysqli_close($conn);
?>