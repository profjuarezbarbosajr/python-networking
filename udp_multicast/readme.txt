1) NOTE
Some networks with managed switches and routers have multicast traffic disabled by default. 
If you have trouble with the example programs, check your network configuration settings.

---------------------------------------------------------

2) TESTING AND EXAMPLE OUTPUT

This example shows the multicast receiver running on two different hosts:

- A has address 192.168.1.17 
- B has address 192.168.1.8

---------------------------------------------------------

[A]$ python ./socket_multicast_sender.py

waiting to receive message
received 19 bytes from ('192.168.1.17', 51382)
very important data
sending acknowledgement to ('192.168.1.17', 51382)

---------------------------------------------------------

[B]$ python ./socket_multicast_receiver.py

binding to ('', 10000)

waiting to receive message
received 19 bytes from ('192.168.1.17', 51382)
very important data
sending acknowledgement to ('192.168.1.17', 51382)
The sender is running on host A.

---------------------------------------------------------

$ python ./socket_multicast_sender.py

sending "very important data"
waiting to receive
received "ack" from ('192.168.1.17', 10000)
waiting to receive
received "ack" from ('192.168.1.8', 10000)
waiting to receive
timed out, no more responses
closing socket

---------------------------------------------------------

The message is sent one time, and two acknowledgements of the outgoing message are received, one from each of host A and B.