# ProjetWebHook
Projet WebHook

menjato@mnKodem ProjetWebHook % python3 --version
Python 3.9.6
menjato@mnKodem ProjetWebHook % pip3 install flask


menjato@mnKodem ProjetWebHook % python3 webhook.py

 * Serving Flask app 'webhook'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 986-814-072

👉 Ce webhook écoute sur :
http://localhost:5000/webhook

curl -X POST http://localhost:5000/webhook \
     -H "Content-Type: application/json" \
     -d '{"event":"test","message":"hello"}'

menjato@mnKodem ProjetWebHook % curl -X POST http://127.0.0.1:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"event":"test","message":"hello"}'

{
  "status": "ok"
}
menjato@mnKodem ProjetWebHook % 

Webhook reçu : {'event': 'test', 'message': 'hello'}

depuis ngrok
menjato@mnKodem ProjetWebHook % curl -X POST https://pseudoanaphylactic-josefine-nonirately.ngrok-free.dev/webhook \
  -H "Content-Type: application/json" \
  -d '{"event":"test","message":"depuis ngrok"}'

{
  "status": "ok"
}
menjato@mnKodem ProjetWebHook
menjato@mnKodem ProjetWebHook % 

Avec secret
menjato@mnKodem ProjetWebHook % curl -X POST https://pseudoanaphylactic-josefine-nonirately.ngrok-free.dev/webhook \
  -H "Content-Type: application/json" \
  -H "X-Webhook-Token: mon_super_secret" \
  -d '{"event":"test","message":"sécurisé"}'

{
  "status": "ok"
}

Pour slipity :

curl -X GET https://pseudoanaphylactic-josefine-nonirately.ngrok-free.dev/webhook

menjato@mnKodem ProjetWebHook % curl -X GET https://pseudoanaphylactic-josefine-nonirately.ngrok-free.dev/webhook

{
  "status": "slide triggered"
}

Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 986-814-072
Webhook GET déclenché!
127.0.0.1 - - [01/Jan/2026 11:26:19] "GET /webhook HTTP/1.1" 200 -

