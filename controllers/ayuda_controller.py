from utils.whatsapp import enviar_mensaje_ayuda

def solicitar_ayuda():
    try:
        sid = enviar_mensaje_ayuda()
        return sid
    except Exception as e:
        raise e