from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

# REST healthcheck
@app.get("/health")
async def healthcheck():
    return {"status": "ok"}

# GraphQL schema and healthcheck
@strawberry.type
class Query:
    @strawberry.field
    def health(self) -> str:
        return "ok"

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

# Mount the GraphQL endpoint
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
