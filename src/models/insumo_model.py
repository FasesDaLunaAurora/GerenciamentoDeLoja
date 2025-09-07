from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Base

class CategoriaInsumo(Base):
    __tablename__ = "categoria_insumo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False, unique=True)

    insumos = relationship("Insumo", back_populates="categoria")

class Insumo(Base):
    __tablename__ = "insumo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categoria_insumo.id"), nullable=False)
    preco_custo = Column(Float, nullable=False)
    preco_venda = Column(Float, nullable=False)
    quantidade_estoque = Column(Integer, default=0)

    categoria = relationship("CategoriaInsumo", back_populates="insumo")