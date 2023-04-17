import variabel
import database

def run():
    print("=========== HELP ===========")
    if variabel.login == False:
        print("""1. login
   Untuk masuk menggunakan akun
2. exit
   Untuk keluar dari program dan kembali ke terminal""")
    elif variabel.role == "bandung_bondowoso":
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. summonjin
   Untuk memanggil jin
3. hapusjin
   Untuk menghapus jin
4. ubahjin
   Untuk mengubah tipe jin
5. batchkumpul
   Untuk mengerahkan pasukan jin mengumpulkan bahan
6. batchbangun
   Untuk mengerahkan pasukan jin membangun candi
7. laporanjin
   Untuk mengambil laporan kinerja para jin
8. laporancandi
   Untuk mengambil laporan progress pembangunan candi""")
    elif variabel.role == "roro_jonggrang":
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
3. ayamberkokok
   Untuk menyelesaikan permainan dengan memalsukan pagi hari""")
    elif variabel.role == "jin_pengumpul":
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi""")
    elif variabel.role == "jin_pembangun":
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi""")