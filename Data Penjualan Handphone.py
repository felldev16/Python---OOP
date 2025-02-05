from datetime import datetime

# super class
class Handphone:
    def __init__(self, merk: str, model: str, tanggal_jual: str, harga: float, jumlah: int, warna: str, memori_internal: int):
        self.merk = merk
        self.model = model
        self.tanggal_jual = datetime.strptime(tanggal_jual, "%d-%m-%Y")
        self.harga = harga
        self.jumlah = jumlah
        self.spesifikasi = {
            "Warna": warna,
            "Memori Internal (GB)": memori_internal
        }
    
    def tampilkan_info(self):
        print(f"\nMerk: {self.merk}")
        print(f"Model: {self.model}")
        print(f"Tanggal Jual: {self.tanggal_jual.strftime('%d-%m-%Y')}")
        print(f"Harga (satuan): Rp{self.harga:,.2f}")
        print(f"Jumlah: {self.jumlah} unit")
        print("Spesifikasi:")
        for key, value in self.spesifikasi.items():
            print(f"  - {key}: {value}")
    
    def total_penjualan(self):
        return self.jumlah * self.harga

#sub class : mewarisi atribut dan fungsi dari super class
class iPhone(Handphone): #sub class 1, tambahan atribut: ios_version dan face_id
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version: float, face_id: bool):
        super().__init__("iPhone", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.ios_version = ios_version
        self.face_id = face_id  # True jika mendukung Face ID

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Versi iOS: {self.ios_version}")
        print(f"Face ID: {'Ya' if self.face_id else 'Tidak'}")

class Samsung(Handphone): #sub class 2, tambahan atribut: oneUI_version dan s_pen
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version: float, s_pen: bool):
        super().__init__("Samsung", model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.oneUI_version = oneUI_version
        self.s_pen = s_pen  # True jika mendukung S-Pen

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"One UI Version: {self.oneUI_version}")
        print(f"S-Pen Support: {'Ya' if self.s_pen else 'Tidak'}")

class Xiaomi(Handphone): #sub class 3, tambahan atribut: miUI_version dan watt_fastCharge
    def __init__(self, model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version: float, watt_fastCharge: int):
        super().__init__("Xiaomi",model, tanggal_jual, harga, jumlah, warna, memori_internal)
        self.miUI_version = miUI_version
        self.watt_fastCharge = watt_fastCharge  # Watt pengisian daya cepat

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"MIUI Version: {self.miUI_version}")
        print(f"Fast Charging (Watt): {self.watt_fastCharge}W")

def input_user():
    model = input("Masukkan model handphone: ")
    harga = float(input("Masukkan harga handphone (Satuan): "))
    jumlah = int(input("Masukkan jumlah handphone: "))
    warna = input("Masukkan warna handphone: ").title()
    memori_internal = int(input("Masukkan memori internal handphone (GB): "))
    return model, harga, jumlah, warna, memori_internal

if __name__ == "__main__":
    daftar_hp = []

    print("DATA PENJUALAN HANDPHONE TOKO ABC")
    print("="*45 + "\n")
    tanggal_jual = input("Masukkan tanggal jual handphone (dd-mm-yyyy): ")
    while True:
        merk = input("Masukkan jenis handphone (iPhone/Samsung/Xiaomi) atau 'done' untuk keluar: ").lower()
        if merk == "done":
            break
        
        model, harga, jumlah, warna, memori_internal = input_user()
        if merk == "iphone":
            ios_version = float(input("Versi iOS: "))
            face_id = input("Mendukung Face ID? (y/n): ").lower() == 'y'
            daftar_hp.append(iPhone(model, tanggal_jual, harga, jumlah, warna, memori_internal, ios_version, face_id))
        elif merk == "samsung":
            oneUI_version = float(input("Versi One UI: "))
            s_pen = input("Mendukung S-Pen? (y/n): ").lower() == 'y'
            daftar_hp.append(Samsung(model, tanggal_jual, harga, jumlah, warna, memori_internal, oneUI_version, s_pen))
        elif merk == "xiaomi":
            miUI_version = float(input("Versi MIUI: "))
            watt_fastCharge = int(input("Fast Charging (Watt): "))
            daftar_hp.append(Xiaomi(model, tanggal_jual, harga, jumlah, warna, memori_internal, miUI_version, watt_fastCharge))
        else:
            print("Merk tidak tersedia")
    
    print(f"\n==== Data Handphone yang Terjual pada {tanggal_jual} ====")
    total_all = 0
    data_terjual = {"iPhone": 0, "Samsung": 0, "Xiaomi": 0}
    
    for hp in daftar_hp:
        hp.tampilkan_info()
        total_penjualan = hp.total_penjualan()
        
        total_all += total_penjualan
        data_terjual[hp.merk] += total_penjualan
    
    print("\n==== Total Penjualan Per Merk ====")
    for merk, total in data_terjual.items():
        print(f"{merk}: Rp{total:,.2f}")
    
    print("\n==== Total Semua Penjualan ====")
    print(f"Total keseluruhan penjualan sebesar Rp{total_all:,.2f}")