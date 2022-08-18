import socket
import http
import threading
import time

# AF -> Address Family -> ipv4
# SOCK_STREAM TCP  -> SOCK_DGRAM UDP

host = "127.0.0.1"
port = 4437

def connectToServer(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(bytes("Hello Class!".encode("utf-8")  + message.encode("utf-8")))
    # CLient socket will have an ephemeral port
    # lAddr (127.0.0.1, SomeEphemeralPort) rAddr (127.0.0.1, 4435)

    data = sock.recv(1024)

    sock.close()

    print(data)


for i in range(1000):
    t = threading.Thread(target=connectToServer, args=(str(i),))
    t.start()
    time.sleep(0.2)

