from pydantic import BaseModel
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)

class Recall(BaseModel):
    id:int

    verdict: List[bool] = None