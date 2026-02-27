<?php

require_once("connectBase.php");
require_once("usuarios.php");

if($_POST) { // si se ha enviado el formulario, entonces ejecuta el codigo
    
    $u = new Usuario(
        $conn, 
    $_POST['usuario'], 
    $_POST['contrasena'], 
    $_POST['email']); 
    
    // creamos un nuevo objeto de la clase Usuario, pasando la conexion a la base de datos y los datos del formulario

    if ($u->registrar()) { // si el registro es exitoso, entonces muestra un mensaje de exito
        echo "Usuario registrado exitosamente.";
        header("Location: /practices/html/index.html"); // redirige a la pagina de inicio de sesion
        exit(); // termina la ejecucion del script
    } else {
        echo "Error al registrar el usuario.";
    }
}

?>
<!DOCTYPE html>
<head>
    <title>Registro de Usuario</title>
    <meta charset="UTF-8">
    <link href="../css/style.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
</head>
<body>
    <div>
        <h2 class="txt_tittle">Registrar Usuario</h2>
        <form action="registro.php" method="POST">
            <label class="txt_text" for="usuario">Usuario:</label>
            <input type="text" id="usuario" name="usuario"><br>
            <label class="txt_text" for="contrasena">Contraseña:</label>
            <input type="password" id="contrasena" name="contrasena"><br>
            <label class="txt_text" for="email">Email:</label>
            <input type="text" id="email" name="email"><br>
            <input type="submit" value="Registrar">
        </form>
    </div>
</body>
</html>