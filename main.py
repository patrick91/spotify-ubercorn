import typer
from dotenv import load_dotenv

from app.spotify import authorize, get_spotify_client, get_last_song
from app.network import get_local_ip

load_dotenv()


def main() -> None:
    ip = get_local_ip()

    spotify = get_spotify_client(hostname=ip)
    authorize(spotify)

    last_song = get_last_song(spotify)

    if not last_song:
        typer.echo("Go play some music! 🎼🎼")

        return

    smallest_album_image = last_song["album"]["images"][-1]

    print(smallest_album_image)


if __name__ == "__main__":
    typer.run(main)
