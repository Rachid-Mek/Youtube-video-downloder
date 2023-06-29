from pytube import YouTube
from sys import argv

link = argv[1] # Get the link from the command line
yt = YouTube(link) # Create a YouTube object

print("Title: ", yt.title) # Print the title of the video

print(f'number of views is {yt.views}')

yd = yt.streams.get_highest_resolution() 

yd.download('\Users\rachi\Downloads')