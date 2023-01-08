#import uuid
#print("ID-" + str(uuid.uuid4())[0:8])


#Header & Greetings
username = input("Silahkan masukkan nama anda : ")
greetings = f"Halo {username} !! Selamat datang di Toko Andi"
breakline = len(greetings)
print("-"*breakline)
print(greetings)
print("-"*breakline)
print()
print("PROMO HARI INI!")
print("Potongan 10% untuk pembelajaan diatas Rp.500.000")
print()
print("Potongan 8% untuk pembelajaan diatas Rp.300.000")
print()
print("Potongan 5% untuk pembelajaan diatas Rp.200.000")
print()

#Product Input
produk = []
jumlah = []
harga = []
total = 0

while True:
    produk_input = input("Masukkan produk yg akan dibeli (tekan y jika selesai) : ")
    if produk_input.lower() == "y":
        break
    else:
        jumlah_input = int(input(f"Masukkan jumlah produk {produk_input} : "))
        #perlu penjagaan jika input jumlah bukan int
        harga_input = float(input(f"Masukkan harga produk {produk_input} : Rp. "))
        
        produk.append(produk_input)
        jumlah.append(jumlah_input)
        harga.append(harga_input)

#Cart
shopping_cart = f"Halo {username} berikut keranjang belanjaan Anda"
print()
print("-"*breakline)
print(shopping_cart)
print("-"*breakline)
print()

for produk_input in produk:
    print(produk)


