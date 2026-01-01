from flask import Flask, request, jsonify

app = Flask(__name__)
""" 
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        print("Webhook GET déclenché!")
        return jsonify({"status": "slide triggered"}), 200

    if request.method == "POST":
        data = request.get_json()
        print("Webhook POST reçu :", data)
        return jsonify({"status": "ok"}), 200

 """

@app.route("/slipity", methods=["GET"])
def slipity():
    print("Slide Slipity déclenché")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)

