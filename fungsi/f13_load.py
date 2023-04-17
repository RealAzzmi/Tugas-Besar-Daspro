from argparse import *
import os

def run(folder):
    pars = ArgumentParser()
    pars.add_argument("nama_folder",nargs="?",type=str,default='')
    arg = pars.parse_args()
    fdr = arg.nama_folder
    if os.path.isdir(fdr) :
        print("Loading...")
        print("\nSelamat datang di program \"Manajerial Candi\"")
        print("Masukkan command \"help\"untuk daftar command yang dapat kamu panggil.")
        folder[0] = fdr
    elif fdr == "":
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: " + "python main.py" + " <nama_folder>")
        exit()
    else :
        print(f"\nfolder \"{fdr}\" tidak ditemukan")
        exit()

