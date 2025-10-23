# É o ponto de entrada da aplicação Flask. 
# Inicializa o servidor web, carrega o blueprint da API
# Define a rota principal para a interface web.
# Cria uma aplicação Flask

from flask import Flask, render_template  # Importa o Flask (framework web) e o render_template (para carregar páginas HTML).
from app.api import chatbot_api           # Importa o "blueprint" da API do chatbot (um módulo separado que organiza as rotas da API).


app = Flask(__name__)                     # Cria a aplicação Flask.
app.register_blueprint(chatbot_api)       # Registra o blueprint do chatbot na aplicação principal. Isso ativa as rotas da API.

@app.route("/")
def index():
    return render_template("index.html")  # Define a rota principal ("/") da página. Quando alguém acessar o site, ele carrega o arquivo

if __name__ == "__main__":
    app.run(debug=True)                   # Inicia o servidor Flask localmente com o modo debug ativado (útil para testes).

#É o ponto de entrada da aplicação Flask. 
#Inicializa o servidor web, carrega o blueprint da API
#e define a rota principal para a interface web.

from flask import Flask, render_template
from app.api import chatbot_api

app = Flask(__name__)
app.register_blueprint(chatbot_api)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
