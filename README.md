# Description:

The package is an idea came out after realizing a decent project which was based on pytube Package and tkinter and the object-oriented programming, and which was about downloading music, videos, playlists of music and playlists of videos .

I used pytube to code this project and provide a module which can help anyone just by one line of code download whatever he wants from Youtube.
I coded this using a different approach, and I hope that you find it inspiring as I found it.

## Features:

* Download videos from with the maximum resolution up to 720p directly by just providing the link , and the path of your choice for saving the video.
* Download audios directly by just providing the link , and the path of your choice for saving the audio.
* Download Playlists of audios or videos by providing  the  **link of the whole playlist** and also the path of your desire.

# Installation:
````shell
pip install tubeConverter
````
# Instructions on how to use :
### For downloading videos:
Specify the link of the video and the path of destination of your desire :
````python
from tubeConverter import *

video=Video("https://youtu.be/S_3z2diEJl8","C://Users//Minfo//OneDrive//Documents//My Recordings")
video.download_file()
````

### For downloading audios:
Specify the link of the video from YouTube you aim to convert to a mp3 file and the path of destination of your desire :
````python
from tubeConverter import *

audio=Video("https://youtu.be/S_3z2diEJl8","C://Users//Minfo//OneDrive//Documents//My Recordings")
audio.download_file()
````
### For downloading Playlists of videos:
Specify the link of the whole playlist from YouTube and the path of destination of your desire for your files:

_*Important*_ : Links of playlists in YouTube have /playlist? included in the url , make sure to use correct links 
````python
from tubeConverter import *

playlist_video=PlaylistVideo("https://youtube.com/playlist?list=PLZgKgfug7rBseIzNn1tXnzPnfAbSQcmsK","C://Users//Minfo//OneDrive//Documents//My Recordings")
playlist_video.download_playlist()

````

### For downloading Playlists of audios:
Specify the link of the whole playlist of videos converted to mp3 files from YouTube and the path of destination of your desire for your files:
```python
from tubeConverter import *

playlist_audio=PlaylistAudio("https://youtube.com/playlist?list=PLZgKgfug7rBseIzNn1tXnzPnfAbSQcmsK","C://Users//Minfo//OneDrive//Documents//My Recordings")
playlist_audio.download_playlist()

```

## At the end :
### Enjoy downloading videos and music 
#### The package is always under improvement , Let's grow together !!
