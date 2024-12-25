class Input_Form_Product:
    def __init__(self):
        self.nama = None
        self.tipe = None
        self.harga = None
    
    def masukka_data_produk(self):
        self.nama = input("Masukkan nama produk : ")
        self.tipe = input("Masukkan tipe produk : ")
        self.harga = input("Masukkan harga produk")
    
    def validasi_form(self):
        if not self.harga.isdigit():
            print("Harga harus berupa angka!")
            return False
        
        return True