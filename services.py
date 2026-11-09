import os
import sqlite3
from dotenv import load_dotenv
from groq import Groq
from schemas import AnaliseSaida
import json

load_dotenv()

def criar_banco_de_dados():
 conexao = sqlite3.connect("banco.db")
 cursor = conexao.cursor()
 cursor.execute(""" CREATE TABLE IF NOT EXISTS feedbacks(
 id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 texto_cliente  TEXT NOT NULL,
 sentimento TEXT NOT NULL,
 risco_desistencia INTEGER NOT NULL)""")
 conexao.commit()
 conexao.close()
 
criar_banco_de_dados()

cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))

def salvar_feedback_no_banco(texto, sentimento, risco):
  conexao = sqlite3.connect("banco.db")
  cursor = conexao.cursor()
  cursor.execute("""INSERT INTO feedbacks (texto_cliente, sentimento, risco_desistencia)
  VALUES (?,?,?)""",  (texto, sentimento, risco))
  conexao.commit()
  conexao.close()

def analisar_feedback_cliente(texto : str) -> AnaliseSaida:
  resposta =  cliente.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages= [{ "role": "system", "content": """  Por favor, análise o feedback do cliente, me dando 2 tipos : sentimento do cliente e o risco de desistência. O formato de resposta deve ser estritamente em JSON e precisa ter os nomes das variaveis identicas a : 'sentimento_cliente' e 'risco_desistencia.  Siga as regras abaixo para preencher os valores:
1. "sentimento_cliente": Uma string contendo apenas "Positivo", "Negativo" ou "Neutro".
2. "risco_desistencia": Um número inteiro de 0 a 100 indicando a porcentagem de risco do cliente cancelar o serviço (sendo 0 sem risco e 100 risco máximo). Responda APENAS com o número, sem palavras ou o símbolo de %.  """} , {"role" : "user", "content" : f"Análise este feedback: {texto}"}],
        response_format={"type" : "json_object"}
    )
  texto_json = resposta.choices[0].message.content
  dados = json.loads(texto_json)
  analise = AnaliseSaida(**dados)
  salvar_feedback_no_banco(texto, analise.sentimento_cliente , analise.risco_desistencia)
  return analise

def buscar_todos_feedbacks():
  conexao = sqlite3.connect("banco.db")
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM feedbacks ")
  registros = cursor.fetchall()
  conexao.close()

  feedbacks = []
  for linha in registros:
    feedbacks.append({
      "id": linha[0],
      "texto_cliente": linha[1],
      "sentimento": linha[2],
      "risco_desistencia": linha[3]
    })
  return feedbacks