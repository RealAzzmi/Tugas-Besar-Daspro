import database.user, database.bahan_bangunan, database.candi

import functions.f01_login
import functions.f02_logout
import functions.f03_summonjin
import functions.f04_hapusjin
import functions.f05_ubahjin
import functions.f06_bangun
import functions.f07_kumpul
import functions.f08_batchbangun
import functions.f08_batchkumpul
import functions.f09_laporanjin
import functions.f10_laporancandi
import functions.f11_hancurkancandi
import functions.f12_ayamberkokok
import functions.f13_load
import functions.f14_save
import functions.f15_help
import functions.f16_exit

def load():
    functions.f13_load.run()

def run(command):
    if command == "login":
        functions.f01_login.run()
    elif command == "logout":
        functions.f02_logout.run()
    elif command == "summonjin":
        functions.f03_summonjin.run()
    elif command == "hapusjin":
        functions.f04_hapusjin.run()
    elif command == "ubahjin":
        functions.f05_ubahjin.run()
    elif command == "bangun":
        functions.f06_bangun.run()
    elif command == "kumpul":
        functions.f07_kumpul.run()
    elif command == "batchbangun":
        functions.f08_batchbangun.run()
    elif command == "batchkumpul":
        functions.f08_batchkumpul.run()
    elif command == "laporanjin":
        functions.f09_laporanjin.run()
    elif command == "laporancandi":
        functions.f10_laporancandi.run()
    elif command == "hancurkancandi":
        functions.f11_hancurkancandi.run()
    elif command == "ayamberkokok":
        functions.f12_ayamberkokok.run()
    elif command == "save":
        functions.f14_save.run()
    elif command == "help":
        functions.f15_help.run()
    elif command == "exit":
        functions.f16_exit.run()
    
    elif command == "melihat":
        print("\nUser:")
        for i in range(database.user.user_list.size):
            print(database.user.user_list.array[i])
        print("\n\nBahan bangunan:")
        print(f"[sand, stone, water] = [{database.bahan_bangunan.bahan_list.sand}, {database.bahan_bangunan.bahan_list.stone}, {database.bahan_bangunan.bahan_list.water}]")
        print(f"deskripsi pasir: {database.bahan_bangunan.sand_description}")
        print(f"deskripsi batu: {database.bahan_bangunan.stone_description}")
        print(f"deskripsi air: {database.bahan_bangunan.water_description}")
        print("\n\nCandi:")
        for i in range(database.candi.candi_list.size):
            print(database.candi.candi_list.array[i])
    else:
        print("Command tidak valid.")