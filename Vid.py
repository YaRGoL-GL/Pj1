
"""import cv2


def haar_detection(image):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # start detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 242, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (229, 244, 65), 2)
    # end detection

    return img


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while (cap.isOpened()):
        ret, img = cap.read()
        img = haar_detection(img)
        cv2.imshow('Video', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()"""
import cv2
import numpy as np
import time

# https://www.youtube.com/watch?v=f2TUxoaKIsA

pengklasifikasiWajah = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("Kamera tidak dapat diakses")
    exit()

tombolQditekan = False
while (tombolQditekan == False):
    ret, kerangka = videoCam.read()

    if ret == True:
        abuAbu = cv2.cvtColor(kerangka, cv2.COLOR_BGR2GRAY)
        dafWajah = pengklasifikasiWajah.detectMultiScale(abuAbu, scaleFactor=1.3, minNeighbors=2)

        for (x, y, w, h) in dafWajah:
            cv2.rectangle(kerangka, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # print("Jumlah Wajah terdeksi: ", len(dafWajah))
        teks = "Jumlah Wajah Terdeteksi = " + str(len(dafWajah))

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(kerangka, teks, (0, 30), font, 1, (255, 0, 0), 1)

        cv2.imshow("Video", kerangka)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tombolQditekan = True
            break

videoCam.release()
cv2.destroyAllWindows()
