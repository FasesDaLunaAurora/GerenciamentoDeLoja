from fastapi import FastAPI
from src.routers.insumo_router import router as insumo_router
from src.routers.cesta_router import router as cesta_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Gerenciador de Loja",
    description="API para gestão de loja de cestas de presente",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir roteadores
app.include_router(insumo_router, prefix="/api/v1")
app.include_router(cesta_router, prefix="/api/v1")

@app.get("/")
async def home() -> dict:
    return {
        "message": "API Gerenciador de Loja funcionando!",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
