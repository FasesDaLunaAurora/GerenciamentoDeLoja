from typing import Dict
from src.models.insumo_model import Insumo

class Cesta:
    _id_counter = 1

    def __init__(self, nome: str, insumos: Dict[int, int]):
        """
        insumos: dict com id do insumo e quantidade
        ex: {1: 2, 3: 1} → 2 unidades do insumo 1 e 1 unidade do insumo 3
        """
        self.id = Cesta._id_counter
        Cesta._id_counter += 1
        self.nome = nome
        self.insumos = insumos  # apenas ids e quantidades
