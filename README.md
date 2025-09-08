# 📌 GerenciamentoDeLoja
Aplicativo web para gestão de uma loja de cestas de presente, para uso real no negócio, com base de expansão e implementação com ferramentas gratuitas mantendo o padrão profissional.

## ✨ Escopo Atual 

- CRUD de insumos (produtos) → Ex.: chocolate, flores, cestas.
- CRUD de cestas (combinações de insumos) → Ex.: “Cesta Romântica” com lista de insumos.

## 🚀 Tecnologias Utilizadas

- Backend: Python + FastAPI
- Frontend: React
- Banco de Dados: PostgreSQL, conexão com banco via SQLAlchemy
- Testes: Pytest
- Validação: Pydantic
- Migrações: Alembic
- Documentação automática: Swagger nativo no FastAPI
- Containerização: Docker
- Versionamento: GitHub
- Deploy: Render

## 🗂 Estrutura do Projeto

O projeto segue uma organização modular, separando **models, services e controllers**, facilitando a escalabilidade futura para microsserviços.

```bash
📁 nome-do-projeto
   ├── 📁 alembic
   │   └── env.py
   ├── 📁 src               
   │   ├── 📁 controllers            
   │   │   ├── insumo_controller.py
   │   │   └── cesta_controller.py
   │   ├── 📁 models         
   │   │   ├── __init__.py
   │   │   ├── insumo_model.py
   │   │   └── cesta_model.py
   │   ├── 📁 routers       
   │   │   ├── insumo_router.py
   │   │   └── cesta_router.py
   │   ├── 📁 services       
   │   │   ├── insumo_service.py
   │   │   └── cesta_service.py
   │   ├── 📁 schemas        
   │   │   ├── insumo_schema.py
   │   │   └── cesta_schema.py
   │   ├── __init__.py            
   │   └── db.py
   │   └── main.py         
   ├── 📄 README.md          
   └── alembic.ini
```

## ✅ Funcionalidades (MVP)

- [ ] **CRUD de Insumos**
  - Cadastrar insumos com nome, categoria, preço unitário, unidade de medida e quantidade em estoque.
  - Editar informações de insumos existentes.
  - Listar todos os insumos.
  - Remover insumos.

- [ ] **CRUD de Cestas**
  - Criar cestas contendo múltiplos insumos e suas respectivas quantidades.
  - Editar informações de cestas existentes.
  - Listar todas as cestas cadastradas.
  - Remover cestas.

- [ ] **API RESTful**
  - Endpoints organizados e versionados (`/api/v1`).
  - Documentação automática via **Swagger** (nativa no FastAPI).

- [ ] **Banco de Dados**
  - Integração com banco relacional (PostgreSQL ou SQLite para ambiente local).
  - Migrações de schema com **Alembic**.

- [ ] **Validação de Dados**
  - Schemas com **Pydantic** para entrada e saída.

- [ ] **Testes Automatizados**
  - Testes unitários com **pytest** para rotas principais.

- [ ] **Configuração de Ambiente**
  - Variáveis de ambiente para credenciais e configurações.
  - Arquivo `.env.example` para referência.

- [ ] **Containerização**
  - Suporte a **Docker** e **Docker Compose** para execução da API e banco de dados.


## 📌 Backlog

- [ ] **Controle de Estoque**
  - Atualização automática da quantidade de insumos ao criar/editar cestas.
  - Alertas para insumos com estoque baixo.

- [ ] **Integração com Pedidos**
  - Cadastro e gerenciamento de pedidos vinculados às cestas.
  - Atualização automática do estoque ao confirmar pedido.

- [ ] **Relatórios e Dashboards**
  - Relatório de vendas por período.
  - Análise de insumos mais utilizados e cestas mais vendidas.

- [ ] **Autenticação e Permissões**
  - Login e cadastro de usuários.
  - Perfis com diferentes níveis de acesso (admin, operador, etc.).
  - Autenticação via JWT.

- [ ] **Interface Web**
  - Painel administrativo para gestão de insumos, cestas e pedidos.
  - UI responsiva (React ou outro framework JS).

- [ ] **Deploy em Produção**
  - Deploy gratuito (Railway, Render, Deta ou outra opção).
  - Configuração de variáveis de ambiente e banco de dados remoto.

- [ ] **Melhorias de Performance e Escalabilidade**
  - Cache com Redis.
  - Paginação nos endpoints.


## 🧪 Testes

Este projeto utiliza **pytest** para rodar os testes automatizados.

### Como rodar os testes

Crie e ative o ambiente virtual, instale as dependências de desenvolvimento e execute:

```bash```
#### Instalar dependências (incluindo pytest)
```$ pip install -r requirements.txt```

#### Rodar todos os testes
```$ pytest```

#### Rodar com exibição detalhada
```$ pytest -v```

#### Rodar testes com cobertura
```$ pytest --cov=app```

#### (Opcional) Gerar relatório de cobertura em HTML
```$ pytest --cov=app --cov-report=html```

## 🛠️ Instalação e Execução

Antes de rodar o projeto localmente, você precisa ter instalado:

- **Python 3.10+** (recomendado 3.11)  
  - Usado para a API (FastAPI).  
  - Verifique com: `python --version` ou `python3 --version`

- **pip** (gerenciador de pacotes do Python)  
  - Verifique com: `pip --version`

- **Git**  
  - Para versionamento e push ao GitHub.  
  - Verifique com: `git --version`

- **FastAPI**  
  - Para funcionamento do back-end.  
  - Instale com: `pip install fastapi`
 
- **Uvicorn**  
  - Para rodar as APIs localmente.  
  - Instale com: `pip install uvicorn`
  - Deploy local: `uvicorn main:app --reload`
    
- **Docker** e **Docker Compose** (recomendado)  
  - Para rodar o banco de dados e ambiente isolado.  
  - Verifique com: `docker --version` e `docker compose version` (ou `docker-compose --version`)

- **PostgreSQL** (opcional localmente — pode ser provisionado via Docker)  
  - Recomendado para produção/semelhança com deploy.  
  - **Observação**: se você estiver começando e não quer instalar Postgres, o projeto pode usar **SQLite** localmente — sem instalação adicional.

- **Node.js 18+ (LTS)** e **npm/yarn** — *opcional*  
  - Apenas necessário se você for desenvolver a interface web (React/Vite).  
  - Verifique com: `node -v` e `npm -v`

- **Recomendado (ferramentas dev)**  
  - Editor: **VSCode** (ou outro de sua preferência)  
  - (Opcional) **poetry** para gerenciamento de dependências e ambiente virtual, ou use `python -m venv` + `pip`.

**Variáveis de ambiente mínimas (serão documentadas na seção de instalação):**
- `DATABASE_URL` (ex.: `postgresql://user:pass@localhost:5432/dbname`)
- `SECRET_KEY` (chave para tokens/JWT)
- `ENV=development|production`

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
