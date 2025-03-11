from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    id: str
    title: str
    content: str
