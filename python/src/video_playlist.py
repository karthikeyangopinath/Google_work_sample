"""A video playlist class."""

from typing import Sequence

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self,playlist_title: str,playlist_videos: Sequence[str]=""):
        self._playlist_title=playlist_title
        self._playlist_videos=list(playlist_videos)
    
    def __str__(self):
        return str(self._playlist_videos)
    
    def list_title(self):
        return self._playlist_title
        
    def list_videos(self):
        return self._playlist_videos
        
