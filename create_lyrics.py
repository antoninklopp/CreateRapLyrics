import lyricsgenius as genius
import os

def create(artist):
    """
    Create a file with all the lyrics from one artist. 
    Downloaded from rap genius 
    """

    # Get token from rap Genius
    client_access_token = os.environ.get("GENIUS_TOKEN", None)
    assert client_access_token is not None, "Must declare environment variable: GENIUS_TOKEN"
    api = genius.Genius(client_access_token)

    artistGenius = api.search_artist(artist)

    with open("lyrics_" + artist + ".txt", 'w') as f:
        for song in artistGenius.songs:
            for line in song.lyrics.split("\n"):
                if len(line) > 1 and line[0] != "[":
                    line = line.replace(".", "")
                    line = line.replace(":", "")
                    line = line.replace(",", "")
                    line = line.replace(";", "")
                    f.write(line + "\n")
            f.write("\n")