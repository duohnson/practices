<?php
require_once("registrarDB.php");

if ($_SERVER['REQUEST_METHOD'] == "POST") { // si el metodo de envio es POST, entonces ejecuta el codigo, 
// es decir, si se envia un formulario

    $cedula = $_POST['cedula'];
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $email = $_POST['email'];
    $numero_celular = $_POST['numero_celular'];
    $fecha_nacimiento = $_POST['fecha_nacimiento'];

    $registro_exitoso = registrarCliente(
        $conn, 
        $cedula, 
        $nombre, 
        $apellidos, 
        $email, 
        $fecha_nacimiento, 
        $numero_celular);

    if ($registro_exitoso) {
        echo "Cliente registrado exitosamente.";
    } else {
        echo "Error al registrar el cliente.";
    }
}

?>

<!DOCTYPE html>
<head>
    <title>Registros Uohnson</title>
    <meta charset="UTF-8">
</head>
<body>
    <!-- aqui vamos a importar la base del registro -->
    <form action="procesar.php" method="POST">
        <label>Nombre:</label>
        <input type="text" name="nombre" required>
        <br>
        <label>Apellido:</label>
        <input type="text" name="apellidos" required>
        <br>
        <label>Cedula:</label>
        <input type="number" name="cedula" required>
        <br>
        <label>Email:</label>
        <input type="text" name="email" required>
        <br>
        <label>Número celular:</label>
        <input type="text" name="numero_celular" required>
        <br>
        <label>Fecha de nacimiento:</label>
        <input type="date" name="fecha_nacimiento" required>
        <br>
        <input type="submit" value="Registrar">
    </form>
</body>
</html>