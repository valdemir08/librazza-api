import traceback

from flask import Blueprint, request, make_response, jsonify
from modules.funcionario.dao import FuncionarioDao
from modules.funcionario.modelo import Funcionario
from util.database import ConnectDB


app_funcionario = Blueprint('app_funcionario', __name__)
app_name = 'funcionario'
dao = FuncionarioDao(database=ConnectDB())


@app_funcionario.route('/{}/'.format(app_name), methods=['GET'])
def get_funcionarios():
    funcionarios = dao.get_all()
    return make_response(jsonify(funcionarios), 200)

@app_funcionario.route('/{}/add/'.format(app_name), methods=['POST'])
def add_funcionarios():
    try:
        data = request.args.to_dict(flat=True)
        funcionario = Funcionario(matricula=data.get('matricula'),
                                  senha=data.get('senha'),
                                  nome=data.get('nome'),
                                  cpf=data.get('cpf'),
                                  telefone=data.get('telefone'),
                                  email=data.get('email'),
                                  data_nascimento=data.get('data_nascimento'),
                                  empresa_id=data.get('empresa_id'))
        funcionario = dao.save(funcionario)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': funcionario.id}, 201)

@app_funcionario.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_funcionario(id):
    data = request.args.to_dict(flat=True)
    funcionario = dao.get_by_id(id)
    if not funcionario:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    funcionario = dao.get_by_id(id)
    return make_response(funcionario, 200)


@app_funcionario.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_funcionario_by_id(id):
    funcionario = dao.get_by_id(id)
    if not funcionario:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(funcionario, 201)

@app_funcionario.route('/{}/delete/<int:id>/'.format(app_name),
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


