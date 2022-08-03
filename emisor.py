import socket


def noise():
    return

HOST = "127.0.0.1"  
PORT = 12345      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


    #ruido

    #se usa b"" para indicar que envie bytes
    s.sendall(b"enviando datos al receptor :)")
