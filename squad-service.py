import os
from fastapi import FastAPI
from pydantic import BaseModel
from model_util import question_answerer
import uvicorn

app = FastAPI()

class SquadItem(BaseModel):
    context: str
    question: str

@app.get("/healthcheck")
def healthcheck():
    return 'Health - OK'

# TODO: Поиск может упасть с ошибкой - Exception: Truncation error: Sequence to truncate too short to respect the provided max_length
# Надо настраивать работу модели !!!
@app.post("/squad/")
def squad(item: SquadItem):
    return question_answerer(question=item.question, context=item.context)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(8090))