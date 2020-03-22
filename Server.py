import socket
import threading
import sys
import time

Host = ""
serverPort = 27019
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((Host,serverPort))
serverSocket.listen(3)

waktu = [0,0] #waktu default 0 untuk kedua peserta
isDone = False #boloen untuk flag apakah quiz sudah selesai atau belum

def pertanyaan(pesertaList,idPeserta,pertanyaan,jawaban):
    global score
    global time
    global isDone
    pesertaList[idPeserta].sendall("Q\n")
    time.sleep(0.1)
    pesertaList[idPeserta].sendall(pertanyaan+"\n") #mengirim pertanyaan ke semua
    time.sleep(0.1)
    jawabanpeserta = pesertaList[idPeserta].recv(1024)
    waktu[idPeserta] = datetime.datetime.now()

    if(not isDone) and (jawaban == jawabanpeserta):
        score[idPeserta]+=10
        isDone = not isDone
        pesertaList[idPeserta].sendall("Benar!\n")
        time.sleep(0.1)
    else:
        if(jawaban == jawabanpeserta):
            pesertaList[idPeserta].sendall("Maaf Kamu Terlambat :( \n")
            time.sleep(0.1)
        else:
            pesertaList[idPeserta].sendall("Jawaban kamu salah!\n")
            time.sleep(0.1)
            score[idPeserta]=0

print("Selamat datang di aplikasi client server quiz..")
print("Quiz akan di ikuti oleh 2 peserta dengan aturan Quiz sebagai berikut : ")
print("1. ")
print("2. ")
print("3. ")
print("4. ")

while 1:
    print("Siap untuk connect dengan 2 peserta untuk memulai : ")
    (peserta1, addr) = serverSocket.accept()
    print("Peserta pertama bergabung dengan addr ",addr)

    (peserta2, addr) = serverSocket.accept()
    print("Peserta kedua bergabung dengan addr ",addr)

    pesertaList = [peserta1,peserta2]
    peserta1.sendall("A\n")
    time.sleep(0.1)
    peserta1.sendall("Kamu adalah peserta 1")

    time.sleep(0.1)
    peserta2.sendall("A\n")
    time.sleep(0.1)
    peserta2.sendall("Kamu adalah peserta 2")

    nomorSoal, clientAddr = serverSocket.recvfrom(2048)
    Soal, clientAddr = serverSocket.recvfrom(2048)
    A, clientAddr = serverSocket.recvfrom(2048)
    B, clientAddr = serverSocket.recvfrom(2048)
    C, clientAddr = serverSocket.recvfrom(2048)
    Jawaban, clientAddr = serverSocket.recvfrom(2048)

    combSoal = nomorSoal+" "+Soal+" "+"\n"+A+"\n"+B+"\n"+C+"\n"
    isDone = False

    peserta1Thread = threading.Thread(target = pertanyaan,name="Thread1", args = (pesertaList, 0, soal,Jawaban,))
    peserta2Thread = threading.Thread(target = pertanyaan,name="Thread2", args = (pesertaList, 1, soal,Jawaban,))
    #start thread
    peserta1Thread.start()
    peserta2Thread.start()
    #join to main thread
    peserta1Thread.join()
    peserta2Thread.join()
    
if score[0]>score[1]:
    print ("Peserta 1 menang, dengan score: ", score)
    conn1.sendall("X\n")
    time.sleep(0.1)
    conn1.sendall("kamu menang\n")
    time.sleep(0.1)
    conn2.sendall("X\n")
    time.sleep(0.1)
    conn2.sendall("kamu kalah\n")
    time.sleep(0.1)
elif score[0]<score[1]:
    print ("Peserta 2 menang, dengan score: ", score)
    conn2.sendall("X\n")
    time.sleep(0.1)
    conn2.sendall("kamu menang\n")
    time.sleep(0.1)
    conn1.sendall("X\n")
    time.sleep(0.1)
    conn1.sendall("kamu kalah\n")
    time.sleep(0.1)
else:
    print ("Kalian seri, dengan score: ", score)
    conn1.sendall("X\n")
    time.sleep(0.1)
    conn1.sendall("seri\n")
    time.sleep(0.1)
    conn2.sendall("X\n")
    time.sleep(0.1)
    conn2.sendall("seri\n")
    time.sleep(0.1)

    # print(nomorSoal.decode())
    # print(Soal.decode())
    # print(A.decode())
    # print(B.decode())
    # print(C.decode())
    # print(Jawaban.decode())
    
    