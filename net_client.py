import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("localhost", 12847)

sock.connect(addr)

try:
	for num in range(101):
		sock.sendall(str(num).encode())
		msg = sock.recv(1024).decode()
		print(msg.encode())
finally:
        sock.close()



