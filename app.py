from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "cc-m03"})

@app.route('/api/info')
def api_info():
    return jsonify({
        "app_name": "First VPS Deployment",
        "student_name": "Tatiana Awalura",
        "server": "tiasrv (IDCloudHost)"
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
