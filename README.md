# 🧠 Analisador de Feedbacks com Inteligência Artificial

Uma API RESTful desenvolvida em **FastAPI** que utiliza modelos de linguagem (LLMs) via **Groq Cloud API** para realizar análises preditivas automatizadas de sentimentos e risco de cancelamento (*churn*) em feedbacks de clientes, persistindo os resultados em banco de dados **SQLite**.

---

## 🎯 Objetivo do Projeto

Automatizar o fluxo de atendimento e retenção de clientes por meio da Inteligência Artificial:
1. **Classificação de Sentimentos:** Identifica o tom do cliente (Positivo, Negativo ou Neutro).
2. **Predição de Churn:** Atribui uma nota de 0 a 100 para o risco de desistência do cliente.
3. **Persistência de Dados:** Registra as análises em um banco relacional para consultas históricas e criação de dashboards.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+ 🐍
* **Framework Web:** FastAPI ⚡
* **Servidor ASGI:** Uvicorn 🚀
* **IA / LLM:** Groq SDK (modelo Llama-3 / GPT-OSS) 🤖
* **Validação de Dados:** Pydantic 🛡️
* **Banco de Dados:** SQLite3 🗄️
* **Variáveis de Ambiente:** python-dotenv 🔐

---

## 🏗️ Arquitetura do Projeto

O projeto segue a separação de responsabilidades (Arquitetura em Camadas):

```text
analisador-feedbacks-ia/
├── main.py          # Ponto de entrada da aplicação FastAPI
├── routes.py        # Definição dos endpoints (POST e GET)
├── services.py      # Regras de negócio, API da Groq e SQLite
├── schemas.py       # Modelos Pydantic para validação
├── banco.db         # Banco de dados SQLite
├── .env             # Chaves de API (protegido pelo .gitignore)
└── requirements.txt # Dependências do projeto
```

---

## 📌 Endpoints da API

| Método | Rota | Descrição | Status HTTP |
| :--- | :--- | :--- | :--- |
| **POST** | `/feedbacks/` | Recebe um texto de feedback, executa a análise via IA e salva no banco de dados. | `200 OK` / `500 Error` |
| **GET** | `/feedbacks/` | Retorna o histórico de todas as análises de feedback registradas. | `200 OK` / `500 Error` |

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/Cdsilva-dev/analisador-feedbacks-ia.git
cd analisador-feedbacks-ia
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com a sua chave da Groq:
```env
GROQ_API_KEY="sua_chave_groq_aqui"
```

### 5. Iniciar a API
```bash
uvicorn main:app --reload
```

Acesse a documentação interativa no navegador através do Swagger UI:
👉 **http://127.0.0.1:8000/docs**