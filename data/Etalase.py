from product import Nama_Product

class Etalase_Barang:
    def __init__(self):
        self.etalase = []
    
    def add_product(self,product):
        return self.etalase.append(product)
    
    def remove_product(self,product_name):
        for production in self.etalase:
            if production.nama.lower() == product_name.lower():
                self.etalase.remove(production)
    def see_etalase(self):
        if not self.etalase:
            print("="*80)
            print("Produk belum ada yang dijual!")
            print("="*80)
        else: 
            print("="*80)
            print(f"| {"No":^8} | {"Nama Produk":^20} | {"Tipe Produk":^20} | {"Harga Produk":^20}")
            for index,product in enumerate(self.etalase,1):
                print(f"| {index:^8} | {product.nama:^20} | {product.tipe:^20} | {product.harga:^20}")
                print("-"*80)
            print("="*80)

etalase = Etalase_Barang()
result1 = Nama_Product("Rexona","Kebersihan",9800)
