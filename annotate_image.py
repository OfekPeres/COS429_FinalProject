from posixpath import join
import cv2
import os
import json

keypointLabels = ["Center", "Right Ankle", "Right Knee", "Right Hip", "Left Hip", "Left Knee", "Left Ankle", "Pelvis", "Thorax",
                  "Upper Neck", "Head Top", "Right Wrist", "Right Elbow", "Right Shoulder", "Left Shoulder", "Left Elbow", "Left Wrist"]
keypoints = []
jointIndex = 0
isImageDone = False

output = {}
output['index'] = [0]
output['imgname'] = ["atlas_001.jpg"]
output['normalize'] = [100]
output['person'] = [0]
output['scale'] = [0]
output['torsoangle'] = [0]
output['visible'] = [[1 for x in range(16)]]
output["part"] = []
output["center"] = []
output["scale"] = []



"""
Right Ankle
Right Knee
Right Hip
Left Hip
Left Knee
Left Ankle
Pelvis
Thorax
Upper Neck
Head Top
Right Wrist
Right Elbow
Right Shoulder
Left Shoulder
Left Elbow
Left Wrist
"""
# function to display the coordinates of
# of the points clicked on the image

def click_event(event, x, y, flags, params):
    global jointIndex, keypoints,img, isImageDone
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"jointIndex: {jointIndex}")
        if jointIndex < len(keypointLabels):
            keypoints.append([x,y])
            print(keypointLabels[jointIndex])
            jointIndex += 1
        else:
            print("All Joints Labeled!")
            isImageDone = True
        # print(f"Len of Keypoints: {len(keypoints)}")

# driver function
if __name__ == "__main__":

    # reading the image

    path2im = os.path.join('data', 'MPII', 'images', "atlas_001.jpg")
    img = cv2.imread(path2im)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)        
    print(keypointLabels[jointIndex])
    print(len(keypointLabels[1:]))
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.waitKey(0)
    output["center"].append(keypoints[0])
    output["part"].append(keypoints[1:])
    output["scale"].append(abs(keypoints[10][1] - keypoints[1][1])/200)
    cv2.destroyAllWindows()
    print(output)
    with open("test_annotations.json", "w") as f:
        f.write(json.dumps(output, indent=4))
