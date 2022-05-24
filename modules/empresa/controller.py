import traceback

from flask import Blueprint, request, make_response, jsonify
from modules.empresa.dao import EmpresaDao
from modules.empresa.modelo import Empresa
from util.database import ConnectDB
import util.validacoes

app_empresa = Blueprint('app_empresa', __name__)
app_name = 'empresa'
dao = EmpresaDao(database=ConnectDB())

@app_empresa.route('/{}/'.format(app_name), methods=['GET'])
def get_empresas():
    empresas = dao.get_all()
    return make_response(jsonify(empresas), 200)

@app_empresa.route('/{}/add/'.format(app_name), methods=['POST'])
def add_empresa():
    try:
        data = request.args.to_dict(flat=True)
        util.validacoes.EmpresaUtil.validate(data)
        empresa = Empresa(nome=data.get('nome'),
                          cnpj=data.get('cnpj'))
        empresa = dao.save(empresa)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': empresa.id}, 201)

@app_empresa.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_empresa(id):
    data = request.args.to_dict(flat=True)
    empresa = dao.get_by_id(id)
    if not empresa:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    empresa = dao.get_by_id(id)
    return make_response(empresa, 200)


@app_empresa.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_empresa_by_id(id):
    empresa = dao.get_by_id(id)
    if not empresa:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(empresa, 201)

@app_empresa.route('/{}/delete/<int:id>/'.format(app_name),
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


