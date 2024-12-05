import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__)
api_url = 'http://127.0.0.1:5001/api/v0'

# 确保 downloads 目录存在
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# 创建一个字典来存储 CID 和原始文件名
file_storage = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    response = requests.post(f"{api_url}/add", files={'file': file})
    result = response.json()
    original_filename = file.filename  # 获取原始文件名
    cid = result['Hash']
    file_storage[cid] = original_filename  # 保存 CID 和原始文件名的映射
    return f"File uploaded with CID: {cid} and original filename: {original_filename}"


@app.route('/download', methods=['GET'])
def download():
    cid = request.args.get('cid')
    original_filename = file_storage.get(cid)  # 获取保存的原始文件名
    if not original_filename:
        return "File not found or CID is incorrect"

    output_path = os.path.join('downloads', original_filename)
    response = requests.get(f"{api_url}/cat?arg={cid}")
    with open(output_path, 'wb') as f:
        f.write(response.content)
    return f"File downloaded to {output_path}"


if __name__ == '__main__':
    app.run(debug=True)
