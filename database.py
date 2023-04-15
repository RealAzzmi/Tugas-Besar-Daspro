from algoritma_umum import split, strip
from algoritma_umum import DynamicArray, append_array, erase_array

user_list = DynamicArray()
user_count = -1 # Karena line pertama diabaikan 'username;password;role\n'
jin_count = 0

class User:
    def __init__(self, username='', password='', role=''):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self): # Dihapus nanti
        return f"[{self.username} & {self.password} & {self.role}]"

def user_equality(user1, user2):
    return user1.username == user2.username and user1.password == user2.password and user1.role == user2.role

def load():
    global user_list, user_count, jin_count
    with open('user.csv') as file:
        for line in file:
            user_count += 1
    with open('user.csv') as file:
        file.readline() # untuk mengabaikan line 'username;password;role\n'
        for i in range(user_count):
            username, password, role = split(strip(file.readline()), ';')
            if role == "jin_pengumpul" or role == "jin_pembangun":
                jin_count += 1
            append_array(user_list, User(username, password, role))

def add_user(username, password, role):
    global user_list, user_count, jin_count
    append_array(user_list, User(username, password, role))
    if role == "jin_pengumpul" or role == "jin_pembangun":
        jin_count += 1
    user_count += 1

def erase_user(username, password, role): # Asumsi sudah eksis
    global user_list, user_count, jin_count 
    if role == "jin_pengumpul" or role == "jin_pembangun":
        jin_count -= 1
    user_count -= 1
    erase_array(user_list, User(username, password, role), user_equality)


def is_user_exist(username):
    for i in range(user_count):
        if user_list.array[i].username == username:
            return True, user_list.array[i]
    return False, User()

def is_password_valid(password):
    return 5 <= len(password) <= 25
