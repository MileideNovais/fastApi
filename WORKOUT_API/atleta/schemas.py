from typing import Annotated
from pydantic import BaseModel,  Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotated [str, Field (description='Nome do Atleta', examples='Joaõ', max_lenght=50)]
    cpf: Annotated [int, Field (description='CPF do Atleta', examples='12345678900', max_lenght=11)]
    idade: Annotated [int, Field (description='Idade do Atleta', examples='25')]
    peso: Annotated [PositiveFloat, Field (description='peso do Atleta', examples='75.5')]
    altura: Annotated [PositiveFloat, Field (description='Altura do Atleta', examples='1.70')]
    sexo: Annotated[str, Field(description= 'Sexo do  Atleta', examples='M', max_length=1)]