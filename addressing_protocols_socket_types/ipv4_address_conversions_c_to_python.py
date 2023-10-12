# Network programs written in C language use the data type struct sockaddr to represent 
# IP addresses as binary values (instead of the string addresses usually found in Python programs)

# Convert IPv4 addresses between the Python representation and the C representation 
# with inet_aton() and inet_ntoa().

# The four bytes in the packed format can be passed to C libraries, 
# transmitted safely over the network, or saved to a database compactly.

import binascii
import socket

string_address = '192.168.1.1'
packed = socket.inet_aton(string_address)

print ('Original:', string_address)
print ('Packed  :', binascii.hexlify(packed))
print ('Unpacked:', socket.inet_ntoa(packed))