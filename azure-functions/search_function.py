import logging
import azure.functions as func
from app.services.search_service import search_documents
from app.models.search import SearchRequest

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        search_request = SearchRequest(**req_body)
        results = search_documents(search_request.query)
        return func.HttpResponse(
            body=results.json(),
            status_code=200,
            mimetype="application/json"
        )
    except ValueError:
        return func.HttpResponse(
            "Invalid input",
            status_code=400
        )
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(
            "Internal server error",
            status_code=500
        )
