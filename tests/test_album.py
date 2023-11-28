from lib.album import Album
from lib.artist import Artist

"""
Constructs with
if, title, realease_year, and artist_id
"""

def test_construct_with_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2
    
def test_artists_format_nicely():
    artist = Artist(1, "The Beatles", "Rock")
    assert str(artist) == "Artist(1, The Beatles, Rock)"
    
def test_constucts_with_fields():
    artist = Artist(1, "The Beatles", "Rock")
    assert artist.id == 1
    assert artist.name == "The Beatles"
    assert artist.genre == "Rock"

