# Simple Checksum

message = input("Enter a short message: ")

checksum = 0

for ch in message:
    checksum = checksum + ord(ch)

print("Original Checksum:", checksum)

# Simulate transmission error
import random

msg = list(message)

index = random.randint(0, len(msg)-1)

msg[index] = chr(ord(msg[index]) + 1)

received = "".join(msg)

print("Received Message:", received)

new_checksum = 0

for ch in received:
    new_checksum = new_checksum + ord(ch)

print("Received Checksum:", new_checksum)

if checksum == new_checksum:
    print("OK")
else:
    print("ERROR DETECTED")
