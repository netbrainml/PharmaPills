from flask import Flask, request, render_template, Response
from camera import VideoCamera
import tensorflow as tf
import numpy as np
from datetime import datetime
import cv2
import time
import os


app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

model = tf.keras.models.load_model('model.h5')
id_model = tf.keras.models.load_model('best_model.h5')

timestamps = []
predictions = []
dui = []

timestamps1 = []
predictions1 = []
dui1 = []

@app.route('/')
def index():
    return render_template('/index.html')



@app.route('/pillid')
def pidindex():
    return render_template('/pillid.html')

@app.route('/camview1')
def camview1():
    return render_template('camview1.html')
@app.route('/logs1')
def logs1():
    return render_template('logs1.html')
@app.route('/log_test1')
def test_log1():
    return render_template('log_test1.html', timestamps = timestamps1, predictions=predictions1, dui=dui1)
    
@app.route('/video_test1')
def test_feed1():
    return Response(test_gen1(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def test_gen1():
    classes=['abacavir','clonazepam','diclofenac', 'lexapro','omeprazole', 'tramadol HCl']
    try:
        while True:
            for file in os.listdir("static/img/test1"):
                try:
                    tmp = "../static/img/test1/"+file
                    img=getIMG("static/img/test1/"+file, size=224)
                    x=np.argmax(id_model.predict(img[None,:]))
                    dui1.append("img/test1/"+file)
                    predictions1.append(classes[int(x)])
                    timestamps1.append(datetime.now())
                    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg',cv2.resize(img*255,(224,224)))[1].tobytes() + b'\r\n\r\n')
                except:
                    continue
    except: return
"""
Camera
"""
@app.route('/pharmavision')
def pvindex():
    return render_template('/pharmavision.html')

@app.route('/camview')
def camview():
    return render_template('camview.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        #timestamp and predict
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_test')
def test_feed():
    time.sleep(1)
    return Response(test_gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def test_gen():
    try:
        while True:
            for file in os.listdir("static/img/test"):
                try:
                    tmp = "../static/img/test/"+file
                    img=getIMG("static/img/test/"+file)
                    x=round(model.predict(img[None,:])[0][0]*100,2)
                    if x>50:
                        dui.append("img/test/"+file)
                        predictions.append(str(x)+"%")
                        timestamps.append(datetime.now())
                    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg',cv2.resize(img*255,(224,224)))[1].tobytes() + b'\r\n\r\n')
                except:
                    continue
    except: return

def getIMG(path, size = 128):
    return cv2.resize(cv2.imread(path), (size,size))/255.0

"""
Logs
"""

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/log_bot')
def log_bot():
    return render_template('log_bot.html', id=1, timestamps = timestamps, predictions=predictions, dui=dui)

@app.route('/log_test')
def test_log():
    return render_template('log_test.html', timestamps = timestamps, predictions=predictions, dui=dui)

if __name__=="__main__":
    app.run(threaded=True)