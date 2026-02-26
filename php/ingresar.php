<?php
require_once("connectBase.php");
require_once("usuarios.php");

if($_POST) {

    $u = new Usuario($conn); // solo ocupamos pasar la conexion,
    if ($u->iniciarSesion($_POST['usuario'], $_POST['contrasena'])) { // si el inicio de sesion es exitoso, entonces muestra un mensaje de exito
        echo "Inicio de sesión exitoso.";
    } else {
        echo "Usuario o contraseña incorrectos.";
    }
}
?>
