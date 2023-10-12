# creates a pair of sockets using the socket.socketpair() function and uses it for the bidirectional
# communication between a parent and child process
import socket
import os

def msgParentProc(childSocket):
    childSocket.send("Hi from child".encode())
    print(childSocket.recv(1024).decode())

def msgChildProc(parentSocket):
    parentSocket.send("Hi from parent".encode())
    print(parentSocket.recv(1024).decode())

# Create a socket pair using Unix domain protocol
sockPair = socket.socketpair(socket.AF_INET)

childProcSocket     = sockPair[0]
parentProcSocket     = sockPair[1]

# Note: os.fork() method is available only on UNIX platforms
retVal    = os.fork()
if retVal == 0:
    print("Child pid:%d"%os.getpid())
    
    #Use child socket
    parentProcSocket.close()
    msgParentProc(childProcSocket)
else:
    print("Parent pid:%d"%os.getpid())
    
    #Use parent socket
    childProcSocket.close()
    msgChildProc(parentProcSocket)
 