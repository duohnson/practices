<?php
function connectToDatabase() {

    $server_name = "localhost";
    $server_user = "root";
    $server_password = "";
    $database_name = "base";

    // $conn es la variable que almacena el resultado de conectar toda la base
    // $conn = mysqli_connect ($server_name, $server_user, $server_password, $database_name    );

    // importacion de base pero con PDO, orientada a POO
    $pdo = new PDO("mysql:host=$server_name;dbname=$database_name;charset=utf8", 
    $server_user, 
    $server_password);


    // ! es operador de negacion, si ! conn es negativo, ejecuta DIE, pero si no, retorna la conexion
    if (!$pdo) {
        die("Error al conectar a la base de datos: ");
    }

    return $pdo;
}

$conn = connectToDatabase();

?>

