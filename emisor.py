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
from bitarray import bitarray
import timeit
import matplotlib.pyplot as plt

from fletcher import fletcher_sum #https://pypi.org/project/bitarray/ (realizar un array de bits)


samples = ['Lorem ipsum dolor sit amet', 
           'Lorem ipsum dolor sit amet, consectetur adipiscing elit, ',
           'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
           'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.']

lenghts = [len(i) for i in samples]


HOST = "127.0.0.1"  
PORT = 12345      

    #ruido
def noise(bits):
    my_bits = bitarray()
    for bit in bits:
        new_bit = int((not(bit))) if numpy.random.choice([0,1], p=[0.95,0.05]) else bit
        my_bits.append(new_bit)
    return my_bits

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
times_avg = []
for sample in samples:
    m_times = []
    for i in range(50):
        #Verificacion del mensaje

        bits = bitarray()
        bits.frombytes(bytes(sample, 'ascii'))

        t1 = timeit.default_timer()
        bits += fletcher_sum(bits)
        t2 = timeit.default_timer()

        m_times.append(t2-t1)

        s.send(noise(bits))
    
    times_avg.append(sum(m_times)/len(m_times))
s.close()
print("Connection closed")

plt.plot(lenghts, times_avg)
plt.show()