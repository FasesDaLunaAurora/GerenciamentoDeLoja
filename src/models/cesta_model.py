from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.db import Base
from src.models.insumo_model import Insumo

# Tabela associativa para muitos-para-muitos
cesta_insumo_table = Table(
    "cesta_insumo",
    Base.metadata,
    Column("cesta_id", Integer, ForeignKey("cesta.id"), primary_key=True),
    Column("insumo_id", Integer, ForeignKey("insumo.id"), primary_key=True),
    Column("quantidade", Integer, nullable=False, default=1),
)

class Cesta(Base):
    __tablename__ = "cesta"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)

    # relacionamento com insumos via tabela associativa
    insumos = relationship(
        "Insumo",
        secondary=cesta_insumo_table,
        back_populates="cestas"
    )

# Adicionar na classe Insumo o back_populates
Insumo.cestas = relationship(
    "Cesta",
    secondary=cesta_insumo_table,
    back_populates="insumos"
)
