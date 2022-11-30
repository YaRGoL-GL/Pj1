'''

class Animal:
    height = 80
    age = 4
    happyness = 50
class Dog(Animal):
    happyness = 70
class Cat(Animal):
    age =  2
    height = 58
alfred = Dog()
murchik = Cat()

print ('Alfreds height - ',alfred.height)
print ('Murchiks height - ',murchik.height)
print ('Alfreds age - ',alfred.age)
print ('Murchiks age - ',murchik.age)
print ('Alfreds happyness - ',alfred.happyness)
print ('Murchiks happyness - ',murchik.happyness)
--------------------------------------------------------------
import unittest
import time
from main import *
a=int(input('a= '))
b=int(input('b= '))

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(a, b), 10)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    unittest.main()
    '''
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
if ret == True:
    abuAbu1 = cv2.cvtColor(kerangka, cv2.COLOR_BGR2BLACK)
    dafWajah1 = pengklasifikasiWajah.detectMultiScale1(abuAbu1, scaleFactor=1.3, minNeighbors=2)
if ret == True:
    abuAbu2 = cv2.cvtColor(kerangka, cv2.COLOR_BGR2WHITE)
    dafWajah2 = pengklasifikasiWajah.detectMultiScale2(abuAbu2, scaleFactor=1.3, minNeighbors=2)

for (x, y, w, h) in dafWajah:
    cv2.rectangle(kerangka, (x, y), (x + w, y + h), (0, 255, 0), 2)
for (x, y, w, h) in dafWajah1:
    cv2.rectangle(kerangka, (x, y), (x + w, y + h), (255, 0, 255), 4)
    for (x, y, w, h) in dafWajah2:
        cv2.rectangle(kerangka, (x, y), (x + w, y + h), (0, 0, 100), 3)

        # print("Jumlah Wajah terdeksi: ", len(dafWajah))
teks = "Jumlah Wajah Terdeteksi = " + str(len(dafWajah))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(kerangka, teks, (0, 30), font, 1, (255, 0, 0), 1)
cv2.imshow("Video", kerangka)
if cv2.waitKey(1) & 0xFF == ord('q'):
    tombolQditekan = True

videoCam.release()
cv2.destroyAllWindows()


