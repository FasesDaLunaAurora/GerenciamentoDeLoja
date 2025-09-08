from sqlalchemy.orm import Session
from src.models.insumo_model import Insumo, CategoriaInsumo
from typing import List, Optional

def listar_insumos(db: Session) -> List[Insumo]:
    return db.query(Insumo).all()

def criar_insumo(db: Session, insumo_data: dict) -> Insumo:
    # Verifica se a categoria existe
    categoria = db.query(CategoriaInsumo).filter(CategoriaInsumo.id == insumo_data["categoria_id"]).first()
    if not categoria:
        raise ValueError(f"Categoria com id {insumo_data['categoria_id']} não existe.")
    
    insumo = Insumo(**insumo_data)
    db.add(insumo)
    db.commit()
    db.refresh(insumo)
    return insumo

def buscar_insumo(db: Session, insumo_id: int) -> Optional[Insumo]:
    return db.query(Insumo).filter(Insumo.id == insumo_id).first()

def atualizar_insumo(db: Session, insumo_id: int, dados: dict) -> Optional[Insumo]:
    insumo = buscar_insumo(db, insumo_id)
    if not insumo:
        return None
    
    # Se categoria_id está sendo atualizada, verifica se existe
    if "categoria_id" in dados:
        categoria = db.query(CategoriaInsumo).filter(CategoriaInsumo.id == dados["categoria_id"]).first()
        if not categoria:
            raise ValueError(f"Categoria com id {dados['categoria_id']} não existe.")
    
    for key, value in dados.items():
        if hasattr(insumo, key):
            setattr(insumo, key, value)
    
    db.commit()
    db.refresh(insumo)
    return insumo

def deletar_insumo(db: Session, insumo_id: int) -> bool:
    insumo = buscar_insumo(db, insumo_id)
    if not insumo:
        return False
    
    db.delete(insumo)
    db.commit()
    return True

def listar_categorias_insumo(db: Session) -> List[CategoriaInsumo]:
    return db.query(CategoriaInsumo).all()

def criar_categoria_insumo(db: Session, nome: str) -> CategoriaInsumo:
    categoria = CategoriaInsumo(nome=nome)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def buscar_categoria_insumo(db: Session, categoria_id: int) -> Optional[CategoriaInsumo]:
    return db.query(CategoriaInsumo).filter(CategoriaInsumo.id == categoria_id).first()
