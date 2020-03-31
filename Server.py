"""
@author: Henrico Leodra (2017730038) & Cristine Artanty (2017730050)
"""

import socket
import threading
import sys
import time
import datetime

HOST = 'localhost'
print ("Selamat datang pada Aplikasi Trivia Kami")
print ("Dibuat oleh:\nHenrico Leodra (2017730038)\nCristine Artanty (2017730050)\n")
PORT = int(input("Input port yang akan digunakan : "))

score = [0, 0] #quiz akan di ikuti oleh 2 peserta

totalQuestions = int(input("Jumlah pertanyaan : "))
filename = input("Masukkan nama file : ")
t = [0, 0] #waktu delta kedua peserta
f = open(filename, 'r')

flag = [False] * totalQuestions #menandakan apakah suatu pertanyan sudah berhasil dijawab

def askQuestion(pesertaList, playerNo, ques, ans, questionNo):    
    pesertaList[playerNo].send(ques.encode())          
    time.sleep(0.1)
    
    data = pesertaList[playerNo].recv(PORT).decode()                    
    t[playerNo] = datetime.datetime.now()
    if ans.rstrip()==data:
        if flag[questionNo]==False:
            score[playerNo]+=10
            flag[questionNo] = True
            pesertaList[playerNo].send(("Correct Answer").encode())
            time.sleep(0.1)
        else:
            pesertaList[playerNo].send(("Too late!").encode())
            time.sleep(0.1)
    else:
        pesertaList[playerNo].send(("Incorrect Answer").encode())
        time.sleep(0.1)

def finalSkor():
    if score[0]>score[1]:
        print ("Player 1 won, with score: ", score)
        peserta1.send("YOU WON".encode())
        time.sleep(0.1)
        peserta2.send("YOU LOST".encode())
        time.sleep(0.1)
    elif score[0]<score[1]:
        print ("Player 2 won, with score: ", score)
        peserta2.send("YOU WON".encode())
        time.sleep(0.1)
        peserta1.send("YOU LOST".encode())
        time.sleep(0.1)
    else:
        print ("It's a tie, with score: ", score)
        peserta1.send("TIE".encode())
        time.sleep(0.1)
        peserta2.send("TIE".encode())
        time.sleep(0.1)

def sendallScore(pesertaList):
    global score
    for i, conn in enumerate(pesertaList):
        conn.send("Skor".encode())
        time.sleep(0.1)
        keteranganSkor = "Player " + str(i+1) + " your score is : " + str(score[i])
        conn.send(keteranganSkor.encode())
        time.sleep(0.1)

        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(2)
print ("Server bound to ", HOST, ":", PORT, "\nHubungkan kedua players sebelum mulai...")
(peserta1, addr) = s.accept()
print ("Connected to Player 1 at ", addr)
(peserta2, addr) = s.accept()
print ("Connected to Player 2 at ", addr)
pesertaList = [peserta1, peserta2]

time.sleep(0.1)
peserta1.send("Intro".encode())
peserta1.send("Selamat datang pada aplikasi trivia kami, You are Player 1".encode())

time.sleep(0.1)
peserta2.send("Intro".encode())
peserta2.send("Selamat datang pada aplikasi trivia kami, You are Player 2".encode())

for questionNo in range(totalQuestions):
    peserta1.send("Ques".encode())
    time.sleep(0.1)
    peserta2.send("Ques".encode())
    time.sleep(0.1)
    
    Soal = "\nPertanyaan Nomor " + str(questionNo+1)
    peserta1.send(Soal.encode())
    time.sleep(0.1)
    peserta2.send(Soal.encode())
    time.sleep(0.1)

    ques = f.readline()+f.readline()+f.readline()+f.readline()+f.readline()
    print (ques)
    ans = f.readline()
    
    playerThread1 = threading.Thread(target = askQuestion, name = "Thread1", args = (pesertaList, 0, ques, ans, questionNo))
    playerThread2 = threading.Thread(target = askQuestion, name = "Thread2", args = (pesertaList, 1, ques, ans, questionNo))
    playerThread1.start()
    playerThread2.start()
    playerThread1.join()
    playerThread2.join()

    if questionNo<totalQuestions:
        sendallScore(pesertaList)

time.sleep(0.1)
peserta1.send("Final".encode())
time.sleep(0.1)
peserta2.send("Final".encode())
finalSkor()
s.close()

    

