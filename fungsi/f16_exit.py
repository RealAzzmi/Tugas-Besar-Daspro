import variabel
import fungsi.f14_save

def run():
    if variabel.login == False:
        print("Anda belum login")
    else:
        simpan_file = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        cek = False
        while cek == False:
            if simpan_file == "y" or simpan_file == "Y":
                fungsi.f14_save.run()
                cek = True
                end = True
            elif simpan_file == "n" or simpan_file == "N":
                cek = True
                end = True
            else:
                simpan_file = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        return end