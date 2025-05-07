#pip3 install flask
#pip3 install playsound

from flask import Flask, request, jsonify
import json, threading
from playsound import playsound

app = Flask(__name__)

def alert_sound():
    playsound("/home/user/mixkit-classic-alarm-995.wav")

@app.route('/create', methods=['POST'])
def trigger_alert():
    token = request.headers.get("Authorization")
    if token != "Bearer my-test-token":
        return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json()
    if not data or data.get("action") != "play sound":
        return jsonify({"error": "Invalid request"}), 400
    threading.Thread(target=alert_sound).start()
    return jsonify({"status": "Sound played"}), 200

app.run(host='0.0.0.0', port=5050)
