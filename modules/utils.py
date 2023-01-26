import base64
import cv2
import math
from imageio import imread
import requests
import io

def get_centroid(points):
    """Calculates centroid of a contour
        Arguments:
            points (numpy.ndarray): list of (x,y) points 
        Returns:
            x,y (int): centroid
    """
    moments = cv2.moments(points)
    x = int(moments['m10'] / moments['m00'])
    y = int(moments['m01'] / moments['m00'])
    return x,y

def distance(A,B):
    """Calculates distance between A and B
        Arguments:
            A,B (tuple): (x,y) point 
        
    """
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def ratio(p1, centroid, p2):
    """
    Calculates ratio of point "centroid" dividing line  p1 to p2
        
    """
    dist_l = distance(p1, centroid)
    dist_r = distance(centroid, p2)
    return ((dist_r-dist_l)/(dist_r+dist_l))

def draw(frame, left_centroid, right_centroid, gaze):
    """
    Annotating the image for display
    """
    cv2.circle(frame, (int(left_centroid[0]), int(left_centroid[1])), 3, (255, 0, 0), -1)
    cv2.circle(frame, (int(right_centroid[0]), int(right_centroid[1])), 3, (255, 0, 0), -1)
    cv2.flip(frame, 1)
    cv2.putText(frame, gaze, (int(left_centroid[0]), int(left_centroid[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (36,255,12), 2)


    return frame

def get_image(url):
    """
    Download an image and convert it for cv2
    """

    data = base64.b64encode(requests.get(url).content)
    b64_string = data.decode()

    # reconstruct image as an numpy array
    img = imread(io.BytesIO(base64.b64decode(b64_string)))

    # finally convert RGB image to BGR for opencv
    # and save result
    frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return frame


