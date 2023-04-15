from algoritma_umum import strip
import database
import fungsi.f01_login, fungsi.f02_logout
import fungsi.f03_summonjin, fungsi.f04_hapusjin, fungsi.f05_ubahjin
import fungsi.f06_bangun

def main():
    database.load()
    
    while True:
        command = input(">>> ")
        command = strip(command)

        if command == "login":
            fungsi.f01_login.run()
        elif command == "logout":
            fungsi.f02_logout.run()
        elif command == "summonjin":
            fungsi.f03_summonjin.run()
        elif command == "hapusjin": # Belum implementasi hapus candi juga; baru hapus jin
            fungsi.f04_hapusjin.run()
        elif command == "ubahjin":
            fungsi.f05_ubahjin.run()
        elif command == "bangun":
            fungsi.f06_bangun.run()

        elif command == "melihat": # Untuk debugging saja; nanti dihapus
            print(f"Total user: {database.user_count}")
            print(f"Total jin: {database.jin_count}")

            for user in database.user_list.array:
                print(user)

                    
if __name__ == "__main__":
    main()