import traceback

from flask import Blueprint, request, make_response, jsonify

from modules.autor.dao import AutorDao
from modules.autor.modelo import Autor
from util.database import ConnectDB

app_autor = Blueprint('app_autor', __name__)
app_name = 'autor'
dao = AutorDao(database=ConnectDB())

@app_autor.route('/{}/'.format(app_name), methods=['GET'])
def get_autores():
    autores = dao.get_all()
    return make_response(jsonify(autores), 200)

@app_autor.route('/{}/add/'.format(app_name), methods=['POST'])
def add_autor():
    try:
        data = request.args.to_dict(flat=True)
        autor = Autor(nome=data.get('nome'))
        autor = dao.save(autor)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': autor.id}, 201)

@app_autor.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_autor(id):
    data = request.args.to_dict(flat=True)
    autor = dao.get_by_id(id)
    if not autor:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    autor = dao.get_by_id(id)
    return make_response(autor, 200)


@app_autor.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_autor_by_id(id):
    autor = dao.get_by_id(id)
    if not autor:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(autor, 201)

@app_autor.route('/{}/delete/<int:id>/'.format(app_name),
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
