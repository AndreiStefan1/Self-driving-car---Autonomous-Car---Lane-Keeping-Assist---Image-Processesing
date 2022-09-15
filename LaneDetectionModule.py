import cv2
import numpy as np
import EditModule
import time

ListValoriCurba = []
SirValori=10
puncte = np.float32([[160, 90], [340, 90], [100, 215], [395, 215]])

def ObtinereValoreCurba(img):

    imgResult = img.copy()
    # Pasul 1 - obtinere imagine alb-negru
    ImagineAlb_Negru = EditModule.albnegru(img)
    #cv2.imshow('thres' , ImagineAlb_Negru)

    # Pasul 2 - obtinere imagine perspectiva transformata
    hT, wT, c = img.shape
    imaginetransformata = EditModule.ImaginePerspectivaNoua(ImagineAlb_Negru,puncte,wT,hT)
    #cv2.imshow('imgtransf' , imaginetransformata)

    # Pasul 3 - obtinere valorea curba
    ValoreaPunctReferinta = EditModule.ObtinereValoreaMedieCurba(imaginetransformata,ProcentajMinim=0.5,regiune=4)
    ValoareMedieCurba = EditModule.ObtinereValoreaMedieCurba(imaginetransformata, ProcentajMinim=0.9)
    ValoreCurba = ValoareMedieCurba - ValoreaPunctReferinta

    # Pasul 4 - medie a cate 10 valori curba
    ListValoriCurba.append(ValoreCurba)
    if len(ListValoriCurba)>SirValori:
        ListValoriCurba.pop(0)
    CurbaFinal = int(sum(ListValoriCurba)/len(ListValoriCurba))
    print('inainteCurbaFinal=' , CurbaFinal)

    # Afisare
    imgInvWarp = EditModule.ImaginePerspectivaNoua(imaginetransformata, puncte, wT, hT, inv=True)
    imgInvWarp2 = cv2.cvtColor(imgInvWarp, cv2.COLOR_GRAY2BGR)
   # imgInvWarp[0:hT // 3, 0:wT] = 0, 0, 0
    imgLaneColor = np.zeros_like(img)
    #culoare linie pe foaie cu scris
    imgLaneColor[:] = 0, 0, 255
    imgLaneColor = cv2.bitwise_and(imgInvWarp2, imgLaneColor)
    cv2.imshow('imglanecolor' , imgLaneColor)
    imgResult = cv2.addWeighted(imgResult, 1, imgLaneColor, 1, 0)
    cv2.putText(imgResult, str(CurbaFinal), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
    cv2.imshow('Resultat', imgResult)

    return CurbaFinal


if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')

    start_time = time.time()
    x = 1  # displays the frame rate every 1 second
    counter = 0

    while True:
        counter += 1
        if (time.time() - start_time) > x:
            print("FPS: ", counter / (time.time() - start_time))
            counter = 0
            start_time = time.time()

        success, img = cap.read()
        img = cv2.resize(img, (480, 240))
        CurbaFinal = ObtinereValoreCurba(img)
        # cv2.imshow('Video',img)
        cv2.waitKey(1)