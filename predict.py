import ultralytics
from ultralytics import YOLO
ultralytics.checks()
import torch

device = 'cuda'

model = YOLO("best.pt")
path ="test.mp4"

results = model.predict(source=path, show = True)   
