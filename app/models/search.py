from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
