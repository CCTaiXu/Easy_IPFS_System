# 下载文件
def download_file(cid, output_path):
    client.get(cid, output_path)
    print(f"File downloaded to {output_path}")

cid = 'Qm...your_cid...'  # 替换为上传文件时返回的 CID
output_path = 'path/to/save/the/file'
download_file(cid, output_path)
