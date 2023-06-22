import cv2

image = cv2.imread("image5.jpg")
text = "HELLO"
x=200
y=150
text_image = cv2.putText(image,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.9,[255,255,255],2)
text_box_image = cv2.rectangle(text_image,(200,70),(450,310),[0,0,255],2)
while True:
    cv2.imshow("This is my Image",text_box_image)
    if cv2.waitKey(1) == ord("q"):
        break
