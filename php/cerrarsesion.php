<?php
session_start(); // iniciamos la sesion para poder usar las variables de sesion
session_unset();
session_destroy(); // destruimos la sesion, esto elimina todas las variables de sesion y
// cierra la sesion actual

header("Location: /practices/html/index.html"); // redirige al inicio de sesion
exit(); // termina la ejecucion del script

?>