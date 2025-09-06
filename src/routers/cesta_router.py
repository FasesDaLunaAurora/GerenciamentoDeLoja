from fastapi import APIRouter
from typing import List
from src.schemas.cesta_schema import CestaCreate, CestaResponse
from src.controllers.cesta_controller import (
    get_all_cestas, get_cesta_by_id, create_cesta, update_cesta, delete_cesta_by_id
)

router = APIRouter(prefix="/cestas", tags=["Cestas"])

router.get("/", response_model=List[CestaResponse])(get_all_cestas)
router.post("/", response_model=CestaResponse)(create_cesta)
router.get("/{cesta_id}", response_model=CestaResponse)(get_cesta_by_id)
router.put("/{cesta_id}", response_model=CestaResponse)(update_cesta)
router.delete("/{cesta_id}")(delete_cesta_by_id)
