<?php
$servername = "localhost"; /* nome da conexão */
$username = "helena"; /* nome do usuario da conexãp */
$password = "ic2023IC*"; /*senha do banco de dados caso exista */
$dbname = "gaia_catalogue_1"; /* nome do seu banco  */

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    echo "Connection failed: " . $conn->connect_error;
} else {
    echo "Conectado";
}
?>
