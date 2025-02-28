from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")  # Force eventlet

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("message")
def handle_message(data):
    print(f"Received: {data}")
    socketio.send(f"Echo: {data}")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
