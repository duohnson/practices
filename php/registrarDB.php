<?php

include("connectBase.php");

// query es la peticion que hacemos a la DB
$query = "SELECT * FROM clientes"; // donde le decimos que cargue todas las tablas de clientes

// creamos la funcion, la cual lleva la conexión con la base de datos,
// y las columnas de la tabla que ocupamos
function registrarCliente ($conn, $cedula, $nombre, $apellidos, $email, $fecha_nacimiento, $numero_celular) {

    // llamamos plantilla sql, aqui hacemos el insert, logica de php directo a la base sql
    // usamos ? como espacios reservados para evitar vulnerabilidad, sql inyector
    $sql = "INSERT INTO clientes (
    cedula, 
    nombre, 
    apellidos, 
    fecha_nacimiento, 
    email, 
    numero_celular)
    VALUES (?, ?, ?, ?, ?, ?)";

    // intenta 
    try {
        // aca se prepara la consulta al servidor, siempre hay que consultar
        $consulta = $conn->prepare($sql); 

        // ejecutar - se pasan los datos en un array y php los carga, donde resultado es la variable de ejecutar
        $resultado = $consulta->execute(array(
            $cedula, 
            $nombre, 
            $apellidos, 
            $fecha_nacimiento, 
            $email, 
            $numero_celular));

        return $resultado; // se devuelve a la funcion si tuvo exito o no

    } catch (Exception $e) { // catch es el except de py, basicamente si hay un error devuelve dicho error
        echo "Error de tipo: ". $e->getMessage();
        return false;
    }
}

// este codigo es basico, es el que me permite interactuar con una base de datos, es un boton que cada vez que
// yo ocupe un registro, lo ejecute, de lo contrario me tocaria manualmente estar escribiendo en sql

?>

