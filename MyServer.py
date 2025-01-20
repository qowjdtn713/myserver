from flask import Flask
from flask import render_template
from flask import request

import os #시스템관련 라이브러리
import Label # Detect Label 관련 내가 만든 라이브러리
import Compare
from werkzeug.utils import secure_filename

app = Flask(__name__)

if not os.path.exists('static/imgs'):
    os.mkdir('static/imgs')

@app.route('/')
def home():
    return render_template('index.html')

#get post 등 데이터를 수신하는 route에는 전송방식을 명시
@app.route('/add', methods = ['GET', 'POST'])
def add():
    #2개의 get으로 온 값을 받아 더해서 출력
    #args get 방식 수신 | form: post 방식 수신
    num1 = int(request.args['num1'])
    num2 = int(request.args['num2'])
    print(num1, num2)
    s = '{} + {} = {}'.format(num1, num2, num1 + num2)
    return s

@app.route('/label', methods=['POST'])
def label():

    #전송방식 약한 체크
    if request.method == 'POST':
        f = request.files['label']
        filename = secure_filename(f.filename)
        f.save('static/imgs/' + filename)

    #도착한 사진의 경로 r 전달
    r = 'static/imgs/' + filename
    result = Label.detect_labels_local_file(r)
    return result

@app.route('/compare', methods = ['POST'])
def compare():
    if request.method == 'POST':
        f1 = request.files['face1']
        f2 = request.files['face2']

        filename1 = secure_filename(f1.filename)
        filename2 = secure_filename(f2.filename)

        f1.save('static/imgs/' + filename1)
        f2.save('static/imgs/' + filename2)

        r1 = 'static/imgs/' + filename1
        r2 = 'static/imgs/' + filename2

        result = Compare.compare_faces(r1, r2)
        return result

if __name__ == '__main__':
    app.run()