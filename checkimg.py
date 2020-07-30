import sourceimg
import basic
import os
import cv2
import numpy as np
import face_recognition as fr
from PIL import ImageGrab

basic.makeFileAttend()
encodedListKnow = sourceimg.findEncoded(sourceimg.images)

while True:
    captureVid = ImageGrab.grab()
    img_np = np.array(captureVid)
    imgSize = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    faceCurrentFrame = fr.face_locations(imgSize)
    encodeCurrentFace = fr.face_encodings(imgSize, faceCurrentFrame)
    for encodeFace, faceLoc in zip(encodeCurrentFace, faceCurrentFrame):
        matches = fr.compare_faces(encodedListKnow, encodeFace)
        faceDist = fr.face_distance(encodedListKnow, encodeFace)
        indexMatch = np.argmin(faceDist)
        if matches[indexMatch]:
            faceName = sourceimg.name[indexMatch].upper()
            basic.makeAttendance(faceName)


