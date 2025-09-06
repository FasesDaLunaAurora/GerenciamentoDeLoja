from fastapi import APIRouter
from typing import List
from src.schemas.insumo_schema import InsumoCreate, InsumoResponse
from src.controllers.insumo_controller import (
    get_all_insumos, get_insumo_by_id, create_insumo, update_insumo, delete_insumo_by_id
)

router = APIRouter(prefix="/insumos", tags=["Insumos"])

router.get("/", response_model=List[InsumoResponse])(get_all_insumos)
router.post("/", response_model=InsumoResponse)(create_insumo)
router.get("/{insumo_id}", response_model=InsumoResponse)(get_insumo_by_id)
router.put("/{insumo_id}", response_model=InsumoResponse)(update_insumo)
router.delete("/{insumo_id}")(delete_insumo_by_id)
