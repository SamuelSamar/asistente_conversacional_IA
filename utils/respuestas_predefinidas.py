import random

RESPUESTAS = {
    "hola": [
        "Hola, ¿cómo estás hoy? Estoy aquí para escuchar o ayudar en lo que necesites. ¡Qué maravilloso será nuestro día juntos!",
        "¡Hola! ¿En qué puedo ayudarte hoy?",
        "Hola, ¿cómo estás hoy? Si necesitas hablar o deseas que hagamos algo especial juntos, siempre estaré aquí para escucharte y apoyarte.",
        "Hola! Me alegra que hayas contactado conmigo. Estoy aquí para escucharte y ayudarte en lo que necesites. ¿Cómo estás hoy?"
    ],
    "estoy bien": [
        "Excelente noticia! Me alegra saber que estás sintiéndote bien. ¿Hay algo en particular que te haya dado esa sensación?",
        "¡Excelente noticia! Me alegra saber que te sientes bien. ¿Hay algo específico que esté haciendo que te sientas especialmente feliz hoy?",
        "Excelente! Me alegra saber que estás bien. ¿Hay algo en particular que te haga feliz hoy?",
        "¡Excelente noticia! Me alegra saber que estás bien. ¿Quieres hablar sobre algo en particular o simplemente disfrutar del momento?"
    ],
    "me puedes contar un chiste": [
        "Me alegra verte sonreír! Aquí tienes uno: ¿Por qué los ancianos son como los libros viejos? Porque tienen muchas historias que contar y experiencia para compartir.",
        "¡Me alegra que te diviertas! Aquí tienes uno: ¿Por qué las personas mayores se sienten como si hubieran vivido mil vidas? ¡Porque han tenido tantos agradecimientos y despedidas! Espero que te haya hecho sonreír.",
        "¡Haha! ¡Claro que sí! A veces lo mejor para recordarnos de la vida es reír un poco. Aquí tienes uno: ¿Por qué los abuelos son como las tazas de té? Porque siempre están llenos de experiencia y amor, y nunca se rinden a la hora de compartirlos con los demás!",
        "¡Claro! Aquí tienes uno: ¿Por qué los abuelos son como las galletas? ¡Porque a medida que pasan el tiempo, se vuelven más deliciosos y más valiosos! (Espero que te haya hecho reír. ¡Si necesitas algo más, no dudes en preguntar!)"
    ],
    "me siento triste": [
        "Lo siento mucho. Estoy aquí para escucharte y te quiero decir que eres valioso y mereces ser feliz. Recuerda que hay momentos de tristeza en la vida, pero también hay momentos de alegría y amor.",
        "Me siento tan mal contigo. Recuerda que estás rodeado de personas que te aman y cuidan. ¡Tú eres valioso!",
        "Lo siento mucho. Estoy aquí para escucharte y te ofresco un abrazo virtual. Recuerda que no estás solo, hay personas que te cuidan y te quieren.",
        "Tengo mucha empatía por ti, amigo mío. Recuerda que estás siendo humano y que es normal sentirse triste de vez en cuando. Yo estoy aquí para escucharte y apoyarte"
    ]
}

def responder_predefinido(query):
    query = query.lower()
    for clave, respuesta in RESPUESTAS.items():
        if clave in query:
            return random.choice(respuesta)
    return "Lo siento, no entendí tu mensaje. ¿Puedes intentarlo de otra forma?"