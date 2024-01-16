import cv2 as cv
import mediapipe as mp
import math
from PIL import Image 
import sys
mp_drawing = mp.solutions.drawing_utils
mp_pose=mp.solutions.pose
pose=mp_pose.Pose(min_detection_confidence=0.8,min_tracking_confidence=0.9)
path='./assets/mum1.jpg'
try:
    im=Image.open(path)
    dpi=im.info['dpi']
except:
    print("Couldnt find DPI from original img")
    dpi=[72,72]

print('DPI=',dpi[0],"\n\n")

cv.startWindowThread()

#cap=cv.VideoCapture(0)

cap=cv.imread(path)

pop=0
po=0

#while True:
if cap is not None:
#    ret, frame=cap.read()
    frame=cap
    frame=cv.resize(frame,(500,750))
    
    frame_rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    
    result=pose.process(frame_rgb)
    #print(result.pose_landmarks)
    
    if result.pose_landmarks:
        landmark_23 = result.pose_landmarks.landmark[23]
        landmark_24 = result.pose_landmarks.landmark[24]
        landmark_12 = result.pose_landmarks.landmark[12]
        landmark_11 = result.pose_landmarks.landmark[11]
        landmark_26 = result.pose_landmarks.landmark[26]
        landmark_25 = result.pose_landmarks.landmark[25]
        landmark_31 = result.pose_landmarks.landmark[31]
        landmark_0 = result.pose_landmarks.landmark[0]
        
        # mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv.circle(frame, (int(landmark_23.x * frame.shape[1]), int(landmark_23.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.circle(frame, (int(landmark_24.x * frame.shape[1]), int(landmark_24.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.circle(frame, (int(landmark_12.x * frame.shape[1]), int(landmark_12.y * frame.shape[0])), 5, (0, 0, 255), -1)
        cv.circle(frame, (int(landmark_11.x * frame.shape[1]), int(landmark_11.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.circle(frame, (int(landmark_26.x * frame.shape[1]), int(landmark_26.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.circle(frame, (int(landmark_25.x * frame.shape[1]), int(landmark_25.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.circle(frame, (int(landmark_31.x * frame.shape[1]), int(landmark_31.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.circle(frame, (int(landmark_0.x * frame.shape[1]), int(landmark_0.y * frame.shape[0])), 5, (0, 0, 255), -1)
        
        cv.line(frame, (int(landmark_24.x * frame.shape[1]), int(landmark_24.y * frame.shape[0])),
                 (int(landmark_23.x * frame.shape[1]), int(landmark_23.y * frame.shape[0])), (0, 0, 255), 2)
        
        distance_pixels = math.sqrt((landmark_24.x - landmark_23.x)**2 + (landmark_24.y - landmark_23.y)**2)
        
        
        conv=350/dpi[0]
        fin=distance_pixels*conv
        if landmark_24 is not None and landmark_31 is not None and landmark_0 is not None and 0 < landmark_0.x< 1 and 0 < landmark_0.y< 1: 
            inch=round((fin*100)/2.54)
            print('Dist Pixel',distance_pixels,'\n\n')
            print("final:",fin*100," cm",'\n ',inch,' inch' )
            # cv.rectangle(frame, (50,50), (650,450), (255,255,255), 2)
            cv.putText(frame,str(inch)+' inch',(80,100),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

        po+=1        
    else:
        if pop%50==0:    
            print("SORRY , Detection failed. Try a different image.")
            sys.exit()
        pop+=1
        
        
        

    cv.imshow('frame',frame)
    #cap.release()
    if cv.waitKey(0) & 0xFF == ord('q'):
        cv.destroyAllWindows()
    
    
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break
    
#cap.release()
cv.destroyAllWindows()
    
    
    