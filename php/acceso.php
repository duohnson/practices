<?php

require_once("connectBase.php");
require_once("usuarios.php");
session_start(); // iniciamos la sesion para poder usar las variables de sesion

if (!isset($_SESSION['usuario'])) { // si no hay una variable de sesion con el nombre de usuario, 
                                    // entonces redirige al inicio de sesion
    header("Location: /practices/html/index.html");
    exit();
}

?>

<!DOCTYPE html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<head>
    <title>Acceso</title>
    <link href="../css/style.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
</head>
<body>
    <a class="btn" style="text-align: left; display: block; width: 130px;" href="/practices/php/cerrarsesion.php">
        Cerrar Sesión
    </a>
    <br>
    <h1 class="txt_tittle">BLOG DUOHNSON</h1>
    <br>
    <a class="btn" href="/practices/html/index.html">
        Inicio
    </a>
    <a class="btn" target="_blank" href="https://www.github.com/duohnson/">
        GitHub
    </a>
    <a class="btn" href="/practices/html/tabla.html">
        Mi Hardware
    </a>
    <h5 class="txt_text">
        Puedes encontrar mi GitHub clickeando arriba!
    </h5>
    <img class="img" src="/practices/html/img/tests.png" width="100">
    <div style="color: white; padding: 2px; font-size: 15px;">
        <div>
            Bienvenido, <?php echo $_SESSION['usuario']; ?>! <!-- 
            mostramos el nombre de usuario guardado en la variable de sesion -->
        </div>
    </div>
<div class="txt_text">
    <div class="docs">
<nav>
  <a href="#inicio">Inicio</a>
  <a href="#noticias.php">Noticias</a>
  <a href="#clientes.php">Clientes</a>
</nav>
<main>
<section class="info-container" id="inicio">
  <h1 class="info">* ====== | Bienvenido| ====== *</h1>
</section>

<section class="info-container" id="noticias.php">
  <h1 class="info">* ====== | Noticias| ====== *</h1>
  <iframe
    id="visor"
    src="/practices/php/noticias.php"
    width="400"
    height="400">
  </iframe>
</section>

<section class="info-container" id="clientes.php">
  <h1 class="info">* ====== | Practica de clientes| ====== *</h1>
  <?php include("clientes.php"); // incluimos el archivo clientes.php, esto es como si copiamos y pegamos el codigo de clientes.php aqui ?>
</section>
</main>
    </div>
</div>
</body>
</html>