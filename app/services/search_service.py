from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from app.config import settings
from app.models.search import SearchResult

def search_documents(query: str) -> list[SearchResult]:
    print(f"Connecting to Azure Search at: {settings.AZURE_SEARCH_ENDPOINT}")
    print(f"Using index: {settings.AZURE_SEARCH_INDEX_NAME_PRODUCT}")
    print(f"Query: {query}")
    client = SearchClient(
        endpoint=settings.AZURE_SEARCH_ENDPOINT,
        index_name=settings.AZURE_SEARCH_INDEX_NAME_PRODUCT,
        credential=AzureKeyCredential(settings.AZURE_SEARCH_ADMIN_KEY)
    )
    results = client.search(query)
    return [
        SearchResult(
            id=doc[settings.PRODUCT_INDEX_COLUMNS['id']],
            name=doc[settings.PRODUCT_INDEX_COLUMNS['name']],
            description=doc[settings.PRODUCT_INDEX_COLUMNS['description']],
            price=doc[settings.PRODUCT_INDEX_COLUMNS['price']],
            category=doc[settings.PRODUCT_INDEX_COLUMNS['category']]
        ) for doc in results
    ]
