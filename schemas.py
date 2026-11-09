from pydantic import BaseModel, Field


class FeedbackEntrada(BaseModel):
    feedback_cliente : str = Field(description="Texto de avaliação do cliente")

class AnaliseSaida(BaseModel):  
    sentimento_cliente : str = Field(description="Um sentimento, podendo ser neutro, negativo ou positivo.")
    risco_desistencia : int = Field(ge=0, le=100, description="Pontuação inteira de risco de cancelamento de 0 a 100")