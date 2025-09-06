from fastapi import HTTPException
from typing import List
from src.schemas.cesta_schema import CestaCreate, CestaResponse
from src.services.cesta_service import (
    listar_cestas, criar_cesta, buscar_cesta, atualizar_cesta, deletar_cesta
)

def get_all_cestas() -> List[CestaResponse]:
    return listar_cestas()

def get_cesta_by_id(cesta_id: int) -> CestaResponse:
    cesta = buscar_cesta(cesta_id)
    if not cesta:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return cesta

def create_cesta(cesta: CestaCreate) -> CestaResponse:
    return criar_cesta(cesta.dict())

def update_cesta(cesta_id: int, dados: CestaCreate) -> CestaResponse:
    atualizado = atualizar_cesta(cesta_id, dados.dict())
    if not atualizado:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return atualizado

def delete_cesta_by_id(cesta_id: int):
    sucesso = deletar_cesta(cesta_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return {"message": "Cesta deletada com sucesso!"}
