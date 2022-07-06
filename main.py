from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector 
from queries import get_list_recall_ai,insert_into_extra_recall,get_list_recall_any
from pydantic_models  import Recall
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/cards")
async def get_cards(node_id: int = -1):
    # data = get_list_recall_ai()
    node_id_in_query = f'= {node_id}' if node_id!=-1 else 'is null'
    data = get_list_recall_any(node_id_in_query)
    data.append({'id':'erere','front':"End",'back':"See you later"})
    print(data)
    return data

@app.post("/recall_insert/")
async def recall_verdict_insert(recall: Recall):
    verdict = 1 if recall.verdict[0] else 2
    insert_into_extra_recall(recall.id, verdict)
    return recall