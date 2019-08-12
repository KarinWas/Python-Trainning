class Song:
    def __init__(self, name, album, artist, track_number):
        self.name = name
        self.album = album
        self.artist = artist
        self.track_number = track_number

        artist.add_song(self)

class Album:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year

        self.tracks = []

        artist.add_album(self)

        def add_track(self,title,artist=None):
            if artist is None: 
                artist = self.artist
            
            track_number = len(self.tracks)

            song = Song (name, self, artist, track_number)

            self.tracks.append(song)
        


class Artist:
    def __init__(self, name, album, songs):
        self.name = name
        self.album = album
        self.songs = songs

        def add_song(song):
            self.songs.append(song)
        
        def add_album(album):
            self.album.append(album)


#class Playlist:
   # def __init__(self,name, songs)
    #    self.