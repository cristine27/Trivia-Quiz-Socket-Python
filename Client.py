import socket
import sys

def intros(s):
    res = s.recv(1024).decode()
    print(res)

def question(s):
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
    print(prompt)

HOST = 'localhost'    # The remote host
PORT = int(input("Enter the port number to which the server is bound: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    choice = s.recv(1024).decode()
    if choice[0] == "I":
        intros(s)
    elif choice[0] == "Q":
        question(s)
    elif choice[0] == "S":
        scores(s)
    elif choice[0] == "X":
        final(s)
        break
    else:
        print ("Invalid choice: ", choice)