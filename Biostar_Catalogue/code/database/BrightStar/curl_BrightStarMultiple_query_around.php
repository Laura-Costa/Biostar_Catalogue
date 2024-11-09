<?php
    // criar um objeto client url para fazer tranferências
    $ch = curl_init();

    // definindo as variaveis para a conexão com o banco de dados
    $servername = "localhost";
    $username = "lh";
    $password = "ic2023";
    $dbname = "Biostar_Catalogue";

    // criar conexão com o banco de dados
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // checar conexao
    if ($conn->connect_error){
        die("connection failed: " . $conn->connect_error);
    } else{
        echo "sucess";
    }

    // o last_ordinal_number nunca mais será reinicializado em todo o script
    $last_ordinal_number = 0;

    // todos os registros com ADS_Comp não nulo têm HD
    $query = mysqli_query($conn, "select HR, HD, simbad_main_identifier from BrightStar where ADS_Comp is not null");
    while($row = mysqli_fetch_array($query)) {

        $HR = $row[0];
        $HD = $row[1];
        $simbad_main_identifier = $row[2];

        // configurar url
        curl_setopt($ch, CURLOPT_URL, "https://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident=" . substr($HD, 0, 2) . "+" . substr($HD, 3));

        // retornar a tranferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a string única retornada pela transferência
        $string_array = explode(" ", $output);

        // definindo variáveis para o processamento dos dados
        $basic_data_started = False;
        $basic_data_ended = False;
        $cont = 0;
        $ra = null;
        $dec = null;

        // inicio do processamento da página
        foreach($string_array as $word){

            if(str_contains($word, "Object")){
                $basic_data_started = True;
            }
            if(str_contains($word, "Identifiers")){
                $basic_data_ended = True;
            }

            // buscar pela ascensão reta e pela declinação
            if(!$basic_data_ended && $basic_data_started && str_contains($word, "ICRS")){
                $ra = $string_array[$cont+1] . "+" . $string_array[$cont+2] . "+" . $string_array[$cont+3] . "+";
                $dec = $string_array[$cont+5] . "+" . $string_array[$cont+6] . "+" . $string_array[$cont+7] . "+";
                $basic_data_ended = True;
            }
            $cont++;
        }
        // buscar no Simbad pelas coordenadas ra e dec

        // configurar url
        curl_setopt($ch, CURLOPT_URL, "https://simbad.cds.unistra.fr/simbad/sim-coo?Coord=" . $ra . "+" . $dec . "&CooFrame=ICRS&Radius.unit=arcmin&submit=Query+around&Radius=2&output.format=ASCII");

        // retornar a tranferência como uma string
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

        // executar a requisição
        $output = curl_exec($ch);

        // criar um array de strings com a string única retornada pela tranferência
        $lines_array = explode("\n", $output);

        // inicio do processamento da página
        $number_of_objects = null;
        foreach($lines_array as $line){
            if(str_contains($line, "Number of objects :")) {
                $number_of_objects = trim(substr($line, strpos($line, ":")+1));
            }
        }

        // coloca o HR e o main_identifier na tabela BrightStarMultiple
        if (is_null($number_of_objects)) {

            printf("\nis_null(number_of_objects): " . $number_of_objects);
            printf("\nsimbad_main_identifier: " . $simbad_main_identifier);
            printf("\nHR: " . $HR);

            // copiar o main_identifier do BrightStar para o BrightStarMultiple
            mysqli_query($conn, "insert into BrightStarMultiple(simbad_main_identifier) values('" . $simbad_main_identifier . "')");
            $last_ordinal_number++;

            // copiar a chave estrangeira HR do BrightStar para o BrightStarMultiple
            mysqli_query($conn, "update BrightStarMultiple set HR = '" . $HR . "' where ordinal_number = " . $last_ordinal_number);

        } else {
            foreach($lines_array as $line){
                for($i=1; $i<=$number_of_objects; $i++){
                    if (strlen($line) == 0) {continue;}
                    if($line[0] == $i){
                        // line is like: | 1 | simbad_name | -- | -- | -- | -- |
                        $simbad_main_identifier = substr($line, strpos($line, "|")+1);
                        $simbad_main_identifier = substr($simbad_main_identifier, strpos($simbad_main_identifier, "|")+1);
                        $simbad_main_identifier = trim(substr($simbad_main_identifier, 0, strpos($simbad_main_identifier, "|")-1));
                        // retirar possíveis espaços entre as palavras
                        $simbad_main_identifier_list = explode(" ", $simbad_main_identifier);
                        $cont_simbad_main_identifier = 0;
                        foreach($simbad_main_identifier_list as $piece){
                            if($cont_simbad_main_identifier == 0){
                                $simbad_main_identifier = $piece; // se é a primeira vez, põe direto
                            } else {
                                $simbad_main_identifier = $simbad_main_identifier . " " . $piece; // se não é a primeira vez, coloca " " antes
                            }
                            $cont_simbad_main_identifier++;
                        }

                        printf("\nnumber_of_objects: " . $number_of_objects);
                        printf("\nsimbad_main_identifier: " . $simbad_main_identifier);
                        printf("\nHR: " . $HR);

                        // aqui eu tenho o identificador da múltipla
                        mysqli_query($conn, "insert into BrightStarMultiple(simbad_main_identifier) values('" . $simbad_main_identifier . "')");
                        $last_ordinal_number++;

                        // carregar a chave estrangeira HR
                        mysqli_query($conn, "update BrightStarMultiple set HR = '" . $HR . "' where ordinal_number = " . $last_ordinal_number);

                    }
                }
            }
        }
    }

    // fechar instancia do client url
    curl_close($ch);

    // fechar a conexao com o banco de dados
    mysqli_close($conn);
?>