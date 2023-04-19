import functions.f14_save
import sys

def run():
    save_file = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    check = False
    while check == False:
        if save_file == "y" or save_file == "Y":
            functions.f14_save.run()
            check = True
        elif save_file == "n" or save_file == "N":
            check = True
        else:
            save_file = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    sys.exit()