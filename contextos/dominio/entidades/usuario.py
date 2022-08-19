from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from libs.usuario import (
    IdEndereco,
    Logradouro,
    Numero,
    Complemento,
    CEP,
)


@dataclass_validate
@dataclass
class Endereco:
    id_endereco: IdEndereco
    logradouro: Logradouro
    numero: Numero
    complemento: Complemento
    cep: CEP
    pais: Pais
    estado: Estado
