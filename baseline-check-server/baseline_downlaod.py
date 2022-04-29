import paramiko

trans = paramiko.Transport(
    sock=("192.168.44.128", 22)
)

trans.connect(
    username="chenbo",
    password="chenboa55"
)
sftp = paramiko.SFTPClient.from_transport(trans)

# 上传
# 把本地的文件settings.py，上传到远端为/root/Desktop/settings.py
# sftp.put("./linuxcheeklist2.2.sh", "./linuxcheeklist2.2.sh")

# 下载
# 从远程/root/Desktop/hh.py获取文件下载到本地名称为hh.py
sftp.get("./checkList.csv","checkList.csv")

sftp.close()

