"""AutoValue AI Flask application factory."""
from flask import Flask
from flask_cors import CORS
from routes.health import health_bp
from routes.predict import predict_bp
from routes.model_info import model_info_bp


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
    CORS(app, resources={r'/api/*': {'origins': ['http://localhost:3000', 'http://127.0.0.1:3000']}})
    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(predict_bp, url_prefix='/api')
    app.register_blueprint(model_info_bp, url_prefix='/api')
    return app


if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=5000, debug=False)
