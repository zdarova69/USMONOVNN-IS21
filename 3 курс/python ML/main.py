from glob import glob
import numpy as np
import cv2
from PIL import Image
import time

start_time = time.time()  # время начала выполнения

cap = cv2.VideoCapture("2023-11-12 14-53-02.mkv")
i = 0
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    i = i + 1
    
    end_time = time.time()  # время окончания выполнения
    execution_time = end_time - start_time  # вычисляем время выполнения
    
    # Сохранять кадр каждые 2 секунды (если execution_time делится на 2 без остатка)
    if execution_time >= 1:
        cv2.imwrite(f'videos_cadr/game{i}.jpeg', img)
        print(f"Сохранен кадр {i}")
        start_time = time.time()  # обновляем время начала выполнения

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(len(glob('videos_cadr/*')))