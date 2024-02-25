import numpy as np
import pandas as pd
import cv2 

cap = cv2.VideoCapture("видео 1.mp4")
instrument_list = ['inst_1','inst_2','inst_3','inst_4','inst_5']
kernel = np.ones((5,5),np.uint8)

while True:
    success, img = cap.read()
    gray_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur33_1 = cv2.GaussianBlur(gray_1, (99,99), 0)
    thresh_1 = cv2.threshold(blur33_1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    all_cnts = cv2.findContours(thresh_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    all_cnts = all_cnts[0] if len(all_cnts) == 2 else all_cnts[1]
    erosion_1 = cv2.erode(thresh_1,kernel,iterations = 1)
    print(len(all_cnts))
    break

print(len(all_cnts))
instrument_dict = dict(zip(instrument_list, all_cnts))
print(instrument_dict)

while True:
    success, img = cap.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur33 = cv2.GaussianBlur(gray, (99,99), 0)
    thresh = cv2.threshold(blur33, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    erosion_1 = cv2.erode(thresh,kernel,iterations = 1)
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    print(len(all_cnts),len(cnts))
    for count, c in enumerate(all_cnts): # перебор контуров игорь копируй это
    #определяет длину контуров
        perimeter = cv2.arcLength(c, True)
        #сглаживание на 4%
        approx = cv2.approxPolyDP(c, 0.04 * perimeter, True)
        print(approx)
        font = cv2.FONT_HERSHEY_SIMPLEX
        #если контур существует
        if len(approx) > 0:
            #определяем координаты
            x,y,w,h = cv2.boundingRect(c)
            #зная ширину,можно узнать диаметр и радиус
            # diameter = w
            # radius = w/2
            # определяем моменты - центр фигуры
            M = cv2.moments(c)
            # если центр найден - вычисляем координаты
            if M["m00"] != 0:
                cX = int(M['m10']/M['m00'])
                cY = int(M['m01']/M['m00'])
                print(cX,cY)
                img = cv2.putText(img, str(instrument_list[count]), (cX, cY), font, 1, (255,0,0), 2, cv2.LINE_AA)
                #рисуем контуру: изображение,контур, индекс контура, цвет, толщина
                cv2.drawContours(img, [c], 0, (36,255,12), 1)
        cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
missing_instrument_value = {}
l = []
for key,value in instrument_dict.items():
  x = cv2.matchShapes(value, cnts[0], 3, 0.0)
  l.append(x)
  missing_instrument_value[key]=x
print(missing_instrument_value)
l = sorted(l)
print(l[0], l[1], l[2])
df = pd.DataFrame(missing_instrument_value, index=[1])
 
	
df.to_csv('output.csv', sep='\t', encoding='utf-8')