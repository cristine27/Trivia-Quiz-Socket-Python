# Aplikasi Trivia Berbasis Python
# Dibuat Oleh 
1. Henrico Leodra (2017730038)
2. Cristine Artanty (2017730050)

# Spesifikasi Program
1. Aplikasi ini hanya dapat digunakan/dimainkan oleh 2 user saja

# Cara menjalankan program
1. Jalankan Server.py pada cmd/terminal
2. Memasukan port yang ingin digunakan
3. Memasukan jumlah pertanyaan yang ingin dijalankan pada aplikasi tersebut
4. Memasukan file soal (file soal memiliki format tertentu yang akan dijelaskan dibawah). Dapat menggunakan sample soal yang sudah disediakan dengan nama file soal.txt
5. Jalnkan Client.py pada 2 cmd/terminal
6. Masukan port yang digunakan untuk memulai server 

# Aturan Program
1. Setiap player dapat menjawab pertanyaan
2. Jika player pertama sudah menjawab pertanyaan tersebut dan memiliki jawaban benar maka player kedua tidak dapat menjawab, dan sebaliknya
3. Tidak ada batas waktu
4. Untuk setiap pertanyaan yang dijawab dengan benar maka player tersebut akan mendapatkan 10 poin
5. Jika diakhir game kedua player memiliki score sama maka hasil dari permainan tersebut adalah TIE (Imbang)

# Format Soal
1. File soal harus bertipe .txt
2. Soal bersifat pilihan ganda
3. Setiap soal memiliki 6 baris
4. Baris pertama adalah keterangan soal atau soalnya sendiri
5. Baris kedua sampai kelima adalah pilihan jawaban yang diawali dengan alphabet untuk mengindikasikan pilihan (A,B,C,D)
6. Baris terakhir adalah jawaban dari soal tersebut
