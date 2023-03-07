import os
import time
import requests


def getAllNewVideoLinks(tiktokId,lastVideoId):
    downloadLink=[]
    videoIds=[]
    url = "https://www.tikwm.com/api/user/posts"
    KeyError = False
    request_data=""
    while not KeyError:
        try:
            url = "https://www.tikwm.com/api/user/posts"

            querystring = {"unique_id":"", "count":"100","cursor":"0","hd":1}
            querystring["unique_id"] = tiktokId

            s = requests.Session()
            gen = s.headers['User-Agent']

            header = {
                "User-Agent": gen
            }
            time.sleep(10)
            request_data = requests.request("GET", url, headers=header, params=querystring).json()
            break
        except:
            pass
    # print(request_data)
    # username = request_data["data"]["videos"][0]['author']["unique_id"]
    # print(request_data)
    videos = request_data["data"]["videos"]
    # print(videos)
    # print(f"""\n{Fore.CYAN}[Programs] {Fore.GREEN}[Status] {Fore.RED}@{username} {Fore.YELLOW}Have Published {Fore.BLUE}{len(videos)} {Fore.YELLOW}Videos. Downloading them...""")
    print(len(videos))
    count = 0
    for video in videos:
        count += 1
        download_url = video["play"]
        uri = video["video_id"]
        if(lastVideoId==uri):
            break
        title = video['title']
        limit = str(f'{title:80.80}')
        downloadLink.append(download_url)
        videoIds.append(uri)
    return downloadLink,videoIds
    pass

def downloadVideo(download_url,uri):
    chunk_size = 1024
    username="videos"
    if not os.path.exists(f"./tiktok/{username}"):
        os.makedirs(f"./tiktok/{username}")
    if not os.path.exists(f"./tiktok/{username}/{uri}.mp4"):

        video_bytes = requests.get(download_url, stream=True)
        total_length = int(video_bytes.headers.get("Content-Length"))
        with open(f'./tiktok/{username}/{uri}.mp4', 'wb') as out_file:
            out_file.write(video_bytes.content)
            time.sleep(0.7)
        return os.path.abspath(f"./tiktok/{username}/{uri}.mp4")
        
    else:
        time.sleep(0.7)
        return os.path.abspath(f"./tiktok/{username}/{uri}.mp4")

if __name__=="__main__":
    downloadLink,videoIds=getAllNewVideoLinks("@animals_funny1988","7205503547755072814")
        
    print(videoIds)
    print(len(videoIds))
    videoPath= downloadVideo(downloadLink[0],videoIds[0])
    print(videoPath)
    pass


