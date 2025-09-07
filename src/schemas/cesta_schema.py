from pydantic import BaseModel
from typing import Dict, Optional

class CestaCreate(BaseModel):
    nome: str
    categoria_id: int  # agora referenciando a tabela CategoriaCesta
    insumos_quantidade: Dict[int, int]  # {insumo_id: quantidade}

class CestaUpdate(BaseModel):
    nome: Optional[str]
    categoria_id: Optional[int]
    insumos_quantidade: Optional[Dict[int, int]]

class CestaOut(BaseModel):
    id: int
    nome: str
    categoria: str  # para saída, podemos exibir o nome da categoria
    valor_custo: float
    valor_venda_minimo: float
    disponivel: bool

    class Config:
        orm_mode = True