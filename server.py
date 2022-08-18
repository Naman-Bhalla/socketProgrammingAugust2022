import socket
import  http.client
import threading

def handleConnection(connection, address):
    data = connection.recv(2048)
    print(data)
    connection.sendall(bytes(str(data).encode("utf-8") + " I RECEIVED THIS FROM YOU".encode("utf-8")))

    connection.close()
    print("Handled another client")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 4437

sock.bind((host, port))
sock.listen()

while True:
    connection, address = sock.accept()
    t = threading.Thread(target=handleConnection, args=(connection, address))
    t.start()

sock.close()

# laddr = address of me
# raddre = oaddress of other


