class Insumo:
    _id_counter = 1

    def __init__(self, nome: str, categoria: str, preco: float, unidade: str, quantidade: int):
        self.id = Insumo._id_counter
        Insumo._id_counter += 1
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.unidade = unidade
        self.quantidade = quantidade
