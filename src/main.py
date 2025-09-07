from fastapi import FastAPI # inicializa o FastAPI
from src.routers.insumo_router import router as insumo_router # importa o roteador de insumos
from src.routers.cesta_router import router as cesta_router # importa o roteador de cestas
from fastapi.middleware.cors import CORSMiddleware # importa middleware CORS para permitir requisições de diferentes origens

app = FastAPI(title="Gerenciador de Loja") # cria a aplicação Gerenciador de Loja

app.include_router(insumo_router) # adiciona o roteador de insumos à aplicação
app.include_router(cesta_router) # adiciona o roteador de cestas à aplicação

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
@app.get("/") # rota raiz para verificar se a API está funcionando
async def home() -> dict:
    return {"message": "API funcionando! Use /docs para testar os endpoints."}
