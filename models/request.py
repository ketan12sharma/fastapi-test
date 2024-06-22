from dataclasses import Field
from typing import List
from pydantic import BaseModel, conlist

class NestedListSumRequest(BaseModel):
    batchid: str
    payload: conlist(conlist(int, min_length=1), min_length=1)