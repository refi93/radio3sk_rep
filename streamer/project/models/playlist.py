from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    Boolean,
    Table,
    ForeignKey,
    Enum,
    Float,
    DateTime,
    )
 
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )
 
from sqlalchemy.ext.hybrid import (
    Comparator,
    hybrid_property,
    )
 
from sqlalchemy.orm import (
    validates,
    relationship,
    scoped_session,
    sessionmaker,
    )
 
from bcrypt import (hashpw, gensalt)

from . import Base

class Playlist(Base):
    """Database table Playlist - contains song.
 
    Attributes:
        id: Identificator of object
        song_id: id of played song
        play_time: the time the song was played
    """
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True)
    song_id = Column(Integer, ForeignKey('song.id'), index=True)
    song=relationship('Song', backref="playlists")
    play_time = Column(DateTime)
    queued = Column(Boolean)

    def __init__(self, song, play_time, queued):
        """Initialization of class.
        """
        self.song = song
        self.play_time = play_time
        self.queued = queued
 
    def __repr__(self):
        """
        Returns representative object of class User.
        """
        return "Song<{id}>".format(id=self.id)
    
    def __json__(self, request):
        return {'song_name': self.song.name, 'interpret': self.song.interpret, 'song': self.song}
