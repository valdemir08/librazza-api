import traceback

from flask import Blueprint, request, make_response, jsonify
from modules.emprestimo.dao import EmprestimoDao
from modules.emprestimo.modelo import Emprestimo
from util.database import ConnectDB

app_emprestimo = Blueprint('app_emprestimo', __name__)
app_name = 'emprestimo'
dao = EmprestimoDao(database=ConnectDB())

@app_emprestimo.route('/{}/'.format(app_name), methods=['GET'])
def get_emprestimos():
    emprestimos = dao.get_all()
    return make_response(jsonify(emprestimos), 200)

@app_emprestimo.route('/{}/add/'.format(app_name), methods=['POST'])
def add_emprestimo():
    try:
        data = request.form.to_dict(flat=True)
        emprestimo = Emprestimo(
                                data_inicio=data.get('data_inicio'),
                                prazo_devolucao=data.get('prazo_devolucao'),
                                data_devolucao=data.get('data_devolucao'),
                                status=data.get('status'),
                                cliente_id=data.get('cliente_id'),
                                funcionario_id=data.get('funcionario_id'),
                                livro_id=data.get('livro_id'))
        emprestimo = dao.save(emprestimo)
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return make_response(
            {
                'error': True,
                'message': str(e)
            }, 400)
    return make_response({'id': emprestimo.id}, 201)

@app_emprestimo.route('/{}/<int:id>/'.format(app_name),
                   methods=['PUT'])
def edit_emprestimo(id):
    data = request.form.to_dict(flat=True)
    emprestimo = dao.get_by_id(id)
    if not emprestimo:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    dao.edit(id, data)
    emprestimo = dao.get_by_id(id)
    return make_response(emprestimo, 200)


@app_emprestimo.route('/{}/<int:id>/'.format(app_name),
                   methods=['GET'])
def get_emprestimo_by_id(id):
    emprestimo = dao.get_by_id(id)
    if not emprestimo:
        return make_response({'error': '{} não existe'.format(app_name)}, 404)
    return make_response(emprestimo, 201)


@app_emprestimo.route('/{}/delete/<int:id>/'.format(app_name),
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
