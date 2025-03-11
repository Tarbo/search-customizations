import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
service_name = os.getenv("AZURE_SEARCH_SERVICE_NAME")
admin_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")

# Ensure service_name and admin_key are valid strings
if not service_name or not isinstance(service_name, str):
    raise ValueError("AZURE_SEARCH_SERVICE_NAME must be a valid string.")
if not admin_key or not isinstance(admin_key, str):
    raise ValueError("AZURE_SEARCH_ADMIN_KEY must be a valid string.")

# Construct the endpoint URL
endpoint = f"https://{service_name}.search.windows.net"

# Create the search client
search_client = SearchClient(endpoint=endpoint, index_name="products", credential=AzureKeyCredential(admin_key))

# Generate sample products
products = [
    {"id": "1", "name": "Product 1", "description": "Description for product 1", "price": 10.99, "category": "Category A"},
    {"id": "2", "name": "Product 2", "description": "Description for product 2", "price": 12.99, "category": "Category B"},
    {"id": "3", "name": "Product 3", "description": "Description for product 3", "price": 9.99, "category": "Category A"},
    {"id": "4", "name": "Product 4", "description": "Description for product 4", "price": 15.99, "category": "Category C"},
    {"id": "5", "name": "Product 5", "description": "Description for product 5", "price": 7.99, "category": "Category B"},
    {"id": "6", "name": "Product 6", "description": "Description for product 6", "price": 11.99, "category": "Category A"},
    {"id": "7", "name": "Product 7", "description": "Description for product 7", "price": 13.99, "category": "Category C"},
    {"id": "8", "name": "Product 8", "description": "Description for product 8", "price": 8.99, "category": "Category B"},
    {"id": "9", "name": "Product 9", "description": "Description for product 9", "price": 14.99, "category": "Category A"},
    {"id": "10", "name": "Product 10", "description": "Description for product 10", "price": 6.99, "category": "Category C"}
]

# Upload the products to the index
search_client.upload_documents(documents=products)

print("Sample products uploaded successfully.")
