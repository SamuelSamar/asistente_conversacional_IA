from twilio.rest import Client

ACCOUNT_SID = ''
AUTH_TOKEN = ''
NUMERO_TWILIO = ''
NUMERO_ENCARGADO = ''

def enviar_mensaje_ayuda():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    mensaje = client.messages.create(
        from_=NUMERO_TWILIO,
        to=NUMERO_ENCARGADO,
        body="El adulto mayor necesita ayuda. Por favor acudir lo antes posible"
    )
    return mensaje.sid