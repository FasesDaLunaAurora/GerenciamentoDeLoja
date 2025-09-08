"""
Script para popular o banco de dados com dados iniciais
"""
from sqlalchemy.orm import Session
from src.db import SessionLocal, engine
from src.models.insumo_model import CategoriaInsumo, Insumo
from src.models.cesta_model import CategoriaCesta, Cesta
from src.db import Base

def create_tables():
    """Cria todas as tabelas"""
    Base.metadata.create_all(bind=engine)

def populate_categorias_insumo(db: Session):
    """Popula categorias de insumos"""
    categorias = [
        "Chocolates",
        "Flores",
        "Cestas",
        "Vinhos",
        "Doces",
        "Frutas",
        "Embalagens"
    ]
    
    for nome in categorias:
        categoria_existente = db.query(CategoriaInsumo).filter(CategoriaInsumo.nome == nome).first()
        if not categoria_existente:
            categoria = CategoriaInsumo(nome=nome)
            db.add(categoria)
    
    db.commit()

def populate_categorias_cesta(db: Session):
    """Popula categorias de cestas"""
    categorias = [
        "Romântica",
        "Aniversário",
        "Natal",
        "Páscoa",
        "Dia das Mães",
        "Corporativa",
        "Gourmet"
    ]
    
    for nome in categorias:
        categoria_existente = db.query(CategoriaCesta).filter(CategoriaCesta.nome == nome).first()
        if not categoria_existente:
            categoria = CategoriaCesta(nome=nome)
            db.add(categoria)
    
    db.commit()

def populate_insumos(db: Session):
    """Popula alguns insumos de exemplo"""
    # Buscar categorias
    cat_chocolate = db.query(CategoriaInsumo).filter(CategoriaInsumo.nome == "Chocolates").first()
    cat_flores = db.query(CategoriaInsumo).filter(CategoriaInsumo.nome == "Flores").first()
    cat_cestas = db.query(CategoriaInsumo).filter(CategoriaInsumo.nome == "Cestas").first()
    
    insumos_exemplo = [
        {
            "nome": "Chocolate Ferrero Rocher 12un",
            "categoria_id": cat_chocolate.id,
            "preco_custo": 25.00,
            "preco_venda": 35.00,
            "quantidade_estoque": 50
        },
        {
            "nome": "Rosas Vermelhas (dúzia)",
            "categoria_id": cat_flores.id,
            "preco_custo": 30.00,
            "preco_venda": 45.00,
            "quantidade_estoque": 20
        },
        {
            "nome": "Cesta de Vime Pequena",
            "categoria_id": cat_cestas.id,
            "preco_custo": 15.00,
            "preco_venda": 25.00,
            "quantidade_estoque": 30
        }
    ]
    
    for insumo_data in insumos_exemplo:
        insumo_existente = db.query(Insumo).filter(Insumo.nome == insumo_data["nome"]).first()
        if not insumo_existente:
            insumo = Insumo(**insumo_data)
            db.add(insumo)
    
    db.commit()

def main():
    """Função principal"""
    print("Criando tabelas...")
    create_tables()
    
    print("Populando banco de dados...")
    db = SessionLocal()
    
    try:
        populate_categorias_insumo(db)
        print("✓ Categorias de insumos criadas")
        
        populate_categorias_cesta(db)
        print("✓ Categorias de cestas criadas")
        
        populate_insumos(db)
        print("✓ Insumos de exemplo criados")
        
        print("✅ Banco de dados populado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao popular banco: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()