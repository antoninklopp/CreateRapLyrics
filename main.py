from model import main
from create_lyrics import create
import sys

MAX_SYLLABLES = 10

def create_song(artist):
    # create the lyrics
    create(artist)

    # train the model
    main(5, True, artist, MAX_SYLLABLES)

    # write the lyrics
    main(5, False, artist, MAX_SYLLABLES)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use : python main.py artist")
        exit()

    create_song(sys.argv[1])
    
