from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from models import Knowledge,ExtraRecall
from environment_variables import username,password,host,port,database
import json
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}', future=True)
session = Session(engine)
stmt = select(Knowledge)

def get_list_recall_ai():
    result = session.query(Knowledge).all()
    return result

def insert_into_extra_recall(memory_id,recall_verdict):

    recall_data = ExtraRecall(
         memory_id=memory_id,
      recall_verdict = recall_verdict
    )
     
    session.add(recall_data)

    session.commit()
