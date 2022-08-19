from dataclasses import dataclass
from . import Comando
from libs.usuario import IdUsuario


@dataclass
class CadastrarUsuario(Comando):
    id_usuario: IdUsuario


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
