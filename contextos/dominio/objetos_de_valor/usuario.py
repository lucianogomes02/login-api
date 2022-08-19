from dataclasses import dataclass
from enum import Enum
from libs.usuario import Pais, Estado


@dataclass
class Pais(Pais, Enum):
    BRASIL: Pais = "Brasil"


@dataclass
class Estado(Estado, Enum):
    ACRE: Estado = "Acre"
    ALAGOAS: Estado = "Alagoas"
    AMAPA: Estado = "Amapá"
    AMAZONAS: Estado = "Amazonas"
    BAHIA: Estado = "Bahia"
    CEARA: Estado = "Ceará"
    DISTRITO_FEDERAL: Estado = "Distrito Federal"
    ESPIRITO_SANTO: Estado = "Espírito Santo"
    GOIAS: Estado = "Goiás"
    MARANHAO: Estado = "Maranhão"
    MATO_GROSSO: Estado = "Mato Grosso"
    MATO_GROSSO_DO_SUL: Estado = "Mato Grosso do Sul"
    MINAS_GERAIS: Estado = "Minas Gerais"
    PARA: Estado = "Pará"
    PARAIBA: Estado = "Paraíba"
    PARANA: Estado = "Paraná"
    PERNAMBUCO: Estado = "Pernambuco"
    PIAUI: Estado = "Piauí"
    RIO_DE_JANEIRO: Estado = "Rio de Janeiro"
    RIO_GRANDE_DO_NORTE: Estado = "Rio Grande do Sul"
    RIO_GRANDE_DO_SUL: Estado = "Rio Grande do Norte"
    RONDONIA: Estado = "Rondônia"
    RORAIMA: Estado = "Rorâima"
    SANTA_CATARINA: Estado = "Santa Catarina"
    SAO_PAULO: Estado = "São Paulo"
    SERGIPE: Estado = "Sergipe"
    TOCANTINS: Estado = "Tocantins"
