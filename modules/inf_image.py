from modules.mesh import Mesh
from modules.eye import Eye
from modules.utils import  get_image, calc_gaze
from imageio import imread
from pydantic import BaseModel

class ImageGazeQueryModel(BaseModel): 
    url : str

class ImageGaze:
    """
    Class to run inference on a single image
    """

    def get_gaze(self,url):

        face_mesh = Mesh(True, 1, True, 0.5)

        frame = get_image(url)

        if frame is None:
            return "Invalid url"

        mesh_points = face_mesh.get_ladmarks(frame)

        if mesh_points is None:
            return "No face detected"

        eye = Eye(mesh_points)

        ratio, left_centroid, right_centroid = eye.calc_ratio()

        gaze = calc_gaze(ratio)

        return gaze

        # if(abs(ratio)<self.threshold):
        #     gaze = "center"
        # elif(ratio<0):
        #     gaze ="right"
        # else:
        #     gaze ="left"
        # return gaze


