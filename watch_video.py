import pafy
import cv2
import pytube
import os
url = 'https://www.youtube.com/watch?v=tF4DML7FIWk'
url = 'https://www.youtube.com/watch?v=fn3KWM1kuAw'
# vPafy = pafy.new(url)
# print(vPafy)
# play = vPafy.getbest()

# yt = pytube.YouTube(url)
# yt.streams.get_highest_resolution().download("atlas_video_2.mp4")
#start the video
path2vid = os.path.join(os.curdir, 'atlas.mp4')
print(path2vid)
cap = cv2.VideoCapture(path2vid)
print(cap)
image_number = 52
while (True):
    print(image_number)
    ret,frame = cap.read()
    for i in range(30):
        ret,frame = cap.read()
    """
    your code here
    """
    cv2.imshow('frame',frame)
    cv2.imwrite(f"./atlas_images/atlas_{image_number:04d}.jpg", frame)
    image_number += 1
    if cv2.waitKey(0) & 0xFF == ord('q'):
        continue
    if cv2.waitKey(0) & 0xFF == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()