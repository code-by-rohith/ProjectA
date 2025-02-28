from flask import Flask, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "WebSocket Server Running!"

@socketio.on('message')
def handle_message(msg):
    print(f"Received message: {msg}")
    send(f"Server received: {msg}", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
