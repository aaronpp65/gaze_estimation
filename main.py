import math
from modules.mesh import Mesh
from modules.eye import Eye
from modules.utils import draw
import numpy as np
import json
import cv2
import os

# eyes closed

if __name__ == '__main__':
    
    config = json.load(open('config.json',))
    threshold = config['threshold']
    camera = config['camera']
    # callibration 
    dist = np.array(config['dist'])
    mtx = np.array(config['mtx'] )

    cap = cv2.VideoCapture(camera)
    face_mesh = Mesh(True, 1, True, 0.5)

    while cap.isOpened():
        success, image = cap.read()

        # # callibrate image
        # h,  w = image.shape[:2]
        # newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

        # # undistort
        # dst = cv2.undistort(image, mtx, dist, None, newcameramtx)

        # # crop the image
        # x, y, w, h = roi
        # image = dst[y:y+h, x:x+w]
        
        # get facial landamrks
        mesh_points = face_mesh.get_ladmarks(image)
        annotated_image = image.copy()
        if mesh_points is None:
            continue
        
        #extract eye and calculate gaze 
        eye = Eye(mesh_points)
        ratio, left_centroid, right_centroid = eye.calc_ratio()


        if(abs(ratio)<threshold):
            gaze = "center"
        elif(ratio<0):
            gaze ="left"
        else:
            gaze ="right"

        # annotate the image and display
        frame = draw(annotated_image, left_centroid, right_centroid, gaze)
        cv2.imshow('MediaPipe Face Mesh', frame)
        print(gaze)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()




