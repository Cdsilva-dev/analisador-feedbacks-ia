from google import genai
from dotenv import load_dotenv

import os

from schemas import AnaliseSaida

load_dotenv()


cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analisar_feedback_cliente(texto : str) -> AnaliseSaida:
  resposta =  cliente.models.generate_content(
        model="gemini-3.8-flash",
        contents= f"Por favor, análise o feedback {texto} deste cliente.",
        config={
            "response_mime_type" : "application/json",
            "response_schema"  : AnaliseSaida
        } 
    )
  return resposta.parsed