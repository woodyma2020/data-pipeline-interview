import json
import time
import sys
import os
import numpy as np    
import onnxruntime    
from PIL import Image
import base64
import io

def init():
    global session
    session = onnxruntime.InferenceSession('modelfile/model.onnx')

def preprocess(input_data_json):
    json_data = json.loads(input_data_json)
    base64_decoded_image = base64.b64decode(json_data['data'])
    image = Image.open(io.BytesIO(base64_decoded_image))
    image = image.convert("RGB")
    image = image.resize((224,224))
    img_data = np.array(image).astype('float32')
    img_data_expanded = np.expand_dims(img_data, axis=0)
    img_data_formatted = (img_data_expanded * 1./255)
    return img_data_formatted

def postprocess(result):
    return (np.array(result)).tolist()[0][0]

def run(input_data_json):
    try:
        start = time.time()
        input_data = preprocess(input_data_json)
        input_name = session.get_inputs()[0].name  
        result = session.run([], {input_name: input_data})
        end = time.time()
        return {"result": postprocess(result),
                "time": end - start}
    except Exception as e:
        result = str(e)
        return "error!:{}".format(result)
