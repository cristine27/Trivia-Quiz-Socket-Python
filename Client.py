"""
@author: Henrico Leodra (2017730038) & Cristine Artanty (2017730050)
"""

import socket
import sys

def intros(s):
    res = s.recv(PORT).decode()
    print(res)

def question(s):
    quesNum = s.recv(PORT).decode()
    print(quesNum)
    ques = s.recv(PORT).decode()
    print(ques)
    ans = input("Jawaban: ")
    while ans not in ['A', 'B', 'C', 'D']:
        print ("Enter a valid choice!")
        ans = input("Jawaban: ")
    s.send(ans.encode())
    response = s.recv(PORT).decode()
    print(response)

def scores(s):
    res = s.recv(PORT).decode()
    print(res)

def final(s):
    res = s.recv(PORT).decode()
    print(res)

HOST = 'localhost'   
PORT = int(input("Input port yang akan digunakan : "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    choice = s.recv(PORT).decode()
    if choice == "Intro": 
        intros(s)
    elif choice == "Ques":
        question(s)
    elif choice == "Skor":
        scores(s)
    elif choice == "Final":
        final(s)
        break
s.close()