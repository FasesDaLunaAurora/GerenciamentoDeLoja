from pydantic import BaseModel
from typing import Dict, Optional

class CategoriaCestaCreate(BaseModel):
    nome: str

class CategoriaCestaResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True

class CestaCreate(BaseModel):
    nome: str
    categoria_id: int
    insumos_quantidade: Dict[int, int]

class CestaUpdate(BaseModel):
    nome: Optional[str] = None
    categoria_id: Optional[int] = None
    insumos_quantidade: Optional[Dict[int, int]] = None

class CestaOut(BaseModel):
    id: int
    nome: str
    categoria_id: int
    valor_custo: float
    valor_venda_minimo: float
    disponivel: bool

    class Config:
        from_attributes = True