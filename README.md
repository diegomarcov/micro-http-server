# GraphQL + FastAPI Healthcheck Server

This is a minimalistic HTTP server using `FastAPI` and `strawberry-graphql` that includes both REST and GraphQL healthcheck endpoints.

## Set up

1. Install the required dependencies:

   ```bash
   pip install pip-tools
   pip-compile requirements.in
   pip install -r requirements.txt
   ```

## Running the Server

1. To start the server, run:

   ```bash
   uvicorn main:app --reload
   ```

2. The server will be available at `http://localhost:8000`.

## Endpoints

- **REST Healthcheck**: `GET /health`
  - Example: `curl http://localhost:8000/health`
  
- **GraphQL Healthcheck**: `POST /graphql`
  - Example: 

    ```bash
    curl -X POST http://localhost:8000/graphql -H "Content-Type: application/json" -d '{"query": "{ health }"}'
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
