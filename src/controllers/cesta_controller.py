from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import get_db
from src.services.cesta_service import (
    listar_cestas,
    buscar_cesta,
    criar_cesta,
    atualizar_cesta,
    deletar_cesta,
    listar_categorias_cesta,
    criar_categoria_cesta,
    buscar_categoria_cesta
)
from src.schemas.cesta_schema import CestaCreate, CestaUpdate, CategoriaCestaCreate, CategoriaCestaResponse

def listar_cestas_controller(db: Session = Depends(get_db)):
    return listar_cestas(db)

def criar_cesta_controller(cesta_data: CestaCreate, db: Session = Depends(get_db)):
    try:
        return criar_cesta(
            db,
            nome=cesta_data.nome,
            categoria_id=cesta_data.categoria_id,
            insumos_quantidade=cesta_data.insumos_quantidade
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def buscar_cesta_controller(cesta_id: int, db: Session = Depends(get_db)):
    cesta = buscar_cesta(db, cesta_id)
    if not cesta:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return cesta

def atualizar_cesta_controller(cesta_id: int, dados: CestaUpdate, db: Session = Depends(get_db)):
    try:
        update_data = dados.model_dump(exclude_unset=True)
        cesta = atualizar_cesta(db, cesta_id, update_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not cesta:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return cesta

def deletar_cesta_controller(cesta_id: int, db: Session = Depends(get_db)):
    sucesso = deletar_cesta(db, cesta_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return {"detail": "Cesta deletada com sucesso"}

def listar_categorias_cesta_controller(db: Session = Depends(get_db)):
    return listar_categorias_cesta(db)

def criar_categoria_cesta_controller(categoria: CategoriaCestaCreate, db: Session = Depends(get_db)):
    return criar_categoria_cesta(db, categoria.nome)

def buscar_categoria_cesta_controller(categoria_id: int, db: Session = Depends(get_db)):
    categoria = buscar_categoria_cesta(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria
