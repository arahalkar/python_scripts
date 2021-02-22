from pytube import YouTube
import os

urls_file = "C:\\Users\\araha\\Documents\\Python Scripts\\video_urls_file.txt"
urls_list =[]
file1 = open(urls_file, mode='r')

while True:
    line1 = file1.readline()
    urls_list.append(line1)
    if not line1:
        break 

for i in urls_list:
    #check whether it is a comment, or any other text without a URL in it 
    url = i.rsplit('https://')
    #proceed only if the line contains a URL that starts with HTTPS
    if(len(url)>1): 
        try:
            #prepend the https:// back to the split URL to make it fully valid
            url = ('https://').join(url)
            print(url)
            video=YouTube(url)
            video.streams.get_by_itag(18).download()
        except:
            print("connection error")