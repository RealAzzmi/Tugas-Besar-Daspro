import functions.f14_save
import sys

def run():
    save_file = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # Meminta masukan konfirmasi save file
    check = False # Set kondisi awal
    while check == False:
        if save_file == "y" or save_file == "Y": # Jika kondisi user setuju
            functions.f14_save.run() # Melakukan program F14-Save
            check = True
        elif save_file == "n" or save_file == "N": # Jika kondisi user tidak setuju
            check = True
        else:
            save_file = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # Menanyakan ulang hingga masukan menjadi valid
    sys.exit() # Keluar dari program
