import socket

#TODO: 这个函数要自己改
def get_request_target(request_data):
    return "baidu.com"

def start_server(ip, port):
    s = socket.socket()
    s.bind((ip, port))
    s.listen()

    # 服务器持续工作
    while True:
        addr, cs = s.accpet()
        request_data = cs.recv(1024)  # 1024最好是配置
        target_host = get_request_target(request_data)
        ip = socket.get_host_by_name(target_host)   # TODO: 确认，根据域名查ip接口

        ts = socket.socket()
        ts.connect((ip, 80))     # TODO: 80写死，可能也要去request_data里取
        ts.send(request_data)
        response_data = ts.recv(10240)     # TODO: 返回的页面信息，10240可能不够，看页面大小

        cs.send(response_data)


if __name__ == '__main__':
    start_server("127.0.0.1", 8099)
