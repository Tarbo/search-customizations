import os
import yaml
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), '../config.yaml'), 'r') as file:
            config = yaml.safe_load(file)
        self.AZURE_SEARCH_SERVICE_NAME = os.getenv("AZURE_SEARCH_SERVICE_NAME")
        self.AZURE_SEARCH_ADMIN_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")
        self.AZURE_SEARCH_QUERY_KEY = os.getenv("AZURE_SEARCH_QUERY_KEY")
        self.AZURE_SEARCH_INDEX_NAME_PRODUCT = os.getenv("AZURE_SEARCH_INDEX_NAME_PRODUCT")       
        self.AZURE_SEARCH_ENDPOINT = f"https://{self.AZURE_SEARCH_SERVICE_NAME}.search.windows.net"
        self.PRODUCT_INDEX_COLUMNS = config['product_index_columns']

settings = Settings()
