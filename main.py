import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"data")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"views")))

from form_product import Input_Form_Product
from Etalase import Etalase_Barang

etalase = Etalase_Barang()

while True:
    print("""
    1. Tambahkan Produk
    2. Hapus Produk 
    3. Tampilkan Produk
    4. Keluar 
""")
    
    answer = input("Masukkan id yang dipilih : ")

    if answer == "1":

        formulir = Input_Form_Product()
        formulir.masukka_data_produk()

        if formulir.validasi_form():
            etalase.add_product(formulir)
            print("produk berhasil ditambahkan ke etalase")

        else:
            print("Produk gagal ditambahkan ke etalase")
    
    elif answer == "2":
        input_nama = input("Masukkan nama barang : ")
        etalase.remove_product(input_nama)
    
    elif answer == "3":
        etalase.see_etalase()
    elif answer == "4":
        print("Terimakasih!")
        break