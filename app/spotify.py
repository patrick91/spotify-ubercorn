import os
import typing
from multiprocessing import Pipe, Process

import uvicorn
from pyfy import ApiError, ClientCreds, Spotify
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


def _code_server(connection):
    async def homepage(request):
        code = request.query_params["code"]

        connection.send(code)
        connection.close()

        return JSONResponse("ok")

    app = Starlette(routes=[Route("/", homepage)])

    uvicorn.run(app, host="0.0.0.0", port=4444, log_level="error")


def wait_for_code():
    parent_conn, child_conn = Pipe()
    p = Process(target=_code_server, args=(child_conn,))
    p.start()

    code = parent_conn.recv()
    p.terminate()

    return code


def get_spotify_client(hostname) -> Spotify:
    client = ClientCreds(
        client_id=os.getenv("SPOTIFY_CLIENT_KEY"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        scopes=["user-read-currently-playing", "user-read-recently-played"],
        redirect_uri=f"http://{hostname}:4444",
    )

    return Spotify(client_creds=client)


def authorize(spotify: Spotify) -> None:
    print(spotify.auth_uri())

    code = wait_for_code()

    spotify.build_user_creds(grant=code, set_user_creds=True)


def get_last_song(spotify: Spotify) -> typing.Optional[typing.Dict]:
    try:
        current_song = spotify.currently_playing()

        if current_song:
            return current_song["item"]
        else:
            last_tracks = spotify.recently_played_tracks(limit=1)["items"]

            return last_tracks[0]["track"] if last_tracks else None

    except ApiError:
        return None
