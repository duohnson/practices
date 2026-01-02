import json
########################################################
########## PEQUEÑO EJEMPLO SOBRE LECTURA DICT ##########
#json_str = '{"nombre":"daniel","apellidos":"uohnson"}'
#convierte_a_dict=json.loads(json_str)
#print(convierte_a_dict)
#print(convierte_a_dict['nombre'])
########################################################

########################################################
### COMO CARGAR ARCHIVOS DE UN DICT DE PYT A UN JSON ###
#base = {
#    "nombre":"daniel",
#    "apellidos":"uohnson"
#}

#base_json = json.dumps(base)
#print(base)
########################################################

########################################################
#################### CON CLASE #########################
registros = {}

class Personal():
    def __init__(self, cedula, nombre, apellidos, edad):
        self.cedula=cedula
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad

    def guardar():
        ced = "70xxx0xxx"
        nom = "Daniel"
        apell = "Uohnson"
        ed = 27

        registrado = Personal(ced,nom,apell,ed)
        registros[registrado.ced] = registrado.__dict__