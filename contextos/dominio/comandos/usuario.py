from dataclasses import dataclass
from . import Comando


@dataclass
class CadastrarUsuario(Comando):
    pass


@dataclass
class AlterarUsuario(Comando):
    pass


@dataclass
class RemoverUsuario(Comando):
    pass


@dataclass
class LogarUsuario(Comando):
    pass


@dataclass
class DeslogarUsuario(Comando):
    pass
