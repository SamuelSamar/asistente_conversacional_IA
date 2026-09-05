from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager = LoginManager()

    login_manager.init_app(app)

    login_manager.login_view = 'asistente.login'

    from models.asistente import Asistente

    @login_manager.user_loader
    def load_user(user_id):
        return Asistente.query.get(int(user_id))

    from routes.chat_routes import chat_bp
    from routes.ayuda_routes import ayuda_bp
    from routes.medicamentos_routes import med_bp
    from routes.rutinas_routes import rut_bp
    from routes.asistente_routes import asistente_bp
    from routes.home_routes import home_bp
    # 
    from routes.medicamento_api_routes import medicamento_api
    from routes.rutina_api_routes import rutina_api
    app.register_blueprint(chat_bp)
    app.register_blueprint(ayuda_bp)
    app.register_blueprint(med_bp)
    app.register_blueprint(rut_bp)
    app.register_blueprint(asistente_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(medicamento_api)
    app.register_blueprint(rutina_api)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)