from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class NestedListSumResponse(BaseModel):
    batchid: str
    response: List[int]
    status: str
    started_at: Optional[datetime]
    completed_at: Optional[datetime]