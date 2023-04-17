import os
from algoritma_umum import *

def pengulangan(ulang):
    count = 1 
    for i in range(len(ulang)) :
        if ulang[i] == '/' :
            if i != len(ulang)-1:
                count+=1
    return count

def run() :
    masukan = input("Masukkan nama folder: ")
    print("\nSaving...")
    fdr = "save"
    fdr +="/"+masukan
    ulangg = pengulangan(fdr)
    cek = split(fdr,"/")
    temp = ''
    for i in range (ulangg) :
        if i>0 :
            temp += "/"
        temp += cek[i]
        if not (os.path.isdir(temp)) :
            os.mkdir(temp)
            print("membuat folder" + temp + "...")
        if i == ulangg-1 :
            #save_data(data_user, path) #ini buat nulis data user ke user.csv cuma gatau caranya
            #save_data(data_candi, path)
            #save_data(data_bahan, path)
            print("Berhasil menyimpan data di folder" + temp + "!")