from typing import Annotated
from pydantic import Field
from WORKOUT_API.contribue.schemas import BaseSchema


class Categorias(BaseSchema):
    nome: Annotated [str, Field (description='Nome da Categoria', example='Scale', max_lenght=10)]
