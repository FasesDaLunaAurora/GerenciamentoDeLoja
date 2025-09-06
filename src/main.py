from fastapi import FastAPI
from src.routers.insumo_router import router as insumo_router
from src.routers.cesta_router import router as cesta_router

app = FastAPI(title="Gerenciador de Loja")

app.include_router(insumo_router)
app.include_router(cesta_router)

@app.get("/")
def home():
    return {"message": "API funcionando! Use /docs para testar os endpoints."}
