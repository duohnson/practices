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
    
    public function registrar(&$usuarios) { // donde llamamos la base de usuarios
        $sql = "INSERT INTO usuarios (usuario, contrasena, email) VALUES (?, ?, ?)"; // query para insertar un nuevo usuario en la base de datos
        $stmt = $this->conn->prepare($sql); // preparamos la consulta
        
        $stmt->bindParam(1, $this->usuario); // bindParam es para vincular los parametros de la consulta con las propiedades del objeto
        $stmt->bindParam(2, $this->contrasena);
        $stmt->bindParam(3, $this->email);
        return $stmt->execute(); // ejecutamos la consulta
        
    }
    
    public static function iniciarSesion($usuario, $contrasena, $usuarios) { // metodo estatico, no necesita una instancia de la clase para ser llamado
        foreach ($usuarios as $u) { // foreach para recorrer la base de usuarios, donde $u es cada usuario en la base
            if ($u->usuario === $usuario && $u->contrasena === $contrasena) {
                return true; // si el usuario y la contraseña coinciden, retorna true
            }
        }
        return false; // si no se encuentra el usuario o la contraseña es incorrecta, retorna false
    }
}
?>