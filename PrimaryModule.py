from MotorModule import Motoare
from LaneDetectionModule import ObtinereValoreCurba
import CameraModule
import cv2
import time

##################################################
Motoare = Motoare(2,3,4,17,27,22)
##################################################

def main():

    img = CameraModule.ObtinereImagine()
    curba= ObtinereValoreCurba(img)

    ValoareMaxima= 30 # intervalul stabilit

    if curba>ValoareMaxima:curba = ValoareMaxima
    if curba<-ValoareMaxima: curba =-ValoareMaxima

    #dreapta
    if curba>0:
        sensibilitate = 2
        if curba< 4: curba=0
    #stanga
    else:
        sensibilitate = 3
        if curba>-4: curba=0


    Motoare.start(60, curba*sensibilitate, 0.01)
    cv2.waitKey(1)

if __name__ == '__main__':
    while True:
        main()