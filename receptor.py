import socket
from bitarray import bitarray


HOST = "127.0.0.1"  
PORT = 12345 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        while True: 

            data = conn.recv(1024)
            if not data:
                break  
            

