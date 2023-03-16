from uuid import UUID, uuid4


class IdUsuario(UUID):
    def __init__(self):
        super().__init__(str(uuid4()))


class IdEndereco(UUID):
    def __init__(self):
        super().__init__(str(uuid4()))


class Logradouro(str):
    class TipoInvalido(Exception):
        pass

    class LogradouroInvalido(Exception):
        pass

    def __init__(self, logradouro: str):
        self._verificar_tipo(logradouro)
        self._verificar_logradouro(logradouro)
        super().__init__()

    @classmethod
    def _verificar_tipo(cls, logradouro: str):
        if not isinstance(logradouro, str):
            raise cls.TipoInvalido(
                "O logradouro precisa ser criado a partir de um tipo string/texto."
            )

    @classmethod
    def _verificar_logradouro(cls, logradouro: str):
        if not logradouro:
            raise cls.LogradouroInvalido("Logradouro não pode estar vázio.")


class Numero(str):
    class TipoInvalido(Exception):
        pass

    class NumeroInvalido(Exception):
        pass

    def __new__(cls, numero: str):
        return super().__new__(cls, numero)

    def __init__(self, numero: str):
        self._verificar_tipo(numero)
        self._verificar_numero(numero)

    @classmethod
    def _verificar_tipo(cls, numero: str):
        if not isinstance(numero, str):
            raise cls.TipoInvalido(
                "O número precisa ser criado a partir de um tipo string/texto."
            )

    @classmethod
    def _verificar_numero(cls, numero: str):
        if numero and not numero.isdigit():
            raise cls.NumeroInvalido(
                "Número inválido! Apenas carácteres númericos são permitidos."
            )


class Complemento(str):
    pass


class Pais(str):
    pass


class Estado(str):
    pass


class CEP(str):
    class TipoInvalido(Exception):
        pass

    class CEPInvalido(Exception):
        pass

    def __init__(self, cep: str):
        self._verificar_tipo(cep)
        self._verificar_cep(cep)
        super().__init__()

    @classmethod
    def _verificar_tipo(cls, cep: str):
        if not isinstance(cep, str):
            raise cls.TipoInvalido(
                "O CEP precisa ser criado a partir de um tipo string/texto."
            )

    @classmethod
    def _verificar_cep(cls, cep: str):
        if cep and not cep.isdigit() and not len(cep) == 8:
            raise cls.CEPInvalido(
                "CEP inválido! Apenas carácteres númericos são permitidos, sendo necessário 8 dígitos "
                "para compor o CEP."
            )


class NomeUsuario(str):
    class TipoInvalido(Exception):
        pass

    class NomeUsuarioInvalido(Exception):
        pass

    def __new__(cls, nome_usuario: str):
        return super().__new__(cls, nome_usuario)

    def __init__(self, nome_usuario: str):
        self._verificar_tipo(nome_usuario)
        self._verificar_nome_usuario(nome_usuario)

    @classmethod
    def _verificar_tipo(cls, nome_usuario: str):
        if not isinstance(nome_usuario, str):
            raise cls.TipoInvalido(
                "O nome de usuário precisa ser criado a partir de um tipo string/texto."
            )

    @classmethod
    def _verificar_nome_usuario(cls, nome_usuario: str):
        if not nome_usuario:
            raise cls.NomeUsuarioInvalido("Nome de usuário precisa ser preenchido.")


class CPF(str):
    pass


class PIS(str):
    pass


class Senha(str):
    pass
