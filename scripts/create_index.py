import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, SimpleField, SearchableField, SearchFieldDataType as sfd
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

# Create the search index client
index_client = SearchIndexClient(endpoint=endpoint, credential=AzureKeyCredential(admin_key))

# Define the index schema
index_name = "products"
fields = [
    SimpleField(name="id", type=sfd.String, key=True, filterable=True),
    SearchableField(name="name", type=sfd.String, sortable=True, filterable=True),
    SearchableField(name="description", type=sfd.String),
    SimpleField(name="price", type=sfd.Double, filterable=True, sortable=True),
    SimpleField(name="category", type=sfd.String, filterable=True, sortable=True, facetable=True)
]

# Create the index
index = SearchIndex(name=index_name, fields=fields)
index_client.create_index(index)

print("Index created successfully.")
