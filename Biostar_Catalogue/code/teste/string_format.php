<?php

$format = "HIP %d \n";
echo sprintf($format, 79672);

//print($format, 79672);
$bool = null;
if (is_null($bool)){
    print("1)sem paralaxe\n");
}
if(!is_null($bool)){
    print("2)com paralaxe\n");
}

$bool = 4.35;
if (is_null($bool)){
    print("3)sem paralaxe\n");
}
if(!is_null($bool)){
    print("4)com paralaxe\n");
}

$slice = "[4.4241]";
print(substr($slice, 1, -1));

?>