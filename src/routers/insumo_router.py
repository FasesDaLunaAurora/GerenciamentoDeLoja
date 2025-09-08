from fastapi import APIRouter
from typing import List
from src.schemas.insumo_schema import InsumoCreate, InsumoResponse, InsumoUpdate, CategoriaInsumoCreate, CategoriaInsumoResponse
from src.controllers.insumo_controller import (
    get_all_insumos, get_insumo_by_id, create_insumo, update_insumo, delete_insumo_by_id,
    get_all_categorias_insumo, create_categoria_insumo, get_categoria_insumo_by_id
)

router = APIRouter(prefix="/insumos", tags=["Insumos"])

# Rotas para insumos
router.get("/", response_model=List[InsumoResponse])(get_all_insumos)
router.post("/", response_model=InsumoResponse)(create_insumo)
router.get("/{insumo_id}", response_model=InsumoResponse)(get_insumo_by_id)
router.patch("/{insumo_id}", response_model=InsumoResponse)(update_insumo)
router.delete("/{insumo_id}")(delete_insumo_by_id)

# Rotas para categorias de insumos
router.get("/categorias/", response_model=List[CategoriaInsumoResponse])(get_all_categorias_insumo)
router.post("/categorias/", response_model=CategoriaInsumoResponse)(create_categoria_insumo)
router.get("/categorias/{categoria_id}", response_model=CategoriaInsumoResponse)(get_categoria_insumo_by_id)
