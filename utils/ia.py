import requests

# URL del endpoint local de la API de Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"

# query (str): Consulta del usuario
def responder_consulta(query, historial=None):
    contexto = ""
    # Si hay historial, se toma solo los últimos 5 turnos para mantener el contexto reciente
    if historial:
        historial = historial[-5:]
        for turno in historial:
            contexto += f"Usuario: {turno['usuario']}\nAsistente: {turno['asistente']}\n"
    # Se construye el prompt con instrucciones específicas para el modelo
    prompt=(
        "Eres un asistente virtual especializado en el cuidado y acompañamiento emocional de adultos mayores. "
        "Responde siempre con empatía, sencillez y motivación. "
        "Evita temas de política, bancos o tecnología avanzada. "
        "Si el usuario expresa tristeza, ofrece palabras de ánimo y apoyo. "
        "Sé breve y claro, máximo 3 frases.\n"
        f"{contexto}Usuario: {query}\nAsistente:"
    )

    # Se prepara el payload para la solicitud POST
    payload = {
        "model":"llama3", # Nombre del modelo a utilizar
        "prompt":prompt, # Prompt completo con contexto
        "stream":False # Se desactiva el streaming para recibir la respuesta completa
    }

    try:
        # Se envía la solicitud al servidor de Ollama
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        # Si la respuesta no es exitosa, se devuelve un mensaje de error
        if response.status_code != 200:
            return f"Error de conexión con Ollama: {response.status_code} - {response.text}"
        # Se extrae y limpia la respuesta del modelo
        respuesta = response.json()
        texto = respuesta.get("response", "").strip()
        # Se limita la respuesta a un máximo de 3 frases
        frases = texto.split('. ')
        return '. '.join(frases[:3]).strip()
    
    except Exception as e:
        # Manejo de errores en caso de fallo en la conexion
        return f"Error al conectar con Ollama: {str(e)}"