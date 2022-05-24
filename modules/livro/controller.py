import traceback

from flask import Blueprint, request, make_response, jsonify

from modules.autor.dao import AutorDao
from modules.livro.dao import LivroDao
from modules.livro.modelo import Livro
from modules.localizacao.dao import LocalizacaoDao
from modules.localizacao.modelo import Localizacao
from modules.shared.autores_livros.dao import AutoresLivrosDao
from modules.shared.autores_livros.modelo import AutoresLivros
from util.database import ConnectDB

app_livro = Blueprint('app_livro', __name__)
app_name = 'livro'
dao = LivroDao(database=ConnectDB())
dao_localizacao = LocalizacaoDao(database=ConnectDB())
dao_autores_livros = AutoresLivrosDao(database=ConnectDB())
dao_autor = AutorDao(database=ConnectDB())

@app_livro.route('/{}/'.format(app_name), methods=['GET'])
def get_livros():
    livros = dao.get_all()
    return make_response(jsonify(livros), 200)

@app_livro.route('/{}/add/'.format(app_name), methods=['POST'])
def add_livro():
    try:
        data = request.args.to_dict(flat=True)

        livro = Livro(titulo=data.get('titulo'),
                                edicao=data.get('edicao'),
                                editora=data.get('editora'),
                                ano_publicacao=data.get('ano_publicacao'),
                                num_paginas=data.get('num_paginas'),
                                cod_barras=data.get('cod_barras'),
                                genero=data.get('genero'),
                                disponivel=data.get('disponivel'),
                                empresa_id=data.get('empresa_id'),
                                isbn = data.get('isbn'))
        livro = dao.save(livro)


        if data.get('autor'):
            autor = "'" + data.get('autor') + "'"
            autor = dao_autor.get_by_autor_name(autor_name=autor)
            autor_livro = AutoresLivros(autor.get('id'), livro.id)
            dao_autores_livros.save(autor_livro)

        if data.get('estante' and 'prateleira'):
            localizacao = Localizacao(estante=data.get('estante'), prateleira=data.get('prateleira'))
            localizacao = dao_localizacao.save(localizacao, livro.id)
            livro.set_localizacao(localizacao)
            print(localizacao)




    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': livro.id}, 201)

@app_livro.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_livro(id):
    data = request.args.to_dict(flat=True)
    livro = dao.get_by_id(id)
    if not livro:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    livro = dao.get_by_id(id)
    return make_response(livro, 200)


@app_livro.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_livro_by_id(id):
    livro = dao.get_by_id(id)
    if not livro:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(livro, 201)


@app_livro.route('/{}/delete/<int:id>/'.format(app_name),
                   methods=['DELETE'])
def delete_autor_by_id(id):
    try:
        dao.delete_by_id(id)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id excluído': id}, 201)
