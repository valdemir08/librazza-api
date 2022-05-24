import traceback

from flask import Blueprint, request, make_response, jsonify

from modules.localizacao.dao import LocalizacaoDao
from modules.localizacao.modelo import Localizacao
from util.database import ConnectDB

app_localizacao = Blueprint('app_localizacao', __name__)
app_name = 'localizacao'
dao = LocalizacaoDao(database=ConnectDB())

@app_localizacao.route('/{}/'.format(app_name), methods=['GET'])
def get_localizacoes():
    localizacoes = dao.get_all()
    return make_response(jsonify(localizacoes), 200)

@app_localizacao.route('/{}/add/'.format(app_name), methods=['POST'])
def add_localizacao():
    try:
        data = request.args.to_dict(flat=True)
        localizacao = Localizacao(estante=data.get('estante'),
                                prateleira=data.get('prateleira'))
        localizacao = dao.save(localizacao)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': localizacao.id}, 201)

@app_localizacao.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_localizacao(id):
    data = request.args.to_dict(flat=True)
    localizacao = dao.get_by_id(id)
    if not localizacao:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    localizacao = dao.get_by_id(id)
    return make_response(localizacao, 200)


@app_localizacao.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_localizacao_by_id(id):
    localizacao = dao.get_by_id(id)
    if not localizacao:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(localizacao, 201)
