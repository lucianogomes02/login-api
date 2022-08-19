from uuid import UUID


class IdUsuario(UUID):
    pass


class IdEndereco(UUID):
    pass


class Logradouro(str):
    class TipoInvalido(Exception):
        pass

    class LogradouroInvalido(Exception):
        pass

    def __new__(cls, logradouro: str):
        return super().__new__(cls, logradouro)

    def __init__(self, logradouro: str):
        self._verificar_tipo(logradouro)
        self._verificar_logradouro(logradouro)

    @classmethod
    def _verificar_tipo(cls, logradouro: str):
        if not isinstance(logradouro, str):
            raise cls.TipoInvalido(
                "O logradouro precisa ser criado a partir de um tipo float."
            )

    @classmethod
    def _verificar_logradouro(cls, logradouro: str):
        if not logradouro and not logradouro.isalnum():
            raise cls.LogradouroInvalido("Logradouro inválido! Verifique o logradouro e tente novamente.")


class Numero(str):
    pass


class Complemento(str):
    pass


class Pais(str):
    pass


class Estado(str):
    pass


class CEP(str):
    pass


class NomeUsuario(str):
    pass


class CPF(str):
    pass


class PIS(str):
    pass


class Senha(str):
    pass
