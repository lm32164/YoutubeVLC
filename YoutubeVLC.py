import subprocess
import youtube_dl

def convertPL(oldURL):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    urlList = []
    with ydl:
        result = ydl.extract_info(oldURL,download=False)
        video = result['entries']

        for i, item in enumerate(video):
            urlList.append(result['entries'][i]['webpage_url'])
    return urlList


def convertVD(oldURL):
    return "$(youtube-dl --get-url --no-playlist --format best '" + oldURL + "')"
    

print('Enter URL') #asks for input
urlid = input()
if 'list' in urlid:
    if 'watch?v' in urlid:
        print('Enter 1 to play all videos in the playlist. Enter 2 to play the first video in the playlist.')
        playlist = str(input())
        if '1' or '1' in playlist:
            playlistURL = convertPL(urlid)
            for x in playlistURL:
                subprocess.run(["powershell", "-Command", 'vlc --playlist-enqueue "' + convertVD(x) + '"'], capture_output=True)
            exit
        elif 'N' or 'n' in playlist:
            subprocess.run(["powershell", "-Command", 'vlc "' + convertVD(urlid) + '"'], capture_output=True)
            exit
        else:
            print('bruh')
            exit
    else:
        playlistURL = convertPL(urlid)
        for x in playlistURL:
            subprocess.run(["powershell", "-Command", 'vlc --playlist-enqueue "' + convertVD(x) + '"'], capture_output=True)
        exit
else:
    subprocess.run(["powershell", "-Command", 'vlc "' + convertVD(urlid) + '"'], capture_output=True)
    exit