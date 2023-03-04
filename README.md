# Pokemon object detections
Using yolov8 after training with Google Colab
## Dataset
Because lack of data, there are only 7 class: ```pikachu```, ```charmander```, ```bulbasaur```, ```squirtle```, ```eevee```, ```jigglypuff``` and ```other```.  
  
![labels](https://github.com/vovod/yolov8-pokemon-object-detection/blob/main/after_train/labels.jfif)
## Requirements
```
pip install ultralytics
```
## Preprocess Data
The ```convert.py``` used to convert *.xml* label file to *.txt* yolo label file.  
Run ```resize_image.py``` to resize image's width to 640.
## Training with Collab
Edit ```coco128.yaml```.
Upload images and labels.
```
!yolo train model=yolov8n.pt data=/content/coco128.yaml epochs=50 imgsz=640
```
## Training's Result
```last.pt``` and ```best.pt``` in result folder.
  
![train](https://github.com/vovod/yolov8-pokemon-object-detection/blob/main/after_train/results.png?raw=true)
## Predict
Run ```predict.py``` to see result. This is my predict to ```test.mp4```:  
  
![result](https://github.com/vovod/yolov8-pokemon-object-detection/blob/main/result.gif?raw=true)

#### Thank you for stopping by!
