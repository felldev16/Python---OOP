from datetime import datetime

class Handphone:
    def __init__(self, model: str, tanggal_beli: str, harga: float, jumlah: int, keterangan: dict):
        self.model = model
        self.tanggal_beli = datetime.strptime(tanggal_beli, "%d-%m-%Y")
        self.harga = harga
        self.jumlah = jumlah
        self.keterangan = keterangan

    def tampilkan_info(self):
        print(f"Model: {self.model}")
        print(f"Tanggal Pembelian: {self.tanggal_beli.strftime('%d-%m-%Y')}")
        print(f"Harga: Rp{self.harga:,.2f}")
        print(f"Jumlah: {self.jumlah} unit")
        print("Keterangan:")
        for key, value in self.keterangan.items():
            print(f"  - {key}: {value}")

class iPhone(Handphone):
    def __init__(self, model, tanggal_beli, harga, jumlah, keterangan, ios_version: float, face_id: bool):
        super().__init__(model, tanggal_beli, harga, jumlah, keterangan)
        self.ios_version = ios_version
        self.face_id = face_id

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Versi iOS: {self.ios_version}")
        print(f"Face ID: {'Ya' if self.face_id else 'Tidak'}")

class Samsung(Handphone):
    def __init__(self, model, tanggal_beli, harga, jumlah, keterangan, oneUI_version: float, s_pen: bool):
        super().__init__(model, tanggal_beli, harga, jumlah, keterangan)
        self.oneUI_version = oneUI_version
        self.s_pen = s_pen

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"One UI Version: {self.oneUI_version}")
        print(f"S-Pen Support: {'Ya' if self.s_pen else 'Tidak'}")

class Xiaomi(Handphone):
    def __init__(self, model, tanggal_beli, harga, jumlah, keterangan, miUI_version: float, watt_fastCharge: int):
        super().__init__(model, tanggal_beli, harga, jumlah, keterangan)
        self.miUI_version = miUI_version
        self.watt_fastCharge = watt_fastCharge

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"MIUI Version: {self.miUI_version}")
        print(f"Fast Charging (Watt): {self.watt_fastCharge}W")

stok_hp = []
transaksi_penjualan = []

def tambah_stok_hp():
    print("\nPilih jenis handphone:")
    print("1. iPhone \t2. Samsung \t3. Xiaomi")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    model = input("Model: ")
    tanggal_beli = input("Tanggal Pembelian (DD-MM-YYYY): ")
    harga = float(input("Harga: "))
    jumlah = int(input("Jumlah: "))

    keterangan = {}
    while True:
        key = input("\nTambahkan keterangan: ")
        value = input(f"Masukkan detail keterangan {key}: ")
        keterangan[key] = value
        if input("Apakah ingin menambahkan lagi? (y/n): ").lower() == 'n':
            break

    if pilihan == "1":
        ios_version = float(input("Versi iOS: "))
        face_id = input("Mendukung Face ID? (y/n): ").lower() == 'y'
        stok_hp.append(iPhone(model, tanggal_beli, harga, jumlah, keterangan, ios_version, face_id))
    elif pilihan == "2":
        oneUI_version = float(input("Versi One UI: "))
        s_pen = input("Mendukung S-Pen? (y/n): ").lower() == 'y'
        stok_hp.append(Samsung(model, tanggal_beli, harga, jumlah, keterangan, oneUI_version, s_pen))
    elif pilihan == "3":
        miUI_version = float(input("Versi MIUI: "))
        watt_fastCharge = int(input("Fast Charging (Watt): "))
        stok_hp.append(Xiaomi(model, tanggal_beli, harga, jumlah, keterangan, miUI_version, watt_fastCharge))
    else:
        print("Pilihan tidak sesuai")
    print("Data berhasil ditambahkan")

def daftar_hp():
    if not stok_hp:
        print("\nTidak ada stok handphone yang tersedia.")
        return
    print("\nDaftar Stok Handphone")
    print("=" * 50)
    for hp in stok_hp:
        hp.tampilkan_info()
        print("-" * 50)

def jual_hp():
    model = input("Masukkan model handphone yang ingin dijual: ")
    jumlah = int(input("Masukkan jumlah unit yang ingin dijual: "))
    
    for hp in stok_hp:
        if hp.model.lower() == model.lower():
            if hp.jumlah >= jumlah:
                hp.jumlah -= jumlah
                transaksi_penjualan.append((model, jumlah, hp.harga * jumlah))
                print("\nHandphone berhasil dijual!")
            else:
                print("Stok tidak mencukupi!")
            return
    print("Model tidak ditemukan!")

def laporan_penjualan():
    if not transaksi_penjualan:
        print("\nBelum ada transaksi penjualan.")
        return
    print("\nLaporan Penjualan")
    print("=" * 50)
    total_pendapatan = 0
    for model, jumlah, total_harga in transaksi_penjualan:
        print(f"Model: {model}, Jumlah Terjual: {jumlah}, Total: Rp{total_harga:,.2f}")
        total_pendapatan += total_harga
    print("=" * 50)
    print(f"Total Pendapatan: Rp{total_pendapatan:,.2f}")

def main():
    while True:
        print("\nAPLIKASI PENJUALAN HANDPHONE - TOKO ABC")
        print("=" * 40)
        print("1. Tambah Stok Handphone")
        print("2. Lihat Stok Handphone")
        print("3. Jual Handphone")
        print("4. Laporan Penjualan")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_stok_hp()
        elif pilihan == "2":
            daftar_hp()
        elif pilihan == "3":
            jual_hp()
        elif pilihan == "4":
            laporan_penjualan()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
