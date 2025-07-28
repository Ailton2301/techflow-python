from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    
    from src.routes.tasks import tasks_bp
    from src.routes.auth import auth_bp
    
    app.register_blueprint(tasks_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app