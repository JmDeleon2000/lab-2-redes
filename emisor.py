'''
Universidad del valle de Guatemala
Laboratorio 2 de redes de computadoras - esquemas de deteccion y correcion de errores
Jorge de León - 19817
Andres Quinto - 18288

'''
import socket
import numpy
from bitarray import bitarray

def noise(bits):
    my_bits = bitarray()
    for bit in bits:
        if bit == 0:
            my_bits.append(1)

    return

HOST = "127.0.0.1"  
PORT = 12345      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


    #ruido

    #se usa b"" para indicar que envie bytes
    s.sendall(b"enviando datos al receptor :)")
