from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src.controllers.cesta_controller import (
    listar_cestas_controller,
    criar_cesta_controller,
    buscar_cesta_controller,
    atualizar_cesta_controller,
    deletar_cesta_controller,
    listar_categorias_cesta_controller,
    criar_categoria_cesta_controller,
    buscar_categoria_cesta_controller
)
from src.schemas.cesta_schema import CestaCreate, CestaUpdate, CestaOut, CategoriaCestaCreate, CategoriaCestaResponse
from typing import List

router = APIRouter(prefix="/cestas", tags=["Cestas"])

# Rotas para cestas
@router.get("/", response_model=List[CestaOut])
def listar_cestas():
    return listar_cestas_controller()

@router.post("/", response_model=CestaOut)
def criar_cesta(cesta_data: CestaCreate):
    return criar_cesta_controller(cesta_data)

@router.get("/{cesta_id}", response_model=CestaOut)
def buscar_cesta(cesta_id: int):
    return buscar_cesta_controller(cesta_id)

@router.patch("/{cesta_id}", response_model=CestaOut)
def atualizar_cesta(cesta_id: int, dados: CestaUpdate):
    return atualizar_cesta_controller(cesta_id, dados)

@router.delete("/{cesta_id}")
def deletar_cesta(cesta_id: int):
    return deletar_cesta_controller(cesta_id)

# Rotas para categorias de cestas
@router.get("/categorias/", response_model=List[CategoriaCestaResponse])
def listar_categorias_cesta(db: Session = Depends(get_db)):
    return listar_categorias_cesta_controller(db)

@router.post("/categorias/", response_model=CategoriaCestaResponse)
def criar_categoria_cesta(categoria: CategoriaCestaCreate, db: Session = Depends(get_db)):
    return criar_categoria_cesta_controller(categoria, db)

@router.get("/categorias/{categoria_id}", response_model=CategoriaCestaResponse)
def buscar_categoria_cesta(categoria_id: int, db: Session = Depends(get_db)):
    return buscar_categoria_cesta_controller(categoria_id, db)
