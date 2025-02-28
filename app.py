from flask import Flask, request, jsonify

app = Flask(__name__)

# Store user data (in-memory)
users = []

# GET route to display all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# POST route to add a user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if not data or "username" not in data or "email" not in data:
        return jsonify({"error": "Missing username or email"}), 400

    users.append({"username": data["username"], "email": data["email"]})
    return jsonify({"message": "User added successfully"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensure it runs on all interfaces
