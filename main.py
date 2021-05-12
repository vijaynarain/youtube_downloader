#this import youtube module from pytube
from pytube import YouTube
from art import logo
from os import system

system("cls")
print(logo)

#here enter your video url
link = input("Enter your youtube url = ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

#print all format to download
for i in video:
  print(i)

print("Which type of file you want to download")

#user have to select the format to download
user_option = int(input("Enter your option = "))
user_video = videos[user_option]

user_video.download()

print("video download sucessfully")

