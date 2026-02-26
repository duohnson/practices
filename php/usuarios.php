<?php
require_once("connectBase.php");
// aqui simplemente definimos la visibilidad, public en este caso
class Usuario {
    public $usuario;
    public $contrasena;
    public $email;
    private $conn; // variable privada para la conexion a la base de datos

    // aca ya empieza lo lindo, primero creare el constructor,
    // es el metodo que se ejecuta automat, cuando se crea un nuevo objeto de la clase, 
    // es decir, cuando se hace new Usuario()
    public function __construct($conn, $usuario = null, $contrasena = null, $email = null) {
        $this->conn = $conn; // asignamos la conexion a la base de datos
        $this->usuario = $usuario; // el this hace referencia a la instancia actual de la clase, 
        // es decir, al objeto que se esta creando - en python sería self
        $this->contrasena = $contrasena;
        $this->email = $email;
    }
    
    public function registrar() { // donde llamamos la base de usuarios
        $sql = "INSERT INTO usuarios (usuario, contrasena, email) VALUES (?, ?, ?)"; // query para insertar un nuevo usuario en la base de datos
        $stmt = $this->conn->prepare($sql); // preparamos la consulta
        
        $stmt->bindParam(1, $this->usuario); // bindParam es para vincular los parametros de la consulta con las propiedades del objeto
        $stmt->bindParam(2, $this->contrasena);
        $stmt->bindParam(3, $this->email);
        return $stmt->execute(); // ejecutamos la consulta
        
    }
    
    public function iniciarSesion($usuario, $contrasena) { // metodo estatico, no necesita una instancia de la clase para ser llamado
        $sql = "SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?"; // query para seleccionar el usuario que coincide con el nombre de usuario y la contraseña
        $stmt = $this->conn->prepare($sql); // preparamos la consulta
        $stmt->bindParam(1, $usuario); // vinculamos los parametros de la consulta con los parametros del metodo
        $stmt->bindParam(2, $contrasena);
        $stmt->execute(); // ejecutamos la consulta

        $usuarioEncontrado = $stmt->fetch(PDO::FETCH_ASSOC); // fetch es para obtener el resultado de la consulta, en este caso un array asociativo

        if ($usuarioEncontrado) { // si se encuentra un usuario que coincide con el nombre de usuario y la contraseña, entonces se inicia sesion
            return true; // se devuelve true para indicar que el inicio de sesion fue exitoso
        } else {
            return false; // se devuelve false para indicar que el inicio de sesion fue fallido
        }
    }
}
?>