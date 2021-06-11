from pytube import YouTube
import urllib.request
import requests
import time 
x,count=4,0
while(x>=0):
    if(x==4):
        url = input('\nEnter the video url: ')
        my_video = YouTube(url)
        file=urllib.request.urlopen(url)
        print('\n******************************Video Info******************************\n')
        print('Title:',my_video.title,'\n')
        print('Duration:',my_video.length,'s\n')
        print('Channel name:',my_video.author,'\n')
        print('Views:',my_video.views,'\n')
        print('Date of Upload:',my_video.publish_date,'\n')
        print('Rating:',round((my_video.rating),2),'\n')
        print(f'Thumbnail: {my_video.thumbnail_url}\n')
        print('Press 1 to Download the Video')
        print('Press 2 to Download the Video in Audio Format')
        print('Press 3 to Download Thumbnail')
        print('Press 0 to EXIT\n')        
        x=int(input('Please select a option: '))
    elif(x==1):   
        vid=my_video.streams.get_highest_resolution()
        print('\nDownloading Video...')
        start_time=time.time()
        vid.download()
        print('\nVideo Downloading Successful!!!!')
        print('\nTime taken:',round((time.time()-start_time),2),'s')
        count+=1
        print('\nPress 1 to Download the Video')
        print('Press 2 to Download the Video in Audio Format')
        print('Press 3 to Download Thumbnail')
        if (count>0):
            print('Press 4 to Renter the Link')
        print('Press 0 to EXIT\n')        
        x=int(input('\nPlease select a option: '))
    elif(x==2):
        audio=my_video.streams.filter(only_audio=True).first()
        print('\nDownloading Audio...')
	start_time=time.time()
        audio.download()
        print('\nAudio Downloading Successful!!!!')
        print('\nTime Taken:',round((time.time()-start_time),2),'s')
        count+=1
        print('\nPress 1 to Download the Video')
        print('Press 2 to Download the Video in Audio Format')
        print('Press 3 to Download Thumbnail')
        if (count>0):
            print('Press 4 to Renter the Link')
        print('Press 0 to EXIT\n')        
        x=int(input('\nPlease select a option: '))
    elif(x==3):
        print('\nDownloading Thumbnail...')
        start_time=time.time()
        t=my_video.thumbnail_url
        response = requests.get(t)
        file = open("Thumbnail.png", "wb")
        file.write(response.content)
        file.close()
        print('\nThumbnail Download Successful!!!!')
        print('\nTime Taken:',round((time.time()-start_time),2),'s')
        count+=1
        print('\nPress 1 to Download the Video')
        print('Press 2 to Download the Video in Audio Format')
        print('Press 3 to Download Thumbnail')
        if (count>0):
            print('Press 4 to Renter the Link')
        print('Press 0 to EXIT\n')        
        x=int(input('Please select a option: '))
    elif(x==0):
        print('\nThanks for using!!!')
        break  
    else:
        print('\nInvalid Option')
        x=int(input('\nPlease select a valid option: '))

        
