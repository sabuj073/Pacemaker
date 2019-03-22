import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:7777")

while True:
    msg = socket.recv_string()
    print("From Client : ",msg)
    smsg = input("Enter your message: ")
    print(smsg)
    socket.send_string(smsg,copy=True)
    print("sending....")
