#-*-coding:UTF-8-*-
import socket
import time
import chardet
import sql
hf='ok'
sqlbuf=[' ']*3
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket (AF_INET:IPv4, AF_INET6:IPv6) (SOCK_STREAM:面向流的TCP协议)
name=socket.gethostname()
port=8080
s.bind((name,port))  # 绑定本机IP和任意端口(>1024)

s.listen(1)  # 监听，等待连接的最大数目为1

print('Server is running...')


def TCP(sock, addr):  # TCP服务器端处理逻辑

    print('Accept new connection from %s:%s.' % addr)  # 接受新的连接请求


    while True:
        data = sock.recv(1024)  # 接受其数据
        buffer=( bytes.decode(data))
        sqlbuf=buffer.split()
        if len(sqlbuf)>2:
            sql.writesql(sqlbuf[0],sqlbuf[1],sqlbuf[2])
        else:
            print("数据异常")
        print (sqlbuf)

        time.sleep(1)  # 延迟
        
        sock.send(hf.encode())  # 发送变成大写后的数据,需先解码,再按utf-8编码,  encode()其实就是encode('utf-8')

    sock.close()  # 关闭连接
    print('Connection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()  # 接收一个新连接
    TCP(sock, addr)  # 处理连接
