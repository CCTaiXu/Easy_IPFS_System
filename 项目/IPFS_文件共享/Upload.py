import ipfshttpclient

# 连接到本地的 IPFS 节点
client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')

# 上传文件
def upload_file(file_path):
    result = client.add(file_path)
    print('File added with CID:', result['Hash'])
    return result['Hash']

file_path = 'path/to/your/file'
upload_file(file_path)
