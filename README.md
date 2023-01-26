# Gaze estimation

Estimate whether the person is slooking to the ```left```, ```right``` or ```center``` .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

```
git clone https://github.com/aaronpp65/Visual-Relationshiop-Detection-Annotation-tool.git
```

### Prerequisites

What things you need to install and how to install them

```
pip install requirements.txt
```
## Usage

To callibrate the camera first take images of chessboard using your camera and copy it to ```calibration/imgs``` folder. Then run the camera callibration file using the command
```
python calibration/calib.py
```

To perform gaze estimation on live video feed from your webcam, run

```
python main.py
```

To perform gaze estimation on a single image,

```
from modules.inf_image import ImageGaze
model = ImageGaze()
gaze = model.get_gaze(image_url)
```
Api for gaze estimation on a single image can be run using ```python api.py``` 

To build and run docker image,

```
sudo docker build -t gaze:v10 .
sudo docker run --name gaze_estimation -p 80:80 gaze:v10
```




## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Aaron Peter** - *Initial work* - [aaronpp65](https://github.com/aaronpp65)


See also the list of [contributors](https://github.com/aaronpp65/Visual-Relationshiop-Detection-Annotation-tool/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [MediaPipe Face Mesh ](https://google.github.io/mediapipe/solutions/face_mesh.html)
* [Camera Calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)

