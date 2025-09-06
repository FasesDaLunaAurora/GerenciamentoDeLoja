from src.models.insumo_model import Insumo
from typing import List, Optional

insumos_db: List[Insumo] = []

def listar_insumos() -> List[Insumo]:
    return insumos_db

def criar_insumo(insumo_data: dict) -> Insumo:
    insumo = Insumo(**insumo_data)
    insumos_db.append(insumo)
    return insumo

def buscar_insumo(insumo_id: int) -> Optional[Insumo]:
    return next((i for i in insumos_db if i.id == insumo_id), None)

def atualizar_insumo(insumo_id: int, dados: dict) -> Optional[Insumo]:
    insumo = buscar_insumo(insumo_id)
    if insumo:
        for key, value in dados.items():
            setattr(insumo, key, value)
    return insumo

def deletar_insumo(insumo_id: int) -> bool:
    insumo = buscar_insumo(insumo_id)
    if insumo:
        insumos_db.remove(insumo)
        return True
    return False
