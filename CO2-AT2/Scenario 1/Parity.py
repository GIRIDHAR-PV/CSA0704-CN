#Error Detection using even parity
msg = input("enter a short msg:")
binary =""

for ch in msg:
    binary= binary + format(ord(ch), '08b')

print("Binary:", binary)

ones = binary.count("1")
if ones %2==0:
    parity = '0'
else:
    parity = '1'

print("Parity Bit:", parity)

#Simulate Transmission error

import random

received = list(binary)
pos= random.randint(0, len(received)-1)

if received[pos] == "0":
    received[pos] = '1'

else:
    received = ''.join(received)
    print("Received Binary:",received)

#Check Parity again

new = received.count('1')

if new %2 == int(parity):
    print("ok")
else:
    print("Error Detected")
    
