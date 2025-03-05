from pytube import YouTube

link = input("Enter video link here -> ")

Y_tube = YouTube(link)

print(f' Video Title ==> {Y_tube.title}')
print()
stream = Y_tube.streams.all()
dt = list(stream)
for i in dt:
    print(i)
