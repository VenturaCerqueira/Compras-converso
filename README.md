# 🛒 Compras Converso – API em Python

Projeto de extração, estruturação e exposição de dados públicos de **licitações e contratos administrativos**, construído com foco em reutilização, análise e transparência.  
A aplicação é modular, extensível e pronta para produção, integrando scraping, banco de dados, validação e documentação com Swagger.

---

## 📌 Funcionalidades

- 🔍 **Consulta de licitações por órgão**
- 📄 **Listagem de contratos vinculados às licitações**
- 📦 **Detalhamento de itens contratados**
- 🔐 **Autenticação via JWT**
- 📚 **Documentação interativa via Swagger (OpenAPI)**
- 🧪 **Testes automatizados com Jest/Supertest (em desenvolvimento)**

---

## 🚀 Tecnologias utilizadas

| Camada         | Tecnologias                                       |
|----------------|---------------------------------------------------|
| **Backend**    | Python 3.11+, FastAPI, SQLAlchemy, Pydantic       |
| **Banco de Dados** | MySQL (via SQLAlchemy ORM)                  |
| **Documentação** | Swagger / OpenAPI (via FastAPI Docs)           |
| **Segurança**  | JWT Authentication                                |
| **Utilidades** | python-dotenv, logging, Alembic (opcional)        |

---

## 📁 Estrutura do Projeto
Compras-converso/<br>
├── app/ <br>
│ ├── main.py # Entrada principal da aplicação<br>
│ ├── models/ # Modelos SQLAlchemy<br>
│ ├── schemas/ # Esquemas Pydantic<br>
│ ├── routes/ # Rotas FastAPI<br>
│ ├── services/ # Lógica de negócio<br>
│ ├── database.py # Conexão com o banco<br>
│ └── utils/ # Funções auxiliares<br>
├── .env # Variáveis de ambiente<br>
├── .gitignore # Arquivos ignorados pelo Git<br>
├── requirements.txt # Dependências do projeto<br>
└── README.md<br>


---

## ⚙️ Como rodar o projeto

### 🔧 Pré-requisitos

- Python 3.11+
- MySQL (com banco e tabelas configuradas)
- `virtualenv` ou `venv`

### 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/VenturaCerqueira/Compras-converso.git
cd Compras-converso

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
