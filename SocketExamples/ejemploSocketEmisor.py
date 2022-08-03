import socket

HOST = "127.0.0.1"  # IP, capa de Red. 127.0.0.1 es localhost
PORT = 65432        # Puerto, capa de Transporte

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #conecta activamente con la ip y puerto especificados
    s.connect((HOST, PORT))
    #se usa b"" para indicar que envie bytes
    s.sendall(b"enviando datos al receptor :)")
    #data = s.recv(1024)

#print(f"Recibido: {data!r}")
