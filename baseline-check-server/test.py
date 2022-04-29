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
sftp.put("./linuxcheeklist2.2.sh", "./linuxcheeklist2.2.sh")

# 下载
# 从远程/root/Desktop/hh.py获取文件下载到本地名称为hh.py
# sftp.get("/root/Desktop/hh.py","hh.py")

sftp.close()
print("上传完成")

# 运行脚本文件
# 创建一个ssh的客户端，用来连接服务器
ssh = paramiko.SSHClient()
# 创建一个ssh的白名单
know_host = paramiko.AutoAddPolicy()
# 加载创建的白名单
ssh.set_missing_host_key_policy(know_host)

ssh.connect(
    hostname="192.168.44.128",
    port=22,
    username="chenbo",
    password="chenboa55"
)

# 执行命令
stdin, stdout, stderr = ssh.exec_command("./linuxcheeklist2.2.sh")
# stdin, stdout, stderr = ssh.exec_command("ls -l")
# stdin  标准格式的输入，是一个写权限的文件对象
# stdout 标准格式的输出，是一个读权限的文件对象
# stderr 标准格式的错误，是一个写权限的文件对象

print(stdout.read().decode())
ssh.close()

print("运行完成")

# csv文件下载
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
print("下载完成")