import os
from flask import Flask, render_template, Response  # Asegúrate de tener Response aquí

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Inicio")

@app.route('/about')
def about():
    return render_template('about.html', title="¿Quién soy?")

@app.route('/chat')
def chat():
    return render_template('chat.html', title="Chat en vivo")

@app.route('/faq')
def faq():
    return render_template('faq.html', title="FAQ")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contacto")

# ✅ FIX: permitir iframe embebido
@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
