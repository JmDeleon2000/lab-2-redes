'''

Universidad del valle de Guatemala
Laboratorio 2 de redes de computadoras - esquemas de deteccion y correcion de errores
Jorge de León - 19817
Andres Quinto - 18288

'''
import socket #https://docs.python.org/3/library/socket.html (Para la conexion de sockets)
import numpy #https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html (para el ruido)
import binascii #https://docs.python.org/3/library/binascii.html (libreria de conversion de binario a ascii)
import pickle
from bitarray import bitarray #https://pypi.org/project/bitarray/ (realizar un array de bits)

HOST = "127.0.0.1"  
PORT = 12345      

    #ruido
def noise(bits):
    my_bits = bitarray()
    for bit in bits:
        new_bit = int((not(bit))) if numpy.random.choice([0,1], p=[0.95,0.05]) else bit
        my_bits.append(new_bit)
    return

    #Funcion para transformar de string a bits
def string_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

    #Verificacion str->binary ASCII->bitarray
def verification(str_):
    bits = string_to_bits(str_)
    return (bitarray(bits))

    #Transmision
s = socket.socket()
s.connect((HOST,PORT))
while True:
    str_ = input("Escriba su mensaje :): ")
    my_bitarray = verification(str_)       #Verificacion del mensaje
    # fletcher = blablabla
    # bits = noise(fletcher + my_bitarray)   #Adicion del ruido por medio de numpy
    print(my_bitarray)
    s.send(bits)
    if(str == "Bye" or str == "bye"):
        break
s.close()
print("Connection closed")
