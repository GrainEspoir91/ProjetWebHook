from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post("/webhook")
def webhook():
    data = request.get_json()  # récupère le JSON envoyé
    print("Webhook reçu :", data)

    # Tu peux faire ton traitement ici (sauvegarde, email, etc.)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
