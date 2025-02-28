import os
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@socketio.on("connect")
def handle_connect():
    print("Client connected!")

@socketio.on("message")
def handle_message(data):
    print(f"Received: {data}")
    socketio.send(f"Echo: {data}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Azure’s assigned port
    socketio.run(app, host="0.0.0.0", port=port, debug=True)
