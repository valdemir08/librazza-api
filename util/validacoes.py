from modules.empresa.modelo import Empresa


class EmpresaUtil:

    @staticmethod
    def validate(data):
        fields = set(data.keys())
        validate_fields = set(Empresa.VALIDATE_FIELDS_REQUIREMENTS).issubset(fields)
        flag_ir_error = False
        for key, value in data.items():
            if value.strip() in ['', None]:
                flag_ir_error = True
        if not validate_fields or flag_ir_error:
            raise Exception('Nome e CNPJ são obrigatórios')
