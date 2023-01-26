import mediapipe as mp
import numpy as np
import cv2

class Mesh():

    def __init__(self, static_image_mode, max_num_faces, refine_landmarks, min_detection_confidence):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
                            static_image_mode=static_image_mode,
                            max_num_faces=max_num_faces,
                            refine_landmarks=refine_landmarks,
                            min_detection_confidence=min_detection_confidence)

    def get_ladmarks(self, frame):
        # image = cv2.imread(frame)
        frame.flags.writeable = True
        img_h, img_w = frame.shape[:2]
        # Convert the BGR image to RGB before processing.
        results = self.face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        mesh_points = None
        if results.multi_face_landmarks:
            mesh_points=np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])

        return mesh_points

if __name__ == '__main__':
    face_mesh = Mesh(True, 1, True, 0.5)
    mesh_points = face_mesh.get_ladmarks('face.jpeg')
    print(len(mesh_points))
