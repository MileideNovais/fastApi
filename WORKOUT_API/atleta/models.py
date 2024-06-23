from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from WORKOUT_API.categorias.models import CategoriaModel
from WORKOUT_API.centro_treinamento.models import CentrotreinamentoModel
from WORKOUT_API.contribue.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column (Integer, primary_key=True)
    nome: Mapped[str] = mapped_column (String[50],nullable=False)
    cpf: Mapped[str] = mapped_column (String[11], unique=True ,nullable=False)
    idade: Mapped[int] = mapped_column (Integer, nullable=False)
    peso: Mapped[float] = mapped_column (Float, nullable=False)
    altura: Mapped[float] = mapped_column (Float, nullable=False)
    sexo: Mapped[str] = mapped_column (String, nullable=False)
    create_at: Mapped[datetime] = mapped_column (DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentrotreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))

    
