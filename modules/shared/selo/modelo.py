
class Selo:

    def __init__(self, valor_selo, id=None):
        self.valor_selo = valor_selo
        self.id = id

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return 'Selo: {}'.format(self.valor_selo)

    def get_values_save(self):
        return [self.valor_selo]
