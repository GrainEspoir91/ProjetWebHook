from flask import Flask, request, jsonify

app = Flask(__name__)

SECRET = "mon_super_secret"   # 👈 change-le !

@app.post("/webhook")
def webhook():
    token = request.headers.get("X-Webhook-Token")

    if token != SECRET:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json()
    print("Webhook reçu :", data)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
