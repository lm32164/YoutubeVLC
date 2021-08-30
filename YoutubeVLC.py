import json
import os
import sys

import subprocess
import youtube_dl

def convertPL(oldURL, u, p):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s', 'username': u, 'password': p, 'cookiefile': 'cookies.txt', 'cachedir': False, 'extract_flat': 'in_playlist'})
    urlList = []
    with ydl:
        result = ydl.extract_info(oldURL,download=False)
        video = result['entries']
        for i, item in enumerate(video):
             urlList.append(result['entries'][i]['url'])
    return urlList

def convertSVD(oldURL, u, p):
    return "$(youtube-dl --get-url --no-playlist --cookies=cookies.txt --no-cache-dir --rm-cache-dir -u " + u + " -p " + p + " --format best 'https://www.youtube.com/watch?v=" + oldURL + "')"

def convertVD(oldURL, u, p):
    return "$(youtube-dl --get-url --no-playlist --cookies=cookies.txt --no-cache-dir --rm-cache-dir -u " + u + " -p " + p + " --format best '" + oldURL + "')"
    

print('Enter URL or enter "PW" to see/change youtube login info') #asks for input
urlid = input()
if 'http' in urlid:
    with open('UserPass.json', 'r') as h:
        loginInfo = json.load(h)
        username = loginInfo["username"]
        password = loginInfo["password"]
    if 'list' in urlid:
        if 'watch?v' in urlid:
            print('Enter 1 to play all videos in the playlist. Enter 2 to only play the video linked.')
            playlist = str(input())
            if '1' in playlist:
                playlistURL = convertPL(urlid, username, password)
                for x in playlistURL:
                    subprocess.run(["powershell", "-Command", 'vlc --play-and-exit "' + convertSVD(x, username, password) + '"'], capture_output=True)
                exit
            elif '2' in playlist:
                subprocess.run(["powershell", "-Command", 'vlc "' + convertVD(urlid, username, password) + '"'], capture_output=True)
                exit
            else:
                print('bruh')
                exit
        else:
            playlistURL = convertPL(urlid, username, password)
            for x in playlistURL:
                subprocess.run(["powershell", "-Command", 'vlc --play-and-exit "' + convertSVD(x, username, password) + '"'], capture_output=True)
            exit
    else:
        subprocess.run(["powershell", "-Command", 'vlc "' + convertVD(urlid, username, password) + '"'], capture_output=True)
        exit
elif 'PW' in urlid:
    with open('UserPass.json') as f:
        login_data = json.load(f)
        print("Username is " + login_data["username"])
        print("Password is " + login_data["password"])
        lConf = input('Change Username and Password? Y/N: ')
        if 'N' in lConf:
            exit
        if 'Y' in lConf:
            nUsername = input('Enter Username: ')
            nPassword = input('Enter Password: ')
            login_data['username'] = nUsername
            login_data['password'] = nPassword
            print("New username is " + login_data["username"])
            print("New password is " + login_data["password"])
            f = open('UserPass.json', 'w')
            json.dump(login_data, f)
            f.close()
            exit
else:
    print('bruh')
    exit
