
class ClientesEmpresas:
    def __init__(self, cliente_id, empresa_id, id=None):
        self.cliente_id = cliente_id
        self.empresa_id = empresa_id
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Cliente id: {} - Empresa id: {}'.format(self.cliente_id, self.empresa_id)

    def get_values_save(self):
        return [self.cliente_id, self.empresa_id]



