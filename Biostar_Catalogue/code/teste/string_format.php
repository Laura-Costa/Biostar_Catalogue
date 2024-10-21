<?php
    printf("\n");
    printf(substr("asd|veve", strpos("asd|veve", "|")+1));
    printf("\n");

    $string = "parallax, parallax_error\n,";
    $array = explode("\n", $string);
    print($array[0]);
    print($array[1]);
    $array = explode(",", $array[1]);
    //print(isset($array[1]));
    //print(strlen($array[0]));
    print($array[1] == "");
?>