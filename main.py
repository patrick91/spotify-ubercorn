import typer
import uvicorn
from dotenv import load_dotenv
from starlette.applications import Starlette
from strawberry.asgi import GraphQL

from app.network import get_local_ip
from app.schema import schema

load_dotenv()


def main() -> None:
    ip = get_local_ip()

    app = Starlette()

    graphql_app = GraphQL(schema)

    app.add_route("/graphql", graphql_app)
    app.add_websocket_route("/graphql", graphql_app)

    typer.echo(f"App running on http://{ip}:8000/graphql")

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")


if __name__ == "__main__":
    typer.run(main)
