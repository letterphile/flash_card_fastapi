from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer,Float
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
import datetime
Base = declarative_base()

class Knowledge(Base):
    __tablename__ = "list_to_recall_AI"

    id = Column(Integer, primary_key=True)
    front = Column(String(250))
    back = Column(String(250))
    
    

    def __repr__(self):
        return f"Knowledge(id={self.id!r}, front={self.question!r}, back={self.answer!r})"

class ExtraRecall(Base):
    __tablename__ = "recall"
    recall_id = Column(Integer,primary_key=True)
    memory_id = Column(Integer)
    recall_verdict = Column(Integer)
    created = Column(DateTime,default=datetime.datetime.now)
    def __repr__(self):
        return f"Extra Recall(memory_id={self.memory_id!r}, verdict={self.recall_verdict!r})"