import json
import os
import sys

import subprocess
import youtube_dl

def conURL(input, u, p, r, s, pl):
    ydlOpt = {'outtmpl': '%(id)s.%(ext)s', 'username': u, 'password': p, 'cookiefile': 'cookies.txt', 'cachedir': False, 'extract_flat': 'in_playlist'}
    if r is True:
        ydlOpt['playlistreverse'] = True
    if s is True:
        ydlOpt['playlistrandom'] = True
    if pl is False:
        ydlOpt['noplaylist'] = True
    ydl = youtube_dl.YoutubeDL(ydlOpt)
    urlList = []
    with ydl:
        result = ydl.extract_info(input,download=False)
    return result

def conVLC(input, u, p):
    return "$(youtube-dl --get-url --no-playlist --cookies=cookies.txt --no-cache-dir --rm-cache-dir -u " + u + " -p " + p + " --format best 'https://www.youtube.com/watch?v=" + input + "')"

reverse = False
shuffle = False
playlist = True
print('Enter URL and options or enter "PW" to edit username and password')
firstInput = input()
if "http" in firstInput:
    if " -r" in firstInput:
        reverse = True
    if " -s" in firstInput:
        shuffle = True
    if " -p" in firstInput:
        playlist = False
    urlid = firstInput.split()[0]
    with open('UserPass.json', 'r') as h:
        loginInfo = json.load(h)
        username = loginInfo["username"]
        password = loginInfo["password"]
    videoDetails = conURL(urlid, username, password, reverse, shuffle, playlist)
    urlList = []
    urlTitle = []
    if 'entries' in videoDetails:
        for i in range(len(videoDetails['entries']) - 1):
            urlList.append(videoDetails['entries'][i]['url'])
            urlTitle.append(videoDetails['entries'][i]['title'])
    else:
        urlList.append(videoDetails['id'])
        urlTitle.append(videoDetails['title'])
    if len(urlList) == 1:
        print('Playing: "' + urlTitle[0] + '"')
        subprocess.run(["powershell", "-Command", 'vlc --play-and-exit "' + conVLC(urlList[0], username, password) + '"'], capture_output=True)
    else:
        for i in range(len(urlList) - 1):
            print('Playing: "' + urlTitle[i] + '"')
            subprocess.run(["powershell", "-Command", 'vlc --play-and-exit "' + conVLC(urlList[i], username, password) + '"'], capture_output=True)
    exit
elif "PW" in firstInput:
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
