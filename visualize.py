import os
import cv2
import numpy as np
import json
import matplotlib.pyplot as plt


index2joint = ["RA", "RK", "RH", "LH", "LK", "LA", "P", "T","UN", "HT", "RW", "RE", "RS", "LS", "LE", "LW"]
def DrawJoints(image, joints, color):
    for index, j in enumerate(joints):
        j = tuple(np.array(j[:2]).round().astype(int))
        cv2.putText(image, index2joint[index], j, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv2.LINE_AA)
    return image

def AnnotateImage(image_index, annotations):
    """ Possible Annotations
    index
    normalize
    part
    person
    scale
    torsoangle
    visible
    """
    # Extract Annotions for the given image
    center = np.array(annotations['center'][image_index]).round().astype(int)
    im_name = annotations['imgname'][image_index]
    index = annotations['index'][image_index]
    normalize = annotations['normalize'][image_index]
    part = annotations['part'][image_index]
    person = annotations['person'][image_index]
    scale = annotations['scale'][image_index]
    torsoangle = annotations['torsoangle'][image_index]
    visible = annotations['visible'][image_index]

    path2im = os.path.join('data', 'MPII','images', f"{im_name}")
    im = cv2.imread(path2im)
    # Annotate Image
    cv2.circle(im, tuple(center), radius=5, color=(0, 0, 255), thickness=-1)
    # DrawJoints(im, part, (0,255,255))

    for keypoints in predictions[path2im]:
        DrawJoints(im, keypoints['keypoints'], (0,255,0))
    cv2.imshow("Image", im)
    cv2.waitKey()


if __name__ == "__main__":
    with open("test_annotations_face_pants.json", 'r') as f:
        val_f = json.load(f)
    f = open('predictions_face_pants.json')
    predictions = json.load(f)
    f.close()
    n = len(val_f["imgname"])
    AnnotateImage(13,val_f)
    # for i in range(n):
    #     AnnotateImage(i, val_f)