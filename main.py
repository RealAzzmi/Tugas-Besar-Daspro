from algoritma_umum import strip
import database
import fungsi.f01_login, fungsi.f02_logout
import fungsi.f03_summonjin, fungsi.f04_hapusjin, fungsi.f05_ubahjin
import fungsi.f06_bangun
import fungsi.f13_load, fungsi.f14_save, fungsi.f15_help, fungsi.f16_exit

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
        elif command == "load":
            fungsi.f13_load.run()
        elif command == "save":
            fungsi.f14_save.run()
        elif command == "help":
            fungsi.f15_help.run()
        elif command == "exit":
            fungsi.f16_exit.run()

        elif command == "melihat": # Untuk debugging saja; nanti dihapus
            print(f"Total user: {database.user_count}")
            print(f"Total jin: {database.jin_count}")

            for user in database.user_list.array:
                print(user)

                    
if __name__ == "__main__":
    main()