from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from typing import List, Optional

from . import Agregado
from libs.usuario import (
    IdUsuario,
    NomeUsuario,
    CPF,
    PIS,
    Senha,
)
from contextos.dominio.entidades.usuario import Endereco


@dataclass_validate
@dataclass
class Usuario(Agregado):
    id: IdUsuario
    nome: NomeUsuario
    enderecos: List[Endereco]
    cpf: CPF
    pis: Optional[PIS]
    senha: Senha
