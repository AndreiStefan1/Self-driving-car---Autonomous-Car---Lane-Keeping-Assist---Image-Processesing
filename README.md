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

## Image Processing Concept
The prototype that was created is an autonomous robot-car that manages to stay on the track both on straight lines and in curves with the help of real-time image processing. The track is made up of a series of white A4 sheets, therefore we have a track consisting of a single lane. The implementation methodology used for a miniature autonomous car contains four main image processing components.
The method used is the summation of pixels from the frames captured in real-time by the camera. A pixel is a small unit of a digital image that can be displayed on a display device. In a digital image, multiple pixels are combined to form a complete image or video, and an image contains multiple pixels arranged in rows and columns.
The number of rows and columns is expressed as the image resolution. Since a computer only understands numbers, each pixel is represented by three numbers corresponding to the amounts of red, green, and blue (RGB) present in that pixel.

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/0b3331a5-ec4a-4dc6-962e-11fcfebe886d)

Figure 5.Figure 13. Interpreting pixels in terms of values in an RGB color space.

To use the pixel summation method, we use 8-bit frames where each pixel occupies exactly one byte (octet). This means that each pixel has 256 (2^8) possible numeric values, ranging from 0 to 255. Therefore, the color palette for an 8-bit image normally contains 256 possible colors, where 0 represents black and 255 represents white.
The use of 8-bit images is necessary in this case because processing and editing them in real-time is much faster than performing the same operations on a 16 or 24-bit image.

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/1e90236e-2961-43b4-ae57-5987702125c2)

Figure 6. Difference between a 24-bit and an 8-bit image.

The processed images in this case are in black and white (binary) format. The pixels in the image either have a value of 255 (white) or 0 (black), at a resolution of 480 x 240. Therefore, we will use the total white pixels (since our track is white) to determine how much the car needs to turn to stay on the lane. The frames that will be edited in real-time are composed of 240 rows of pixels and 480 columns of pixels.

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/c41b90ce-4ed1-4d17-8faf-1e458938a5d4)

Figure 7. Representation of a black and white track image in terms of pixels and the sum of white pixels per column.

In Figure 6, the interpretation of the track in terms of pixels is shown. We can see that a right curve is illustrated, where white pixels have a value of 255, and black pixels have a value of 0. We can add up the sum of white pixels for each column, resulting in the total number of pixels per column.

The car will know how much to turn based on the curve value, which is calculated using the average of the columns that contain white pixels in each frame. Knowing that a column of pixels has a sum of values greater than 0, it will contribute to our calculation to determine the curve value. If the sum of the column's values is 0, then that column is not considered.

## Code Implementation
1.First step - Converting the images from RGB to HSV to Black and White

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/04496544-fa68-455a-8b65-f9ca78722377)

Figure 8. Original camera frame and resulting frame 

2.Second step - Changing the image peresective from 3D Plan to 2D Plan

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/9a223b39-a4d0-41c7-9f62-657adaa987db)

Figure 9. 3D Plan to 2D plan 

3.Third Step - Change point of view

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/3b3c8923-d448-4acf-9469-5fbc5042a495)

Figure 10.Orginal View Point to Transformed View Point

4.Fourth step - Eliminate image noise

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/35cadfc9-d600-41a1-a1cd-810d947c0ab9)

Figure 11. Eliminate Image Noise

5.Fifth image - Calculate pixels for every frame to have an output

![image](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/2a6b5a2a-c37c-4d37-89e2-112b8578ba72)

Figure 12. Calculating the pixels for every frame (example of a frame for straight  line)

![Curba Dreapta](https://github.com/AndreiStefan1/Self-driving-car---Autonomous-Car---Lane-Keeping-Assist/assets/111795066/8eaebb40-2522-4b11-a398-1c98e105245e)

Figure 13. Calculating the pixels for every frame (example of a frame for turnning right )
