from pprint import pprint
from bitarray import bitarray


def fletcher_sum(buffer):
    sum1 = 0
    sum2 = 0
    for i in range(len(buffer)//8):
        a = int.from_bytes(buffer[i*8:(i+1)*8:].tobytes(), 
            byteorder='big')
        sum1 = (sum1+a)%255
        sum2 = (sum1+sum2)%255
    
    sumpt1 = bitarray()
    sumpt1.frombytes(sum1.to_bytes(2, 'big')) 
    sumpt1 <<=8
    sumpt2 = bitarray()
    sumpt2.frombytes(sum2.to_bytes(2, 'big'))
    return sumpt1 | sumpt2


def fletchet_check(buffer):
    sum = buffer[-16::]
    new_sum = fletcher_sum(buffer[:len(buffer)-16:])
    return sum == new_sum

#a = 32 * bitarray('0')
#a[1:15:3] = 5 * bitarray('1')
#a[30] = 1
#
#b = 32 * bitarray('0')
#b[1:15:3] = 5 * bitarray('1')
#b[20] = 1
#
#
#x = fletcher_sum(a)
#xa = b+x
#
#
#print(fletchet_check(xa))