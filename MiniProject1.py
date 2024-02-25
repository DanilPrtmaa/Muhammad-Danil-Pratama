class Produk:
    def __init__(self, kode, nama, harga, stok, deskripsi):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.deskripsi = deskripsi

    def tampilkan_info(self):
        formatted_harga = "Rp {:,}".format(self.harga)
        print("Kode:", self.kode)
        print("Nama:", self.nama)
        print("Harga:", formatted_harga)
        print("Stok:", self.stok)
        print("Deskripsi:", self.deskripsi)
        print("------------------------")

class TokoElektronik:
    def __init__(self):
        self.produk_dict = {}
        self.tambah_produk_otomatis()

    def tambah_produk_otomatis(self):
        produk1 = Produk("P001", "Laptop Asus Tuf Gaming F15", 10499000, 10, "Laptop gaming kelas atas dengan spesifikasi mumpuni.")
        self.tambah_produk(produk1)
        produk2 = Produk("P002", "Crystal UHD CU8000 4K Smart TV", 5799000, 15, "TV cerdas dengan resolusi 4K yang memukau.")
        self.tambah_produk(produk2)
        produk3 = Produk("P003", "LG Kulkas 2 Pintu GN-B195SQMT Smart Inverter", 3199000, 8, "Kulkas hemat energi dengan teknologi inverter.")
        self.tambah_produk(produk3)
        produk4 = Produk("P004", "Sanken Mesin Cuci Twin Turbo TW-882NP 9kg", 1599000, 12, "Mesin cuci dengan teknologi twin turbo yang cepat dan efisien.")
        self.tambah_produk(produk4)
        produk5 = Produk("P005", "AC Panasonic Premium Inverter CS-XU10VKP", 6900000, 7, "AC premium dengan teknologi inverter untuk hemat energi.")
        self.tambah_produk(produk5)

    def tambah_produk(self, produk):
        self.produk_dict[produk.kode] = produk
        print("Produk dengan kode", produk.kode, "telah ditambahkan.")

    def lihat_produk(self):
        if self.produk_dict:
            print("Daftar Produk:")
            for produk in self.produk_dict.values():
                produk.tampilkan_info()
        else:
            print("Tidak ada produk dalam daftar.")

    def update_produk(self, kode, **kwargs):
        if kode in self.produk_dict:
            produk = self.produk_dict[kode]
            for key, value in kwargs.items():
                setattr(produk, key, value)
            print("Produk dengan kode", kode, "telah diperbarui.")
        else:
            print("Produk dengan kode", kode, "tidak ditemukan.")

    def hapus_produk(self, kode):
        if kode in self.produk_dict:
            del self.produk_dict[kode]
            print("Produk dengan kode", kode, "telah dihapus.")
        else:
            print("Produk dengan kode", kode, "tidak ditemukan.")

    def tambah_menu(self):
        print("\nTambah Produk")
        kode = input("Masukkan kode produk: ")
        nama = input("Masukkan nama produk: ")
        harga = int(input("Masukkan harga produk: "))
        stok = int(input("Masukkan stok produk: "))
        deskripsi = input("Masukkan deskripsi produk: ")
        produk_baru = Produk(kode, nama, harga, stok, deskripsi)
        self.tambah_produk(produk_baru)

    def update_menu(self):
        print("\nUpdate Produk")
        kode = input("Masukkan kode produk yang ingin diupdate: ")
        if kode in self.produk_dict:
            print("Pilih atribut yang ingin diupdate:")
            print("1. Nama")
            print("2. Harga")
            print("3. Stok")
            print("4. Deskripsi")
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                nama_baru = input("Masukkan nama baru: ")
                self.update_produk(kode, nama=nama_baru)
            elif pilihan == 2:
                harga_baru = int(input("Masukkan harga baru: "))
                self.update_produk(kode, harga=harga_baru)
            elif pilihan == 3:
                stok_baru = int(input("Masukkan stok baru: "))
                self.update_produk(kode, stok=stok_baru)
            elif pilihan == 4:
                deskripsi_baru = input("Masukkan deskripsi baru: ")
                self.update_produk(kode, deskripsi=deskripsi_baru)
            else:
                print("Pilihan tidak valid.")
        else:
            print("Produk dengan kode", kode, "tidak ditemukan.")

    def hapus_menu(self):
        print("\nHapus Produk")
        kode = input("Masukkan kode produk yang ingin dihapus: ")
        self.hapus_produk(kode)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Update Produk")
            print("4. Hapus Produk")
            print("5. Keluar")
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                self.tambah_menu()
            elif pilihan == 2:
                self.lihat_produk()
            elif pilihan == 3:
                self.update_menu()
            elif pilihan == 4:
                self.hapus_menu()
            elif pilihan == 5:
                break
            else:
                print("Pilihan tidak valid.")

# Contoh penggunaan
if __name__ == "__main__":
    toko = TokoElektronik()
    toko.menu()
