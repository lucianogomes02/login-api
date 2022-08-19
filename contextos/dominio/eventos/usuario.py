from dataclasses import dataclass
from . import Evento
from libs.usuario import IdUsuario


@dataclass
class UsuarioCadastrado(Evento):
    id_usuario: IdUsuario


@dataclass
class UsuarioAlterado(Evento):
    id_usuario: IdUsuario


@dataclass
class UsuarioRemovido(Evento):
    id_usuario: IdUsuario


@dataclass
class UsuarioLogado(Evento):
    id_usuario: IdUsuario


@dataclass
class UsuarioDeslogado(Evento):
    id_usuario: IdUsuario
