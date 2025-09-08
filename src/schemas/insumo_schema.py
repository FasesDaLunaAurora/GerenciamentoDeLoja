from pydantic import BaseModel
from typing import Optional

class InsumoCreate(BaseModel):
    nome: str
    categoria_id: int
    preco_custo: float
    preco_venda: float
    quantidade_estoque: Optional[int] = 0

class InsumoUpdate(BaseModel):
    nome: Optional[str] = None
    categoria_id: Optional[int] = None
    preco_custo: Optional[float] = None
    preco_venda: Optional[float] = None
    quantidade_estoque: Optional[int] = None

class InsumoResponse(BaseModel):
    id: int
    nome: str
    categoria_id: int
    preco_custo: float
    preco_venda: float
    quantidade_estoque: int

    class Config:
        from_attributes = True

class CategoriaInsumoCreate(BaseModel):
    nome: str

class CategoriaInsumoResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True
