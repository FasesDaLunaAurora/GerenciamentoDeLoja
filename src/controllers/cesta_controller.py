from fastapi import Depends, HTTPException 
from sqlalchemy.orm import Session 
from src.db import get_db 
from src.services.cesta_service import (
    listar_cestas,
    buscar_cesta,
    criar_cesta,
    atualizar_cesta,
    deletar_cesta
)
from src.schemas.cesta_schema import CestaCreate, CestaUpdate 

def listar_cestas_controller(db: Session = Depends(get_db)): 
    return listar_cestas(db) 

def criar_cesta_controller(cesta_data: CestaCreate, db: Session = Depends(get_db)):
    return criar_cesta(
        db, 
        nome=cesta_data.nome,
        categoria_id=cesta_data.categoria_id, 
        insumos_quantidade=cesta_data.insumos_quantidade 
    )

def buscar_cesta_controller(cesta_id: int, db: Session = Depends(get_db)):
    cesta = buscar_cesta(db, cesta_id)
    if not cesta:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return cesta

def atualizar_cesta_controller(cesta_id: int, dados: CestaUpdate, db: Session = Depends(get_db)):
    update_data = dados.dict(exclude_unset=True)
    cesta = atualizar_cesta(db, cesta_id, update_data)
    if not cesta:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return cesta

def deletar_cesta_controller(cesta_id: int, db: Session = Depends(get_db)):
    sucesso = deletar_cesta(db, cesta_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cesta não encontrada")
    return {"detail": "Cesta deletada com sucesso"}
