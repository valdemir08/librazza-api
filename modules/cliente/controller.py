import traceback

from flask import Blueprint, request, make_response, jsonify

from modules.cliente.dao import ClienteDao
from modules.cliente.modelo import Cliente
from modules.empresa.dao import EmpresaDao
from modules.shared.confiabilidade.dao import ConfiabilidadeDao
from modules.shared.confiabilidade.modelo import Confiabilidade
from modules.shared.endereco.dao import EnderecoDao
from modules.shared.endereco.modelo import Endereco
from util.database import ConnectDB


app_cliente = Blueprint('app_cliente', __name__)
app_name = 'cliente'
dao = ClienteDao(database=ConnectDB())
dao_endereco = EnderecoDao(database=ConnectDB())
dao_confiabilidade = ConfiabilidadeDao(database=ConnectDB())
dao_empresa = EmpresaDao(database=ConnectDB())


@app_cliente.route('/{}/'.format(app_name), methods=['GET'])
def get_clientes():
    clientes = dao.get_all()
    return make_response(jsonify(clientes), 200)#transforma a lista em .json

@app_cliente.route('/{}/add/'.format(app_name), methods=['POST'])
def add_cliente():
    try:
        data = request.form.to_dict(flat=True)

        confiabilidade = Confiabilidade(0, 1, 0)  # padrão de criação
        confiabilidade = dao_confiabilidade.save(confiabilidade)
        cliente = Cliente(nome=data.get('nome'),
                        cpf=data.get('cpf'),
                        telefone=data.get('telefone'),
                        email=data.get('email'),
                        data_nascimento=data.get('data_nascimento'),
                        confiabilidade_id=confiabilidade.id,
                        empresa_id=data.get('empresa_id'))

        cliente = dao.save(cliente)

        if(data.get('logradouro')):
            endereco = Endereco(data.get('tipo_logradouro'), data.get('logradouro'), data.get('numero'), data.get('bairro'), data.get('cidade'), data.get('cep'), data.get('estado'))
            endereco = dao_endereco.save(endereco, cliente.id)
            cliente.set_endereco(endereco)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': cliente.id}, 201)

@app_cliente.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_cliente(id):
    data = request.form.to_dict(flat=True)
    cliente = dao.get_by_id(id)
    if not cliente:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    cliente = dao.get_by_id(id)
    return make_response(cliente, 200)


@app_cliente.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_cliente_by_id(id):
    cliente = dao.get_by_id(id)
    if not cliente:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(cliente, 201)


@app_cliente.route('/{}/delete/<int:id>/'.format(app_name),
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


