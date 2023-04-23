import database.user, database.bahan_bangunan, database.candi
import variables


def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "bandung_bondowoso" :
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa \"ambil laporan candi\".")
    else:
        if database.candi.candi_list.size == 0:
            print()
            print("""> Total Candi: 0
> Total Pasir yang digunakan: 0
> Total Batu yang digunakan: 0
> Total Air yang digunakan: 0
> ID Candi Termahal: -
> ID Candi Termurah: -""")
            return
        total_sand = 0
        total_stone = 0
        total_water = 0
        
        cheapest_candi_id = 0
        cheapest_candi_price = database.candi.candi_price(database.candi.candi_list.array[0])
        most_expensive_candi_id = 0
        most_expensive_candi_price = database.candi.candi_price(database.candi.candi_list.array[0])
        
        for i in range(database.candi.candi_list.size):
            total_sand += database.candi.candi_list.array[i].sand
            total_stone += database.candi.candi_list.array[i].stone
            total_water += database.candi.candi_list.array[i].water
            price = database.candi.candi_price(database.candi.candi_list.array[i])
            if price < cheapest_candi_price:
                cheapest_candi_id = i
                cheapest_candi_price = price
            if price > most_expensive_candi_price:
                most_expensive_candi_id = i
                most_expensive_candi_price = price
            
        print()
        print(f"""> Total Candi: {database.candi.candi_list.size}
> Total Pasir yang digunakan: {total_sand}
> Total Batu yang digunakan: {total_stone}
> Total Air yang digunakan: {total_water}
> ID Candi Termahal: {most_expensive_candi_id} ({most_expensive_candi_price})
> ID Candi Termurah: {cheapest_candi_id} ({cheapest_candi_price})""")
