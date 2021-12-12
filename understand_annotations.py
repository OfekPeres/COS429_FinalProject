import h5py
import os
import data.MPII.ref as ds
import cv2
import numpy as np
import json
import matplotlib.pyplot as plt
# val_f = h5py.File(os.path.join(ds.annot_dir, 'valid.h5'), 'r')

with open("test_annotations.json", 'r') as f:
    val_f = json.load(f)
# f = open('predictions.json')
# predictions = json.load(f)
# f.close()

# for k, v in val_f.items():
#     print("----------------------")
#     print(k)
#     print(v[12])
#     print("----------------------")

# im_name = val_f['imgname'][12]
# path2im = os.path.join('data', 'MPII','images', f"{im_name.decode('utf-8')}")
# im = cv2.imread(path2im)
# # print(f"Max Dim Normalized: {(im.shape[0]*im.shape[1])/val_f['normalize'][i]}")
# plt.imshow(im)
# plt.show()
# exit()

# for i in range(20):
#     print(f"Normalization value: {val_f['normalize'][i]}")
#     im_name = val_f['imgname'][i]
#     path2im = os.path.join('data', 'MPII','images', f"{im_name.decode('utf-8')}")
#     im = cv2.imread(path2im)
#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     # print(f"Max Dim Normalized: {(im.shape[0]*im.shape[1])/val_f['normalize'][i]}")
#     cv2.imshow("Image", im)
#     cv2.waitKey()
# exit()
def DrawJoints(image, joints, color):
    for index, j in enumerate(joints):
        j = tuple(np.array(j[:2]).round().astype(int))
        cv2.putText(image, str(index), j, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
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

    # print(f"Index: {index}")
    # print(f"normalize: {normalize}")
    # print(f"part: {part}")
    # print(f"person: {person}")
    # print(f"scale: {scale}")
    # print(f"torsoangle: {torsoangle}")
    # print(f"visible: {visible}")

    # path2im = os.path.join(os.getcwd(), 'data', 'MPII','images', f"{im_name.decode('utf-8')}")
    # path2im = os.path.join('data', 'MPII','images', f"{im_name.decode('utf-8')}")
    path2im = os.path.join('data', 'MPII','images', f"{im_name}")
    im = cv2.imread(path2im)
    # Annotate Image
    cv2.circle(im, tuple(center), radius=5, color=(0, 0, 255), thickness=-1)
    DrawJoints(im, part, (255,0,0))

    # for keypoints in predictions[path2im]:
    #     DrawJoints(im, keypoints['keypoints'], (0,255,0))
    cv2.imshow("Image", im)
    cv2.waitKey()


num_ims = 1
AnnotateImage(66, val_f)
# for i in range(0,num_ims):
    # AnnotateImage(i, val_f)

