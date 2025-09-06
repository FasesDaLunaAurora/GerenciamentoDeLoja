from pydantic import BaseModel

class InsumoCreate(BaseModel):
    nome: str
    categoria: str
    preco: float
    unidade: str
    quantidade: int

class InsumoResponse(InsumoCreate):
    id: int
