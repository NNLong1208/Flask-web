from flask import Flask,render_template,jsonify
import random
import base64
from datetime import datetime
app = Flask(__name__)

data = []

check_ = ['Fake','Real']

#name =_[('name', id), ...]
#data = ten/time/anh/check/id
#main them tham so name_
# data them tham so id

def create():
    data.clear()
    name = random.choice(name_)
    check = random.choice(check_) #Real/Face
    now = datetime.now().strftime("%H:%M:%S")
    with open(r"static\img\building.jpg", "rb") as image_file:
        img = base64.b64encode(image_file.read()).decode("utf-8")
    data.append(name[0])
    data.append(now)
    data.append(img)
    data.append(check)
    data.append(name[1])

def create_list_name(link):
    text_file = open(link, encoding="utf8")
    lines = text_file.readlines()
    list_name = []
    for line in lines:
        idx = [i for i in range(len(line)) if line[i] == " "]
        name = line[: idx[-1]]
        l = line[idx[-1]:-1]
        list_name.append((name,l))
    return list_name
name_ = create_list_name('label.txt')

@app.route('/update_table', methods=['POST', 'GET'])
def updatetable():
    create()
    if len(data) > 0:
        return jsonify(data = data)

@app.route('/')
def main():
    return render_template('index.html', data = data, date = datetime.now().strftime("%d/%m/%Y"), list_name = create_list_name('label.txt'))

if __name__ == "__main__":
    app.run(debug=True)