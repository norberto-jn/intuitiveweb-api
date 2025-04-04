from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from health_insurance_providers.controllers.health_insurance_providers_controller import health_insurance_providers_controller

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')
    app.register_blueprint(health_insurance_providers_controller)
    
    return app, socketio

app, socketio = create_app()

if __name__ == '__main__':
    socketio.run(app, port=3002, debug=True, host='0.0.0.0')