from fastapi import APIRouter, HTTPException
from app.models.search import SearchRequest, SearchResult
from app.services.search_service import search_documents

router = APIRouter()

@router.post("/search", response_model=list[SearchResult])
def search(request: SearchRequest):
    results = search_documents(request.query)
    if not results:
        raise HTTPException(status_code=404, detail="No documents found")
    return results
