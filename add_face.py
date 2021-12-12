import json
import cv2
import os
import math
with open("test_annotations.json") as f:
    annotations = json.load(f)

annotations_face = annotations.copy()
face_image = cv2.imread(os.path.join(os.curdir, "atlas_images", "face.jpg"))
for index, imgname in enumerate(annotations['imgname']):
    imgpath = os.path.join(os.curdir, 'atlas_images', imgname)
    atlas_img = cv2.imread(imgpath)
    upper_head = annotations["part"][index][9]
    upper_neck = annotations["part"][index][8]
    height = abs(upper_head[1] - upper_neck[1])
    height = int(height*1.2)
    width = height
    face_image_resized = cv2.resize(face_image, (width, height))
    offset_x_l,offset_x_u  = math.floor(width/2), math.ceil(width/2)
    offset_y_l,offset_y_u  = math.floor(height/2), math.ceil(height/2)
    atlas_image_face  = atlas_img.copy()
    atlas_image_face[upper_neck[1]-offset_y_l:upper_neck[1]+offset_y_u, upper_neck[0]-offset_x_l: upper_neck[0]+offset_x_u] = face_image_resized
    
    cv2.imwrite(f"./atlas_images/{imgname[:-4]}_face.jpg", atlas_image_face)
    
    annotations_face['imgname'][index] = f"{imgname[:-4]}_face.jpg"

with open("test_annotations_face.json", "w") as f:
    f.write(json.dumps(annotations_face, indent=4))    
    