import socket
from bitarray import bitarray
from fletcher import fletchet_check



HOST = "127.0.0.1"  
PORT = 12345 

def default_ver(a):
    print('no verification function was given')

verification_func = fletchet_check

in_buffer = bitarray()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        while True: 

            data = conn.recv(1024)
            data_bytes = bytes(str(data), 'ascii')
            x = bitarray()
            x.frombytes(data_bytes)
            in_buffer += x
            if not data:
                break  
        # se recibió todo

        # verificación
        verification_func(in_buffer)


