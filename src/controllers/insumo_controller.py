from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from src.db import get_db
from src.schemas.insumo_schema import InsumoCreate, InsumoResponse, InsumoUpdate, CategoriaInsumoCreate, CategoriaInsumoResponse
from src.services.insumo_service import (
    listar_insumos, criar_insumo, buscar_insumo, atualizar_insumo, deletar_insumo,
    listar_categorias_insumo, criar_categoria_insumo, buscar_categoria_insumo
)

def get_all_insumos(db: Session = Depends(get_db)) -> List[InsumoResponse]:
    return listar_insumos(db)

def get_insumo_by_id(insumo_id: int, db: Session = Depends(get_db)) -> InsumoResponse:
    insumo = buscar_insumo(db, insumo_id)
    if not insumo:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return insumo

def create_insumo(insumo: InsumoCreate, db: Session = Depends(get_db)) -> InsumoResponse:
    try:
        return criar_insumo(db, insumo.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def update_insumo(insumo_id: int, dados: InsumoUpdate, db: Session = Depends(get_db)) -> InsumoResponse:
    try:
        atualizado = atualizar_insumo(db, insumo_id, dados.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not atualizado:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return atualizado

def delete_insumo_by_id(insumo_id: int, db: Session = Depends(get_db)):
    sucesso = deletar_insumo(db, insumo_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Insumo não encontrado")
    return {"message": "Insumo deletado com sucesso!"}

def get_all_categorias_insumo(db: Session = Depends(get_db)) -> List[CategoriaInsumoResponse]:
    return listar_categorias_insumo(db)

def create_categoria_insumo(categoria: CategoriaInsumoCreate, db: Session = Depends(get_db)) -> CategoriaInsumoResponse:
    return criar_categoria_insumo(db, categoria.nome)

def get_categoria_insumo_by_id(categoria_id: int, db: Session = Depends(get_db)) -> CategoriaInsumoResponse:
    categoria = buscar_categoria_insumo(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria
