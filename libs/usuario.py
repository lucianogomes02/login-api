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
        if not numero and not numero.isdigit():
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

    def __new__(cls, cep: str):
        return super().__new__(cls, cep)

    def __init__(self, cep: str):
        self._verificar_tipo(cep)
        self._verificar_cep(cep)

    @classmethod
    def _verificar_tipo(cls, cep: str):
        if not isinstance(cep, str):
            raise cls.TipoInvalido(
                "O CEP precisa ser criado a partir de um tipo string/texto."
            )

    @classmethod
    def _verificar_cep(cls, cep: str):
        if not cep and not cep.isdigit() and not len(cep) == 8:
            raise cls.CEPInvalido(
                "CEP inválido! Apenas carácteres númericos são permitidos, sendo necessário 8 dígitos "
                "para compor o CEP."
            )


class NomeUsuario(str):
    pass


class CPF(str):
    pass


class PIS(str):
    pass


class Senha(str):
    pass
