import socket
import sys

def intros(s):
    res = s.recv(1024).decode()
    print(res)

def question(s):
    quesNum = s.recv(1024).decode()
    print(quesNum)
    ques = s.recv(1024).decode()
    print(ques)
    ans = input("Answer: ")
    while ans not in ['A', 'B', 'C', 'D']:
        print ("Enter a valid choice!")
        ans = input("Answer: ")
    s.send(ans.encode())
    response = s.recv(1024).decode()
    print(response)

def scores(s):
    res = s.recv(1024).decode()
    print(res)

def final(s):
    res = s.recv(1024).decode()
    print(res)

HOST = 'localhost'   
PORT = int(input("Enter the port number to which the server is bound: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    choice = s.recv(1024).decode()
    if choice == "Intro": 
        intros(s)
    elif choice == "Ques":
        question(s)
    elif choice == "Skor":
        scores(s)
    elif choice == "Final":
        final(s)
        break
    else:
        print ("Invalid choice: ", choice)
s.close()