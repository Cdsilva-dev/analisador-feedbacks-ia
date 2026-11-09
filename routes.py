from fastapi import FastAPI,APIRouter,HTTPException
from schemas import AnaliseSaida, FeedbackEntrada
from services import analisar_feedback_cliente,buscar_todos_feedbacks

router = APIRouter(prefix="/feedbacks", tags=["Feedbacks"])
@router.post("/", response_model= AnaliseSaida)

def processar_feedback(dados : FeedbackEntrada):    
    try:
     resultado = analisar_feedback_cliente(dados.feedback_cliente)
     return resultado
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))

@router.get("/")
def listar_feedbacks():
    try:
     return buscar_todos_feedbacks()
    except Exception as erro:
       raise HTTPException(status_code=500 , detail= str(erro))