import io
import os

f = io.open("D:\Quiz\Рок vs Попсы\\artist_list.txt", encoding='utf-8')
artists = [x[:-1] for x in f.readlines() if not x.isspace()]
#x.replace("\n","")
artists = artists[:]


j = 0
isnotempty = False
element = None
for j in range(len(artists)):
    path = "D:\Quiz\\artists_photo\\" + artists[j] + ".jpg"
    if os.path.isfile(path):
        continue
    else:
        print(artists[j])