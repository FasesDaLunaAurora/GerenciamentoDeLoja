from fastapi import APIRouter
from src.controllers.cesta_controller import (
    listar_cestas_controller,
    criar_cesta_controller,
    buscar_cesta_controller,
    atualizar_cesta_controller,
    deletar_cesta_controller
)
from src.schemas.cesta_schema import CestaCreate, CestaUpdate, CestaOut
from typing import List

router = APIRouter(prefix="/cestas", tags=["Cestas"])

@router.get("/", response_model=List[CestaOut])
def listar_cestas():
    return listar_cestas_controller()

@router.post("/", response_model=CestaOut, status_code=201)
def criar_cesta(cesta_data: CestaCreate):
    return criar_cesta_controller(cesta_data)

@router.get("/{cesta_id}", response_model=CestaOut)
def buscar_cesta(cesta_id: int):
    return buscar_cesta_controller(cesta_id)

@router.put("/{cesta_id}", response_model=CestaOut)
def atualizar_cesta(cesta_id: int, dados: CestaUpdate):
    return atualizar_cesta_controller(cesta_id, dados)

@router.delete("/{cesta_id}", status_code=204)
def deletar_cesta(cesta_id: int):
    return deletar_cesta_controller(cesta_id)
