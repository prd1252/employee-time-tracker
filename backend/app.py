from flask import Flask, request, jsonify

app = Flask(__name__)
time_logs = []

@app.route('/')
def home():
    return "Employee Time Tracker API is running!"

@app.route('/log-time', methods=['POST'])
def log_time():
    data = request.json
    time_logs.append(data)
    return jsonify({"message": "Time logged successfully"}), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(time_logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)