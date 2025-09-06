from typing import List, Optional
from src.models.cesta_model import Cesta

cestas_db: List[Cesta] = []

def listar_cestas() -> List[Cesta]:
    return cestas_db

def criar_cesta(cesta_data: dict) -> Cesta:
    cesta = Cesta(**cesta_data)
    cestas_db.append(cesta)
    return cesta

def buscar_cesta(cesta_id: int) -> Optional[Cesta]:
    return next((c for c in cestas_db if c.id == cesta_id), None)

def atualizar_cesta(cesta_id: int, dados: dict) -> Optional[Cesta]:
    cesta = buscar_cesta(cesta_id)
    if cesta:
        for key, value in dados.items():
            setattr(cesta, key, value)
    return cesta

def deletar_cesta(cesta_id: int) -> bool:
    cesta = buscar_cesta(cesta_id)
    if cesta:
        cestas_db.remove(cesta)
        return True
    return False
