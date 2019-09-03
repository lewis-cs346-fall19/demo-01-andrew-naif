import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("0.0.0.0", 12847)
    
sock.bind(addr)

sock.listen(5)

while True:
	(connectedSock, clientAddress) = sock.accept()
	try:
		while True:
			msg = connectedSock.recv(1024).decode()
			if not msg:
				break
			addition = "Here's the data: "
			fin = addition + msg
			connectedSock.sendall(fin.encode())
	finally:
		connectedSock.close()


	
	
