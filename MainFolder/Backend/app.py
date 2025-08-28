from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import uuid
import threading
import subprocess

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'txt','pdf'}

def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

TODO
#Ajustar nome do script
#Ver como funciona o subprocess com python

def run_external_script(file_path):
    try:
        subprocess.run(['python', 'meu_script.py', file_path], check=True)
    except Exception as e:
        print(f"Erro ao executar script: {e}")

def run_external_script_async(file_path):
    threading.Thread(target=run_external_script, args=(file_path,)).start()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        if file and file.filename != '':
            if allowed(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(file_path)

                run_external_script_async(file_path)

                return jsonify({"message": f"Arquivo salvo: {filename}"}), 200
            else:
                return jsonify({"message": "Extensão não permitida"}), 400

    if 'text' in request.form and request.form['text'].strip():
        text_content = request.form['text'].strip()
        text_filename = f"texto_{uuid.uuid4().hex[:8]}.txt"
        text_path = os.path.join(UPLOAD_FOLDER, text_filename)
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text_content)
        return jsonify({"message": f"Texto salvo: {text_filename}"}), 200

    return jsonify({"message": "Nenhum dado enviado"}), 400

if __name__ == '__main__':
    app.run(debug=True)
