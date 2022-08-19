from dataclasses import dataclass
from . import Evento


@dataclass
class UsuarioCadastrado(Evento):
    pass


@dataclass
class UsuarioAlterado(Evento):
    pass


@dataclass
class UsuarioRemovido(Evento):
    pass


@dataclass
class UsuarioLogado(Evento):
    pass


@dataclass
class UsuarioDeslogado(Evento):
    pass
