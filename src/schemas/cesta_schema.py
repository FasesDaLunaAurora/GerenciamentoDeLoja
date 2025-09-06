from pydantic import BaseModel
from typing import Dict

class CestaCreate(BaseModel):
    nome: str
    insumos: Dict[int, int]  # id do insumo : quantidade

class CestaResponse(CestaCreate):
    id: int
