from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store client information: {id: {ip, port}}
clients = {}

@app.route("/client", methods=["POST"])
def register():
    """Register a client's external IP and port."""
    data = request.json
    client_id = data.get("id")
    ip = data.get("ip")
    port = data.get("port")
    time = data.get("time")

    if not client_id or not ip or not port:
        return jsonify({"error": "Missing id, ip, or port"}), 400

    clients[client_id] = {"ip": ip, "port": port, "time": time}
    return jsonify({"message": f"Client {client_id} registered successfully"})


@app.route("/client/<client_id>", methods=["GET"])
def get_client(client_id):
    """Retrieve a client's details by ID."""
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": f"Client {client_id} not found"}), 404
    return jsonify(client)


@app.route("/clients", methods=["GET"])
def all_clients():
    """Retrieve all registered clients."""
    return jsonify(clients)
