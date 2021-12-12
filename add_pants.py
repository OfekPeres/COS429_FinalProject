import json
import cv2
import os
import math
with open("test_annotations.json") as f:
    annotations = json.load(f)

annotations_pants = annotations.copy()
pants_image = cv2.imread(os.path.join(os.curdir, "atlas_images", "pants.jpg"))
for index, imgname in enumerate(annotations['imgname']):
    print(index)
    imgpath = os.path.join(os.curdir, 'atlas_images', imgname)
    atlas_img = cv2.imread(imgpath)
    pelvis = annotations["part"][index][6]
    rankle = annotations["part"][index][0]
    lankle = annotations["part"][index][5]
    
    width = max(10,abs(lankle[0] - rankle[0]))
    height = min(abs(pelvis[1] - rankle[1]), abs(pelvis[1] - lankle[1]))
    pants_image_resized = cv2.resize(pants_image, (width, height))
    # offset_x_l,offset_x_u  = math.floor(width/2), math.ceil(width/2)
    # offset_y_l,offset_y_u  = math.floor(height/2), math.ceil(height/2)
    atlas_image_pants  = atlas_img.copy()
    atlas_image_pants[pelvis[1]:pelvis[1]+height, lankle[0]-width:lankle[0]] = pants_image_resized
    
    cv2.imwrite(f"./atlas_images/{imgname[:-4]}_pants.jpg", atlas_image_pants)
    # cv2.imshow("FACE PANTS!!", atlas_image_pants)
    # cv2.waitKey(0)
    annotations_pants['imgname'][index] = f"{imgname[:-4]}_pants.jpg"

with open("test_annotations_pants.json", "w") as f:
    f.write(json.dumps(annotations_pants, indent=4))    
    