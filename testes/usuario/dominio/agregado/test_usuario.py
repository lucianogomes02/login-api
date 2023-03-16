from contextos.dominio.agregados.usuario import Usuario
from contextos.dominio.entidades.usuario import Endereco
from contextos.dominio.objetos_de_valor.usuario import Pais, Estado
from libs.usuario import (
    IdUsuario,
    IdEndereco,
    Logradouro,
    NomeUsuario,
    Numero,
    Complemento,
    CEP,
    CPF,
    PIS,
    Senha,
)

from contextos.dominio.comandos.usuario import CadastrarUsuario, AlterarUsuario


def test_cadastrar_usuario():
    comando = CadastrarUsuario(
        id_usuario=IdUsuario(int=0x12345678123456781234567812345678),
        nome=NomeUsuario("Usuario Teste Cadastro"),
        endereco=Endereco(
            id=IdEndereco(int=0x12345678123456781234567812345678),
            logradouro=Logradouro("Rua Teste"),
            numero=Numero("123"),
            complemento=Complemento(""),
            cep=CEP("00000-000"),
            pais=Pais.BRASIL,
            estado=Estado.SAO_PAULO,
        ),
        cpf=CPF("000.000.000-00"),
        pis=PIS(""),
        senha=Senha("testesenha123"),
    )

    usuario_cadastrado = Usuario.cadastrar_usuario(cadastrar_usuario=comando)

    assert usuario_cadastrado


def test_alterar_usuario():
    cadastrar_usuario = CadastrarUsuario(
        id_usuario=IdUsuario(int=0x12345678123456781234567812345678),
        nome=NomeUsuario("Usuario Teste Cadastro"),
        endereco=Endereco(
            id=IdEndereco(int=0x12345678123456781234567812345678),
            logradouro=Logradouro("Rua Teste"),
            numero=Numero("123"),
            complemento=Complemento(""),
            cep=CEP("00000000"),
            pais=Pais.BRASIL,
            estado=Estado.SAO_PAULO,
        ),
        cpf=CPF("000.000.000-00"),
        pis=PIS(""),
        senha=Senha("testesenha123"),
    )

    usuario_cadastrado = Usuario.cadastrar_usuario(cadastrar_usuario=cadastrar_usuario)

    assert usuario_cadastrado

    alterar_usuario = AlterarUsuario(id_usuario=usuario_cadastrado.id)

    usuario_alterado = usuario_cadastrado.alterar_usuario(
        alterar_usuario=alterar_usuario
    )

    assert usuario_alterado == usuario_cadastrado.id
