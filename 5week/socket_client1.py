import socket


sock = socket.socket()
sock.connect(("127.0.0.1", 10001))
sock.sendall("pind".encode("utf8"))
sock.close()