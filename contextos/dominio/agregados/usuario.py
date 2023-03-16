from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from typing import Optional

from contextos.dominio.agregados import Agregado
from libs.usuario import (
    IdUsuario,
    NomeUsuario,
    CPF,
    PIS,
    Senha,
)
from contextos.dominio.entidades.usuario import Endereco
from contextos.dominio.comandos.usuario import CadastrarUsuario, AlterarUsuario


@dataclass_validate
@dataclass
class Usuario(Agregado):
    id: IdUsuario
    nome: NomeUsuario
    endereco: Endereco
    cpf: CPF
    pis: Optional[PIS]
    senha: Senha

    @classmethod
    def cadastrar_usuario(cls, cadastrar_usuario: CadastrarUsuario):
        # TODO implementar lógica de CADASTRAR USUARIO aqui
        return cls(
            cadastrar_usuario.id_usuario,
            cadastrar_usuario.nome,
            cadastrar_usuario.endereco,
            cadastrar_usuario.cpf,
            cadastrar_usuario.pis,
            cadastrar_usuario.senha,
        )

    def alterar_usuario(self, alterar_usuario: AlterarUsuario):
        # TODO implementar lógica de ALTERAR USUARIO aqui
        # TODO validar classmethod
        return alterar_usuario.id_usuario

    def remover_usuario(self):
        pass

    def logar_usuario(self):
        pass

    def deslogar_usuario(self):
        pass
