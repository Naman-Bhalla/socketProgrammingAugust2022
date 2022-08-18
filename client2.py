import socket

host = "127.0.0.1"
port = 4437

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.sendall(bytes("Hello PEOPEPEPELELE!".encode("utf-8")))
# CLient socket will have an ephemeral port
# lAddr (127.0.0.1, SomeEphemeralPort) rAddr (127.0.0.1, 4435)

data = sock.recv(1024)

sock.close()

print(data)