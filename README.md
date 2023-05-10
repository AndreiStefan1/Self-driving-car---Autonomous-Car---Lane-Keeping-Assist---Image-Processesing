# Lane-Assist-System---Autonomous-Car
Implementation of a real Lane Assist system on a project car . The car is using a Raspberry Pi and a dedicated camera to follow any given route . The whole project is based on image processing made possible by using NumPy and OpenCV libraries. 

## Components of the car : 
- Raspberry Pi 4B
- Raspberry camera Pi V1.3
- 5.000 mAh external baterry to power the Raspbery Pi microprocessor 
- L298N DC Motor Driver 
- 4 AAA batteries to power up the engines and L298N DC Motor Driver
- 4x D.C motors ~ 3V-6V 


## The concept 
Image processing is the use of a digital computer to process digital images through an algorithm. In this case we use a microprocessor (Raspberry PI 4) to make the process possible . In order for the process to work , the road must be white (or if any other color is chosed , then the color coordinates should be changed in the HSV color space). The camera should be positioned high and centered. 

The used algorithm is doing the following important steps:

- transforming the RGB live images recieved from the camera in black & white images
- changing the camera's point of view from a three-dimensional one to a two-dimensional one 
- calculating the road's curve based on the live images that are transformed instantly
- transmitting the raod's curve value to the engines wich rotate accordingly 



## Getting started
To make the process easier , a video can be made with any other camera from the car's perspective of any path. This video then can be edited in the code editor , so it won't be necessary to run the car on the path anytime we want to make a change regarding the path's perspective . To test the changes made in the code editor on the test video , simply run the code from the "LaneDetectionModule" . 
Anytime you want to test the full code , run the whole code from the main module .

![image](https://user-images.githubusercontent.com/111795066/190509310-b1800fb2-d640-4fc4-b18c-b3449944d75c.png)

Figure 1. Full Built Concept

## Assembly Process

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/1cba76df-e2d9-487a-a1d3-5507f3828f12)

Figure 2. DC Motors and L298N DC Motor Driver positions

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/7d0b1ba5-a9c0-40d9-b0fc-5177a9607e0a)

Figure 3. Graphical Wiring diagram 

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/80d6e118-61c8-4ced-8924-e2ed3c7638c5)

Figure 4. Wiring diagram 
