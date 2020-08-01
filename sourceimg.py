import os
import cv2
import numpy as np
import face_recognition as fr

path = input("Add path to folder where sample photos of the person is stored\nEnter the path: ")
'''Please add the path from were you have the photos of 
student or people you want to recognise, also not those photo's name should be of that person(eg alex.jpg)'''
name = []
images = []
listOfImage = os.listdir(path)
for im in listOfImage:
    img = cv2.imread(f'{path}/{im}')
    images.append(img)
    name.append(os.path.splitext(im)[0])


def findEncoded(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeReferenceFace = fr.face_encodings(img)[0]
        encodeList.append(encodeReferenceFace)
    return encodeList
