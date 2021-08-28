# YoutubeVLC
Use youtube-DL to access DRM blocked videos and playlists in VLC

## Requirements
Python
VLC with terminal
Youtube-DL (you can install here: https://github.com/ytdl-org/youtube-dl/releases/tag/2021.06.06)
Youtube-DL module (pip install youtube_dl)

## Features
You can watch videos with copyrighted material in them.
You can use playlists.
Note about playlists: 1] Each video queues after the first one is finished or if the VLC window is closed. 2] Youtube-DL is slow in getting playlists, wouldn't recommend for playlists with >50 videos. 

## How it works
For single videos: runs a command in powershell to get the video URL from youtube-DL and put it into VLC
For playlists: gets a list of URLs from youtube-DL, puts them into a list, then plays each of them using the same method above.
