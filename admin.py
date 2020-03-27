import socket
HOST = 'localhost'
PORTSERVER = 27019

def validate():
    if(not(username.strip() and password.strip())):
        return False
    else:
        if((username=='Admin' or username=='admin') and (password=='Admin' or password=='admin'))
        
adminSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
adminSocket.connect((HOST,PORTSERVER))
print("Welcome admin please input your username and password")
username = input("Username : ")
password = input("Password : ")

print("Validating the username and password..")
if(validate()):
    paketSoal = input("silahkan masukkan paket soal yang akan digunakan : (contoh input : 1 untuk paket satu)")
    jumlahSoal = int(input("jumlah soal : "))
    
	if(paketSoal==1):
		fileSoal = open('paketSatu.txt', 'r')
		jawaban = open('jawabanPaketSatu.txt','r')
		
	Soal = fileSoal.readlines()
	Jawaban = jawaban.readlines()
	
	adminSocket.send(Soal)
    adminSocket.sendto(Jawaban)

    
    
    
    


