# 4. Create a class called Playlist that represents a music playlist. The class should have attributes for the playlist's name and a list to store songs. It should have methods to add a song to the playlist, remove a song from the playlist, and play the next song in the playlist. 

class playlist:
    playlist_name="malayalam duets"
    l=[]
    def add_song(self,b):
        self.l.append(b)
        print(self.l)
    
    def remove_song(self,e):
        if e in self.l:
            self.l.remove(e)
            print(self.l)

obj=playlist()
obj.add_song("song1")
obj.add_song("song2")
obj.add_song("song3")
obj.remove_song("song1")