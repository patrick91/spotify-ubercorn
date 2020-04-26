import time

import typer
from dotenv import load_dotenv

from app.network import get_local_ip
from app.screen import display_remote_image
from app.spotify import authorize, get_last_song, get_spotify_client

load_dotenv()


def main() -> None:
    ip = get_local_ip()

    spotify = get_spotify_client(hostname=ip)
    authorize(spotify)

    while True:
        last_song = get_last_song(spotify)

        if last_song:
            smallest_album_image = last_song["album"]["images"][-1]
            display_remote_image(smallest_album_image['url'])

        time.sleep(1)


if __name__ == "__main__":
    typer.run(main)
