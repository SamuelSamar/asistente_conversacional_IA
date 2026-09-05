from models.rutinas import Rutina
from models import db

def registrar_rutina(nombre, url):
    url_embed = transformar_a_embed(url)
    nueva_rutina = Rutina(rutina=nombre, url=url_embed)
    db.session.add(nueva_rutina)
    db.session.commit()

def obtener_rutinas():
    return Rutina.query.order_by(Rutina.rutina.asc()).all()

def eliminar_rutina_por_id(id):
    rut = Rutina.query.get_or_404(id)
    db.session.delete(rut)
    db.session.commit()

def obtener_rutina_por_id(id):
    return Rutina.query.get_or_404(id)

def actualizar_rutina(id, nombre, url):
    rut = Rutina.query.get_or_404(id)
    rut.rutina = nombre
    rut.url = url
    db.session.commit()

def transformar_a_embed(url):
    if "youtube.com/watch?v=" in url:
        video_id = url.split("watch?v=")[-1].split("&")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1].split("?")[0]
        return f"https://www.youtube.com/embed/{video_id}"
    return url
