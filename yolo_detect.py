import torch
import numpy as np
import yaml

class ImageDetect:
    # field
    model = torch.hub.load('ultralytics/yolov5', 'custom', 'yolov5s', force_reload=True)
    data = {}

    # 클래스 생성 시 자동으로 호출되는 생성자 함수
    def __init__(self):
        with open('coco.yaml','r',encoding='UTF-8') as f :
            self.data = yaml.full_load(f)['names']

    # self : 파이썬에서 self 키워드는 해당 함수를 호출한 객체를 가리킵니다.
    def detect_img(self, img):
        return self.model(img).xyxyn[0].numpy()