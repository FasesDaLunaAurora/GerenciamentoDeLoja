from fastapi import HTTPException
from typing import List
from src.schemas.insumo_schema import InsumoCreate, InsumoResponse
from src.services.insumo_service import (
    listar_insumos, criar_insumo, buscar_insumo, atualizar_insumo, deletar_insumo
)

def get_all_insumos() -> List[InsumoResponse]:
    return listar_insumos()

def get_insumo_by_id(insumo_id: int) -> InsumoResponse:
    insumo = buscar_insumo(insumo_id)
    if not insumo:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return insumo

def create_insumo(insumo: InsumoCreate) -> InsumoResponse:
    return criar_insumo(insumo.dict())

def update_insumo(insumo_id: int, dados: InsumoCreate) -> InsumoResponse:
    atualizado = atualizar_insumo(insumo_id, dados.dict())
    if not atualizado:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return atualizado

def delete_insumo_by_id(insumo_id: int):
    sucesso = deletar_insumo(insumo_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return {"message": "Insumo deletado com sucesso!"}
