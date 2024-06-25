from typing import Annotated
from pydantic import Field
from WORKOUT_API.contribue.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated [str, Field (description='Nome do Centro de Treinamento', example='CT King', max_lenght=20)]
    endereco: Annotated [str, Field (description='Enddereço do Centro de Treinamento', example='Rua x, 002', max_lenght=60)]
    proprietario: Annotated [str, Field (description='Proprietário do Centro de Treinamento', example='Marcos', max_lenght=30)]

