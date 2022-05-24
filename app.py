from flask import Flask

from modules.autor.controller import app_autor
from modules.cliente.controller import app_cliente
from modules.empresa.controller import app_empresa
from modules.emprestimo.controller import app_emprestimo
from modules.funcionario.controller import app_funcionario
from modules.livro.controller import app_livro
from modules.localizacao.controller import app_localizacao

app = Flask(__name__)

app.register_blueprint(app_empresa)
app.register_blueprint(app_cliente)
app.register_blueprint(app_autor)
app.register_blueprint(app_emprestimo)
app.register_blueprint(app_funcionario)
app.register_blueprint(app_livro)
app.register_blueprint(app_localizacao)

if __name__ == '__main__':
    app.run(debug=True)