import typing
import strawberry

from .screen import display_remote_image


@strawberry.type
class Query:
    a: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def display_image_from_url(
        self, info, url: str, brightness: typing.Optional[float]
    ) -> str:
        display_remote_image(url, brightness=brightness or 0.3)

        return "ok"


schema = strawberry.Schema(Query, Mutation)
