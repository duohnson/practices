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
    <title>duohnson practica</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="../css/style.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
</head>
<body>
    <article id="fondo">
    Mi primer sitio web, espero que les guste! (hermoso no? siempre que tu crees algo, será hermoso, y nadie nunca podrá quitarle valor a lo que nace de tu esfuerzo!!)
    </article>
    <h1 class="txt_tittle">Hola Mundo!</h1>
    <br>
    <a class="btn" href="/practices/html/index.html">
        Inicio
    </a>
    <a class="btn" target="_blank" href="https://github.com/duohnson/">
        GitHub
    </a>
    <a class="btn" href="/practices/html/tabla.html">
        Mi Hardware
    </a>
    <h5 class="txt_text">
        Puedes encontrar mi GitHub clickeando arriba!
    </h5>
    <img class="img" src="/practices/html/img/tests.png" width="100">
    <br>
    <div class="card" style="width: 350px; height: 300px;">
        <h2 class="txt_text">Registrar Usuario</h2>
        <form action="registro.php" method="POST">
            <input style="margin-bottom: 10px;" type="text" id="usuario" name="usuario" placeholder="¿Usuario?"><br>
            <input style="margin-bottom: 10px" type="password" id="contrasena" name="contrasena" placeholder="¿Contraseña?"><br>
            <input type="text" id="email" name="email" placeholder="¿Email?"><br>
            <input class="btn" type="submit" value="Registrar">
        </form>
    </div>
</body>
</html>