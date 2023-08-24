usuarios = {
    'usuario': {'contraseña': 'user', 'nivel': 'usuario'},
    'admin': {'contraseña': 'admin', 'nivel': 'administrador'},
    'superusuario': {'contraseña': 'user123', 'nivel': 'superusuario'}
}

def validar(usuario, contraseña):
    if usuario in usuarios and usuarios[usuario]['contraseña'] == contraseña:
        return usuarios[usuario]['nivel']
    return "Error, los datos ingresados son incorrectos"

def validacion(n_permiso):
    def funcion_autenticada(funcion):
        def ingreso_validar():
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            nivel = validar(usuario, contraseña)
            if nivel == n_permiso:
                return funcion()
            else:
                return "Los datos que ingresaste no te permiten acceder a esta función."
        return ingreso_validar
    return funcion_autenticada

@validacion('usuario')
def funcion_de_usuario():
    return "Autenticación de usuario realizada correctamente."

@validacion('administrador')
def funcion_de_administrador():
    return "Autenticación de administrador realizada correctamente."

@validacion('superusuario')
def funcion_de_superusuario():
    return "Autenticación de superusuario realizada correctamente."

print("***************Sistema de autenticación.***************")
while True:
    op = input("Elegir autenticación (1 para usuario, 2 para administrador, 3 para superusuario, 0 para salir): ")

    if op == '1':
        print(funcion_de_usuario())
    elif op == '2':
        print(funcion_de_administrador())
    elif op == '3':
        print(funcion_de_superusuario())
    elif op == '0':
        print("Saliste del sistema de autenticación!")
        break
    else:
        print("Opción incorrecta,  ingresa de nuevo.")
