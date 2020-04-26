import strawberry

from .screen import display_remote_image


@strawberry.type
class Query:
    a: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def display_image_from_url(self, info, url: str) -> str:
        display_remote_image(url)

        return "ok"


schema = strawberry.Schema(Query, Mutation)
