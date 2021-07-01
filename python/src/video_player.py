"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random
import re


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._curr_video_id='NULL'
        self._curr_state='NULL'
        self._video_playlist={}
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        d={}
        for x in range(len(self._video_library.get_all_videos())):
            d[self._video_library.get_all_videos()[x].title]=self._video_library.get_all_videos()[x].video_id
        
        sorted_d = sorted(d.items())
        for (key,value) in sorted_d:    
            print(self._video_library.get_video(value).title+' ('+self._video_library.get_video(value).video_id+') '+self._video_library.get_video(value).tags)

    # def setCurrVideoId(self,video_id):
    #     self._curr_video_id = video_id
    
    # def setCurrState(self,state):
    #     self._curr_state=state
    
    # def getCurrState(self):
    #     return self._curr_state
    
    # def getCurrVideoId(self):
    #     return self._curr_video_id
    
    def play_video(self, video_id):
        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        if not self._video_library.get_video(video_id):
            print('Cannot play video: Video does not exist')
            
        elif self._curr_video_id=='NULL':
            print('Playing video:',self._video_library.get_video(video_id).title)
            self._curr_video_id=video_id
            self._curr_state='playing'
                
        elif video_id == self._curr_video_id or video_id != self._curr_video_id:
            print('Stopping video:', self._video_library.get_video(self._curr_video_id).title)
            print('Playing video:', self._video_library.get_video(video_id).title)
            self._curr_video_id=video_id
            self._curr_state='playing'
#        print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if not self._video_library.get_video(self._curr_video_id):
            print('Cannot stop video: No video is currently playing')
        
        else:
            print('Stopping video:',self._video_library.get_video(self._curr_video_id).title)
            self._curr_video_id='NULL'
            self._curr_state='NULL'
        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        
#        if not self._video_library.get_video(self._curr_video_id):
#            print('No videos available')
        
        if self._curr_video_id=='NULL':
            self._curr_video_id=self._video_library.get_all_videos()[3].video_id
            self._curr_state='playing'
            print('Playing video:',self._video_library.get_video(self._curr_video_id).title)
        
        else:
            play_number=random.randint(0,len(self._video_library.get_all_videos())-1)
            print('Stopping video:',self._video_library.get_video(self._curr_video_id).title)
            print('Playing video:',self._video_library.get_all_videos()[play_number].title)
            self._curr_video_id=self._video_library.get_all_videos()[play_number].video_id
            self._curr_state='playing'
        #print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if not self._video_library.get_video(self._curr_video_id):
            print('Cannot pause video: No video is currently playing')
        
        elif self._curr_state=='paused':
            print('Video already paused:',self._video_library.get_video(self._curr_video_id).title)
        
        else:
            print('Pausing video:',self._video_library.get_video(self._curr_video_id).title)
            self._curr_state='paused'
        
        #print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        if not self._video_library.get_video(self._curr_video_id):
            print('Cannot continue video: No video is currently playing')
        
        elif self._curr_state!='paused':
            print('Cannot continue video: Video is not paused')
        
        elif self._curr_state=='paused':
            print('Continuing video:',self._video_library.get_video(self._curr_video_id).title)
            self._curr_state='playing'
        
        #print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        
        if not self._video_library.get_video(self._curr_video_id):
            print('No video is currently playing')
        
        elif self._curr_state=='paused':
            print('Currently playing:',self._video_library.get_video(self._curr_video_id).title+' ('+self._video_library.get_video(self._curr_video_id).video_id+') '+self._video_library.get_video(self._curr_video_id).tags+' - PAUSED')
        
        elif self._curr_state=='playing':
            print('Currently playing:',self._video_library.get_video(self._curr_video_id).title+' ('+self._video_library.get_video(self._curr_video_id).video_id+') '+self._video_library.get_video(self._curr_video_id).tags)

               
#        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_upper=str.upper(playlist_name)
        if playlist_name_upper in self._video_playlist:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            self._video_playlist[str.upper(playlist_name)]=Playlist(playlist_name)
            print(f'Successfully created new playlist: {self._video_playlist[str.upper(playlist_name)].list_title()}')
       # print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_name_upper=str.upper(playlist_name)
        
        if playlist_name_upper not in self._video_playlist:
            print(f'Cannot add video to {playlist_name}: Playlist does not exist')
        
        elif playlist_name_upper  in self._video_playlist and not self._video_library.get_video(video_id):
            print(f'Cannot add video to {playlist_name}: Video does not exist')       
        
        elif playlist_name_upper  in self._video_playlist and video_id in self._video_playlist[playlist_name_upper].list_videos():
            print(f'Cannot add video to {playlist_name}: Video already added')
        
        else:
            video_list=self._video_playlist[playlist_name_upper].list_videos()
            video_list.append(video_id)
            video_list_name=self._video_playlist[playlist_name_upper].list_title()            
            self._video_playlist[playlist_name_upper]=Playlist(video_list_name,video_list)
            print(f'Added video to {playlist_name}: {self._video_library.get_video(video_id).title}')
       
        #print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        if not self._video_playlist:
            print('No playlists exist yet')
        else:
            print('Showing all playlists:')
            sorted_d = sorted(self._video_playlist.items())
            for (keys,value) in sorted_d:
                print(self._video_playlist[str.upper(keys)].list_title())
        
    #print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_upper=str.upper(playlist_name)
        if playlist_name_upper  not in self._video_playlist:
            print(f'Cannot show playlist {playlist_name}: Playlist does not exist') 
        
        else:
            print(f'Showing playlist: {playlist_name}')
            if not self._video_playlist[playlist_name_upper].list_videos():
                print('No videos here yet')
            else:
                for v_id in self._video_playlist[playlist_name_upper].list_videos():
                    print(self._video_library.get_video(v_id).title+' ('+self._video_library.get_video(v_id).video_id+') '+self._video_library.get_video(v_id).tags)
        
#        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_name_upper=str.upper(playlist_name)
        
        if playlist_name_upper not in self._video_playlist:
            print(f'Cannot remove video from {playlist_name}: Playlist does not exist')
        
        elif playlist_name_upper  in self._video_playlist and not self._video_library.get_video(video_id):
            print(f'Cannot remove video from {playlist_name}: Video does not exist')       

        elif playlist_name_upper  in self._video_playlist and self._video_library.get_video(video_id) and video_id not in self._video_playlist[playlist_name_upper].list_videos():
            print(f'Cannot remove video from {playlist_name}: Video is not in playlist')                
        else:
            video_list=self._video_playlist[playlist_name_upper].list_videos()
            video_list.remove(video_id)
            video_list_name=self._video_playlist[playlist_name_upper].list_title()
            self._video_playlist[playlist_name_upper]=Playlist(video_list_name,video_list)
            print(f'Removed video from {playlist_name}: {self._video_library.get_video(video_id).title}')
        
        #print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_upper=str.upper(playlist_name)
        
        if playlist_name_upper not in self._video_playlist:
            print(f'Cannot clear playlist {playlist_name}: Playlist does not exist')
        else:
            video_list_name=self._video_playlist[playlist_name_upper].list_title()        
            self._video_playlist[playlist_name_upper]=Playlist(video_list_name) 
            print(f'Successfully removed all videos from {playlist_name}')
        #print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_name_upper=str.upper(playlist_name)
        
        if playlist_name_upper not in self._video_playlist:
            print(f'Cannot delete playlist {playlist_name}: Playlist does not exist')
        else:
            self._video_playlist.pop(playlist_name_upper,None)
            print(f'Deleted playlist: {playlist_name}')
        #print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        d={}
        for x in range(len(self._video_library.get_all_videos())):
            d[self._video_library.get_all_videos()[x].title]=self._video_library.get_all_videos()[x].video_id
        
        sorted_d = sorted(d.items())
        search_list=[]
        for (key,value) in sorted_d:    
            if re.search(str.upper(search_term),str.upper(key)):
                search_list.append((key,value))
                
        if search_list:
            c=1
            print(f'Here are the results for {search_term}:')
            for (key,value) in search_list:
                print(f"{c}) {self._video_library.get_video(value).title} ({self._video_library.get_video(value).video_id}) {self._video_library.get_video(value).tags}")
                c+=1
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")
            play_search_1=input()
            
            if play_search_1.isdigit():
                play_search=int(play_search_1)
                if play_search >0 and (play_search) <= len(search_list):
                    self._curr_video_id=search_list[play_search-1][1]
                    self._curr_state='playing'       
                    print('Playing video:',search_list[play_search-1][0])
        else:
            print('No search results for',search_term)
        
        
        #print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        d={}
        for x in range(len(self._video_library.get_all_videos())):
            d[self._video_library.get_all_videos()[x].tags]=self._video_library.get_all_videos()[x].video_id
        
        sorted_d = sorted(d.items())
        search_list=[]
        for (key,value) in sorted_d:    
            if str.upper(video_tag) in str.upper(key) and video_tag[0]=='#':
                search_list.append(key,value)
        print(search_list)        
        if search_list:
            c=1
            print(f'Here are the results for {video_tag}:')
            for ([key],value) in video_tag:
                print(f"{c}) {self._video_library.get_video(value).title} ({self._video_library.get_video(value).video_id}) {self._video_library.get_video(value).tags}")
                c+=1
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")
            play_search_1=input()
            
            if play_search_1.isdigit():
                play_search=int(play_search_1)
                if play_search >0 and (play_search) <= len(search_list):
                    self._curr_video_id=search_list[play_search-1][1]
                    self._curr_state='playing'       
                    print('Playing video:',search_list[play_search-1][0])
        else:
            print('No search results for',video_tag)
        
        
        
       
        
       
        #print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
