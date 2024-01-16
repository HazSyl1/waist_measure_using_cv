import numpy as np
import cv2 as cv


hog=cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


cv.startWindowThread()

cap = cv.VideoCapture(0)
#cap=cv.imread('./assets/360f33dc27c1b92d32c29fbb91e1254b.jpg')

while(True):
# if cap is not None:
    ret,frame=cap.read()
    #frame=cv.resize(cap,(400,400))
    
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    print
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    print(boxes) if boxes.any() else print("No Detection")
        

    for (xA, yA, xB, yB) in boxes:
        cv.rectangle(frame, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
        
    
    
    cv.imshow('frame',frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
        
    #cap.release()
    # if cv.waitKey(0) & 0xFF == ord('q'):
    #     cv.destroyAllWindows()
cap.release()
cv.destroyAllWindows()
cv.waitKey(1)