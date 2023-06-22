import boto3
import requests
import cv2


class aws(object):

   def ObjectDetection(imagePath , Service):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    image = open(imagePath, "rb").read()
    imgH , imgW = cv2.imread(imagePath).shape[:2]
    MyImage = cv2.imread(imagePath)
    response = Service.detect_labels(Image={"Bytes": image})
    for objects in response["Labels"]:
        if objects["Instances"]:
            objectName = objects["Name"]
            for boxs in objects["Instances"]:
                box = boxs["BoundingBox"]
                x = int(imgW * box["Left"])
                y = int(imgH * box["Top"])
                w = int(imgW * box["Width"])
                h = int(imgH * box["Height"])

                MyImage = cv2.rectangle(MyImage, (x,y), (x+w, y+h), (0,255,0), 2 )
                MyImage = cv2.putText(MyImage,objectName,(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.9,[255,255,255],2)
    cv2.imwrite(imagePath, MyImage)

   def CelebDetection(imagePath , Service):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    image = open(imagePath, "rb").read()
    imgH , imgW = cv2.imread(imagePath).shape[:2]
    MyImage = cv2.imread(imagePath)
    response = Service.recognize_celebrities(Image={"Bytes": image})
    print(response)
    for objects in response["CelebrityFaces"]:
        celName = objects["Name"]
        Face = objects["Face"]
        box = Face["BoundingBox"]
        x = int(imgW * box["Left"])
        y = int(imgH * box["Top"])
        w = int(imgW * box["Width"])
        h = int(imgH * box["Height"])

        MyImage = cv2.rectangle(MyImage, (x,y), (x+w, y+h), (0,255,0), 2 )
        MyImage = cv2.putText(MyImage,celName,(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.9,[255,255,255],2)
    cv2.imwrite(imagePath, MyImage)

   def FaceAny(imagePath , Service):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    image = open(imagePath, "rb").read()
    imgH , imgW = cv2.imread(imagePath).shape[:2]
    MyImage = cv2.imread(imagePath)
    response = Service.recognize_celebrities(Image={"Bytes": image})
    print(response)
    for objects in response["FaceDetails"]:
        Face = objects["Face"]
        box = Face["BoundingBox"]
        x = int(imgW * box["Left"])
        y = int(imgH * box["Top"])
        w = int(imgW * box["Width"])
        h = int(imgH * box["Height"])

        MyImage = cv2.rectangle(MyImage, (x,y), (x+w, y+h), (0,255,0), 2 )
        MyImage = cv2.putText(MyImage,(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,0.9,[255,255,255],2)
    cv2.imwrite(imagePath, MyImage)


