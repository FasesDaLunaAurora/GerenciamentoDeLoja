from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.db import Base
from src.models.insumo_model import Insumo

# Tabela associativa muitos-para-muitos com quantidade de cada insumo
cesta_insumo_table = Table(
    "cesta_insumo",
    Base.metadata,
    Column("cesta_id", Integer, ForeignKey("cesta.id"), primary_key=True),
    Column("insumo_id", Integer, ForeignKey("insumo.id"), primary_key=True),
    Column("quantidade", Integer, nullable=False, default=1),
)

class CategoriaCesta(Base):
    __tablename__ = "categoria_cesta"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)

class Cesta(Base):
    __tablename__ = "cesta"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categoria_cesta.id"), nullable=False)
    valor_custo = Column(Float, nullable=False, default=0.0)
    valor_venda_minimo = Column(Float, nullable=False, default=0.0)
    disponivel = Column(Boolean, default=False)

    # relacionamento com insumos via tabela associativa
    insumos = relationship(
        "Insumo",
        secondary=cesta_insumo_table,
        back_populates="cestas"
    )

    # relacionamento com categoria
    categoria = relationship("CategoriaCesta")

# Atualizar a classe Insumo para back_populates
Insumo.cestas = relationship(
    "Cesta",
    secondary=cesta_insumo_table,
    back_populates="insumos"
)
