from sqlalchemy.orm import Session
from src.models.cesta_model import Cesta, cesta_insumo_table, CategoriaCesta
from src.models.insumo_model import Insumo
from typing import Optional, List

MARGEM_LUCRO_PADRAO = 0.2
IMPOSTO_PADRAO = 0.1

def listar_cestas(db: Session) -> List[Cesta]:
    return db.query(Cesta).all()

def buscar_cesta(db: Session, cesta_id: int) -> Optional[Cesta]:
    return db.query(Cesta).filter(Cesta.id == cesta_id).first()

def criar_cesta(
    db: Session,
    nome: str,
    categoria_id: int,
    insumos_quantidade: dict,
    margem_lucro: float = MARGEM_LUCRO_PADRAO,
    imposto: float = IMPOSTO_PADRAO
) -> Cesta:
    # Valida categoria
    categoria = db.query(CategoriaCesta).filter(CategoriaCesta.id == categoria_id).first()
    if not categoria:
        raise ValueError(f"CategoriaCesta com id {categoria_id} não existe.")

    # Busca insumos do banco
    insumos = db.query(Insumo).filter(Insumo.id.in_(insumos_quantidade.keys())).all()

    # Calcula valor_custo e valor_venda_minimo
    valor_custo = sum(insumo.preco_custo * insumos_quantidade[insumo.id] for insumo in insumos)
    valor_venda_minimo = valor_custo * (1 + margem_lucro + imposto)

    # Checa disponibilidade
    disponivel = all(insumo.quantidade_estoque >= insumos_quantidade[insumo.id] for insumo in insumos)

    # Cria a cesta
    cesta = Cesta(
        nome=nome,
        categoria_id=categoria_id,
        valor_custo=valor_custo,
        valor_venda_minimo=valor_venda_minimo,
        disponivel=disponivel,
    )
    db.add(cesta)
    db.commit()
    db.refresh(cesta)

    # Adiciona insumos à cesta (tabela associativa)
    for insumo in insumos:
        db.execute(
            cesta_insumo_table.insert().values(
                cesta_id=cesta.id,
                insumo_id=insumo.id,
                quantidade=insumos_quantidade[insumo.id]
            )
        )
    db.commit()
    db.refresh(cesta)
    return cesta

def atualizar_cesta(db: Session, cesta_id: int, dados: dict) -> Optional[Cesta]:
    cesta = buscar_cesta(db, cesta_id)
    if not cesta:
        return None

    if "nome" in dados:
        cesta.nome = dados["nome"]

    if "categoria_id" in dados:
        categoria = db.query(CategoriaCesta).filter(CategoriaCesta.id == dados["categoria_id"]).first()
        if not categoria:
            raise ValueError(f"CategoriaCesta com id {dados['categoria_id']} não existe.")
        cesta.categoria_id = dados["categoria_id"]

    if "insumos_quantidade" in dados:
        insumos_quantidade = dados["insumos_quantidade"]
        insumos = db.query(Insumo).filter(Insumo.id.in_(insumos_quantidade.keys())).all()

        # Remove relações antigas
        db.execute(cesta_insumo_table.delete().where(cesta_insumo_table.c.cesta_id == cesta.id))

        # Insere novas relações
        for insumo in insumos:
            db.execute(
                cesta_insumo_table.insert().values(
                    cesta_id=cesta.id,
                    insumo_id=insumo.id,
                    quantidade=insumos_quantidade[insumo.id]
                )
            )

        # Recalcula valores e disponibilidade
        cesta.valor_custo = sum(insumo.preco_custo * insumos_quantidade[insumo.id] for insumo in insumos)
        cesta.valor_venda_minimo = cesta.valor_custo * (1 + MARGEM_LUCRO_PADRAO + IMPOSTO_PADRAO)
        cesta.disponivel = all(insumo.quantidade_estoque >= insumos_quantidade[insumo.id] for insumo in insumos)

    db.commit()
    db.refresh(cesta)
    return cesta

def deletar_cesta(db: Session, cesta_id: int) -> bool:
    cesta = buscar_cesta(db, cesta_id)
    if not cesta:
        return False

    # Remove relações
    db.execute(cesta_insumo_table.delete().where(cesta_insumo_table.c.cesta_id == cesta.id))
    db.delete(cesta)
    db.commit()
    return True