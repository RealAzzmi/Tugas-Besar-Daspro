import commands
import database.user, database.bahan_bangunan, database.candi
from algorithms.string_processing import strip


def main():
    commands.load()

    database.user.load()
    database.bahan_bangunan.load()
    database.candi.load()

    while True:
        command = input(">>> ")
        command = strip(command)
        commands.run(command)

if __name__ == "__main__":
    main()