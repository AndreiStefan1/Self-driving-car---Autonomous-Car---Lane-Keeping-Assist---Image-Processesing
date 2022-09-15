import cv2
import numpy as np

def albnegru(img):
    imagineHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    limite_albe_inferior = np.array([30,0,0])
    limite_alb_superior = np.array([179,160,255])
    ImagineAlbNegru = cv2.inRange(imagineHSV,limite_albe_inferior,limite_alb_superior)
    #cv2.imshow('albnegru' , ImagineAlbNegru)
    return ImagineAlbNegru

def ImaginePerspectivaNoua(img,puncte,w,h,inv = False):
    puncte1 = np.float32(puncte)
    puncte2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matricetransformare = cv2.getPerspectiveTransform(puncte2, puncte1)
    else:
        matricetransformare = cv2.getPerspectiveTransform(puncte1,puncte2)
    imaginetransformata = cv2.warpPerspective(img,matricetransformare,(w,h))
    return imaginetransformata

def ObtinereValoreaMedieCurba(img,ProcentajMinim=0.1,regiune=1):

    if regiune ==1:
        SumaPixeliColoane = np.sum(img, axis=0)
    else:
        SumaPixeliColoane = np.sum(img[img.shape[0]//regiune:,:], axis=0)

    ValoreaMaxima = np.max(SumaPixeliColoane)
    ValoreaMinima = ProcentajMinim*ValoreaMaxima

    PozitieColoane = np.where(SumaPixeliColoane >= ValoreaMinima)
    ValoareMedieCurba = int(np.average(PozitieColoane))

    return ValoareMedieCurba