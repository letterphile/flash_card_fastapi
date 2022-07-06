from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from models import Knowledge,ExtraRecall
from environment_variables import username,password,host,port,database
from data_processing import list_of_tuples_to_json
import mysql.connector 
from long_queries import recall_from_any_node_query
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

def get_list_recall_any(node_query,):
    cnx = mysql.connector.connect(user=username, database=database,password=password,host=host,port=port)
    cursor = cnx.cursor()
    query = recall_from_any_node_query(node_query)
    cursor.execute(query)
    result = list_of_tuples_to_json( cursor.fetchall())
    cursor.close()
    cnx.close()
    return result