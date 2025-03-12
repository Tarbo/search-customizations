import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AZURE_SEARCH_ENDPOINT: str = f"https://{os.getenv('AZURE_SEARCH_SERVICE_NAME')}.search.windows.net"
    AZURE_SEARCH_KEY: str = os.getenv("AZURE_SEARCH_ADMIN_KEY")
    AZURE_SEARCH_INDEX_NAME_PRODUCT: str = os.getenv("AZURE_SEARCH_INDEX_NAME_PRODUCT")  # Updated index name variable
    AZURE_SEARCH_QUERY_KEY: str = os.getenv("AZURE_SEARCH_QUERY_KEY")

settings = Settings()
