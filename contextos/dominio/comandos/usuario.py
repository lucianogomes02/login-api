from dataclasses import dataclass
from typing import Optional

from contextos.dominio.comandos import Comando
from libs.usuario import IdUsuario, NomeUsuario, CPF, PIS, Senha
from contextos.dominio.entidades.usuario import Endereco


@dataclass
class CadastrarUsuario(Comando):
    id_usuario: IdUsuario
    nome: NomeUsuario
    endereco: Endereco
    cpf: CPF
    pis: Optional[PIS]
    senha: Senha


@dataclass
class AlterarUsuario(Comando):
    id_usuario: IdUsuario


@dataclass
class RemoverUsuario(Comando):
    id_usuario: IdUsuario


@dataclass
class LogarUsuario(Comando):
    id_usuario: IdUsuario


@dataclass
class DeslogarUsuario(Comando):
    id_usuario: IdUsuario
