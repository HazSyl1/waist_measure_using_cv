# Measuring Waist using CV

## Intro

#### This repo , contains few approaches to measure the body dimensions of the human body using just computer vision. 
#### Approach 1 : Involves , HOG object detection for detetion of human body. This methos was dropped due to very poor acuracy and mesurements. Apart from this , the detection was very fragile , and calculating the distance between pixels to get the waist size , is very complex.
#### Approach 2: Involes Mediapipe , and specifically the POSE library for detection human body . This involves detecting various vector features of the human body in order to study them. The 0th tag aka the vector representing the nose and 31th represening the right foot are considered , to figure if the object is in the correct place. Then , the vectors representing the waist area are detected , and the distance between is calculated . This distance is in pixels hence in order to convert them to cm and then to inches , we use the PPI or DPP . And then we get the final wiast size , approximation.

#### Make sure to change the path , in the file to the directry of your imgae .

## Running

```bash
python MP.py
```