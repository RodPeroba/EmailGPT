import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from openai import OpenAI, OpenAIError

# Configurações
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

API_KEY = "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" # Substitua pela sua chave real ;)
MODEL_LLM = "deepseek/deepseek-chat-v3.1:free"
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=API_KEY)
app = Flask(__name__, template_folder='templates')

def allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def call_openai_api(message: str) -> str:
    """Envia a mensagem para a API e retorna a resposta."""
    try:
        response = client.chat.completions.create(
            model=MODEL_LLM,
            messages=[
                {"role": "system", "content": "Você é um assistente no setor financeiro da empresa, sua função é ler emails e responder da melhor forma, sendo profissional para emails profissionais e casual para emails casuais."},
                {"role": "user", "content": message}
            ],
            seed=42
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        return f"Erro na chamada da API: {e}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    print("Requisição recebida")  # Log
    text_content = ""

    if 'file' in request.files:
        print("Arquivo detectado")  # Log
        file = request.files['file']
        if file and file.filename != '' and allowed(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            if filename.lower().endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    text_content = f.read()
            elif filename.lower().endswith(".pdf"):
                text_content = extract_text_from_pdf(file_path)
        else:
            return jsonify({"status": "Extensão não permitida"}), 400

    elif 'text' in request.form:
        print("Texto detectado")  # Log
        text_content = request.form['text'].strip()
    else:
        return jsonify({"status": "Nenhum dado enviado"}), 400

    resposta = call_openai_api(text_content)
    return jsonify({"status": "Processamento concluído", "response": resposta}), 200

if __name__ == "__main__":
    app.run(debug=True)