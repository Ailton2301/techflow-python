import os
import sys
from pathlib import Path
from flask import Flask, jsonify, redirect
from flask_cors import CORS

BASE_DIR = Path(__file__).parent.parent
sys.path.append(str(BASE_DIR))

def create_app():
    """Factory principal da aplicação Flask"""
    app = Flask(__name__)
    
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
        FLASK_ENV=os.getenv('FLASK_ENV', 'development')
    )
    
    CORS(app)
    
    register_blueprints(app)
    
    register_error_handlers(app)
    
    
    @app.route('/')
    def home():
        return redirect('/api')
    
    return app

def register_blueprints(app):
    """Registra todos os blueprints da aplicação"""
    from src.routes.tasks import tasks_bp
    from src.routes.auth import auth_bp
    
    app.register_blueprint(tasks_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')

def register_error_handlers(app):
    """Registra handlers globais de erro"""
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Endpoint não encontrado",
            "message": "Consulte /api para rotas disponíveis"
        }), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "error": "Erro interno do servidor",
            "message": "Tente novamente mais tarde"
        }), 500

if __name__ == '__main__':
    app = create_app()
    
    if app.config['FLASK_ENV'] == 'development':
        print("\nRotas registradas:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint}: {rule}")
    
    app.run(host='0.0.0.0', port=5000)