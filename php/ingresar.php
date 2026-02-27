<?php
require_once("connectBase.php");
require_once("usuarios.php");

if($_POST) {

    $u = new Usuario($conn); // solo ocupamos pasar la conexion,
    if ($u->iniciarSesion($_POST['usuario'], $_POST['contrasena'])) { // si el inicio de sesion es exitoso, entonces muestra un mensaje de exito
        
        $_SESSION['usuario'] = $_POST['usuario']; // guardamos el nombre de usuario 
        // en la variable de sesion para usarla en otras paginas

        header("Location: ./acceso.php"); // redirige a la pagina principal
        exit(); // termina la ejecucion del script
    } else {
        echo "Usuario o contraseña incorrectos.";
    }
}
?>
