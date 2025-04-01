# Search Customizations

Customizing the Azure Search AI using Azure Functions.

## Project Structure

```
search-customizations/
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── search.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── search.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── search_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_search.py
├── azure-functions/
│   ├── __init__.py
│   ├── function.yaml
│   ├── search_function.py
└── .env
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/search-customizations.git
    cd search-customizations
    ```

2. Install dependencies:
    ```sh
    poetry install
    ```

3. Create a `.env` file and add your environment variables.

## Usage

Run the FastAPI application:
```sh
uvicorn app.main:app --reload
```

## Testing

Run tests using pytest:
```sh
pytest
```

## License

This project is licensed under the BSD 3-Clause License.
