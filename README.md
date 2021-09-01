# YoutubeVLC
Use youtube-DL to access DRM blocked videos and playlists in VLC

## Requirements
Python

VLC with terminal

Youtube-DL (you can install here: https://github.com/ytdl-org/youtube-dl/releases/tag/2021.06.06)

Youtube-DL module (pip install youtube_dl)

## How to setup

Install all of the requirements.

Go to youtube.com and export a text file of the cookies (can be done through this extension: https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid/related?hl=en).

Rename the text file to cookies.txt and place it in the directory where you installed YoutubeVLC.

Launch the python script and enter PW to set up login information (this needs to be done to access private and age-restricted videos).

After the program closes, you can now enter links to youtube videos and playlists.

## Note about playlists
1] Each video queues after the first one is finished or if the VLC window is closed. 

~~2] Youtube-DL is slow in getting playlists, wouldn't recommend for playlists with >50 videos. ~~THIS HAS BEEN FIXED! ENJOY LONG PLAYLISTS

3] To end playback, you must end the python script before closing the VLC window, or the next video will play.

4] To randomize playlist, add " -r" to the end of the video url. To shuffle playlist, add " -s" to the end of the video url.

## How it works

For single videos: runs a command in powershell to get the video URL from youtube-DL and put it into VLC

For playlists: gets a list of URLs from youtube-DL, puts them into a list, then plays each of them using the same method above.

##Changelog
v1 Initial Script
v2 - Added login system to allow age-restricted videos to play
v3 - Uses extract-flat to make getting playlist urls much quicker
v4 - Added Randomize and Shuffle Playlist
