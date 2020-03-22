import socket
HOST = 'localhost'
PORTSERVER = 27019

def validate():
    if(not(username.strip() and password.strip())):
        return False
    else:
        return True
        
adminSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
adminSocket.connect((HOST,PORTSERVER))
print("Welcome admin please input your username and password")
username = input("Username : ")
password = input("Password : ")

print("Validating the username and password..")
if(validate()):
    paketSoal = input("silahkan masukkan paket soal yang akan digunakan : (contoh input : paketSoal.txt)")
    jumlahSoal = int(input("jumlah soal : "))
    
    current_line=0
    fileSoal = open(paketSoal, 'r')
    while(jumlahSoal>0):
        nomorSoal = fileSoal.readline()
        Soal = fileSoal.readline()
        A = fileSoal.readline()
        B = fileSoal.readline()
        C = fileSoal.readline()
        Jawaban = fileSoal.readline()

        adminSocket.sendto(nomorSoal.encode(),(HOST,PORTSERVER))
        adminSocket.sendto(Soal.encode(),(HOST,PORTSERVER))
        adminSocket.sendto(A.encode(),(HOST,PORTSERVER))
        adminSocket.sendto(B.encode(),(HOST,PORTSERVER))
        adminSocket.sendto(C.encode(),(HOST,PORTSERVER))
        adminSocket.sendto(Jawaban.encode(),(HOST,PORTSERVER))

        current_line=current_line+6
        jumlahSoal=jumlahSoal-1

    
    
    
    


