import json
from modules.utils import get_centroid, ratio

class Eye():
    """
    class to extract the eye, iris and centroid from face mesh points and calulate position of pupil in the eye
    """

    def __init__(self,mesh_points):
        """
        Extract different eye related features

        """
        config = json.load(open('config.json',))

        self.left_eye = mesh_points[config['eye']['left']['full']]
        self.left_iris = mesh_points[config['eye']['left']['iris']]

        self.right_eye = mesh_points[config['eye']['right']['full']]
        self.right_iris = mesh_points[config['eye']['right']['iris']]

    def calc_ratio(self):
        
        """
        Calculate the positioning of iris with respect to the eye(left and right) using ratios
        """
        left_centroid = get_centroid(self.left_iris)
        left_ratio = ratio(self.left_eye[0],left_centroid, self.left_eye[8])
        
        right_centroid = get_centroid(self.right_iris)
        right_ratio = ratio(self.right_eye[0],right_centroid, self.right_eye[8])

        return (left_ratio+right_ratio)/2, left_centroid, right_centroid

