from lib.artist import Artist

"""
When I consttuct an Artists
with an id, name and genre
They are reflected un the instance properties
"""
def test_constucts_with_fields():
    artist = Artist(1, "The Beatles", "Rock")
    assert artist.id == 1
    assert artist.name == "The Beatles"
    assert artist.genre == "Rock"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Artist(1, "The Beatles", "Rock")
    assert str(artist) == "Artist(1, The Beatles, Rock)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""

def test_artists_are_equal():
    artist1 = Artist(1, "The Beatles", "Rock")
    artist2 = Artist(1, "The Beatles", "Rock")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
