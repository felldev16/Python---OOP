from datetime import datetime

"""
super class
"""
class Handphone:
    def __init__(self,  model: str, tanggal_beli: datetime, harga: float, jumlah: int, keterangan: dict):
        self.model = model
        self.tanggal_beli = datetime.strptime(tanggal_beli, "%d-%m-%Y")
        self.harga = harga
        self.jumlah = jumlah
        self.keterangan = keterangan

    def tampilkan_info(self):
        print(f"Model Handphone: {self.model}")
        print(f"Tanggal Pembelian: {self.tanggal_beli.strftime('%d-%m-%Y')}")
        print(f"Harga: Rp{self.harga:,.2f}")
        print(f"jumlah: {self.jumlah} unit")
        print("Spesifikasi:")
        for key, value in self.keterangan.items():
            print(f"  - {key}: {value}")

"""
sub class : mewarisi atribut dan fungsi dari super class
"""
class iPhone(Handphone): #sub class 1
    def __init__(self, model, tanggal_beli, harga, jumlah, keterangan, ios_version: float, face_id: bool):
        super().__init__(model, tanggal_beli, harga, jumlah, keterangan)
        # tambahan atribut, yaitu ios_version dan face_id
        self.ios_version = ios_version
        self.face_id = face_id  # True jika mendukung Face ID

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Versi iOS: {self.ios_version}")
        print(f"Face ID: {'Ya' if self.face_id else 'Tidak'}")

class Samsung(Handphone): #sub class 2
    def __init__(self, model, tanggal_beli, harga, jumlah, keterangan, oneUI_version: float, s_pen: bool):
        super().__init__(model, tanggal_beli, harga, jumlah, keterangan)
        # tambahan atribut, yaitu oneUI_version dan s_pen
        self.oneUI_version = oneUI_version
        self.s_pen = s_pen  # True jika mendukung S-Pen

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"One UI Version: {self.one_ui_version}")
        print(f"S-Pen Support: {'Ya' if self.s_pen else 'Tidak'}")

class Xiaomi(Handphone): #sub class 3
    def __init__(self, model, tanggal_beli, harga, jumlah, keterangan, miUI_version: float, watt_fastCharge: int):
        super().__init__(model, tanggal_beli, harga, jumlah, keterangan)
        # tambahan atribut, yaitu miUI_version dan watt_fastCharge
        self.miUI_version = miUI_version
        self.watt_fastCharge = watt_fastCharge  # Watt pengisian daya cepat

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"MIUI Version: {self.miUI_version}")
        print(f"Fast Charging (Watt): {self.watt_fastCharge}W")

"""
Function yang ada pada menu aplikasi
"""

def tambah_hp(data_hp):
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
        if input("Apakah ingin menambahkan lagi? (y/n): ").lower() == 'n':
            break

    keterangan[key] = value

    if pilihan == "1":
        ios_version = input("Versi iOS: ")
        face_id = input("Mendukung Face ID? (y/n): ").lower() == 'y'
        data_hp.append(iPhone(model, tanggal_beli, harga, jumlah, keterangan, ios_version, face_id))
    elif pilihan == "2":
        oneUI_version = input("Versi One UI: ")
        s_pen = input("Mendukung S-Pen? (y/n): ").lower() == 'y'
        data_hp.append(Samsung(model, tanggal_beli, harga, jumlah, keterangan, oneUI_version, s_pen))
    elif pilihan == "3":
        miUI_version = float(input("Versi MIUI: "))
        watt_fastCharge = int(input("Fast Charging (Watt): "))
        data_hp.append(Xiaomi(model, tanggal_beli, harga, jumlah, keterangan, miUI_version, watt_fastCharge))
    else:
        print("Pilihan tidak sesuai")

print("Data berhasil ditambahkan")

def daftar_hp(data_hp):
    if not data_hp:
        print("\nTidak ada data handphone yang tersedia.")
        return

    # Header tabel
    print(f"{'Model':<20} {'Tanggal Beli':<15} {'Harga':<15} {'Jumlah':<10} {'Keterangan'}")
    print("=" * 70)

    # Menampilkan data handphone satu per satu
    for hp in data_hp:
        keterangan = " | ".join([f"{key}: {value}" for key, value in hp.keterangan.items()])
        print(f"{hp.model:<20} {hp.tanggal_beli.strftime('%d-%m-%Y'):<15} Rp{hp.harga:,.2f} {hp.jumlah:<10} {keterangan}")


def hapus_hp(data_hp):
    model = input("Masukkan model handphone yang ingin dihapus: ")
    global daftar_handphone
    daftar_handphone = [hp for hp in daftar_handphone if hp.model != model]
    print("\nHandphone berhasil dihapus!")

"""
Main Program
"""
def main():
    data_hp = []

    while True:
        print("APLIKASI MANAGEMENT PEMBELIAN HANDPHONE")
        print("DI TOKO ABC")
        print('=' * 35)
        print("\nMenu:")
        print("1. Tambah Handphone")
        print("2. Lihat Daftar Handphone")
        print("3. Hapus Handphone")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            tambah_hp(data_hp)
        elif pilihan == "2":
            daftar_hp(data_hp)
        elif pilihan == "3":
            hapus_hp(data_hp)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()