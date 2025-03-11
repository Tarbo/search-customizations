import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm, SearchableField
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
admin_key = os.getenv("AZURE_SEARCH_ADMIN_KEY")

# Create the search index client
index_client = SearchIndexClient(endpoint=endpoint, credential=AzureKeyCredential(admin_key))

# Define the index schema
index_name = "products"
fields = [
    SimpleField(name="id", type=edm.String, key=True, filterable=True),
    SearchableField(name="name", type=edm.String, sortable=True, filterable=True),
    SearchableField(name="description", type=edm.String),
    SimpleField(name="price", type=edm.Double, filterable=True, sortable=True),
    SimpleField(name="category", type=edm.String, filterable=True, sortable=True, facetable=True)
]

# Create the index
index = SearchIndex(name=index_name, fields=fields)
index_client.create_index(index)

# Create the search client
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

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

print("Index created and sample products uploaded successfully.")
