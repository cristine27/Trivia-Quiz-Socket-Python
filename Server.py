#!/usr/bin/env python
import socket
import threading
import sys
import time
import datetime

HOST = 'localhost'
PORT = int(input("input port yang akan digunakan : "))

score = [0, 0] #quiz akan di ikuti oleh 2 peserta

totalQuestions = int(input("jumlah pertanyaan : "))
filename = input("Masukkan nama file : ")
t = [0, 0] #waktu delta kedua peserta
f = open(filename, 'r')
isDone = False

def askQuestion(connlist, playerNo, ques, ans):    
    connlist[playerNo].send(ques.encode())          #sendall question
    time.sleep(0.1)


    data = connlist[playerNo].recv(1024)                    #receive answer
    data = data.decode()

    t[playerNo] = datetime.datetime.now()
    if (str(ans) == str(data)):
        if(not isDone):
            score[playerNo]+=10
            isDone = not isDone
            connlist[playerNo].send(("Correct Answer").encode())
            time.sleep(0.1)
        else:
            connlist[playerNo].send(("Too late!").encode())
            time.sleep(0.1)
    else:
        connlist[playerNo].send(("Incorrect Answer").encode())
        time.sleep(0.1)
        score[playerNo]-=10


def sendallScore(connlist):
    global score
    for i, conn in enumerate(connlist):
        conn.send("S".encode())
        time.sleep(0.1)
        keteranganSkor = "Player " + str(i+1) + " your score is : " + str(score[i])
        conn.send(keteranganSkor.encode())
        time.sleep(0.1)

        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(2)
print ("Server bound to ", HOST, ":", PORT, "\nConnect both players before continuing...")
(peserta1, addr) = s.accept()
print ("Connected to Player 1 at ", addr)
(peserta2, addr) = s.accept()
connlist = [peserta1, peserta2]

time.sleep(0.1)
peserta1.send("I".encode())
time.sleep(0.1)
peserta1.send("You are Player 1".encode())
time.sleep(0.1)
peserta2.send("I".encode())
time.sleep(0.1)
peserta2.send("You are Player 2".encode())
time.sleep(0.1)
print ("Connected to Player 2 at ", addr)

for questionNo in range(totalQuestions):
    # Soal = "Question Number " + str(questionNo+1)
    # peserta1.send(Soal.encode())
    # time.sleep()
    # peserta2.send(Soal.encode())
    # time.sleep()

    ques = f.readline()
    ans = f.readline()
    isDone = False

    peserta1.send("Q".encode())
    time.sleep(0.1)
    peserta2.send("Q".encode())
    time.sleep(0.1)
    
    playerThread1 = threading.Thread(target = askQuestion, name = "Thread1", args = (connlist, 0, ques, ans,))
    playerThread2 = threading.Thread(target = askQuestion, name = "Thread2", args = (connlist, 1, ques, ans,))
    playerThread1.start()
    playerThread2.start()
    playerThread1.join()
    playerThread2.join()
    # TODO Buzzer Round Implementation using threading, threading not required for current task
    sendallScore(connlist)
if score[0]>score[1]:
    print ("Player 1 won, with score: ", score)
    peserta1.send("X\n".encode())
    time.sleep(0.1)
    peserta1.send("YOU WON\n".encode())
    time.sleep(0.1)
    peserta2.send("X\n".encode())
    time.sleep(0.1)
    peserta2.send("YOU LOST\n".encode())
    time.sleep(0.1)
elif score[0]<score[1]:
    print ("Player 2 won, with score: ", score)
    peserta2.send("X\n".encode())
    time.sleep(0.1)
    peserta2.send("YOU WON\n".encode())
    time.sleep(0.1)
    peserta1.send("X\n".encode())
    time.sleep(0.1)
    peserta1.send("YOU LOST\n".encode())
    time.sleep(0.1)
else:
    print ("It's a tie, with score: ", score)
    peserta1.send("X\n".encode())
    time.sleep(0.1)
    peserta1.send("IT'S A TIE\n".encode())
    time.sleep(0.1)
    peserta2.send("X\n".encode())
    time.sleep(0.1)
    peserta2.send("IT'S A TIE\n".encode())
    time.sleep(0.1)
s.close()
