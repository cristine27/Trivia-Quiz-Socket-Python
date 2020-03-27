import socket
HOST = 'localhost'
PORTSERVER = 27019

def pertanyaan(s):
    soal = s.recv(1024)
    print(soal)

    jawaban = input("Jawaban : ")
    while jawaban not in ['A','B','C']:
        print("Tidak ada pilihan jawaban tersebut")
        jawaban = input("Jawaban : ")
    clientSocket.sendall(jawaban)

    hasilJawaban = clientSocket.recv(1024)
    print hasilJawaban

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect((HOST,PORTSERVER))
while True:
	
	try:
		soal = s.recv(1024)
		print(soal)

		jawaban = input("Jawaban : ")
		while jawaban not in ['A','B','C']:
			print("Tidak ada pilihan jawaban tersebut")
			jawaban = input("Jawaban : ")
		clientSocket.sendall(jawaban)

		hasilJawaban = clientSocket.recv(1024)
		print hasilJawaban
	
	except:
		clientSocket.close()
		exit(0)