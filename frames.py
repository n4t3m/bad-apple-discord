import cv2
import os
import glob

#I copied like 80% of this from somewhere but changed it a bit for the sake of organization

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(f"./frames/image" + str(count).zfill(6) + ".jpg", image)     # save frame as JPG file
    return hasFrames


if not os.path.exists('frames'):
    try:
        os.makedirs('frames')
    except:
        print("Write Permissions for the Current Directory are Needed")


files = glob.glob('frames/*')
for f in files:
    try:
        os.remove(f)
    except:
        continue

vidcap = cv2.VideoCapture('badapple.mkv')


sec = 0
frameRate = 1/3
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)