import json
import uvicorn
from fastapi import FastAPI
from modules.inf_image import ImageGaze, ImageGazeQueryModel

config = json.load(open('config.json',))
threshold = config['threshold']
app = FastAPI()
model = ImageGaze(threshold)

@app.post('/predict')
def predict(data: ImageGazeQueryModel):
    data = data.dict()   
    gaze = model.get_gaze(data['url'])  
    return { 'gaze': gaze }  

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000) 