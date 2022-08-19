from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from libs.usuario import (
    IdEndereco,
    Logradouro,
    Numero,
    Complemento,
    CEP,
)
from contextos.dominio.objetos_de_valor.usuario import Pais, Estado


@dataclass_validate
@dataclass
class Endereco:
    id: IdEndereco
    logradouro: Logradouro
    numero: Numero
    complemento: Complemento
    cep: CEP
    pais: Pais
    estado: Estado
