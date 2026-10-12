def iniciar_sesion(intento_password):
    password_real = "Uc3m2026"
    global intentos_fallidos
    if intento_password == password_real:
        print("Acceso concedido.")
        intentos_fallidos = 0
    else:
        intentos_fallidos += 1
        print(f" Contraseña incorrecta. Fallo numero: {intentos_fallidos}")
        if intentos_fallidos >= 3:
            print("ALERTA: Cuenta bloqueada por Fuerza Bruta.")
intentos_fallidos = 0
iniciar_sesion("hola123")
iniciar_sesion("passsword")
iniciar_sesion("admin124")

        