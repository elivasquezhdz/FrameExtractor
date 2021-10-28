import cv2
import os

EXTENSION = "MOV"
OUT_FOLDER = "frames"
SAVE_FREQ = 10

files = [x for x in os.listdir(os.getcwd()) if x[-3:]=='MOV']

count = 0
for f in files:
    video = cv2.VideoCapture(f)
    ret, frame = video.read()
    while (ret):
        cv2.imwrite("{}/{}-{}.jpg".format(OUT_FOLDER,f,count),frame)
        ret, frame = video.read()
        count +=1
        if count % SAVE_FREQ == 0:
            print("Writing {} {}".format(f,count))