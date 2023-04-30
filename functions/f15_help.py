import variables

def run():
    print("=========== HELP ===========")
    # Mengecek apakah sudah login
    if variables.login == False: # Output untuk kondisi belum login
        print("""1. login
   Untuk masuk menggunakan akun
2. exit
   Untuk keluar dari program dan kembali ke terminal""")
    elif variables.role == "bandung_bondowoso": # Output untuk kondisi login sebagai Bandung Bondowoso
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
    elif variables.role == "roro_jonggrang": # Output untuk kondisi login sebagai Roro Jonggrang
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
3. ayamberkokok
   Untuk menyelesaikan permainan dengan memalsukan pagi hari""")
    elif variables.role == "jin_pengumpul": # Output untuk kondisi login sebagai Jin Pengumpul
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi""")
    elif variables.role == "jin_pembangun": # Output untuk kondisi login sebagai Jin Pembangun
        print("""1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi""")
