import glob
import cv2
import json
from os.path import basename

# 1: Read in all images from directory to annotate
path2images = glob.glob("./atlas_images/atlas_????.jpg")

path2images.sort()
# 2: annotate each image, include occlusion count
# Define output structure

keypointLabels = ["Center", "Right Ankle", "Right Knee", "Right Hip", "Left Hip", "Left Knee", "Left Ankle", "Pelvis", "Thorax",
                  "Upper Neck", "Head Top", "Right Wrist", "Right Elbow", "Right Shoulder", "Left Shoulder", "Left Elbow", "Left Wrist"]
keypoints = []
visible = []
jointIndex = 0
isImageDone = False

output = {}
output['index'] = []
output['imgname'] = []
output['normalize'] = []
output['person'] = []
output['scale'] = []
output['torsoangle'] = []
output['visible'] = []
output["part"] = []
output["center"] = []
output["scale"] = []



def click_event(event, x, y, flags, params):
    global jointIndex, keypoints, img, isImageDone
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        if jointIndex < len(keypointLabels):
            keypoints.append([x,y])
            visible.append(1)
            jointIndex += 1
        else:
            print("All Joints Labeled!")
            isImageDone = True
        if (jointIndex < len(keypointLabels)):
            print(f"jointIndex: {jointIndex}")
            print(keypointLabels[jointIndex])
    elif event == cv2.EVENT_RBUTTONDOWN:
        if jointIndex < len(keypointLabels):
            keypoints.append([x,y])
            visible.append(0)
            jointIndex += 1
        else:
            print("All Joints Labeled!")
            isImageDone = True
        if (jointIndex < len(keypointLabels)):
            print(f"jointIndex: {jointIndex}")
            print(keypointLabels[jointIndex])


if __name__ == "__main__":
    read_in_data = True
    if read_in_data:
        with open("test_annotations.json") as f:
            output = json.load(f)
    for index, imgpath in enumerate(path2images):
        if basename(imgpath) in output['imgname']:
            print("Image Already annotated")
            continue
        img = cv2.imread(imgpath)
        cv2.imshow('Image', img)
        cv2.setMouseCallback('Image', click_event) 
        print(f"jointIndex: {jointIndex}")   
        print(keypointLabels[jointIndex]) # Print out center
        # setting mouse handler for the image
        # and calling the click_event() function
        cv2.waitKey(0)
        # o for toggling occlusion of joint
        output['index'].append(index)
        output['imgname'].append(basename(imgpath))
        output['normalize'].append(100)
        output['person'].append(0)
        output['torsoangle'].append(0)
        output['visible'].append(visible[1:17])
        output["part"].append(keypoints[1:17])
        output["center"].append(keypoints[0])
        output["scale"].append(abs(keypoints[10][1] - keypoints[1][1])/200)
        
        keypoints = []
        visible = []
        jointIndex = 0
        print(f"Current Image Index: {index}")
        with open("test_annotations_2.json", "w") as f:
            f.write(json.dumps(output, indent=4))    
    cv2.destroyAllWindows()